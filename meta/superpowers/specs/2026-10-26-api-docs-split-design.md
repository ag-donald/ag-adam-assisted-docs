# Splitting the API documentation, with an endpoint audit

## Intent

Appendix C, `docs/api-access-to-adam.md`, is a single page of 4,137 lines. It holds the API introduction, token
management, request and response conventions, and 92 endpoint entries. Its readers are schools and third parties who
are building integrations with ADAM. At this length, an integrator can't find the endpoints for one area of ADAM
without scrolling through all the others.

Nothing checks the page against the code either. Endpoints are added to ADAM and the docs fall behind. Today the source
serves 104 endpoints and the docs cover 91 of them correctly.

This work has three goals:

1. Split the API documentation into one page per module (URL prefix).
2. Make coverage deterministically verifiable. A script compares the endpoints ADAM serves with the endpoints the docs
   describe, and a Claude skill runs that script and acts on what it reports.
3. Close the current gap so that the audit passes.

## Goals

- An overview page plus one page per module, reachable from the navigation and included in the PDF manual.
- An audit script that always gives the same result for the same inputs, and exits non-zero when coverage is
  incomplete.
- A project skill that tells Claude when to run the audit and how to resolve each kind of finding.
- Every endpoint ADAM serves is documented on the correct page. The audit reports nothing.
- The unused migration endpoints are removed from ADAM.

## Non-goals

- Keeping old deep links from outside the site working. A bookmarked URL such as
  `api-access-to-adam.html#dataquerygetget` will land on the overview page without reaching the endpoint, or 404 if
  the page moved. The user accepted this. No redirect script is added.
- Alerting ADAM developers when they add an endpoint. Running the audit in ADAM's CI or in the docs build may come
  later, but nobody has decided where. The script must not be designed in a way that rules that out.
- Rewriting the existing endpoint entries. They move as they are, apart from the fixes listed below.
- Changing the order of the existing endpoint entries beyond grouping them by module.

## Anti-goals

- Coverage judged by reading. If a human or a model has to decide whether an endpoint is "covered", the requirement
  has failed. Only the script decides.
- Broken links inside the manual. Every link from another page of this repository to Appendix C must still resolve
  after the split.
- Pages titled only by URL prefix. Integrators look for "Families" or "Reporting", not for `familyrelationships`.

## Constraints and facts

### Where endpoints come from

ADAM declares each endpoint with a PHP attribute on a static or instance method:

```php
#[ApiResource ("get", "absentees/summarycount")]
```

`php adam build` compiles every declaration into `~/dev/adam/includes/methods_apiresource.php`. That file is committed
to the ADAM repository. Each entry has `callback`, `method` (lower case) and `endpoint` (lower case, `prefix/name`). It
is the router's own list, so it is the source of truth for the audit.

One method can carry more than one `ApiResource` attribute. Three do today:

| Method                                          | Endpoints                                                                     |
|-------------------------------------------------|-------------------------------------------------------------------------------|
| `FamilyRelationships::apiGetChildren`           | `families/children:get`, `families/get_children_by_family:get`                |
| `Psychometric::apiGetAssessmentsByCategory`     | `psychometric/assessmentsbycategory:get`, `psychometric/assessments_by_category:get` |
| `PupilsApi::searchByID`                         | `pupils/searchbyid:get`, `pupils/search-id:get`                               |

### How the docs name endpoints

Each endpoint entry is a level-3 heading of the form `### Prefix/name:method`, for example
`### Families/children:get`. The prefix is title-cased in the docs and lower case in the source, so the comparison
ignores case. Some headings carry an explicit anchor such as `{#api-resources-pupilsimageget}`. The parser must ignore
that suffix. Four endpoints have three path segments, for example `reporting/grade/comments`, so the parser must allow
more than one `/`. The prefix is always the first segment.

### The current gap (12 endpoints in the source, not in the docs)

- Five `migration/*` endpoints. These are removed from ADAM (see Part 1).
- Two aliases: `families/get_children_by_family:get` and `psychometric/assessments_by_category:get`.
- Four endpoints with no documentation at all:
  - `classes/enrolment:get`
  - `families/email:patch`
  - `families/emailpreferences:patch`
  - `familyrelationships/family:patch`
- One endpoint with a typo in its heading. `reporting/pupilreportingperiods:get` has an entry at line 3236, but the
  heading reads `### Reporting/pupilreportingperiods:ge`. That heading is also the only documented endpoint the source
  does not serve.

### Other known defects in the current page

- `Pupils/image:get` appears twice. One copy sits among the Families entries, around line 1894. It omits the optional
  `<width>` parameter and its example URL is wrong (`/api/reporting/pupils/image/123`). The other copy, in the Pupils
  entries around line 2673, is more complete.
- `Questions/questionbreakdown:get` sits among the Assessment entries. Grouping by prefix moves it.
- A `## Specific Integration Requirements` section sits after the endpoint entries, at the end of the page. It moves
  to the overview page.
- The "API Resources" introduction says that other resources exist but are not listed until they are stable. That
  contradicts full coverage, so the sentence is removed.

### Inbound links that must keep working

- `third-party-integration.md` and `moodle-integration.md` link to `api-access-to-adam.md#api-access-to-adam`,
  `#managing-api-tokens-in-adam` and `#create-a-data-query-secret`.
- `online-applications.md` links to `api-access-to-adam.md#applicationscreatepost`.
- The `#create-a-data-query-secret` anchor is inside the DataQuery entries, not the general material. It moves to the
  DataQuery page, so the links to it from `third-party-integration.md` must be updated.
- Intra-page links inside the endpoint entries (for example `[created above](#create-a-data-query-secret)` in the
  DataQuery entries) become cross-page links when the entries move.

The builder must find every such link with a search, not rely on this list. The site build in `--dev` mode runs
`mkdocs build --strict`, which fails on broken links, and that is the final check.

### Repository conventions

- `docs/` is flat. Every page is a single file in `docs/`.
- The navigation is in `mkdocs.yml`. The PDF build (`mkdocs.pdf.yml`) inherits it, so `mkdocs.yml` controls the
  page order of both the site and the PDF manual.
- `scripts/chapters.json` and `scripts/generate_nav.mjs` are left over from the one-off Google Docs conversion.
  `generate_nav.mjs` rewrites the nav as a flat alphabetical list and would erase the new Appendix C section. Neither
  is edited or run as part of this work.
- Project skills live in `.claude/skills/<name>/SKILL.md`. `capturing-screenshots` is the existing example.
- Repository scripts are Python, with `unittest` tests beside them (`scripts/rewrite_anchors.py` and
  `scripts/test_rewrite_anchors.py`).
- New user-facing text follows the `writing-user-documentation` skill.

## Part 1: Remove the migration code from ADAM

This is done first, in `~/dev/adam`, so that the audit's source list is final before the docs work starts.

- Delete `classes/ADAM/Support/Database/Migration.php`, which declares the five `migration/*` endpoints.
- Delete `classes/ADAM/Support/Database/MigrationImporter.php`, which is the only client of those endpoints. Nothing
  else references it.
- Delete `tests/Unit/Support/Database/MigrationTest.php`.
- Run `php adam build` to regenerate `includes/methods_apiresource.php`. It should then list 99 endpoints.
- Remove the `Migration::apiGetTableData` and `Migration::apiGetTableRows` entries from `sql-audit-baseline.json`.
- Search for any other reference (config, docs, CLI commands, PHPStan baseline entries) and remove it.
- Run the test suite and static analysis as ADAM's `AGENTS.md` describes.

Work on a new branch from ADAM's `development` branch, following ADAM's own commit conventions. Push the branch and
open a pull request against `development`. The user reviews and merges it. Until it is merged, the docs work is audited
against that branch. The user decided this removal and this review step.

## Part 2: The page split

### Pages

- **Overview: `docs/api-access-to-adam.md`.** This keeps its file name and its title, "API Access to ADAM". It holds
  everything before "API Resources": the introduction, managing API tokens, best practice security principles, and API
  interactions (authentication, requests, responses). The "API Resources" heading is replaced by a short list that
  links to each module page.
- **Module pages: `docs/api-<module>.md`.** One page per ADAM area. A page holds one or more prefixes.
- **Other Endpoints: `docs/api-other-endpoints.md`.** One page for single-endpoint prefixes that have no natural home
  on a module page.

The user left the grouping to Claude. It is based on ADAM areas, not on endpoint counts:

| Page                         | Title                 | Prefixes                                                                 |
|------------------------------|-----------------------|--------------------------------------------------------------------------|
| `api-absentees.md`           | Absentees             | `absentees`, `absenteekiosk`                                             |
| `api-applications.md`        | Online Applications   | `applications`                                                           |
| `api-assessment.md`          | Assessment            | `assessment`, `questions`                                                |
| `api-calendar.md`            | Calendar              | `calendar`                                                               |
| `api-classes.md`             | Classes               | `classes`                                                                |
| `api-data-query.md`          | Data Query            | `dataquery`                                                              |
| `api-devman-export.md`       | DevMan Export         | `xdevman`                                                                |
| `api-documents.md`           | Documents             | `documents`                                                              |
| `api-families.md`            | Families              | `families`, `familylogin`                                                |
| `api-family-relationships.md`| Family Relationships  | `familyrelationships`                                                    |
| `api-messaging-logs.md`      | Messaging Logs        | `messaginglogs`                                                          |
| `api-psychometric.md`        | Psychometric          | `psychometric`                                                           |
| `api-pupils.md`              | Pupils                | `pupils`                                                                 |
| `api-records-and-points.md`  | Records and Points    | `recordsandpoints`                                                       |
| `api-registration.md`        | Registration          | `registration`, `registrations`                                          |
| `api-reporting.md`           | Reporting             | `reporting`                                                              |
| `api-subjects.md`            | Subjects              | `subjects`                                                               |
| `api-other-endpoints.md`     | Other Endpoints       | `admin`, `changelog`, `cron`, `export`, `externalauth`, `formfields`, `leaves`, `medical`, `request`, `staff`, `tablefields` |

The builder may adjust a title or merge two pages if reading the entries shows that a different grouping is clearer.
Any such change must be made in the page declarations (below), which the audit reads.

### Declaring prefixes

Each API page, including the Other Endpoints page, declares the prefixes it holds in YAML front matter:

```yaml
---
api_prefixes:
  - families
  - familylogin
---
```

The overview page declares none. This front matter is the only place the mapping lives. Adding a new page means adding
a file with this front matter; the script has no hard-coded list. The builder must confirm that MkDocs and the PDF hooks
ignore this key, which they should, since MkDocs passes unknown front matter keys through as page metadata.

### Page content

- Each module page has a plain-language title naming the ADAM area, for example "Families" or "Data Query". The URL
  prefix appears in the opening text, for example "All endpoints on this page are under `/api/families/`." The builder
  chooses the titles.
- Each module page opens with one or two sentences on what the module covers, and a link to the overview page's
  authentication section. Integrators may arrive at a module page straight from a search.
- Endpoint headings keep their current form, `### Prefix/name:method`. The audit depends on that form.
- Endpoint entries move without being rewritten. The exceptions are the fixes listed under "Other known defects", and
  links that must change because their target moved.

### Navigation and PDF

- In `mkdocs.yml`, "Appendix C: API Access to ADAM" becomes a section. The overview comes first, then the module pages
  in alphabetical order by title, then "Other Endpoints" last. The PDF manual picks this up through `mkdocs.pdf.yml`.

## Part 3: The audit script

`scripts/audit_api_endpoints.py`, with tests in `scripts/test_audit_api_endpoints.py`.

### Inputs

- The ADAM checkout. The default is `~/dev/adam`, and a `--adam <path>` option overrides it. The script reads
  `<adam>/includes/methods_apiresource.php` as text and extracts each `'method' => '...'` and `'endpoint' => '...'`
  pair. It must not need PHP to run.
- The docs. The script reads every `docs/api-*.md` file plus `docs/api-access-to-adam.md`. From each page it collects
  the `api_prefixes` front matter and every `### Prefix/name:method` heading.

### Checks

The script normalises everything to lower case, then reports:

1. **Undocumented.** The source serves the endpoint, but no heading describes it.
2. **Not in source.** A heading describes an endpoint the source does not serve.
3. **Duplicated.** More than one heading describes the same endpoint.
4. **Wrong page.** The heading's prefix is not declared by the page it sits on. An endpoint heading on the overview
   page is always on the wrong page.
5. **Unassigned prefix.** The source has a prefix that no page declares.
6. **Prefix declared twice.** More than one page declares the same prefix.
7. **Stale prefix.** A page declares a prefix the source does not serve.

### Output

- Findings are grouped by check and sorted alphabetically within each group, so two runs over the same inputs print
  identical output.
- Exit status 0 when there are no findings, 1 when there are findings, and 2 when the inputs cannot be read (for
  example, the ADAM checkout is missing).
- A `--json` option prints the same findings as JSON, for later use in CI or by the skill.

### Aliases

An alias is a separate endpoint. Both URLs need their own heading. My call: the alias gets a short entry of its own
that says which endpoint it is equivalent to and links to the full entry. This keeps the rule "one heading per
endpoint" with no exceptions in the script. The builder chooses the wording.

### Tests

Unit tests cover the PHP parser, the heading and front matter parsers (including headings with `{#...}` anchors), each
of the seven checks,
and the exit statuses. The tests use small fixture files, not the real ADAM checkout.

## Part 4: The skill

`.claude/skills/auditing-api-docs/SKILL.md`. It tells Claude to:

- Run the audit when asked to audit or update the API documentation, after ADAM has gained or lost endpoints, and
  before finishing any change to an API page.
- Check which branch the ADAM checkout is on and say so in the report. Normally it is `development`. During this
  work it is the migration-removal branch until that branch is merged. Check that `includes/methods_apiresource.php`
  is current; if in doubt, run `php adam build` in the ADAM checkout first.
- Resolve findings by type:
  - **Undocumented:** read the endpoint's method in the ADAM source and write an entry in the house format on the
    correct page, following `writing-user-documentation`.
  - **Not in source:** confirm with the user before deleting the entry. The endpoint may have been renamed, in which
    case the entry is updated instead.
  - **Duplicated:** merge the entries, keeping the more accurate content.
  - **Wrong page:** move the entry and fix any links to it.
  - **Unassigned prefix:** decide which page the prefix belongs on. Add it to the `api_prefixes` of a related module
    page, give it a new page if it is a new ADAM area with several endpoints, or add it to Other Endpoints. A new page
    is added to the Appendix C section of `mkdocs.yml`.
  - **Prefix declared twice:** keep the declaration on the page that holds its entries and remove the other.
  - **Stale prefix:** remove the declaration once the page holds no entries for it.
- Run the audit again and the strict site build until both pass.

## Part 5: Close the gap

- Fix the `Reporting/pupilreportingperiods:ge` heading, and check its entry against the source.
- Document the four missing endpoints from their ADAM source, in the house format, on their module pages.
- Add alias entries for `families/get_children_by_family:get` and `psychometric/assessments_by_category:get`. The
  existing `pupils/searchbyid:get` and `pupils/search-id:get` entries are already separate. Leave them as they are,
  or make the alias one point to the other if that reads better.
- Merge the two `Pupils/image:get` entries into the Pupils page, keeping the more complete one.
- The docs work is finished when the audit exits 0 against the migration-removal branch and the strict site build
  passes. It is fully finished once that branch is merged and the audit still exits 0 against `development`.

## Order of work

1. Part 1, in ADAM.
2. Part 3, the audit script with tests. Run it against the current single page to confirm that it reports the
   expected gap, that every existing heading is on the wrong page, and that every prefix is unassigned.
3. Part 2, the split. Then the audit should report only the undocumented endpoints, the mistyped heading and the
   duplicate.
4. Part 5, closing the gap.
5. Part 4, the skill, written last so that it describes the finished workflow.

## Calls made by Claude, not by the user

- The page grouping in the table under "Pages" (the user left it to Claude).
- The prefix-to-page mapping lives in each page's front matter, not in the script or a separate file.
- Pages stay flat in `docs/` as `api-<module>.md`, not in a subdirectory, to match the rest of the manual.
- The overview keeps the file name `api-access-to-adam.md`, so existing links to its sections keep working.
- The audit reads the generated `methods_apiresource.php` rather than scanning PHP attributes.
- Aliases are documented as separate short entries.
- The "not listed until stable" sentence is removed.
- The script is Python, to match the repository's other scripts.
- `scripts/chapters.json` is not updated, because it no longer controls anything.

## Left to the builder

- Module page titles and opening text.
- The wording of alias entries and new endpoint entries.
- Command-line details of the script beyond what is specified above.
- Branch names and commit structure in both repositories.
