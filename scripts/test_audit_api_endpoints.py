"""Tests for scripts/audit_api_endpoints.py."""
import contextlib
import io
import json
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

E = audit.Endpoint


class TestAudit(unittest.TestCase):
    def test_clean_audit_has_no_findings(self):
        pages = [audit.Page("api-families.md", ["families"], [E("families/children", "get")])]
        findings = audit.audit({E("families/children", "get")}, pages)
        self.assertEqual(list(findings), list(audit.CHECKS))
        self.assertTrue(all(v == [] for v in findings.values()))

    def test_undocumented_and_not_in_source(self):
        pages = [audit.Page("api-reporting.md", ["reporting"],
                            [E("reporting/pupilreportingperiods", "ge")])]
        f = audit.audit({E("reporting/pupilreportingperiods", "get")}, pages)
        self.assertEqual(f["undocumented"], ["reporting/pupilreportingperiods:get"])
        self.assertEqual(f["not_in_source"], ["reporting/pupilreportingperiods:ge"])

    def test_methods_are_distinct_endpoints(self):
        pages = [audit.Page("api-families.md", ["families"], [E("families/email", "get")])]
        f = audit.audit({E("families/email", "get"), E("families/email", "patch")}, pages)
        self.assertEqual(f["undocumented"], ["families/email:patch"])

    def test_duplicated(self):
        pages = [audit.Page("api-pupils.md", ["pupils"],
                            [E("pupils/image", "get"), E("pupils/image", "get")])]
        f = audit.audit({E("pupils/image", "get")}, pages)
        self.assertEqual(f["duplicated"], ["pupils/image:get (api-pupils.md, api-pupils.md)"])

    def test_wrong_page_including_overview(self):
        pages = [audit.Page("api-access-to-adam.md", [], [E("families/children", "get")]),
                 audit.Page("api-families.md", ["families"], [])]
        f = audit.audit({E("families/children", "get")}, pages)
        self.assertEqual(f["wrong_page"], ["families/children:get (api-access-to-adam.md)"])

    def test_prefix_checks(self):
        pages = [audit.Page("api-families.md", ["families", "migration"], []),
                 audit.Page("api-pupils.md", ["families"], [])]
        f = audit.audit({E("families/children", "get"), E("medical/offsport", "get")}, pages)
        self.assertEqual(f["unassigned_prefix"], ["medical"])
        self.assertEqual(f["prefix_declared_twice"], ["families (api-families.md, api-pupils.md)"])
        self.assertEqual(f["stale_prefix"], ["migration (api-families.md)"])


def _php(*endpoints):
    blocks = "".join(
        f"  \\ADAM\\API\\ApiResource::__set_state(array(\n"
        f"     'method' => '{m}',\n     'endpoint' => '{e}',\n  )),\n"
        for e, m in endpoints)
    return f"<?php return [\n{blocks}];\n"


class TestMain(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.adam = Path(tmp.name) / "adam"
        (self.adam / "includes").mkdir(parents=True)
        self.docs = Path(tmp.name) / "docs"
        self.docs.mkdir()

    def source(self, text):
        (self.adam / "includes" / "methods_apiresource.php").write_text(text)

    def page(self, name, text):
        (self.docs / name).write_text(text)

    def run_main(self, *extra):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = audit.main(["--adam", str(self.adam), "--docs", str(self.docs), *extra])
        return code, out.getvalue(), err.getvalue()

    def clean(self):
        self.source(_php(("families/children", "get")))
        self.page("api-families.md", "---\napi_prefixes:\n  - families\n---\n### Families/children:get\n")

    def test_clean_exits_0(self):
        self.clean()
        code, out, _ = self.run_main()
        self.assertEqual(code, 0)
        self.assertEqual(out, "All 1 endpoints are documented on the correct pages.\n")

    def test_findings_exit_1(self):
        self.source(_php(("families/children", "get"), ("families/email", "patch")))
        self.page("api-families.md", "---\napi_prefixes:\n  - families\n---\n### Families/children:get\n")
        code, out, _ = self.run_main()
        self.assertEqual(code, 1)
        self.assertEqual(out, "Undocumented (1):\n  - families/email:patch\n")

    def test_main_is_deterministic(self):
        self.source(_php(("families/children", "get"), ("families/email", "patch"),
                         ("a/b", "get")))
        self.page("api-families.md", "---\napi_prefixes:\n  - families\n---\n### Families/children:get\n")
        for flags in ((), ("--json",)):
            self.assertEqual(self.run_main(*flags), self.run_main(*flags))

    def test_json_output(self):
        self.clean()
        code, out, _ = self.run_main("--json")
        self.assertEqual(code, 0)
        self.assertEqual(list(json.loads(out)), list(audit.CHECKS))

    def test_missing_adam_checkout_exits_2(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = audit.main(["--adam", "/nonexistent", "--docs", str(self.docs)])
        self.assertEqual(code, 2)
        self.assertTrue(err.getvalue().startswith("audit_api_endpoints: "))

    def test_missing_docs_exits_2(self):
        self.clean()
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = audit.main(["--adam", str(self.adam), "--docs", "/nonexistent"])
        self.assertEqual(code, 2)
        self.assertTrue(err.getvalue().startswith("audit_api_endpoints: "))

    def test_zero_endpoints_exits_2(self):
        self.source("<?php return [];")
        code, _, err = self.run_main()
        self.assertEqual(code, 2)
        self.assertTrue(err.startswith("audit_api_endpoints: "))

    def test_malformed_front_matter_exits_2(self):
        self.clean()
        self.page("api-x.md", "---\napi_prefixes: families\n---\n")
        code, _, err = self.run_main()
        self.assertEqual(code, 2)
        self.assertTrue(err.startswith("audit_api_endpoints: "))
        self.assertEqual(err.count("\n"), 1)


if __name__ == "__main__":
    unittest.main()
