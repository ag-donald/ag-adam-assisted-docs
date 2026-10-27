# API Documentation Split Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split Appendix C into an overview page plus one page per ADAM module, add a deterministic audit that proves
every endpoint ADAM serves is documented on the right page, and close today's coverage gap.

**Architecture:** ADAM's generated `includes/methods_apiresource.php` is the list of endpoints. Each API page declares
the URL prefixes it holds in `api_prefixes` front matter. `scripts/audit_api_endpoints.py` compares the two and exits
non-zero on any finding. A project skill tells Claude when to run it and how to resolve each finding.

**Tech Stack:** Python 3.10 with `unittest` and PyYAML (already installed in `.venv` with MkDocs), MkDocs 1.6, and
ADAM (PHP 8.4, Pest) for Task 1.

**Spec:** `meta/superpowers/specs/2026-10-26-api-docs-split-design.md`

## Global Constraints

- Docs work happens on the `docs/api-split` branch of `/home/philip/dev/adam-docs`, which already holds the spec.
- ADAM work happens in a worktree at `/home/philip/dev/adam/.worktrees/remove-migration-api` on a new branch
  `remove-migration-api` from `development`. Do not switch the branch of `/home/philip/dev/adam` itself.
- Until the ADAM PR is merged, run the audit with `--adam /home/philip/dev/adam/.worktrees/remove-migration-api`.
- Endpoint headings keep the form `### Prefix/name:method`, with an optional ` {#anchor}` suffix.
- Pages are flat in `docs/` and named `api-<module>.md`. The overview stays `docs/api-access-to-adam.md`.
- `scripts/chapters.json` and `scripts/generate_nav.mjs` are not edited or run.
- New prose follows the `writing-user-documentation` skill. Existing entries move without being rewritten, except for
  the fixes in Task 5.
- Docs repo commit messages are a plain imperative sentence (for example "Document Show when rules on input forms"),
  ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. ADAM commits follow ADAM's `committing` skill.
- Run docs tests with `.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'`.

## Review Focus

1. **Headings inside fenced code blocks.** A `### Foo/bar:get` line inside a fenced block must not count as an entry.
   Pinned by `test_ignores_headings_in_code_fences` (Task 2).
2. **Silent parser failure on the PHP file.** If `var_export`'s layout changes and nothing parses, every heading would
   be reported "not in source". Zero parsed endpoints must exit 2 instead. Pinned by `test_zero_endpoints_exits_2`
   (Task 3).
3. **One path with several methods.** `families/email` is served as `get`, `post`, `patch` and `delete`. These are four
   endpoints, and documenting one must not cover the others. Pinned by `test_methods_are_distinct_endpoints` (Task 3).
4. **Mixed-case and three-segment headings.** `### XDevMan/alumni:get` and `### Reporting/grade/comments:get` must
   match `xdevman/alumni:get` and `reporting/grade/comments:get`. Pinned by `test_parses_mixed_case_and_deep_paths`
   (Task 2).
5. **Broken links after the split.** Anchor links from one module page to another are not checked by the normal
   strict build. Pinned by the anchor-checking build in Task 4, Step 7.

---

### Task 1: Remove the migration code from ADAM

**Files (in the ADAM worktree):**
- Delete: `classes/ADAM/Support/Database/Migration.php`
- Delete: `classes/ADAM/Support/Database/MigrationImporter.php`
- Delete: `tests/Unit/Support/Database/MigrationTest.php`
- Modify: `sql-audit-baseline.json:398-399` (remove the two `Migration::` entries)
- Regenerate: `includes/methods_apiresource.php` and any other `php adam build` artefacts it changes

**Interfaces:**
- Produces: a `remove-migration-api` branch whose `includes/methods_apiresource.php` lists 99 endpoints, and an open PR
  against `development`.

- [ ] **Step 1: Create the worktree**

Follow `/home/philip/dev/adam/docs/ai-worktrees.md`: `git -C /home/philip/dev/adam worktree add .worktrees/remove-migration-api -b remove-migration-api development`,
copy `config.ini` and `config.dev.ini`, run `composer install`. Give it the database `adam_agent_remove_migration`
(`php adam db:create`, `php adam db:install`).

- [ ] **Step 2: Delete the three files and the baseline entries**

- [ ] **Step 3: Search for remaining references**

Run: `git grep -n "Support\\\\Database\\\\Migration\b\|MigrationImporter\|api/migration\|\"migration/" -- . ':!docs/audits' ':!docs/superpowers'`
Expected: no output. (Historical audit reports and old specs under `docs/` stay as they are.)

- [ ] **Step 4: Regenerate build artefacts**

Run: `php adam build`, then `grep -c "'endpoint'" includes/methods_apiresource.php`
Expected: `99`, and `grep -c "migration/" includes/methods_apiresource.php` gives `0`.

- [ ] **Step 5: Run tests and static analysis**

Run: `vendor/bin/pest`, `php vendor/bin/phpstan analyse -c phpstan.neon --memory-limit=4G`, `composer php84`
Expected: all pass. A PHPStan baseline entry for a deleted file that now errors as unmatched gets removed from
`phpstan-baseline.neon`.

- [ ] **Step 6: Commit, push and open the PR**

Use ADAM's `committing` skill for the commit and its `create-pull-request` skill for a PR against `development`.
The PR description says the five `migration/*` endpoints had no caller, since `MigrationImporter` was never used.
Tear down the database with `php adam db:drop` only after the docs work is finished; the audit only reads files, but
keep the worktree until Task 6.

---

### Task 2: Audit script parsers

**Files:**
- Create: `scripts/audit_api_endpoints.py`
- Test: `scripts/test_audit_api_endpoints.py`

**Interfaces:**
- Produces:
  - `class Endpoint(NamedTuple): path: str; method: str`, both lower case, with property `prefix -> str` (first
    path segment) and `__str__` returning `"path:method"`.
  - `@dataclass class Page: name: str; prefixes: list[str]; headings: list[Endpoint]`. `name` is the file name, for
    example `api-families.md`. `headings` keeps duplicates in file order.
  - `parse_source(php_text: str) -> set[Endpoint]`
  - `parse_page(name: str, text: str) -> Page`. Raises `ValueError` when front matter is present but is not valid
    YAML, or when `api_prefixes` is not a list of strings.
  - `load_pages(docs_dir: Path) -> list[Page]`: every `docs_dir/api-*.md`, sorted by file name.

- [ ] **Step 1: Write the failing tests**

Follow the structure of `scripts/test_rewrite_anchors.py` (import via `sys.path.insert`). Fixture text is inline.

```python
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

def test_parse_source(self):
    self.assertEqual(audit.parse_source(SOURCE),
                     {audit.Endpoint("dataquery/get", "get"),
                      audit.Endpoint("reporting/grade/comments", "patch")})

def test_endpoint_prefix_and_str(self):
    e = audit.Endpoint("reporting/grade/comments", "get")
    self.assertEqual(e.prefix, "reporting")
    self.assertEqual(str(e), "reporting/grade/comments:get")

def test_parses_mixed_case_and_deep_paths(self):
    page = audit.parse_page("api-x.md",
        "### XDevMan/alumni:get\n\n### Reporting/grade/comments:get {#custom-anchor}\n")
    self.assertEqual(page.headings, [audit.Endpoint("xdevman/alumni", "get"),
                                     audit.Endpoint("reporting/grade/comments", "get")])

def test_reads_front_matter_prefixes(self):
    page = audit.parse_page("api-families.md",
        "---\napi_prefixes:\n  - families\n  - familylogin\n---\n# Families\n")
    self.assertEqual(page.prefixes, ["families", "familylogin"])

def test_no_front_matter_declares_nothing(self):
    self.assertEqual(audit.parse_page("api-access-to-adam.md", "# API Access to ADAM\n").prefixes, [])

def test_malformed_front_matter_raises(self):
    with self.assertRaises(ValueError):
        audit.parse_page("api-x.md", "---\napi_prefixes: families\n---\n")

def test_ignores_headings_in_code_fences(self):
    page = audit.parse_page("api-x.md", "```\n### Foo/bar:get\n```\n### Real/one:get\n")
    self.assertEqual(page.headings, [audit.Endpoint("real/one", "get")])

def test_ignores_non_endpoint_headings(self):
    page = audit.parse_page("api-x.md", "### Create a Data Query Secret\n#### Request\n## API Resources\n")
    self.assertEqual(page.headings, [])

def test_keeps_mistyped_method(self):
    page = audit.parse_page("api-x.md", "### Reporting/pupilreportingperiods:ge\n")
    self.assertEqual(page.headings, [audit.Endpoint("reporting/pupilreportingperiods", "ge")])

def test_keeps_duplicate_headings(self):
    page = audit.parse_page("api-x.md", "### Pupils/image:get\n\n### Pupils/image:get\n")
    self.assertEqual(len(page.headings), 2)
```

- [ ] **Step 2: Run the tests and confirm they fail**

Run: `.venv/bin/python -m unittest scripts.test_audit_api_endpoints -v` (from the repo root)
Expected: FAIL with `ModuleNotFoundError: No module named 'audit_api_endpoints'`.

- [ ] **Step 3: Implement the parsers**

`parse_source` takes each `'method' => '...'` and the `'endpoint' => '...'` that follows it within the same
`__set_state(array(` block; it reads the file as text and never runs PHP. `parse_page` reads front matter only when
the text starts with `---\n`, using `yaml.safe_load`. Endpoint headings match
`^### ([A-Za-z][A-Za-z0-9_]*(?:/[A-Za-z0-9_-]+)+):([a-z]+)(?:\s+\{#[^}]*\})?\s*$`. Lines between a pair of lines
starting with three backticks are skipped.

- [ ] **Step 4: Run the tests and confirm they pass**

Run: `.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'`
Expected: all tests pass, including the 34 existing ones.

- [ ] **Step 5: Commit**

Message: "Add parsers for the API endpoint audit".

---

### Task 3: Audit checks and command line

**Files:**
- Modify: `scripts/audit_api_endpoints.py`
- Test: `scripts/test_audit_api_endpoints.py`

**Interfaces:**
- Consumes: `Endpoint`, `Page`, `parse_source`, `load_pages` from Task 2.
- Produces:
  - `CHECKS: tuple[str, ...] = ("undocumented", "not_in_source", "duplicated", "wrong_page", "unassigned_prefix",
    "prefix_declared_twice", "stale_prefix")`, the fixed output order.
  - `audit(source: set[Endpoint], pages: list[Page]) -> dict[str, list[str]]`: every key of `CHECKS` is present, and
    each list is sorted. Item formats:
    - undocumented, not_in_source: `"families/email:patch"`
    - duplicated: `"pupils/image:get (api-access-to-adam.md, api-access-to-adam.md)"` (page names in heading order)
    - wrong_page: `"families/children:get (api-access-to-adam.md)"`
    - unassigned_prefix: `"medical"`
    - prefix_declared_twice: `"families (api-families.md, api-pupils.md)"` (page names sorted)
    - stale_prefix: `"migration (api-other-endpoints.md)"`
  - `main(argv: list[str] | None = None) -> int` with options `--adam PATH` (default `~/dev/adam`), `--docs PATH`
    (default the `docs/` directory beside `scripts/`) and `--json`. Returns 0, 1 or 2 as the spec defines.
  - Text output: for each non-empty check, a line `<Title> (<count>):` then one `  - <item>` line per item. Titles are
    "Undocumented", "Not in source", "Duplicated", "Wrong page", "Unassigned prefix", "Prefix declared twice",
    "Stale prefix". With no findings it prints `All <n> endpoints are documented on the correct pages.`
  - `--json` prints `json.dumps(findings, indent=2)` with keys in `CHECKS` order.
  - Errors (exit 2) print one line to stderr starting `audit_api_endpoints: `.
  - The file ends with `if __name__ == "__main__": sys.exit(main())`.

- [ ] **Step 1: Write the failing tests**

Build `Page` and `Endpoint` values directly. Use a temporary directory (`tempfile.TemporaryDirectory`) for `main`
tests, with a fake `includes/methods_apiresource.php` and a `docs/` folder.

```python
E = audit.Endpoint

def test_clean_audit_has_no_findings(self):
    pages = [audit.Page("api-families.md", ["families"], [E("families/children", "get")])]
    findings = audit.audit({E("families/children", "get")}, pages)
    self.assertEqual(list(findings), list(audit.CHECKS))
    self.assertTrue(all(v == [] for v in findings.values()))

def test_undocumented_and_not_in_source(self):
    pages = [audit.Page("api-reporting.md", ["reporting"], [E("reporting/pupilreportingperiods", "ge")])]
    f = audit.audit({E("reporting/pupilreportingperiods", "get")}, pages)
    self.assertEqual(f["undocumented"], ["reporting/pupilreportingperiods:get"])
    self.assertEqual(f["not_in_source"], ["reporting/pupilreportingperiods:ge"])

def test_methods_are_distinct_endpoints(self):
    pages = [audit.Page("api-families.md", ["families"], [E("families/email", "get")])]
    f = audit.audit({E("families/email", "get"), E("families/email", "patch")}, pages)
    self.assertEqual(f["undocumented"], ["families/email:patch"])

def test_duplicated(self):
    pages = [audit.Page("api-pupils.md", ["pupils"], [E("pupils/image", "get"), E("pupils/image", "get")])]
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

def test_main_exit_codes_and_output(self):
    # clean fixture -> returns 0 and prints "All 1 endpoints are documented on the correct pages."
    # one undocumented endpoint -> returns 1 and prints "Undocumented (1):" then "  - families/email:patch"
    ...

def test_main_is_deterministic(self):
    # two runs over the same fixture produce identical stdout, for text and for --json

def test_missing_adam_checkout_exits_2(self):
    self.assertEqual(audit.main(["--adam", "/nonexistent", "--docs", str(docs)]), 2)

def test_zero_endpoints_exits_2(self):
    # methods_apiresource.php exists but contains "<?php return [];" -> returns 2

def test_malformed_front_matter_exits_2(self):
    # a docs/api-x.md with "api_prefixes: families" -> returns 2
```

Capture stdout and stderr with `contextlib.redirect_stdout` and `redirect_stderr`.

- [ ] **Step 2: Run the tests and confirm they fail**

Run: `.venv/bin/python -m unittest scripts.test_audit_api_endpoints -v`
Expected: the new tests FAIL with `AttributeError: module 'audit_api_endpoints' has no attribute 'audit'`.

- [ ] **Step 3: Implement `audit`, `CHECKS` and `main`**

Use `argparse`. Expand `~` in `--adam`.

- [ ] **Step 4: Run the tests and confirm they pass**

Run: `.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'`
Expected: all pass.

- [ ] **Step 5: Run the audit against the current single page**

Run: `.venv/bin/python scripts/audit_api_endpoints.py --adam /home/philip/dev/adam/.worktrees/remove-migration-api; echo "exit $?"`
Expected, with exit 1:
- Undocumented (7): `classes/enrolment:get`, `families/email:patch`, `families/emailpreferences:patch`,
  `families/get_children_by_family:get`, `familyrelationships/family:patch`, `psychometric/assessments_by_category:get`,
  `reporting/pupilreportingperiods:get`.
- Not in source (1): `reporting/pupilreportingperiods:ge`
- Duplicated (1): `pupils/image:get (api-access-to-adam.md, api-access-to-adam.md)`
- Wrong page (92): one line per heading, all on `api-access-to-adam.md`.
- Unassigned prefix: all 32 prefixes.

If any count differs, find out why before going on.

- [ ] **Step 6: Commit**

Message: "Add the API endpoint audit".

---

### Task 4: Split the page

**Files:**
- Modify: `docs/api-access-to-adam.md` (becomes the overview)
- Create: the 18 pages in the spec's "Pages" table, from `docs/api-absentees.md` to `docs/api-other-endpoints.md`
- Modify: `mkdocs.yml:144` (Appendix C becomes a section)
- Modify: `docs/third-party-integration.md`, `docs/online-applications.md`, and any other page that links to an entry
  that moved

**Interfaces:**
- Consumes: `scripts/audit_api_endpoints.py` from Task 3.
- Produces: the page files and their `api_prefixes`, exactly as the spec's table lists them.

- [ ] **Step 1: Move the entries with a throwaway script**

Write a one-off script in the scratchpad (not committed). It cuts lines 199–4134 of `docs/api-access-to-adam.md`
into entries, where each entry runs from one `### ` endpoint heading to the line before the next one. It appends each
entry, in its original order, to the page that declares the entry's prefix in the spec's table. Each page starts with
its front matter and `# <Title>`.

The overview keeps lines 1–193, keeps the `## API Resources` heading (so the existing `#api-resources` link on line 27
still works), replaces lines 195–197 with a sentence and a bulleted list linking to each module page in nav order,
and then keeps the `## Specific Integration Requirements` section (line 4135 to the end).

- [ ] **Step 2: Check that no entry line was lost or duplicated**

Run:
```bash
diff <(git show HEAD:docs/api-access-to-adam.md | sed -n '199,4134p' | sort) \
     <(for f in docs/api-*.md; do [ "$f" = docs/api-access-to-adam.md ] || awk '/^### /{p=1} p' "$f"; done | sort)
```
Expected: no output. Blank-line differences at page boundaries are the only acceptable difference.

- [ ] **Step 3: Write each module page's opening text**

Under each title: one or two sentences on what the area covers, the line "All endpoints on this page are under
`/api/<prefix>/`." (list each prefix for multi-prefix pages), and a link to
`api-access-to-adam.md#authentication`. Follow `writing-user-documentation`. Remove the sentence saying other
resources are not listed until they are stable.

- [ ] **Step 4: Update the navigation**

In `mkdocs.yml`, replace line 144 with an `"Appendix C: API Access to ADAM"` section: the overview first, then the
module pages alphabetically by title, then "Other Endpoints" last.

- [ ] **Step 5: Run the audit**

Run: `.venv/bin/python scripts/audit_api_endpoints.py --adam /home/philip/dev/adam/.worktrees/remove-migration-api`
Expected: exit 1, with only the 7 undocumented endpoints, the 1 not-in-source heading, and the duplicate
`pupils/image:get (api-pupils.md, api-pupils.md)`. No wrong-page or prefix findings.

- [ ] **Step 6: Commit the move**

Message: "Split the API documentation into one page per module". Committing before the link fixes keeps the move
reviewable as a pure move.

- [ ] **Step 7: Fix links and check them with anchor validation on**

Search with `grep -rn "api-access-to-adam.md#\|](#" docs/` and repoint every link whose target moved:
- links in other pages to endpoint anchors and to `#create-a-data-query-secret`, which is now on `api-data-query.md`;
- links inside module pages to anchors that are now on a different page (for example the `Classes/list:get` link
  at the original line 1195 stays on `api-classes.md`, but check each one).

Then create `/tmp/claude-1000/-home-philip-dev-adam-docs/46e99c3e-efa3-40b2-a152-7f93661d1824/scratchpad/anchors.yml`:
```yaml
INHERIT: /home/philip/dev/adam-docs/mkdocs.yml
docs_dir: /home/philip/dev/adam-docs/docs
validation:
  anchors: warn
```
Run: `.venv/bin/mkdocs build --strict -f /tmp/claude-1000/-home-philip-dev-adam-docs/46e99c3e-efa3-40b2-a152-7f93661d1824/scratchpad/anchors.yml --site-dir /tmp/claude-1000/-home-philip-dev-adam-docs/46e99c3e-efa3-40b2-a152-7f93661d1824/scratchpad/site-anchors`
Expected: the build succeeds. If it fails on broken anchors in pages this work did not touch, record them for the
user and do not fix them here; nothing in the API pages or in links to them may appear in the warnings.

- [ ] **Step 8: Build the site and the PDF as CI does**

Run: `bin/build.sh --dev` and `.venv/bin/mkdocs build -f mkdocs.pdf.yml --site-dir /tmp/claude-1000/-home-philip-dev-adam-docs/46e99c3e-efa3-40b2-a152-7f93661d1824/scratchpad/site-pdf`
Expected: both succeed. If the PDF build cannot run locally (it needs `requirements-pdf.txt`), say so in the report
instead of skipping silently.

- [ ] **Step 9: Commit**

Message: "Point links at the new API pages".

---

### Task 5: Close the coverage gap

**Files:**
- Modify: `docs/api-reporting.md`, `docs/api-pupils.md`, `docs/api-families.md`, `docs/api-family-relationships.md`,
  `docs/api-classes.md`, `docs/api-psychometric.md`

**Interfaces:**
- Consumes: the pages from Task 4 and the audit from Task 3.

- [ ] **Step 1: Fix the mistyped heading**

Change `### Reporting/pupilreportingperiods:ge` to `:get`, along with its `{#reportingpupilreportingperiodsge-...}`
anchors. Check the entry against `apiGetPupilReportingPeriods` (or whatever method `reporting/pupilreportingperiods`
maps to in the source), and correct it where it differs.

- [ ] **Step 2: Merge the two `Pupils/image:get` entries**

Keep the copy that documents `<width>`. Take anything correct and missing from the other copy. Drop the wrong example
URL `/api/reporting/pupils/image/123`. Check the result against the method in the ADAM source.

- [ ] **Step 3: Add the two alias entries**

`### Families/get_children_by_family:get` on `api-families.md` and `### Psychometric/assessments_by_category:get` on
`api-psychometric.md`. Each says it is equivalent to the full entry and links to it. Place each directly after its
full entry.

- [ ] **Step 4: Document the four missing endpoints**

`classes/enrolment:get`, `families/email:patch`, `families/emailpreferences:patch`, `familyrelationships/family:patch`.
For each, find its method in `methods_apiresource.php`, read it in the ADAM source, and write an entry in the house
format (description, `#### Request`, `#### Parameters`, `#### Response`, and an example where the neighbouring entries
have one), using `writing-user-documentation`. Put each next to the entries for the same path (for example
`Families/email:patch` after `Families/email:post`).

- [ ] **Step 5: Run the audit**

Run: `.venv/bin/python scripts/audit_api_endpoints.py --adam /home/philip/dev/adam/.worktrees/remove-migration-api; echo "exit $?"`
Expected: `All 99 endpoints are documented on the correct pages.` and `exit 0`.

- [ ] **Step 6: Run the anchor-checking build from Task 4 Step 7 again**

Expected: no warnings from the API pages.

- [ ] **Step 7: Commit**

Message: "Document the remaining API endpoints".

---

### Task 6: The auditing skill

**Files:**
- Create: `.claude/skills/auditing-api-docs/SKILL.md`

**Interfaces:**
- Consumes: the command line from Task 3 and the page layout from Task 4.

- [ ] **Step 1: Write the skill**

Front matter in the style of `.claude/skills/capturing-screenshots/SKILL.md`, with `name: auditing-api-docs` and a
`description` starting "Use when". The body covers what the spec's Part 4 lists: when to run the audit, checking the
ADAM branch and running `php adam build` if `methods_apiresource.php` may be stale, the exact command, how to resolve
each of the seven finding types, and rerunning the audit and the anchor-checking build until both pass. Say that
`scripts/generate_nav.mjs` must not be run, because it flattens the navigation.

- [ ] **Step 2: Test the skill on a planted fault**

In a scratch copy, or on the branch and then reverted: delete one alias entry and add a prefix to two pages. Follow
the skill as written, with nothing else to go on. Expected: the audit reports exactly those two findings, and
the skill's instructions are enough to fix both. Revert the plant.

- [ ] **Step 3: Commit**

Message: "Add a skill for auditing the API documentation".

- [ ] **Step 4: Report the remaining step to the user**

The ADAM PR is still waiting for the user's review. Once it is merged, run the audit with the default `--adam`
against `/home/philip/dev/adam` on `development` and confirm exit 0. Then remove the worktree and drop
`adam_agent_remove_migration`.
