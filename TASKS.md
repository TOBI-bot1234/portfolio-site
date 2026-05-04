# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

- (none)

## Backlog

1. Consolidate duplicate `.nav` selector in `styles.css` — the selector is defined twice (lines ~62 and ~314, the second only adding `animation`). Merge into a single rule, no visual change. Pure refactor.

## Done (last 10)

- 2026-05-04 — Add robots.txt and sitemap.xml — commit ae51770
- 2026-05-04 — Add skip-to-content link on all pages — commit b4f0f9f
- 2026-05-04 — Swap cursor to Old Roblox style (32x32) — commit 4e1db6e
- 2026-05-04 — Cursor: enlarge to 24x24 and make interior solid — commit 3e0e32d
- 2026-05-03 — Pixel-art retro cursor site-wide — commit e278acb
- 2026-05-03 — Ambient animation: wordmark micro-interaction — commit e52c757
- 2026-05-03 — Ambient animation: fade-in on load — commit 19ee39a
- 2026-05-03 — Ambient animation: nav link hover underline — commit 1542e92
- 2026-05-03 — Ambient animation: hero button hover lift — commit e8bc2f0
- 2026-05-02 — Typewrite "talk to tobi" CTA after intro — commit 6a1ce43

## Needs Owen's input

- Resume button — the broken `/resume.pdf` link has been removed from the hero. Reinstate when Owen drops a PDF at the repo root or provides a hosted URL.
- "talk to tobi" link is currently a no-op. Decide where it should go (mailto, contact page anchor, future chat surface).
- og:image — social previews currently use `twitter:card=summary` (no image). Provide a 1200x630 PNG or approve generating one, then upgrade to `summary_large_image`.
- Cursor art — Old Roblox cursor (SweezyCursors) downscaled to 32x32 RGBA. Swap the PNGs (same filenames) for a different style if you want.
