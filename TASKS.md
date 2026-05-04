# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

- (none)

## Backlog

1. Add skip-to-content link — keyboard users currently have to tab through the whole nav before reaching `<main>`. Add a visually-hidden `<a class="skip-link" href="#main">Skip to content</a>` as the first focusable element on every page, with a focus state that brings it on-screen. Add `id="main"` to each `<main>`.
2. Add `robots.txt` and `sitemap.xml` — site is currently invisible to crawlers beyond default behaviour. Ship a permissive `robots.txt` and a hand-written `sitemap.xml` covering the four indexable pages (index, work, about, contact). Reference sitemap from robots.txt.
3. Consolidate duplicate `.nav` selector in `styles.css` — the selector is defined twice (lines ~62 and ~314, the second only adding `animation`). Merge into a single rule, no visual change. Pure refactor.

## Needs Owen's input

- Resume button — the broken `/resume.pdf` link has been removed from the hero. Reinstate when Owen drops a PDF at the repo root or provides a hosted URL.
- "talk to tobi" link is currently a no-op. Decide where it should go (mailto, contact page anchor, future chat surface).
- og:image — social previews currently use `twitter:card=summary` (no image). Provide a 1200x630 PNG or approve generating one, then upgrade to `summary_large_image`.
- Cursor art — Old Roblox cursor (SweezyCursors) downscaled to 32x32 RGBA. Swap the PNGs (same filenames) for a different style if you want.

## Done (last 10)

- 2026-05-04 — Shrink cursors from 32x32 to 24x24 — commit ca598bd
- 2026-05-04 — Swap cursor to Old Roblox style (32x32) — commit 4e1db6e
- 2026-05-04 — Cursor: enlarge to 24x24 and make interior solid — commit 3e0e32d
- 2026-05-03 — Pixel-art retro cursor site-wide — commit e278acb
- 2026-05-03 — Ambient animation: wordmark micro-interaction — commit e52c757
- 2026-05-03 — Ambient animation: fade-in on load — commit 19ee39a
- 2026-05-03 — Ambient animation: nav link hover underline — commit 1542e92
- 2026-05-03 — Ambient animation: hero button hover lift — commit e8bc2f0
- 2026-05-02 — Typewrite "talk to tobi" CTA after intro — commit 6a1ce43
- 2026-05-02 — Flesh out README with description, live URL, and stack notes — commit b6b0bf4
- 2026-05-02 — Add Open Graph and Twitter card meta tags — commit c159b42
- 2026-05-02 — Add a favicon (OK monogram SVG, linked on all pages) — commit 045b917
