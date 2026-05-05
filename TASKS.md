# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

(none)

## Backlog

1. Dark mode support — add `prefers-color-scheme: dark` CSS variables and invert sparkle/dark elements. Needs Owen's signoff on dark palette.
2. Add JSON-LD Person structured data to all pages — helps Google/recruiters identify Owen.
3. Update sitemap.xml lastmod dates — still show May 04 after May 05 commits.

## Needs Owen's input

- Resume button — the broken `/resume.pdf` link has been removed from the hero. Reinstate when Owen drops a PDF at the repo root or provides a hosted URL.
- "talk to tobi" link is currently a no-op. Decide where it should go (mailto, contact page anchor, future chat surface).
- og:image — social previews currently use `twitter:card=summary` (no image). Provide a 1200x630 PNG or approve generating one, then upgrade to `summary_large_image`.
- Cursor art — Old Roblox cursor (SweezyCursors) downscaled to 32x32 RGBA. Swap the PNGs (same filenames) for a different style if you want.

## Done (last 10)

- 2026-05-05 — Fix robots.txt Sitemap order + add color-scheme meta — commit b9f82ce
- 2026-05-05 — Sparkle effect on mouse hold — commit b84f97a
- 2026-05-04 — Remove stray bug_sweep.py (untracked, deleted from disk)
- 2026-05-04 — Add theme-color meta to all pages — commit d37f745
- 2026-05-04 — Add canonical links to all pages — commit 05addbf
- 2026-05-04 — Consolidate duplicate .nav selector in styles.css — commit 5279dae
- 2026-05-04 — Add robots.txt and sitemap.xml — commit ae51770
- 2026-05-04 — Add skip-to-content link on all pages — commit b4f0f9f
- 2026-05-04 — Swap cursor to Old Roblox style (32x32) — commit 4e1db6e
- 2026-05-04 — Cursor: enlarge to 24x24 and make interior solid — commit 3e0e32d
