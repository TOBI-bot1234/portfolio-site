# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

- Trim JSON-LD duplication: remove redundant Person schema from sub-pages (index.html Person + WebSite is sufficient)

## Backlog

## Needs Owen's input

1. [Fix nav aria-current gap on chat.html] — Chat page is served but not in the nav, so it has no `aria-current="page"`. Either add Chat to nav links or accept the gap. Needs Owen's signoff.
- Add `next`/`prev` page navigation to sub-pages — needs Owen to specify page order and link text
- Add Chat to sub-page nav — currently all sub-pages have Work/About/Contact but no Chat link. Should Chat appear in nav?

## Done (last 10)

- 2026-05-10 — Consolidate repeated footer SVG into assets/footer.js — fe50af3
- 2026-05-10 — Add noreferrer to resume link rel attribute — 2ae3f45
- 2026-05-09 — Update structured data canonical URLs on sub-pages — 796c808
- 2026-05-09 — Extract inline SVG styles to CSS classes — b4deec4
- 2026-05-08 — Audit: add missing twitter:image meta to all 6 pages — 50174cf
- 2026-05-08 — Clean up stale task briefs in TASKS.md (~495 lines removed) — 0fdee2c
- 2026-05-08 — Show noscript CTA link when JS disabled — 446e335
- 2026-05-08 — Add scripts/ regeneration docs to README — 5370b25
- 2026-05-08 — Ignore __pycache__/*.pyc/scripts/ in .gitignore — 685ce94
- 2026-05-08 — Sync sitemap.xml lastmod dates to today — 2008064
