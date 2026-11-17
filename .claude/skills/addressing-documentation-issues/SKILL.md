---
name: addressing-documentation-issues
description: Use when asked to address, work on, fix or resolve a GitHub issue in phinor/adam-docs, to take "the first" or "the next" documentation issue, or when an issue titled "ADAM: …" asks for help pages to be written or changed
---

# Addressing Documentation Issues

One issue becomes one branch, one PR to `main`, and a closed issue. The manual describes ADAM, so
every claim comes from the ADAM source at `~/dev/adam` (GitHub `phinor/adam`), not from the issue's
wording.

## 1. Pick the issue

If the user names an issue number, use it. Otherwise "the first issue" is the **oldest open issue**,
the lowest number. `gh issue list` sorts newest first, so do not take the top row.

```bash
gh issue list --state open --json number,title --jq 'sort_by(.number) | .[0]'
gh issue view <N> --json number,title,body,comments,labels
```

`gh issue view` without `--json` fails in this repository with a Projects (classic) error.

Read the comments. The owner's comments settle choices the body leaves open, such as "one page per
feature".

Issues from ADAM follow a template. Use each section like this:

| Section | What it gives you |
|---|---|
| What changed / Where it is in ADAM | The feature. Find it in the source before you write. |
| Who it affects / Settings | Audience and conditional visibility. Check both in the code. |
| Help pages affected | Starting points. Search for other pages on the topic as well. |
| Suggested wording | A draft. Check every label in it against the views. |
| Help link wanted | Pages and anchors ADAM will link to. They must exist, and be reported back. |
| Release | Where the ADAM change lives. Decides the PR's "Before merging" note. |

## 2. Check the state of both repositories

Do this before you write anything.

```bash
cd /home/philip/dev/adam-docs
git fetch origin
git status --short
git log --oneline origin/main..main
git branch -a | grep docs/
git log --oneline -20 origin/main
```

- **The issue may already be done.** Search the recent log, the unpushed commits and the local
  `docs/*` branches for work on it. If the work exists, finish it. Do not write it a second time.
- **Commits that were never pushed** (on local `main` or on a local `docs/*` branch) are not yours
  to ship. If any belong to this issue, list them, and the branch that holds them, and ask the user
  once whether the PR should carry them and on which branch. Keep existing commits as they are: add
  new commits on top, and do not reword, squash or rebase them without asking. If none belong to
  this issue, branch from `origin/main` so the PR leaves them out.
- **Uncommitted changes** belong to someone else. Leave them alone, and stage only the files you
  change.

Then find where the ADAM change is. **Release** names a commit, a branch or a pull request:

```bash
git -C ~/dev/adam fetch origin
git -C ~/dev/adam branch --show-current
git -C ~/dev/adam status --short
git -C ~/dev/adam merge-base --is-ancestor <sha> origin/main && echo released
gh pr view <PR> -R phinor/adam --json state,mergedAt,mergeCommit,headRefName
gh pr list -R phinor/adam --head <branch> --state all --json number,state,mergeCommit
```

`origin/main` in ADAM is what schools run, because every push to it is released. `development` is
the next release. Read code from the branch named in **Release** with
`git -C ~/dev/adam show origin/<branch>:<path>`. This leaves the checkout alone.

The screenshot site serves whatever `~/dev/adam` has checked out. If the change is not on the
checked-out branch, the screenshots cannot show it. Do not switch the checkout yourself: it may
hold the user's work. Write the text, list the screenshots that are still needed, and ask the user
before you switch.

## 3. Branch

```bash
git switch -c docs/<short-slug> origin/main
```

Use the existing `docs/` branch when step 2 found one.

## 4. Write the change

Follow the `writing-user-documentation` skill. Its Discover phase is the rule that matters most:
take menu paths, labels and visibility from the ADAM source, never from the issue or a summary.

In this repository:

- Edit the Markdown under `docs/`. A new page also needs an entry in the `nav:` section of
  `mkdocs.yml`. Do not run `scripts/generate_nav.mjs`. It flattens the navigation.
- A change to a `docs/api-*.md` page also needs the `auditing-api-docs` skill.
- Code and manual disagree, or ADAM has a fault: record it in `TODO.md` under the existing
  headings. Do not write around it.

## 5. Screenshots

A screenshot needs taking when the change adds an image, or when the screen in an existing image
has changed. Look at each image on the pages you touched, and compare it with the current view.

Capture every one with the `capturing-screenshots` skill. That skill holds the host, the safety
checks and the framing rules. When a capture cannot be done (the feature is not on the checked-out
branch, the data will not cooperate), add a brief to `TODO.md` and list it in the PR.

Before you push, check every image the branch adds or changes, including images in commits you did
not make:

```bash
git diff --name-only origin/main...HEAD -- '*.png'
```

Each one needs a `captures.yml` entry that says it was captured on the screenshot site
(`screenshot.theta.adam.co.za`, `screenshot.localhost:8124` or `adam_agent_screenshot`). An entry
that names `dev.theta`, a "dev host", or no host at all may show a real school's pupils. The
repository is public, so a push publishes them. Stop, push nothing, and tell the user which images
need recapturing.

## 6. Verify

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$(pwd):/docs" -w /docs \
  squidfunk/mkdocs-material:latest build --strict --site-dir /docs/.build-verify
```

It must exit 0. For every page and anchor in **Help link wanted**, and every new heading another
page links to, confirm the anchor exists in the built HTML. Do not guess the slug from the heading.

```bash
grep -o 'id="<anchor>"' .build-verify/<page>.html
rm -rf .build-verify
```

## 7. Commit, push, open the PR

Stage the files by name. Never use `git add -A` or `git add .`.

The commit message is a subject line that says what the manual now does, in the imperative, then
prose paragraphs that say what changed and why. End it with the attribution lines from the system
reminder.

```bash
git push -u origin docs/<short-slug>
gh pr create --base main --title "<subject>" --body-file <file in the scratchpad>
```

The PR body has these parts, in this order:

1. **Why**: what was wrong or missing, in one or two sentences, with `Addresses #<N>`.
2. **What changes**: one bullet per page, naming the sections added or rewritten.
3. **Screenshots**: each image captured or recaptured, and each one still needed, with its
   `TODO.md` brief.
4. **Help links**: for each item in **Help link wanted**, the full URL,
   `https://help.adam.co.za/<page>.html#<anchor>`. Omit this part when the issue asks for none.
5. **Before merging**: only when the ADAM change is not yet in ADAM's `origin/main`. Name the ADAM
   commit, branch or PR, and say to merge once it is released.
6. The build result: `mkdocs build --strict` passes.
7. The attribution line from the system reminder.

## 8. Close the issue

`Addresses #N` does not close an issue, and a closing keyword would only take effect on merge. The
user wants the issue closed now:

```bash
gh issue comment <N> --body "<comment>"
gh issue close <N> --reason completed
```

The comment links the PR and repeats the help-link URLs, because the ADAM developer reads the issue
rather than the PR.

## Report to the user

Say which issue you took and why, the PR URL, the screenshots taken and those still needed, and
anything you asked about or left undone.
