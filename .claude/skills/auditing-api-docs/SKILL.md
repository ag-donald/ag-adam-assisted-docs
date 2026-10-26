---
name: auditing-api-docs
description: Use when asked to audit or update the ADAM API documentation, after ADAM gains or loses API endpoints, or before finishing any change to a docs/api-*.md page
---

# Auditing the API Documentation

`scripts/audit_api_endpoints.py` compares the endpoints ADAM serves with the entries on the `docs/api-*.md` pages. Run it whenever you are asked to audit or update the API documentation, after ADAM has gained or lost endpoints, and before you finish any change to an API page.

## Before you run it

Check which branch the ADAM checkout is on, and say so in your report:

```bash
git -C ~/dev/adam branch --show-current
```

Normally it is `development`. If it is another branch, the audit describes that branch, not the released API.

The audit reads `~/dev/adam/includes/methods_apiresource.php`. `php adam build` generates that file from the `#[ApiResource ("get", "prefix/name")]` attributes. If ADAM has changed since the last build, or you are not sure, rebuild first:

```bash
cd ~/dev/adam && php adam build
```

## Run the audit

```bash
python3 scripts/audit_api_endpoints.py
```

Options: `--adam <path>` for another ADAM checkout, `--docs <path>` for another docs directory, `--json` for machine-readable output.

Exit 0 means the docs match the source. Exit 1 means there are findings, listed under the headings below. Exit 2 means an input could not be read (missing `methods_apiresource.php`, bad front matter); fix the input and run again.

## Resolve each finding

Pages declare the URL prefixes they hold in `api_prefixes` front matter. An entry belongs on the page that declares its prefix. Entry headings look like `### Prefix/name:method`, with sub-headings `#### Request {#prefixnamemethod-request}`.

- **Undocumented:** find the endpoint in `includes/methods_apiresource.php` to get its class and method, and read that method in the ADAM source. Write an entry on the page that declares its prefix, in the same format as its neighbours. Follow the `writing-user-documentation` skill. If the endpoint is an alias of another, write a short entry that points to the original, as `Families/get_children_by_family:get` does.
- **Not in source:** the page has an entry ADAM no longer serves. Ask the user before you delete it. If ADAM renamed the endpoint, update the entry instead.
- **Duplicated:** the same heading appears more than once. Merge the entries, keep the more accurate content, and fix links to the one you removed.
- **Wrong page:** move the entry to the page that declares its prefix and fix any links to it.
- **Unassigned prefix:** no page declares this prefix. Decide where it belongs. Add it to `api_prefixes` on a related module page, or add it to `api-other-endpoints.md`. If it is a new ADAM area with several endpoints, create a new `docs/api-<module>.md` with `api_prefixes` front matter and add it to the Appendix C section of `mkdocs.yml`.
- **Prefix declared twice:** keep the declaration on the page that holds its entries and remove the other. If neither page holds entries for it, remove both (the audit also reports it as stale).
- **Stale prefix:** remove the declaration from the page once the page holds no entries for it.

Do not run `scripts/generate_nav.mjs`. It flattens the navigation in `mkdocs.yml`.

## Check the result

Run the audit again until it exits 0. Then build the site with anchor checking. The normal strict build does not check anchors, so make a config in a scratch location (do not commit it):

```yaml
INHERIT: /home/philip/dev/adam-docs/mkdocs.yml
docs_dir: /home/philip/dev/adam-docs/docs
validation:
  anchors: warn
```

```bash
.venv/bin/mkdocs build --strict -f <that config> --site-dir <a scratch directory>
```

Fix every warning, then run the audit and this build once more. Both must pass.
