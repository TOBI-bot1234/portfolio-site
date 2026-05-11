# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

### 3. Mobile-only: loosen vertical rhythm under the hero buttons

**Why.** `mobile-fold.png` review explicitly named the problem twice this cycle: *"elements feel too tightly packed, which contradicts the loose, sketchy nature of hand-drawn designs"* and *"content feels compressed vertically, particularly between the main heading and the buttons."* On desktop the hero breathes. On mobile (375px) the same vertical stack lands in a column with cramped 0.75rem-ish gaps and the "start here" arrow loses its punchline because it's whispered into a wall. The fix is **mobile-only** spacing — desktop is fine, leave it alone.

This is a single `@media` block. No HTML changes, no new files.

**Files to touch.**
- `styles.css` (append only)

**Exact copy / content.** Append to the end of `styles.css`:

```css
/* Hero: loosen mobile vertical rhythm (desktop untouched) */
@media (max-width: 600px) {
  .hero {
    padding-top: 3.5rem;
    padding-bottom: 4rem;
    gap: 2rem;
  }
  .hero-text {
    margin-bottom: 0.75rem;
    line-height: 1.18;
  }
  .hero-actions {
    flex-direction: column;
    align-items: stretch;
    gap: 0.875rem;
    width: min(18rem, 100%);
    margin-left: auto;
    margin-right: auto;
  }
  .hero-actions .btn {
    width: 100%;
    text-align: center;
  }
  .hero-doodle-arrow {
    margin-top: 1.25rem;
  }
}
```

**Acceptance criteria.**
- [ ] At 375px viewport, the three hero buttons are stacked, each ~18rem wide, ~14px apart vertically.
- [ ] At 375px, there is visible breathing room (≥1.5rem) between the headline and the first button.
- [ ] At 1024px+ viewport, the buttons remain horizontal pills as today — no visual diff.
- [ ] No new HTML, no new files; only one new `@media (max-width: 600px)` block appended to `styles.css`.
- [ ] Lighthouse mobile screenshot at 375×667 shows clearly stacked, breathable buttons (eyeball check is fine).

## Backlog

### 4. Document Chat-not-in-nav decision; close the aria-current loophole

Add HTML comment in `chat.html` inside `<nav class="nav-links">`, add `## Pages` section to `README.md`.

See full brief in git history (commit ab0a77d).

## Needs Owen's input

(none — see task 4 approval notes)

## Done (last 10)

- 2026-05-11 — Add corner doodle to 404.html and update copy — 4978912
- 2026-05-11 — Rewrite contact.html body with voice and inline ink underline — 9e5a9b3
- 2026-05-10 — Trim redundant Person JSON-LD from sub-pages — 2fc79cd
- 2026-05-10 — Consolidate repeated footer SVG into assets/footer.js — fe50af3
- 2026-05-10 — Add noreferrer to resume link rel attribute — 2ae3f45
- 2026-05-09 — Update structured data canonical URLs on sub-pages — 796c808
- 2026-05-09 — Extract inline SVG styles to CSS classes — b4deec4
- 2026-05-08 — Audit: add missing twitter:image meta to all 6 pages — 50174cf
- 2026-05-08 — Clean up stale task briefs in TASKS.md (~495 lines removed) — 0fdee2c
- 2026-05-08 — Show noscript CTA link when JS disabled — 446e335
