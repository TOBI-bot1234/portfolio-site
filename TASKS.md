# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

- [Extract inline SVG styles to CSS] — chat.html and 404.html have inline `style` on decorative SVGs that should live in CSS classes

## Backlog

- [Update structured data canonical URLs on sub-pages] — all pages point Person schema URL to homepage; sub-pages could point to their own canonical for SEO

## Needs Owen's input

1. [Fix nav aria-current gap on chat.html] — Chat page is served but not in the nav, so it has no `aria-current="page"`. Either add Chat to nav links or accept the gap. Needs Owen's signoff.
- Add `next`/`prev` page navigation to sub-pages — needs Owen to specify page order and link text
- Add Chat to sub-page nav — currently all sub-pages have Work/About/Contact but no Chat link. Should Chat appear in nav?

## Done (last 10)

- 2026-05-08 — Audit: add missing twitter:image meta to all 6 pages — 50174cf
- 2026-05-08 — Clean up stale task briefs in TASKS.md (~495 lines removed) — 0fdee2c
- 2026-05-08 — Show noscript CTA link when JS disabled — 446e335
- 2026-05-08 — Add scripts/ regeneration docs to README — 5370b25
- 2026-05-08 — Ignore __pycache__/*.pyc/scripts/ in .gitignore — 685ce94
- 2026-05-08 — Sync sitemap.xml lastmod dates to today — 2008064
- 2026-05-08 — Add chat.html to README; add page-link class to contact email — 547f5f2
- 2026-05-07 — Sync og/twitter meta descriptions for 404 + chat — 429744c
- 2026-05-07 — Loosen mobile hero button spacing — 729f58a
- 2026-05-07 — Replace about.html with tighter two-line manifesto — 967c5e4
- 2026-05-07 — Add global footer with doodle sigil to all pages — 2e35ff3
