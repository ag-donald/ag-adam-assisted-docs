"""Tests for scripts/audit_api_endpoints.py."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_api_endpoints as audit  # noqa: E402


SOURCE = """
  \\ADAM\\API\\ApiResource::__set_state(array(
     'callback' =>
    [
         ADAM\\API\\DataQuery::class,
        'apiGetGet',
    ],
     'method' => 'get',
     'endpoint' => 'dataquery/get',
  )),
  \\ADAM\\API\\ApiResource::__set_state(array(
     'callback' => [ ADAM\\X::class, 'apiPatch' ],
     'method' => 'patch',
     'endpoint' => 'reporting/grade/comments',
  )),
"""


class TestParseSource(unittest.TestCase):
    def test_parse_source(self):
        self.assertEqual(audit.parse_source(SOURCE),
                         {audit.Endpoint("dataquery/get", "get"),
                          audit.Endpoint("reporting/grade/comments", "patch")})

    def test_endpoint_prefix_and_str(self):
        e = audit.Endpoint("reporting/grade/comments", "get")
        self.assertEqual(e.prefix, "reporting")
        self.assertEqual(str(e), "reporting/grade/comments:get")


class TestParsePage(unittest.TestCase):
    def test_parses_mixed_case_and_deep_paths(self):
        page = audit.parse_page(
            "api-x.md",
            "### XDevMan/alumni:get\n\n### Reporting/grade/comments:get {#custom-anchor}\n")
        self.assertEqual(page.headings, [audit.Endpoint("xdevman/alumni", "get"),
                                         audit.Endpoint("reporting/grade/comments", "get")])

    def test_reads_front_matter_prefixes(self):
        page = audit.parse_page(
            "api-families.md",
            "---\napi_prefixes:\n  - families\n  - familylogin\n---\n# Families\n")
        self.assertEqual(page.prefixes, ["families", "familylogin"])

    def test_no_front_matter_declares_nothing(self):
        self.assertEqual(
            audit.parse_page("api-access-to-adam.md", "# API Access to ADAM\n").prefixes, [])

    def test_malformed_front_matter_raises(self):
        with self.assertRaises(ValueError):
            audit.parse_page("api-x.md", "---\napi_prefixes: families\n---\n")

    def test_invalid_yaml_raises(self):
        with self.assertRaises(ValueError):
            audit.parse_page("api-x.md", "---\n: : [\n---\n")

    def test_ignores_headings_in_code_fences(self):
        page = audit.parse_page("api-x.md", "```\n### Foo/bar:get\n```\n### Real/one:get\n")
        self.assertEqual(page.headings, [audit.Endpoint("real/one", "get")])

    def test_ignores_non_endpoint_headings(self):
        page = audit.parse_page(
            "api-x.md", "### Create a Data Query Secret\n#### Request\n## API Resources\n")
        self.assertEqual(page.headings, [])

    def test_keeps_mistyped_method(self):
        page = audit.parse_page("api-x.md", "### Reporting/pupilreportingperiods:ge\n")
        self.assertEqual(page.headings,
                         [audit.Endpoint("reporting/pupilreportingperiods", "ge")])

    def test_keeps_duplicate_headings(self):
        page = audit.parse_page("api-x.md", "### Pupils/image:get\n\n### Pupils/image:get\n")
        self.assertEqual(len(page.headings), 2)


class TestLoadPages(unittest.TestCase):
    def test_loads_api_pages_sorted(self):
        with tempfile.TemporaryDirectory() as d:
            docs = Path(d)
            (docs / "api-b.md").write_text("### B/one:get\n")
            (docs / "api-a.md").write_text("### A/one:get\n")
            (docs / "other.md").write_text("### C/one:get\n")
            self.assertEqual([p.name for p in audit.load_pages(docs)],
                             ["api-a.md", "api-b.md"])


if __name__ == "__main__":
    unittest.main()
