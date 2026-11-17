# ADAM User Documentation

End-user documentation for ADAM (Academic Data Manager), authored as Markdown and built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Local development

### Option A: Python venv

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

The site is served at `http://127.0.0.1:8000` and live-reloads on change.

### Option B: Docker (no Python install required)

```bash
docker run --rm -it --user "$(id -u):$(id -g)" \
    -p 8000:8000 -v "$(pwd):/docs" -w /docs \
    squidfunk/mkdocs-material:latest serve --dev-addr=0.0.0.0:8000
```

Replace `serve --dev-addr=0.0.0.0:8000` with `build --strict` to produce a static site under `site/`.

## Authoring conventions

- One Markdown file per top-level chapter, lower-kebab-case filenames under `docs/`.
- UI labels are in **bold**.
- Menu paths are written as natural prose: "click on the **Administration tab**, then under the **Absentee Administration heading**, click on **Edit the absentee reasons**."
- Screenshots live under `docs/assets/screenshots/<chapter-slug>/` and are referenced with relative paths.

## Screenshots

Screenshots are captured against the local screenshot site, `https://screenshot.theta.adam.co.za/`.
Apache serves it from the ADAM checkout against `adam_agent_screenshot`, a randomised copy of the ADAM
database. Never capture against production, or against
`dev.theta.adam.co.za`, whose database holds a real school's data. An agent can capture them: see the
`capturing-screenshots` skill in
[`.claude/skills/capturing-screenshots/SKILL.md`](.claude/skills/capturing-screenshots/SKILL.md), and
copy `.mcp.json.dist` to `.mcp.json`. Check two values for your machine:

- the screenshot site's origin, in `--allowed-origins`. The template already names
  `https://screenshot.theta.adam.co.za`; change it only if your screenshot site runs elsewhere, and never
  to a host that serves real school data;
- the Chromium executable path, in `--executable-path`, which is a placeholder. This lives wherever Playwright cached the
  browser it downloaded, typically `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome` — run
  `ls ~/.cache/ms-playwright/` to see the exact version installed and fill in the real path.

## The PDF manual

The whole manual is also published as a single PDF, linked from the home page and served at
`/adam-manual.pdf`. It is **not** built by `bin/build.sh`: rendering it needs a headless Chromium that
the mkdocs image does not carry, and the deploy script runs every five minutes.

Instead [`.github/workflows/pdf.yml`](.github/workflows/pdf.yml) builds it on every push to `main`
that touches the documentation, and uploads it to the `manual-pdf` release. `bin/build.sh` then
collects that asset into each deploy, with a conditional request so an unchanged manual costs one
round trip rather than 40 MB. A missing or unreachable PDF is never fatal to a deploy; it just leaves
the download link 404ing until the next successful workflow run.

To build it yourself:

```bash
pip install -r requirements.txt -r requirements-pdf.txt
python -m playwright install --with-deps chromium
mkdocs build -f mkdocs.pdf.yml --site-dir site-pdf
```

That takes a couple of minutes and writes `site-pdf/adam-manual.pdf` (~750 pages, ~40 MB) alongside a
PDF of each individual chapter.

[`mkdocs.pdf.yml`](mkdocs.pdf.yml) inherits the whole site config, so the two builds cannot drift
apart, and adds five hooks that exist only for the PDF: `hooks/pdf_theme.py` (makes this theme
printable), `hooks/pdf_links.py` (stops `mailto:` addresses being rewritten into web URLs),
`hooks/pdf_bookmarks.py` (adds the chapter bookmarks), `hooks/pdf_cover.py` (dates the front cover)
and `hooks/pdf_internal_links.py` (keeps cross-references inside the document). Each explains in its
docstring what breaks without it — all five failures are silent, producing a PDF that builds
successfully and is wrong. `hooks/test_pdf_internal_links.py` covers the link rewriting; run it with
`python -m unittest discover -s hooks`.

A cross-reference between chapters is a link within the PDF, and lands on the heading it names rather
than at the top of the chapter. That takes two steps, because a page is rendered long before anything
knows where it sits in the manual: `hooks/pdf_theme.py` puts a hidden anchor after every heading,
which is what makes Chrome record a destination for it, and `hooks/pdf_internal_links.py` resolves
each link against those destinations once the chapters have been assembled. Links it cannot place —
other websites, `mailto:` addresses, and the reference to the site's own home page — stay as they
are.

The manual opens on a cover page: the site header's blue, the ADAM logo, and the date of the last
commit that touched `docs/`. Its markup is [`pdf/cover.html`](pdf/cover.html) and its styling is the
`Front cover` section of [`pdf/print.css`](pdf/print.css); `hooks/pdf_cover.py` fills in the date,
because mkdocs-exporter reads cover templates as plain text rather than as Jinja. The cover is
attached to every page and then removed from all but the first by `aggregator.covers: limits`, so
each per-chapter PDF carries a copy of it too. Nothing publishes those, so it does not matter.

Every page after the cover carries its number at the foot. The numbers run continuously across all 100
chapters, which they would not do by themselves — each chapter is rendered as its own document and
the aggregator concatenates them — and they match the page numbers a PDF reader shows, because the
cover is counted even though it is left unnumbered.

## Deployment

The site is self-hosted at `https://help.adam.co.za/`, served as static files by the same web server that hosts ADAM. The deployment server runs `bin/build.sh` from a cron, which:

1. fetches the latest commit on `main`,
2. builds the site via the `squidfunk/mkdocs-material` Docker image,
3. atomically swaps the freshly-built `site/` into the path the web server reads from.

If `main` has not advanced since the last build, the script exits without rebuilding.

### One-time server setup

```bash
# Clone alongside any existing checkouts
git clone git@github.com:phinor/adam-docs.git /opt/adam-docs

# Pre-pull the build image so the first cron run isn't slow
docker pull squidfunk/mkdocs-material:latest

# Point the web server at the build output. Either:
#   (a) leave PUBLISH_DIR empty so the site is built in /opt/adam-docs/site/,
#       and configure the vhost root to that path, or
#   (b) export PUBLISH_DIR to wherever the existing vhost already serves from
#       (e.g. /var/www/help.adam.co.za) so no nginx/Apache changes are needed.
```

### Cron entry

Every five minutes is generally fine — the no-op path is cheap.

```cron
*/5 * * * * PUBLISH_DIR=/var/www/help.adam.co.za /opt/adam-docs/bin/build.sh >> /var/log/adam-docs.log 2>&1
```

Set `FORCE_PULL=1` once a week (or in a separate weekly entry) if you want the script to refresh the MkDocs Docker image.

### Switching from the legacy pipeline

The old `adam-documentation` PHP project deployed to the same `help.adam.co.za` vhost. To cut over:

1. Disable its cron (`generate.php`).
2. Run `bin/build.sh` once on the server with `PUBLISH_DIR` pointing at the existing vhost root — the old HTML is replaced with the MkDocs build.
3. Verify the site loads, then enable the new cron entry.

The legacy repo can stay checked out as a fallback until the new site is validated.

## History

This site replaces a fragile pipeline that consumed a Google Doc published as HTML. The initial Markdown corpus was converted from that source by `scripts/convert.mjs`.

## Licence

Two licences, split by what the file is. The documentation under `docs/` is CC
BY-NC-SA 4.0; the build and theme machinery is MIT. See [LICENSE](LICENSE) for
the split, the trade mark position and the text-and-data-mining reservation,
and [CONTRIBUTING.md](CONTRIBUTING.md) for the terms a contribution arrives
under.
