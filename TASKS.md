# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

_(none)_

## Backlog

1. Add subtle ambient animations across the site — creative latitude. Think hover lifts, fade-ins on load, soft nav underline, gentle wordmark interaction. Nothing heavy, nothing that hurts CLS or distracts. Decompose when picked up.
2. Pixel-art retro cursor site-wide — replace the default cursor with a small pixely cursor (and a matching pointer variant for interactive elements). Use CSS `cursor: url(...)` with PNG/SVG, include fallback, respect touch devices.

## Needs Owen's input

- Resume button — the broken `/resume.pdf` link has been removed from the hero. Reinstate when Owen drops a PDF at the repo root or provides a hosted URL.
- "talk to tobi" link is currently a no-op. Decide where it should go (mailto, contact page anchor, future chat surface).
- og:image — social previews currently use `twitter:card=summary` (no image). Provide a 1200x630 PNG or approve generating one, then upgrade to `summary_large_image`.

## Done (last 10)

- 2026-05-02 — Typewrite "talk to tobi" CTA after intro — commit 6a1ce43
- 2026-05-02 — Flesh out README with description, live URL, and stack notes — commit b6b0bf4
- 2026-05-02 — Add Open Graph and Twitter card meta tags — commit c159b42
- 2026-05-02 — Add a favicon (OK monogram SVG, linked on all pages) — commit 045b917
- 2026-05-02 — Add static intro fallback for prefers-reduced-motion — commit b026c97
- 2026-05-02 — Fix typewriter final message getting erased before CTA appears — commit ce69208
- 2026-05-01 — Add typewriter intro under wordmark with "talk to tobi" CTA — commit 830ca30
- 2026-05-01 — Fix nav and hero links 404ing on GitHub Pages (absolute → relative paths) — commit 44db40e
- 2026-05-01 — Add a 404 page and audit for dead links — commit 700e837
- 2026-05-01 — Wire `index.html` nav and hero buttons to the new pages — commit a7ebda5
