"""Tests for hooks/pdf_bookmarks.py."""
import io
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

from pypdf import PdfReader, PdfWriter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pdf_bookmarks as bookmarks  # noqa: E402


def section(title, parent=None):
    return SimpleNamespace(title=title, parent=parent, is_section=True)


def page(title, parent=None, src_path=None):
    return SimpleNamespace(title=title, parent=parent, file=SimpleNamespace(src_path=src_path or f'{title}.md'))


def blank_writer(count):
    writer = PdfWriter()
    for _ in range(count):
        writer.add_blank_page(100, 100)
    return writer


class TestWriteOutline(unittest.TestCase):
    def tree(self, pages, offsets):
        writer = blank_writer(max(offsets) + 1)
        bookmarks.write_outline(writer, pages, offsets)

        buffer = io.BytesIO()
        writer.write(buffer)
        reader = PdfReader(buffer)

        def walk(items):
            tree = []
            for index, item in enumerate(items):
                if isinstance(item, list):
                    continue
                following = items[index + 1] if index + 1 < len(items) else None
                children = walk(following) if isinstance(following, list) else []
                tree.append((item.title, reader.get_destination_page_number(item), children))
            return tree

        return walk(reader.outline)

    def test_top_level_pages_are_flat(self):
        pages = [page('Home'), page('Grades')]
        self.assertEqual(self.tree(pages, [0, 3]), [('Home', 0, []), ('Grades', 3, [])])

    def test_pages_in_a_section_nest_under_its_label(self):
        appendix = section('Appendix C: API Access to ADAM')
        pages = [
            page('Home'),
            page('API Access to ADAM', appendix),
            page('Absentees', appendix),
            page('Year-end Functions'),
        ]
        self.assertEqual(
            self.tree(pages, [0, 2, 5, 7]),
            [
                ('Home', 0, []),
                ('Appendix C: API Access to ADAM', 2, [('API Access to ADAM', 2, []), ('Absentees', 5, [])]),
                ('Year-end Functions', 7, []),
            ],
        )

    def test_nested_sections_nest_twice(self):
        outer = section('Outer')
        inner = section('Inner', outer)
        pages = [page('A', outer), page('B', inner)]
        self.assertEqual(
            self.tree(pages, [0, 4]),
            [('Outer', 0, [('A', 0, []), ('Inner', 4, [('B', 4, [])])])],
        )

    def test_page_without_title_falls_back_to_source_path(self):
        pages = [page(None, src_path='grades.md')]
        self.assertEqual(self.tree(pages, [0]), [('grades.md', 0, [])])

    def test_returns_the_number_of_page_bookmarks(self):
        appendix = section('Appendix')
        writer = blank_writer(3)
        count = bookmarks.write_outline(writer, [page('A'), page('B', appendix)], [0, 2])
        self.assertEqual(count, 2)


if __name__ == '__main__':
    unittest.main()
