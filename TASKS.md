# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

_(none)_

## Backlog

1. Add a static intro fallback for `prefers-reduced-motion` — currently the reduced-motion path sets `textContent = ''` and shows only the CTA, so reduced-motion users get no introduction at all. Render the final message text statically instead.
2. Add a favicon — every page currently 404s on `/favicon.ico`. A minimal SVG favicon with the "OK" wordmark or a simple monogram, plus `<link rel="icon">` in each page head.
3. Add Open Graph and Twitter card meta tags — site has no social preview when shared. Title, description, og:type=website, og:url, twitter:card=summary on each page.
4. Flesh out README — currently two lines. Add a one-paragraph description, the live URL, and a note that the site is plain static HTML/CSS deployed via GitHub Pages.

## Needs Owen's input

- Resume button — the broken `/resume.pdf` link has been removed from the hero. Reinstate when Owen drops a PDF at the repo root or provides a hosted URL.
- "talk to tobi" link is currently a no-op. Decide where it should go (mailto, contact page anchor, future chat surface).

## Done (last 10)

- 2026-05-02 — Fix typewriter final message getting erased before CTA appears — commit ce69208
- 2026-05-01 — Add typewriter intro under wordmark with "talk to tobi" CTA — commit 830ca30
- 2026-05-01 — Fix nav and hero links 404ing on GitHub Pages (absolute → relative paths) — commit 44db40e
- 2026-05-01 — Add a 404 page and audit for dead links — commit 700e837
- 2026-05-01 — Wire `index.html` nav and hero buttons to the new pages — commit a7ebda5
- 2026-05-01 — Add Work, About, Contact placeholder pages — commit e2b2a17
- 2026-05-01 — Add shared inner-page layout styles — commit 0c0a13c
