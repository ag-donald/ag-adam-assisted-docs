"""MkDocs build-time hook: teach mkdocs-exporter how to print this theme.

Loaded only by `mkdocs.pdf.yml`; the website build never sees it.

Three things stand between this theme and a paginated PDF, and all of them are
silent failures — the build reports success and hands back blank or missing
pages — so each is worth recording.

**The exporter does not know this theme.** `mkdocs_exporter.themes.factory`
matches on `theme.name`, and ships adapters only for `material` and
`readthedocs`. A `custom_dir`-only theme like ours has `name: null`, so the
factory raises `RuntimeError` before a page is rendered. Registering an adapter
below is what makes the real theme usable; borrowing `readthedocs` instead
would silently apply another theme's assumptions to our markup.

**paged.js empties the page when a stylesheet mentions `position: fixed`.**
Its parser harvests *every* selector whose rule carries that declaration,
ignoring the media query the rule is nested in, then lifts the matching
elements out of the flow to repeat them on each page. `theme/css/styles.css`
declares `article { position: fixed }` inside `@media screen and (min-width:
640px)`, which makes the whole content container a fixed overlay: paged.js then
paginates an empty flow and every page comes out blank. No later override can
undo this — the declaration's presence is what counts, not whether it wins the
cascade — so the screen-only rules have to be gone before the CSS is parsed.
They mean nothing in print regardless.

**Two embeds stall the browser until it times out.** The Google CSE script
fetches cross-origin CSS that is refused under `file://`, and pagination never
completes. A YouTube iframe never settles either, so Playwright's `networkidle`
wait expires and the page is lost from the manual. Both are worthless on paper.

The chrome is removed from the DOM rather than hidden with CSS: `header` and
`nav` are `position: fixed` too, and paged.js mis-places the content when they
are present, `display: none` or not.

The adapter also prepares the DOM for `hooks/pdf_internal_links.py`, which
cannot do the work itself: the destinations a PDF can be sent to are decided
while the page is rendered, long before the manual it belongs to exists.
"""

import logging
import os
import re

from mkdocs_exporter.preprocessor import Preprocessor
from mkdocs_exporter.theme import Theme as BaseTheme
from mkdocs_exporter.themes.factory import Factory

log = logging.getLogger('mkdocs.hooks.pdf_theme')

# Where the built site lives. Stylesheet hrefs are resolved against it so the
# CSS can be read off disk and inlined. Set from the config, because the
# adapter is handed a DOM and nothing else.
site_dir = None

# Elements belonging to the website rather than to the printed manual. The
# licence footer is one of them: it is per-page markup, so leaving it in would
# repeat the whole notice at the foot of every chapter. The PDF states its
# terms once instead, in the `Copyright and Reuse` section of `docs/index.md`,
# which the aggregator places on its first page. Document metadata is not an
# option: mkdocs-exporter 6.2.0 accepts `aggregator.metadata` in the config
# and then calls `Aggregator.save()` with no arguments, so the dict is parsed
# and discarded.
CHROME = ['header', 'nav', '#navtoggle', '.toc-sidebar', '.searchbar', '.site-footer']

# `@media screen` and everything it contains, matched to its closing brace by
# `strip_screen_rules` rather than by a regex, which cannot count braces.
SCREEN_AT_RULE = re.compile(r'@media\s+screen[^{]*\{')

YOUTUBE_EMBED = re.compile(r'youtube\.com/embed/([A-Za-z0-9_\-]+)')


def on_config(config):
    """Records the site directory for the theme adapter."""

    global site_dir

    site_dir = config['site_dir']

    return config


def strip_screen_rules(css):
    """Removes every `@media screen` block from a stylesheet.

    Brace counting, because the blocks nest: `@media screen { article { ... } }`
    ends at the second closing brace, and a non-greedy regex stops at the first.
    An unterminated block (a truncated file) consumes the remainder, which
    fails towards dropping styles rather than towards emitting broken CSS.
    """

    out = []
    index = 0

    for match in SCREEN_AT_RULE.finditer(css):
        if match.start() < index:
            # Inside a block already consumed by the previous iteration.
            continue

        out.append(css[index:match.start()])

        depth = 1
        position = match.end()

        while depth and position < len(css):
            if css[position] == '{':
                depth += 1
            elif css[position] == '}':
                depth -= 1
            position += 1

        index = position

    out.append(css[index:])

    return ''.join(out)


class Theme(BaseTheme):
    """The ADAM documentation theme."""

    # Matches a theme declared as `name: null` with a `custom_dir`.
    name = None

    def preprocess(self, preprocessor):
        """Prepares the document for pagination."""

        preprocessor.remove(CHROME)
        self.link_destinations(preprocessor)
        self.flatten_embeds(preprocessor)
        self.inline_stylesheets(preprocessor)

    def link_destinations(self, preprocessor):
        """Gives every heading somewhere for a link to point at.

        Chrome writes a named destination for each `<a href="#id">` a document
        contains, and only for those: an id nothing links to is not a place the
        PDF can be sent to. With `permalink: false` the pages carry no heading
        anchors, so `hooks/pdf_internal_links.py` would have nothing to resolve
        a cross-reference against.

        A `display: none` link is enough — the destination is written, no mark
        appears, and no clickable box is added to the page.
        """

        for heading in preprocessor.html.select('h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]'):
            anchor = preprocessor.html.new_tag('a', href='#' + heading['id'])

            anchor['style'] = 'display: none'

            heading.insert_after(anchor)

    def flatten_embeds(self, preprocessor):
        """Turns video embeds into links.

        An iframe cannot be watched on paper, and a YouTube one never settles
        under `file://`, so the page would be dropped from the manual entirely.
        A link keeps the reference and costs nothing to render.
        """

        for iframe in preprocessor.html.select('iframe'):
            match = YOUTUBE_EMBED.search(iframe.get('src', ''))

            if not match:
                iframe.decompose()
                continue

            url = f'https://www.youtube.com/watch?v={match.group(1)}'
            paragraph = preprocessor.html.new_tag('p', attrs={'class': 'video-link'})
            anchor = preprocessor.html.new_tag('a', href=url)

            anchor.string = url
            paragraph.append('Video: ')
            paragraph.append(anchor)

            iframe.replace_with(paragraph)

    def inline_stylesheets(self, preprocessor):
        """Replaces stylesheet links with print-safe inline copies.

        The site's own CSS file is left untouched: the exporter offers a
        `stylesheet()` hook for this, but it rewrites the stylesheet *in the
        published site directory*, which would take the website's layout with
        it.
        """

        if not site_dir:
            log.warning('pdf_theme: site directory unknown; screen rules left in place.')

            return

        for link in preprocessor.html.select('link[rel="stylesheet"]'):
            href = link.get('href')

            if not href:
                continue

            # The theme appends `?v=<build time>` to bust browser caches. On
            # disk the file has no query string, and a path that keeps it is
            # never found, which would leave the screen rules in and blank
            # every page.
            path = os.path.normpath(os.path.join(site_dir, href.split('?', 1)[0]))

            if not os.path.isfile(path):
                # A remote or generated stylesheet; nothing to inline.
                continue

            with open(path, 'r', encoding='utf-8') as reader:
                css = strip_screen_rules(reader.read())

            style = preprocessor.html.new_tag('style', type='text/css')
            style.string = css

            link.replace_with(style)

    def button(self, preprocessor, title, icon, attributes={}):
        """The PDF carries no download buttons of its own."""

    def icon(self, name):
        """No themed icons."""

        return None


if Theme not in Factory.themes:
    Factory.themes = [Theme, *Factory.themes]
