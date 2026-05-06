# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.
## In progress

- Fix README.md typo ("Tobi" -> "Owen Kelley")

## Backlog

2. Add JSON-LD WebSite + SearchAction schema to index.html — recommended for homepage with Person schema
3. Clean .gitignore — remove framework-specific entries (node_modules, .next, pnpm) irrelevant to static site
4. Add email link to contact.html — page is all placeholder, at minimum add mailto: link

## Needs Owen's input

- Dark mode support — needs Owen's signoff on the dark palette before implementing.
- Resume button — the broken `/resume.pdf` link has been removed from the hero. Reinstate when Owen drops a PDF at the repo root or provides a hosted URL.
- "talk to tobi" link is currently a no-op. Decide where it should go (mailto, contact page anchor, future chat surface).
- og:image — social previews currently use `twitter:card=summary` (no image). Provide a 1200x630 PNG or approve generating one, then upgrade to `summary_large_image`.
- Cursor art — Old Roblox cursor (SweezyCursors) downscaled to 32x32 RGBA. Swap the PNGs (same filenames) for a different style if you want.

## Done (last 10)

- 2026-05-06 — Add `prefers-reduced-motion` guard to sparkle CSS animation — commit a12a5e1
- 2026-05-06 — Add `<noscript>` fallback for typing animation on index.html — commit 6cb9255
- 2026-05-05 — Add 2s safety timeout for sparkle cleanup — commit ec4256a
- 2026-05-05 — Update sitemap.xml lastmod dates — commit f35ad2f
- 2026-05-05 — Add JSON-LD Person structured data to all pages — commit 30e5e24
- 2026-05-05 — Fix robots.txt Sitemap order + add color-scheme meta — commit b9f82ce
- 2026-05-05 — Sparkle effect on mouse hold — commit b84f97a
- 2026-05-04 — Remove stray bug_sweep.py (untracked, deleted from disk)
- 2026-05-04 — Add theme-color meta to all pages — commit d37f745
- 2026-05-04 — Add canonical links to all pages — commit 05addbf
