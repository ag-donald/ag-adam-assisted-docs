"""MkDocs build-time hook: give the aggregated PDF a chapter outline.

Loaded only by `mkdocs.pdf.yml`; the website build never sees it.

mkdocs-exporter's aggregator is a plain `PdfWriter.append()` loop and emits no
outline of any kind, so the manual opens with an empty bookmarks pane. At ~750
pages that leaves a reader no way to reach a chapter except scrolling.

Where each chapter starts is only knowable while the aggregate is being
assembled — the per-chapter PDFs are re-rendered for the aggregate and deleted
straight afterwards, so counting the standalone files would be an assumption
rather than a measurement. Each offset is therefore recorded as its chapter is
appended, and the outline written just before the document is saved.

`Aggregator.save()` is wrapped rather than replaced: it also stamps the PDF
metadata, and the outline has to be added to the same writer before that runs.
"""

import logging

from mkdocs_exporter.formats.pdf.aggregator import Aggregator

log = logging.getLogger('mkdocs.hooks.pdf_bookmarks')

_open = Aggregator.open
_append = Aggregator.append
_save = Aggregator.save


def open(self, path):
    """Starts a fresh set of chapter offsets."""

    self.offsets = []

    return _open(self, path)


def append(self, document):
    """Records where this chapter begins, before it is appended."""

    self.offsets.append(len(self.writer.pages))

    return _append(self, document)


def write_outline(writer, pages, offsets):
    """Adds one bookmark per page, nested under the nav sections it sits in.

    A page inside a nav section (such as "Appendix C: API Access to ADAM")
    goes under a bookmark carrying the section's label, which points at the
    section's first page. Without it the section's label would be missing from
    the outline and its pages would read as top-level chapters.

    Returns the number of page bookmarks written.
    """

    sections = {}
    count = 0

    def section_item(section, offset):
        if id(section) not in sections:
            parent = _parent_section(section)
            parent_item = section_item(parent, offset) if parent else None
            sections[id(section)] = writer.add_outline_item(str(section.title), offset, parent=parent_item)

        return sections[id(section)]

    for page, offset in zip(pages, offsets):
        # `title` is the nav label; the source path is a legible last resort
        # for a page that somehow reaches here without one.
        title = getattr(page, 'title', None) or page.file.src_path
        parent = _parent_section(page)
        parent_item = section_item(parent, offset) if parent else None

        writer.add_outline_item(str(title), offset, parent=parent_item)
        count += 1

    return count


def _parent_section(item):
    """The nav section directly containing `item`, or None at the top level."""

    parent = getattr(item, 'parent', None)

    return parent if getattr(parent, 'is_section', False) else None


def save(self, metadata={}):
    """Writes the chapter outline, then saves."""

    count = write_outline(self.writer, self.pages, getattr(self, 'offsets', []))

    log.info('pdf_bookmarks: wrote %d chapter bookmarks.', count)

    return _save(self, metadata)


Aggregator.open = open
Aggregator.append = append
Aggregator.save = save
