# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

- [#3] Add sitemap completeness check to .audit.py

## Backlog

1. [Task A] Track `scripts/` in git with tightened `.gitignore` — remove bare `scripts/` from .gitignore, add `scripts/gen_og_image.py` to tracking
2. [Task B] Replace `work.html` items 1–3 with three real, specific entries — current items are meta-self-referential filler
3. [Task C] Add a single warm accent color, used in exactly two places — hero underline + doodle arrow only
4. [Task D] Stretch the About page from two thin lines to a short, specific paragraph — replace second paragraph with substantive copy
5. [#4] Add apple-touch-icon for iOS home screen — currently no apple-touch-icon, site will look generic when added to iOS home screen
6. [#5] Consider adding .nojekyll — GitHub Pages convention to skip Jekyll processing (already working without it, but explicit is safer)

## Needs Owen's input

(none — `scripts/gen_og_image.py` git tracking resolved 2026-05-14 by designer; see Task A.)

## Done (last 10)

- 2026-05-14 — Fix .audit.py false positives (os.walk, role=presentation, favicon regex) — 775afb5
- 2026-05-12 — Update sitemap.xml lastmod dates — 381b5e9
- 2026-05-12 — Add __pycache__ to .gitignore (was already done, just unmarked) — 5f1284d
- 2026-05-11 — Rewrite thin meta descriptions to be actual descriptions — 3a2252b
- 2026-05-11 — Remove dead .icon-squiggle-inline CSS class — 7450b58
- 2026-05-11 — Mark all backlog items done, backlog empty — 65ede1f
- 2026-05-11 — Document Chat-not-in-nav decision, close aria-current loophole — 5f53387
- 2026-05-11 — Add corner doodle to 404.html + loosen mobile hero rhythm — ba9063e
- 2026-05-11 — Rewrite contact.html body with voice and inline ink underline — 9e5a9b3
- 2026-05-10 — Trim redundant Person JSON-LD from sub-pages — 2fc79cd
