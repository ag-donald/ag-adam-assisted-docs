---
name: capturing-screenshots
description: Use when capturing or re-capturing a screenshot for the ADAM manual — taking a brief from TODO.md or the user, driving the randomised screenshot site in a browser, framing the shot to house conventions, and placing it in the manual with its provenance recorded
---

# Capturing Screenshots for the ADAM Manual

Screenshots are captured against the local **screenshot site** at
`https://screenshot.theta.adam.co.za/`, never against a school's live site. The Playwright MCP server
is configured so the browser physically cannot reach anything else.

Apache serves the screenshot site from `~/dev/adam`, and the host name makes ADAM load
`config.screenshot.ini`. Its database,
`adam_agent_screenshot`, is a randomised copy of `adam_dev`. **Never capture on
`https://dev.theta.adam.co.za/`.** That host serves `adam_dev` itself, which holds a real school's
data. A whole capture run was thrown away on 2026-11-17 because this skill still pointed there.

## Before you start

Confirm the site is up:

```bash
curl -s -o /dev/null -w "%{http_code}\n" --max-time 10 https://screenshot.theta.adam.co.za/login/staff
```

Expected `200`. Anything else — stop and report; do not begin a capture run. The Apache log for the
site is `/var/log/apache2/screenshot-error.log`. A `503` with "Permission denied" on
`config.screenshot.ini` in that log means PHP-FPM, which runs as `www-data`, cannot read the
file: it must be mode `644`, like `config.dev.ini`.

Confirm the data is randomised, once you are logged in as staff and before you open any pupil,
family or staff page. The randomiser replaces every email address with a `testing+…@adam.co.za`
address, including the school's own sending address. Check that setting:

```js
async () => {
  const html = await (await fetch('/admin/settings/site')).text();
  const doc = new DOMParser().parseFromString(html, 'text/html');
  return doc.querySelector('[name="setting[emailfromaddress]"]')?.value;
}
```

It must start with `testing+`. Anything else — a school's domain, or nothing at all — means the data
is real or the check could not run. Stop, capture nothing, and report it. Do not log in as a family
or pupil, and do not trigger anything that sends mail, until the user has confirmed the database.

Confirm the real typeface is available, not a silent fallback. ADAM's stylesheet pulls Open Sans
from `fonts.googleapis.com` and falls back to Arial, then to whatever sans-serif the system has —
but the allowed-origins rail blocks `fonts.googleapis.com` on purpose, so the webfont never loads
here. If the machine also lacks Open Sans and Arial installed locally, the page renders in
something like DejaVu Sans instead: it looks fine, nothing errors, and every screenshot taken that
way has the wrong letterforms and won't match the manual's existing images. This failure is silent,
so check for it explicitly rather than trusting that the page "looks right":

```js
() => {
  const c = document.createElement('canvas').getContext('2d');
  const s = 'Manage permissions groups — Birthdays 0123';
  c.font = '16px "Open Sans"';
  const openSans = c.measureText(s).width;
  c.font = '16px "DejaVu Sans"';
  const dejaVu = c.measureText(s).width;
  return {openSans, dejaVu};
}
```

If `openSans` and `dejaVu` come back identical, the browser has no real Open Sans and is silently
substituting its generic fallback for both font names — stop and fix this before capturing anything.
The fix is to install the font locally, not to widen the rail: install Open Sans (regular and
italic) to `~/.local/share/fonts/`, run `fc-cache -f`, then **restart the browser**, since Chromium
only reads fontconfig at startup and won't pick up a newly installed font in a running session.
Re-run the measurement afterwards and confirm the two widths now differ. Do not "fix" this by
adding `fonts.googleapis.com` to `--allowed-origins` instead — that would weaken the safety rail that
keeps the browser off the open internet, and would make every future capture depend on Google's
CDN being reachable, which is exactly the kind of external dependency the rail exists to remove.

Confirm the browser draws dates the South African way. Chromium renders date and time fields — and
their empty placeholders — in its interface language, which it takes from the `LANG`, `LANGUAGE`
and `LC_ALL` environment of the process that launched it. Playwright's own `locale` option does not
reach them. Left to the default, a filled field reads `09/16/2026, 08:00 AM`, which no South
African reader's browser would show them. `.mcp.json` sets all three variables to `en_ZA` so that
fields read `16/09/2026, 08:00` instead. Check it on any page:

```js
() => navigator.languages
```

It must be `['en-GB']`. Chromium has no South African English language pack and falls back to
British English, which formats dates identically; `en-ZA` never appears. `['en-US']` means the
setting has not taken: `.mcp.json` is missing the `env` block from
`.mcp.json.dist`, or the MCP server was not restarted after it was added. Do not substitute a
locale that gives year-first dates: only Japanese and Chinese do so with slashes, and they turn every
other browser-drawn string — empty date placeholders, file inputs — into characters the machine
has no font for.

## Logging in

No credentials exist or are needed. `env = dev` enables a bypass:

1. `browser_navigate` to `https://screenshot.theta.adam.co.za/login/staff`
2. `browser_click` the **Login** button, `target: "#login-button"`, leaving both fields empty

This signs you in as `staff_id` 1.

The login lands on the staff dashboard. If it returns a 500 rather than the dashboard, the session is
still sound — navigate straight to the screen you need, and only stop if the brief wants the dashboard
itself.

To be somebody else, go to the login page for that role, fill in the **Login Name** field only, leave
**Password** empty, and click **Login**:

- **A named staff member** — `/login/staff`, their `staff_username`.
- **A parent** — `/login/parent`, a family member's ID number. Left blank, you get the most recently
  created family.
- **A pupil** — `/login/pupil`, their username. Left blank, you get the most recently created pupil.

Use this for briefs that need a particular permission set, or a parent's view of the portal.

## Framing

The viewport is fixed at 900×1200 and screenshots are taken with `scale: "css"`, so a 900px viewport
yields a 900px image. Padding defaults to 8px.

**Mode 1 — element.** One CSS selector, passed as `target` to `browser_take_screenshot`. Use this
whenever the region is a single panel, table or fieldset.

**Mode 2 — vertical span.** For "this row plus the rows above and below". There is no `clip`
parameter, so measure, resize, re-measure, scroll, then shoot:

1. `browser_evaluate` to measure the union box:

```js
() => {
  const els = Array.from(document.querySelectorAll('<your selectors>'));
  if (!els.length) return {error: 'no match'};
  const rs = els.map(e => e.getBoundingClientRect());
  const top = Math.min(...rs.map(r => r.top)) + scrollY;
  const bot = Math.max(...rs.map(r => r.bottom)) + scrollY;
  return {top: Math.round(top), height: Math.round(bot - top)};
}
```

2. `browser_resize` to `width: 900`, `height: height + 16`
3. `browser_evaluate` the same measurement again — changing the viewport height can reflow the page,
   so the `top` from step 1 may no longer be right. Use this fresh `top`, not the first one.
4. `browser_evaluate` — `() => { window.scrollTo(0, <top - 8>); return Math.round(scrollY); }`
5. `browser_take_screenshot` with no `target`, capturing the viewport

Check the returned `scrollY` matches what you asked for. If the page is too short to scroll that far,
the crop will be wrong — resize taller, or frame from an element instead.

## House rules

- **Light mode always.** Verify before capturing:
  `() => getComputedStyle(document.body).backgroundColor` must be `rgb(239, 246, 255)`. The footer
  toggle persists across pages.
- **Never include the development banner** — the blue "Development Environment: Not for General Use"
  strip at the top of every page.
- **No browser chrome, no page header or navigation**, unless the brief explicitly asks for it.
- **No annotations.** The manual has no arrows or highlight boxes anywhere; adding them would make
  new images look foreign.
- **No real school data.** The screenshot site holds a randomised copy of the school, which is why it
  is the only host the browser can reach. The data check under *Before you start* proves it each
  run.

## Naming and placement

`browser_take_screenshot`'s `filename` resolves against the repository root, not `--output-dir`, so
write straight to the destination:

```
docs/assets/screenshots/<chapter-slug>/<chapter-slug>-NN.png
```

Two digits, zero-padded. A re-capture **keeps its existing filename** — the Markdown reference is
already in place and must not need editing.

Reference it with empty alt text and a path relative to `docs/`:

```markdown
![](assets/screenshots/<chapter-slug>/<chapter-slug>-NN.png)
```

## Setting a shot up

Many briefs need the school configured before the picture means anything — a permission granted, a
date moved, a time frame closed. Do it **through ADAM's interface**, never by writing to `adam_agent_screenshot`
directly, so the capture exercises the path a school would take. Record what you changed, and put it
back if the brief says to.

## Recording what you did

Append to `docs/assets/screenshots/<chapter-slug>/captures.yml`, creating it if absent. This is the
real entry for `parent-and-pupil-portal-09.png`:

```yaml
- image: parent-and-pupil-portal-09.png
  captured: 2026-08-04
  as: staff
  path: Pupils tab → Security → Manage permissions groups → privileges (Full Access group, id 1)
  frame:
    mode: span
    selectors: >
      Birthdays heading li, its permission row li (View birthdays);
      2 rows above from the Academic Goal Setting section (Capture academic
      goals, View academic goals); the Family heading li and its first 2
      permission rows (Request online detail update form, Upload family
      documents)
    padding: 8
  setup: >
    Group chosen: "Full Access" — the only pupil login group with any pupils
    assigned (3), against "No Academics", "No Access", "No Markbook" and
    "No Reports" which all have 0. View birthdays was already ticked for both
    Pupils and Families on this group (Full Access grants everything by
    default), so no change was made before capturing.
  revert: none
  note: >
    Re-captured 2026-08-04 (same day, fix round 1): the original capture used
    the browser's DejaVu Sans fallback because fonts.googleapis.com is
    blocked by the allowed-origins rail and no Open Sans/Arial was installed
    on the machine. Open Sans was installed locally and the browser
    restarted; this file is the re-capture, same framing and group, only the
    typeface differs (image height changed slightly, 386px content height
    became 421px, because Open Sans and DejaVu Sans have different metrics).
```

`note` is optional — most entries will not need one; this one records why a first attempt was
discarded. Note the `selectors` field describes the span in prose rather than a CSS selector: mode 2's
page is built from `li` elements, not a table, and no single selector captures a heading plus rows
from two different sections above it plus the target row — so record what was measured, well enough
that someone could reconstruct it, rather than force it into a selector that would not actually work
if fed to `querySelectorAll`. Existing images are not back-filled; the file grows only as shots are
taken.

## The checklist

1. Restate what the image must show, before opening a browser.
2. Confirm the screenshot site is up.
3. Log in as staff and confirm the data is randomised — `emailfromaddress` starts with `testing+`.
4. Log in as the role the brief needs.
5. Confirm the real typeface is loaded, not a silent fallback — `browser_evaluate` with the canvas
   check above.
6. Set the school up, if the brief calls for it.
7. Navigate to the screen.
8. Confirm light mode.
9. Frame and capture.
10. **Read the saved PNG back and check it against the brief** — every named element in shot, nothing
    cut off, no development banner, no data that should not be there.
11. Write the Markdown reference where the brief says.
12. Append to `captures.yml`; revert any setup that should be reverted.
13. Remove the entry from `TODO.md` — that file's own standing rule.
14. Run `docker run --rm --user "$(id -u):$(id -g)" -v "$(pwd):/docs" -w /docs squidfunk/mkdocs-material:latest build --strict --site-dir /docs/.build-verify` and confirm it exits 0, then `rm -rf .build-verify`.
15. Commit.

Step 3 keeps real people out of the manual, and step 10 is the one that matters most for quality. You can see what you captured — a wrong crop caught there costs
nothing, while a wrong crop that ships is a page that misleads a reader.

## When it goes wrong

Every one of these ends in a report, never a substitute image.

- **Selector matches nothing, or the page looks unfamiliar.** Stop. Do not capture something adjacent
  and hope. Report which selector failed and what was actually on the page.
- **The feature is not on this build.** Report it and leave the `TODO.md` entry standing.
- **The data will not cooperate.** A section reading well without a picture is a legitimate outcome —
  the 2FA dashboard card was left without one for exactly this reason.
- **The brief carries an open question.** Surface it. Do not paper over a discrepancy in the manual.
- **The screenshot site is unreachable.** Fail fast and say so. Do not fall back to
  `dev.theta.adam.co.za` or any other host.
- **The data check fails.** Stop before capturing anything, and say what `emailfromaddress` held.
