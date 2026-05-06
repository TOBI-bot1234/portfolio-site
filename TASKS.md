# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

- Dark mode CSS variables — add prefers-color-scheme dark palette to styles.css, replace hardcoded colors with variables

## Backlog

1. Dark mode sparkle colors — fix sparkle particle background for dark background (sparkle.css)
2. Dark mode meta tags — update color-scheme meta to "light dark" on all pages, add dark theme-color
3. Resume button — wire `/resume.pdf` link back to hero. Owen will drop PDF at repo root as `resume.pdf`.
4. "talk to tobi" link — create a new page that serves as a placeholder chat surface for the future
5. og:image — generate or add a 1200x630 social preview image, upgrade `twitter:card` to `summary_large_image`
6. Sparkle colors — change sparkle particles from solid dark to random confetti-like colors
7. Add a hand-lettered tagline doodle as a separate file `assets/tagline-doodle.svg` — see brief below
8. Wire the tagline doodle into the hero — see brief below
9. Make the 404 page actually fun — see brief below
10. Replace `work.html` placeholder paragraph with a hand-numbered "things in progress" list — see brief below

---

### Task 6 — Create `assets/tagline-doodle.svg`

**Why.** `desktop-full.png` review noted: "massive empty space below the hero content… reads as 'just a div'… seems like placeholder space waiting for content." A small hand-drawn ink mark in the lower hero — a curved arrow pointing from empty space toward the "View work" button with the word "start here" — turns the dead zone into intentional marginalia. We're shipping the asset on its own first so the next task can wire it in cleanly.

**Files to touch.**
- `assets/tagline-doodle.svg` (new file).

**Exact file contents.** Write this SVG verbatim:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 90" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
  <path d="M12 14 C 28 8, 50 22, 60 38 S 70 64, 92 70" />
  <path d="M86 62 L 92 70 L 100 64" />
  <text x="6" y="48" font-family="'Caveat','Patrick Hand','Comic Sans MS',cursive" font-size="20" fill="currentColor" stroke="none" transform="rotate(-8 6 48)">start here</text>
</svg>
```

**Visual / behavior spec.**
- Curved ink arrow that loops down-right and ends in a clean arrowhead.
- Hand-lettered "start here" tilted -8° to the left of the arrow.
- Stroke is `currentColor` so it inherits the page foreground.
- The text uses a cursive stack with system fallback; we are *not* loading a webfont in this task.

**Acceptance criteria.**
- [ ] File `assets/tagline-doodle.svg` exists in repo at the exact path.
- [ ] File contents are valid SVG and render in a modern browser (test by opening locally).
- [ ] No CSS, HTML, or JS changes in this task.

**Out of scope.** Do not embed it into any page in this task — that is task 8.

---

### Task 8 — Wire the tagline doodle into the hero

**Why.** Standalone SVG file from task 7 needs a home. We place it in the lower-right of the hero block, near the "Get in touch" button — small (max 140px wide), pointing toward "View work" so it reads as an arrow guiding the eye to the primary CTA. This is the moment the page stops looking like a Tailwind starter.

**Depends on.** Task 7 must be merged first.

**Files to touch.**
- `index.html` — insert one new element inside `<main class="hero">`, immediately *after* the `<div class="hero-actions">…</div>` block.
- `styles.css` — add one new rule block.

**Exact markup change in `index.html`.**
Immediately after the closing `</div>` of `.hero-actions`, insert:

```html
    <img class="hero-doodle-arrow" src="assets/tagline-doodle.svg" alt="" role="presentation" />
```

**Exact CSS to add (append to end of `styles.css`):**

```css
.hero-doodle-arrow {
  display: block;
  width: clamp(96px, 14vw, 140px);
  height: auto;
  margin: 1.25rem auto 0;
  opacity: 0.75;
  transform: rotate(-4deg);
  pointer-events: none;
}
@media (max-width: 640px) {
  .hero-doodle-arrow { width: 92px; opacity: 0.7; }
}
```

**Visual / behavior spec.**
- Doodle sits centered beneath the buttons, not crowding them (1.25rem of breathing room above).
- Tilted -4° to look casually placed.
- 75% opacity so it reads as marginalia, not a CTA.
- Decorative — `alt=""` and `role="presentation"` so screen readers skip it.
- No motion.

**Acceptance criteria.**
- [ ] Doodle appears below the two hero buttons, roughly centered.
- [ ] Doodle is between 96px and 140px wide depending on viewport.
- [ ] Doodle is rotated approximately -4° and at ~75% opacity.
- [ ] Doodle does not appear on Work/About/Contact/404 pages.
- [ ] Doodle is announced as nothing by VoiceOver / NVDA (test: tab through, it should not stop on it).

**Out of scope.** Do not animate it. Do not load a webfont. Do not change the hero text.

---

### Task 9 — Make the 404 page actually fun

**Why.** `404.html` currently reads: "That page does not exist, or it has moved." That is a SaaS funeral, not a doodle. Every doodle site has one moment where a tiny human voice peeks through, and the 404 is the cheapest, highest-upside place to put it. We replace the dead body copy with a single hand-feeling sentence and a tiny inline doodle of a crumpled paper.

**Files to touch.**
- `404.html` — replace the `.page-title` text and the body paragraph contents only.

**Exact change.**
Replace the existing `<main>` block contents:

```html
    <h1 class="page-title">Not found</h1>
    <p class="page-body">
      That page does not exist, or it has moved.
    </p>
    <p class="page-body">
      <a class="page-link" href="index.html">Back to home</a>
    </p>
```

…with:

```html
    <h1 class="page-title">Hmm.</h1>
    <p class="page-body">
      I looked, and there's nothing here.
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false" style="vertical-align:-4px;margin-left:4px;">
        <path d="M5 7 C 8 5, 11 9, 14 6 S 19 8, 21 5" />
        <path d="M4 12 C 7 10, 12 14, 16 11 S 21 13, 22 11" />
        <path d="M6 17 C 9 15, 13 19, 17 16" />
      </svg>
      Maybe try one of these instead:
    </p>
    <p class="page-body">
      <a class="page-link" href="index.html">home</a> &nbsp;·&nbsp;
      <a class="page-link" href="work.html">work</a> &nbsp;·&nbsp;
      <a class="page-link" href="about.html">about</a> &nbsp;·&nbsp;
      <a class="page-link" href="contact.html">contact</a>
    </p>
```

**Visual / behavior spec.**
- Title becomes "Hmm." (deliberately small, conversational, period included).
- Inline crumpled-paper doodle (three wavy lines stacked) sits inline with the prose at 22×22px, baseline-aligned.
- The "back to home" link is replaced with all four nav destinations as a single dot-separated row of `.page-link` underlines — gives a lost visitor a useful set of recovery doors.
- No new CSS file required, no styles.css change.

**Acceptance criteria.**
- [ ] 404 page title reads exactly `Hmm.` (with the period).
- [ ] First paragraph contains the inline 3-wavy-line SVG between "nothing here." and "Maybe try…" — visible inline at body-text size.
- [ ] Second paragraph offers four links: home, work, about, contact — separated by a middle-dot character.
- [ ] All four links go to the correct existing pages.
- [ ] No `styles.css` changes.

**Out of scope.** Do not add a header/illustration block, do not change the page chrome, do not touch other pages.

---

### Task 10 — Replace `work.html` placeholder paragraph with a hand-numbered "things in progress" list

**Why.** `desktop-full.png` review: the Work page is one filler sentence. A portfolio without work is a bigger lie than a portfolio that admits it's mid-build. The doodle move here is to *show the work-in-progress as work-in-progress* — a hand-numbered list with deliberately vague, honest entries. This makes the empty state feel intentional instead of unfinished. **Approval note:** Owen has not approved entry copy. I am picking three honest placeholders that don't overcommit. Owen can rewrite later; the structure is what matters.

**Files to touch.**
- `work.html` — replace the contents of `<main>` only.
- `styles.css` — append one new selector block for the numbered list styling.

**Exact change in `work.html`.**
Replace the existing `<main>` contents:

```html
    <h1 class="page-title">Work</h1>
    <p class="page-body">
      A selection of recent projects is on its way. In the meantime, the
      shortest version: I build software with care for the details that
      tend to get skipped.
    </p>
```

…with:

```html
    <h1 class="page-title">Work</h1>
    <p class="page-body work-intro">
      Half-finished, half-honest. Here's what's on the desk right now —
      <span class="work-arrow" aria-hidden="true">↓</span>
    </p>
    <ol class="work-list">
      <li><span class="work-num">1.</span> A small CLI for scratching the same itch twice in one week.</li>
      <li><span class="work-num">2.</span> This site, getting less templated every Monday and Thursday.</li>
      <li><span class="work-num">3.</span> Notes that want to become an essay about restraint.</li>
    </ol>
    <p class="page-body work-footer">
      The polished case studies are coming. The list above is the truth in the meantime.
    </p>
```

**Exact CSS to add (append to end of `styles.css`):**

```css
.work-intro {
  margin-bottom: 1.5rem;
}
.work-arrow {
  display: inline-block;
  margin-left: 0.25rem;
  transform: translateY(2px) rotate(8deg);
  font-size: 1.1em;
}
.work-list {
  list-style: none;
  padding: 0;
  margin: 0 0 2rem;
  max-width: 60ch;
  font-size: 1.0625rem;
  line-height: 1.6;
}
.work-list li {
  padding: 0.55rem 0;
  border-bottom: 1px dashed currentColor;
}
.work-list li:last-child {
  border-bottom: none;
}
.work-num {
  display: inline-block;
  min-width: 1.6em;
  font-weight: 600;
}
.work-footer {
  font-size: 0.95rem;
  color: #6a6a6a;
}
```

**Visual / behavior spec.**
- Three hand-numbered items, each on its own line, separated by dashed underlines that look ruled, not designed.
- A small `↓` arrow tilts 8° at the end of the intro line, casually pointing at the list.
- The `1.` `2.` `3.` are inline-block with a fixed minimum width so the text aligns regardless of single vs double digits — like a notebook list.
- Footer paragraph in a quieter gray (`#6a6a6a`).

**Acceptance criteria.**
- [ ] Work page renders three numbered items with the exact copy above.
- [ ] Each item is separated from the next by a dashed bottom border (not solid).
- [ ] The intro line ends with a tilted `↓` arrow.
- [ ] The list is left-aligned and respects the existing `.page` max-width.
- [ ] No JavaScript added.

**Out of scope.** Do not link the items anywhere. Do not add images. Do not touch about/contact/index.

**Approval notes (this task).** Owen had not weighed in on the Work page copy — I'm setting the structure and a usable first draft so the page stops being one limp sentence. Owen can revise the three list items at any time without touching CSS.

## Needs Owen's input

(none)

## Done (last 10)

- 2026-05-06 — Add hand-drawn underline under hero word "thoughtful" — commit 0bb2522
- 2026-05-06 — Wire contact page mailto link to owenbkelley@gmail.com — commit f858a50
- 2026-05-06 — Add JSON-LD WebSite structured data to index.html — commit 1624c6b
- 2026-05-06 — Clean .gitignore — remove unused framework-specific entries — commit eaa544e
- 2026-05-06 — Fix README.md "Tobi" reference to "him" — commit c7e194e
- 2026-05-06 — Add `prefers-reduced-motion` guard to sparkle CSS animation — commit a12a5e1
- 2026-05-06 — Add `<noscript>` fallback for typing animation on index.html — commit 6cb9255
- 2026-05-05 — Add 2s safety timeout for sparkle cleanup — commit ec4256a
- 2026-05-05 — Update sitemap.xml lastmod dates — commit f35ad2f
- 2026-05-05 — Add JSON-LD Person structured data to all pages — commit 30e5e24
