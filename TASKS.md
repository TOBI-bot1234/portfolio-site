# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

### 2. Add a corner doodle to `404.html` only

**Why.** The 404 page is the cheapest, highest-upside doodle moment in the whole repo and we still haven't shipped anything on it. A visitor who hits 404 is already mildly annoyed; a moment of human warmth there pays for itself instantly. Every screenshot review (going back to the 2026-05-06 cycle) has called this out. The page currently uses the same plain `page-title` + `page-body` template as everything else. We don't need a full redesign — we need one inline SVG sketch sitting in the upper corner of the main column, like someone doodled in the margin of a "not found" page.

**Files to touch.**
- `404.html`
- `styles.css` (append only)

**Exact copy / content.** In `404.html`, replace the entire `<main>` block with:

```html
  <main class="page page-404" id="main">
    <svg class="page-404-doodle" viewBox="0 0 80 80" aria-hidden="true" focusable="false">
      <path d="M14 22 C 18 14, 30 12, 38 18 C 46 24, 38 36, 28 36 C 22 36, 22 44, 28 46" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
      <circle cx="28" cy="56" r="2.2" fill="currentColor" />
      <path d="M52 30 L 70 48 M70 30 L 52 48" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" />
    </svg>
    <h1 class="page-title">Hmm.</h1>
    <p class="page-body">
      That page either moved, broke, or never existed.
      Either way, sorry about it.
    </p>
    <p class="page-body page-404-links">
      Try
      <a class="page-link" href="index.html">home</a>,
      <a class="page-link" href="work.html">work</a>,
      or just
      <a class="page-link" href="contact.html">email me</a>
      and tell me which link sent you here.
    </p>
  </main>
```

Append to `styles.css`:

```css
/* 404 page — corner doodle + lowered title */
.page-404 {
  position: relative;
}
.page-404-doodle {
  width: 64px;
  height: 64px;
  display: block;
  margin-bottom: 0.5rem;
  color: currentColor;
  opacity: 0.85;
  transform: rotate(-6deg);
  transform-origin: 20% 50%;
}
.page-404-links {
  margin-top: 1.25rem;
}
@media (prefers-reduced-motion: no-preference) {
  .page-404-doodle {
    animation: page-404-wobble 6s ease-in-out infinite alternate;
  }
}
@keyframes page-404-wobble {
  0%   { transform: rotate(-6deg); }
  100% { transform: rotate(-3deg); }
}
```

**Acceptance criteria.**
- [ ] Visiting `/404.html` renders the doodle SVG in the upper-left of the main column, rotated -6deg.
- [ ] With `prefers-reduced-motion: reduce` set, the SVG does not animate.
- [ ] Heading reads exactly `Hmm.` (capital H, period).
- [ ] All three recovery links (`home`, `work`, `email me`) work and target the right pages.
- [ ] No layout shift on mobile (375px) — the SVG sits inside the main column padding.
- [ ] No changes to `<head>`, nav, scripts, or the `noscript` footer.

## Backlog

### 3. Mobile-only: loosen vertical rhythm under the hero buttons

Single `@media (max-width: 600px)` block appended to `styles.css`. No HTML changes. Stack hero buttons vertically on mobile, add breathing room.

See full brief in git history (commit ab0a77d).

---

### 4. Document Chat-not-in-nav decision; close the aria-current loophole

Add HTML comment in `chat.html` inside `<nav class="nav-links">`, add `## Pages` section to `README.md`.

See full brief in git history (commit ab0a77d).

## Needs Owen's input

(none — see task 4 approval notes)

## Done (last 10)

- 2026-05-11 — Rewrite contact.html body with voice and inline inkunderline — 9e5a9b3
- 2026-05-10 — Trim redundant Person JSON-LD from sub-pages — 2fc79cd
- 2026-05-10 — Consolidate repeated footer SVG into assets/footer.js — fe50af3
- 2026-05-10 — Add noreferrer to resume link rel attribute — 2ae3f45
- 2026-05-09 — Update structured data canonical URLs on sub-pages — 796c808
- 2026-05-09 — Extract inline SVG styles to CSS classes — b4deec4
- 2026-05-08 — Audit: add missing twitter:image meta to all 6 pages — 50174cf
- 2026-05-08 — Clean up stale task briefs in TASKS.md (~495 lines removed) — 0fdee2c
- 2026-05-08 — Show noscript CTA link when JS disabled — 446e335
- 2026-05-08 — Add scripts/ regeneration docs to README — 5370b25
