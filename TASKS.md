# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

- Fix `mousemove` listener in sparkle.js to use `pointermove` for touch device support

## Backlog

1. Standardize 404 page link capitalization — nav uses title case ("Work", "About"), 404 uses lowercase ("work", "about")
2. Standardize brand wrapper div — index.html wraps wordmark+intro in `<div class="brand">`, sub-pages don't

## Needs Owen's input

- [Add Chat to nav links] — Chat page exists but isn't in the nav. Needs Owen's signoff on whether it should appear.
- [Add next/prev page navigation to sub-pages] — needs Owen to specify page order and link text
- [Fix nav aria-current gap on chat.html] — Chat page is served but not in the nav, so it has no `aria-current="page"`. Either add Chat to nav or accept the gap.
- [Improve meta descriptions] — all pages have thin one-line descriptions. Needs Owen to provide better copy.

## Done (last 10)

- 2026-05-10 — Trim redundant Person JSON-LD from sub-pages — 2fc79cd
- 2026-05-10 — Consolidate repeated footer SVG into assets/footer.js — fe50af3
- 2026-05-10 — Add noreferrer to resume link rel attribute — 2ae3f45
- 2026-05-09 — Update structured data canonical URLs on sub-pages — 796c808
- 2026-05-09 — Extract inline SVG styles to CSS classes — b4deec4
- 2026-05-08 — Audit: add missing twitter:image meta to all 6 pages — 50174cf
- 2026-05-08 — Clean up stale task briefs in TASKS.md (~495 lines removed) — 0fdee2c
