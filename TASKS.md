# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

(none)

## Backlog

### 1. Rewrite `contact.html` body — kill the support-ticket tone

**Why.** Contact is currently the most generic page on the site. The body is one line — *"The best way to reach me is by email."* — followed by a `mailto:`. That sentence could be on a Zendesk help center. The rest of the site (hero underline, "start here" arrow, About's voicey two paragraphs, Work's hand-numbered notebook list) is the opposite of this. `desktop-full.png` review across two cycles has consistently flagged inner pages as falling off a cliff vs the hero; Contact is the worst offender because it's the page where a real human is supposed to be on the other end and we sound like a form.

This is pure copy + one inline ink mark. No CSS work, no new files.

**Files to touch.**
- `contact.html`

**Exact copy / content.** Replace the entire `<main class="page" id="main">` block with:

```html
  <main class="page" id="main">
    <h1 class="page-title">Contact</h1>
    <p class="page-body">
      Email is the front door. I read everything that lands and I write back
      <span class="contact-emph">on purpose<svg class="contact-emph-underline" viewBox="0 0 110 10" aria-hidden="true" focusable="false" preserveAspectRatio="none"><path d="M2 7 C 25 2, 60 10, 108 4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" /></svg></span>,
      usually within a day or two.
    </p>
    <p class="page-body">
      <a class="page-link" href="mailto:owenbkelley@gmail.com">owenbkelley@gmail.com</a>
    </p>
    <p class="page-body contact-aside">
      Subject lines optional. Pleasantries encouraged. One-line emails are my favorite kind.
    </p>
  </main>
```

Then add this CSS block to the end of `styles.css` (do not modify any existing rule):

```css
/* Contact page — inline ink underline under "on purpose" */
.contact-emph {
  position: relative;
  display: inline-block;
  white-space: nowrap;
}
.contact-emph-underline {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -0.18em;
  width: 100%;
  height: 0.4em;
  pointer-events: none;
  color: currentColor;
  opacity: 0.85;
}
.contact-aside {
  margin-top: 1.5rem;
  opacity: 0.7;
  font-size: 0.95em;
}
```

**Visual / behavior spec.**
- The phrase "on purpose" gets a hand-drawn ink swoop underneath it, in the same ink-stroke language as the hero's `thoughtful` underline (same `stroke-linecap="round"`, similar curve, no fill).
- Underline sits 0.18em below the text baseline, scales with the line, never wraps separately.
- Aside paragraph ("Subject lines optional...") sits 1.5rem below the email link, 70% opacity, 0.95em — quieter voice, like a margin note.
- No interactivity, no animation, no JS. Pure SVG inline + CSS.

**Acceptance criteria.**
- [ ] `contact.html` `<main>` contains exactly the markup above, byte for byte.
- [ ] `styles.css` ends with the three new rules above; no existing rules were modified.
- [ ] The `<svg>` underline has `aria-hidden="true"`, `focusable="false"`, `preserveAspectRatio="none"`.
- [ ] Page still validates as HTML5 (no unclosed tags, no nested anchors).
- [ ] Email link still resolves to `mailto:owenbkelley@gmail.com`.
- [ ] No changes to `<head>`, nav, footer, or scripts.

**Out of scope.** Do not touch the underline in `index.html`. Do not add new doodle SVGs to any other page in this PR. Do not change the `<title>` or meta description.

---

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

**Visual / behavior spec.**
- A 64×64px SVG sketch sits above the heading, slightly rotated (-6deg).
- The sketch is a curled question-mark glyph + a small period dot + a crossed-out symbol next to it. Pure currentColor strokes, no fill except the dot.
- Wobbles between -6deg and -3deg over 6s, ease-in-out, infinite alternate. Suppressed under `prefers-reduced-motion: reduce`.
- Heading is "Hmm." (period included, three characters).
- Recovery links sit 1.25rem below the apology line, inline in a single sentence.

**Acceptance criteria.**
- [ ] Visiting `/404.html` renders the doodle SVG in the upper-left of the main column, rotated -6deg.
- [ ] With `prefers-reduced-motion: reduce` set, the SVG does not animate.
- [ ] Heading reads exactly `Hmm.` (capital H, period).
- [ ] All three recovery links (`home`, `work`, `email me`) work and target the right pages.
- [ ] No layout shift on mobile (375px) — the SVG sits inside the main column padding.
- [ ] No changes to `<head>`, nav, scripts, or the `noscript` footer.

**Out of scope.** Do not add an animated keyframe to any other page's doodle (the hero underline stays static). Do not change the page's `<title>` ("404 — Owen Kelley") or any meta tags.

---

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

**Visual / behavior spec.**
- At ≤600px viewport width: hero padding grows to 3.5rem top / 4rem bottom, internal `gap` becomes 2rem.
- The three CTA buttons (`View work`, `Resume`, `Get in touch`) stack vertically, full-width inside an 18rem max container, centered.
- Vertical gap between stacked buttons is 0.875rem.
- The `start here` arrow gets an extra 1.25rem of top margin so it lands clearly below the button stack instead of crowding it.
- At >600px, every existing desktop rule wins (no change).

**Acceptance criteria.**
- [ ] At 375px viewport, the three hero buttons are stacked, each ~18rem wide, ~14px apart vertically.
- [ ] At 375px, there is visible breathing room (≥1.5rem) between the headline and the first button.
- [ ] At 1024px+ viewport, the buttons remain horizontal pills as today — no visual diff.
- [ ] No new HTML, no new files; only one new `@media (max-width: 600px)` block appended to `styles.css`.
- [ ] Lighthouse mobile screenshot at 375×667 shows clearly stacked, breathable buttons (eyeball check is fine).

**Out of scope.** Do not touch the hero typography size, do not move the `start here` arrow's anchor element, do not add any animation. Do not change the `hero-doodle-arrow` SVG itself.

---

### 4. Document Chat-not-in-nav decision; close the aria-current loophole

**Why.** Three of the three "Needs Owen's input" items revolve around Chat in the nav. Resolving them: **Chat stays out of the nav.** It's an Easter-egg page reached only from the hero typing animation's final state. Putting it in the main nav broadcasts "we have a chat product" — we don't, and the page itself says so. The aria-current "gap" on `chat.html` is therefore not a gap, it's correct: no nav link points at this page, so nothing should claim `aria-current="page"`. But we should document this decision in code so the next pass doesn't re-open the question.

This is the smallest possible task — a single HTML comment in one file, plus a one-line README note.

**Files to touch.**
- `chat.html`
- `README.md`

**Exact copy / content.**

In `chat.html`, immediately after the `<nav class="nav-links" aria-label="Primary">` opening tag (before the three `<a>` links), insert this comment:

```html
      <!-- Chat is intentionally not in the primary nav. It's a soft-launch
           page reached only from the hero typing animation on index.html.
           No nav link → no aria-current="page" needed here. Decided 2026-05-11. -->
```

In `README.md`, find the section header that lists pages (or, if none exists, append at the end of the file under a new `## Pages` heading), and add this line:

```
- `chat.html` — Easter-egg page reached from the hero typing animation only. Deliberately omitted from the primary nav.
```

If `README.md` already lists pages but does not yet mention `chat.html`, insert this bullet at the correct alphabetical position. If `README.md` has no Pages section, append:

```markdown

## Pages

- `index.html` — Home (hero + typing animation)
- `work.html` — Selected work in progress
- `about.html` — About Owen
- `contact.html` — Email contact
- `chat.html` — Easter-egg page reached from the hero typing animation only. Deliberately omitted from the primary nav.
- `404.html` — Not found
```

**Visual / behavior spec.** No visual change. This is a documentation-only fix that closes a recurring TASKS.md loop.

**Acceptance criteria.**
- [ ] `chat.html` contains the HTML comment exactly as written above, inside `<nav class="nav-links">`.
- [ ] `README.md` mentions `chat.html` and explains it is deliberately omitted from the primary nav.
- [ ] No visual rendering change at any viewport.
- [ ] No CSS changes, no JS changes, no nav link changes.

**Out of scope.** Do not add Chat to the nav. Do not add prev/next pagination anywhere. Do not touch `aria-current` on any other page.

**Approval notes (resolved by designer 2026-05-11).** All three "Needs Owen's input" items in this section resolve to the same answer: **Chat is not a nav item.** It's an Easter egg. Documenting the choice in code is the close-out — not adding more navigation surface. The "next/prev page navigation" item is also killed: 5-page personal sites don't need magazine-style pagination; the persistent nav already covers it. After this task lands, the "Needs Owen's input" section should be empty.


## Needs Owen's input

(none — see Backlog task 4 approval notes, 2026-05-11)

## Done (last 10)

- 2026-05-10 — Trim redundant Person JSON-LD from sub-pages — 2fc79cd
- 2026-05-10 — Consolidate repeated footer SVG into assets/footer.js — fe50af3
- 2026-05-10 — Add noreferrer to resume link rel attribute — 2ae3f45
- 2026-05-09 — Update structured data canonical URLs on sub-pages — 796c808
- 2026-05-09 — Extract inline SVG styles to CSS classes — b4deec4
- 2026-05-08 — Audit: add missing twitter:image meta to all 6 pages — 50174cf
- 2026-05-08 — Clean up stale task briefs in TASKS.md (~495 lines removed) — 0fdee2c
- 2026-05-08 — Show noscript CTA link when JS disabled — 446e335
- 2026-05-08 — Add scripts/ regeneration docs to README — 5370b25
- 2026-05-08 — Ignore __pycache__/*.pyc/scripts/ in .gitignore — 685ce94
