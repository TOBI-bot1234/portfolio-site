# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

- Replace `work.html` placeholder paragraph with a hand-numbered "things in progress" list — see brief below

## Backlog

1. Replace `work.html` placeholder paragraph with a hand-numbered "things in progress" list — see brief below
2. Add a small doodled sigil + one-line sign-off footer to all pages — see brief below
3. Replace `about.html` body copy with a tighter two-line manifesto — see brief below
4. Loosen mobile spacing under the hero buttons — see brief below

## Needs Owen's input

(none)

## Done (last 10)

- 2026-05-07 — Replace chat.html body copy with doodle-style placeholder — c3bc3ba
- 2026-05-07 — Make the 404 page actually fun — 80a6807
- 2026-05-07 — Wire tagline doodle into hero section — d00a248
- 2026-05-07 — Add tagline doodle SVG asset — 9b6cc23
- 2026-05-07 — Sparkle colors — change particles to confetti palette — 8154b73
- 2026-05-07 — og:image — d9a4fee
- 2026-05-07 — "Talk to Tobi" placeholder chat page, wired CTA link in hero — commit 3141446
- 2026-05-07 — Resume button in hero with dashed-outline variant — commit bc13a24
- 2026-05-07 — Dark mode meta tags — color-scheme and theme-color updated on all pages — commit c72abc0
- 2026-05-07 — Fix sparkle particles to adapt to dark mode via --fg CSS variable — commit 0186b2d

---

### Task 3 — Create `assets/tagline-doodle.svg`

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

### Task 4 — Wire the tagline doodle into the hero

**Why.** Standalone SVG file from task 3 needs a home. We place it in the lower-right of the hero block, near the "Get in touch" button — small (max 140px wide), pointing toward "View work" so it reads as an arrow guiding the eye to the primary CTA. This is the moment the page stops looking like a Tailwind starter.

**Depends on.** Task 3 must be merged first.

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

### Task 5 — Make the 404 page actually fun

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

### Task 6 — Replace `work.html` placeholder paragraph with a hand-numbered "things in progress" list

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

---

### Task 7 — Add a small doodled sigil + one-line sign-off footer to all pages

**Why.** Every screenshot in this cycle ends the same way: page content stops, white (or dark) space, edge of screen. The vision review explicitly flagged it on `desktop-full.png` ("page appears to end abruptly… no footer, no doodle elements") and on `mobile-full.png` ("page ends abruptly after 'Get in touch' with no footer padding or visual conclusion"). A portfolio that admits a hand made it should *sign* the page, not just cut to black. We add one global footer: a 18×18px scribble (three short ink dashes), the line "made by hand", and the year — quiet, consistent, ends every page on a small human note instead of a void.

**Files to touch.**
- `index.html` — insert one `<footer>` element immediately before the closing `</body>`, after the existing `<script>` tags.
- `work.html` — same insert.
- `about.html` — same insert.
- `contact.html` — same insert.
- `chat.html` — same insert.
- `404.html` — same insert.
- `styles.css` — append the new `.site-footer` rule block below.

**Exact markup to insert in each of the six HTML files** (place immediately before `</body>`, after the last `<script>` line that already exists in that file):

```html
  <footer class="site-footer" role="contentinfo">
    <svg class="site-footer-mark" viewBox="0 0 24 12" width="18" height="9" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true" focusable="false">
      <path d="M2 9 C 5 4, 7 9, 10 5" />
      <path d="M12 8 C 14 5, 16 9, 18 6" />
      <path d="M20 7 L 22 5" />
    </svg>
    <span class="site-footer-text">made by hand · 2026</span>
  </footer>
```

**Exact CSS to add (append to end of `styles.css`):**

```css
.site-footer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 1.5rem var(--pad-x) 1.75rem;
  font-size: 0.78rem;
  letter-spacing: 0.02em;
  color: var(--muted);
}
.site-footer-mark {
  display: inline-block;
  flex-shrink: 0;
  transform: translateY(1px) rotate(-3deg);
  opacity: 0.85;
}
.site-footer-text { white-space: nowrap; }
@media (max-width: 640px) {
  .site-footer { padding-top: 1.25rem; padding-bottom: 1.5rem; font-size: 0.72rem; }
}
```

**Visual / behavior spec.**
- Footer is centered, single horizontal row: small ink scribble on the left, "made by hand · 2026" text on the right.
- Foreground inherits `var(--muted)` so it stays whisper-quiet in both light and dark modes.
- The scribble is rotated -3° and at ~85% opacity to read as a margin mark, not a logo.
- No motion, no link, no border above. Just a small human note where the page ends.
- The 6 footer markups are byte-identical across the six pages so we can grep them later.

**Acceptance criteria.**
- [ ] All six pages (`index.html`, `work.html`, `about.html`, `contact.html`, `chat.html`, `404.html`) render the footer at the bottom.
- [ ] Footer text reads exactly `made by hand · 2026` (with the middle-dot character).
- [ ] Inline SVG renders inline with the text, vertically centered.
- [ ] Footer text color matches `var(--muted)` and changes correctly in dark mode.
- [ ] No JS added, no font loaded.
- [ ] Markup is byte-identical across all six files (verify with a single-line `grep -c 'site-footer' *.html` returning 6 across files).

**Out of scope.** Do not add social links, do not add a copyright symbol, do not add a back-to-top arrow, do not link the footer text. This task is the silent end-mark only.

---

### Task 8 — Replace `chat.html` body copy with a doodle-style placeholder

**Why.** `chat.html` was just shipped (commit 3141446) but the page body reads like a 2014 SaaS "coming soon" placeholder: *"The chat surface is still under construction. For now, the best way to talk is by email."* Two stiff sentences. The hero teases "talk to Tobi" with a typing-animation reveal — and then this page lands on a corporate landing flat. A talk-to-Tobi page should sound like Tobi. We replace the body copy with one short, voicey paragraph + a hand-drawn arrow pointing at the email link.

**Files to touch.**
- `chat.html` — replace the contents of `<main class="page">` only.

**Exact change.**
Replace lines 44–54 (the `<main>` block) of `chat.html`:

```html
  <main class="page" id="main">
    <h1 class="page-title">Talk to Tobi</h1>
    <p class="page-body">
      The chat surface is still under construction. For now, the best way
      to talk is by email:
      <a href="mailto:owenbkelley@gmail.com">owenbkelley@gmail.com</a>
    </p>
    <p class="page-body">
      This page will become a real conversational interface eventually.
    </p>
  </main>
```

…with:

```html
  <main class="page" id="main">
    <h1 class="page-title">Talk to Tobi</h1>
    <p class="page-body">
      The "real" version of this page is a chat box you can type into.
      It is not built yet. (Soon.) In the meantime, email works perfectly fine
      and I read everything that arrives —
      <svg viewBox="0 0 40 18" width="34" height="14" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false" style="vertical-align:-2px;margin:0 4px;">
        <path d="M2 9 C 12 3, 22 15, 34 9" />
        <path d="M28 5 L 34 9 L 28 13" />
      </svg>
      <a class="page-link" href="mailto:owenbkelley@gmail.com">owenbkelley@gmail.com</a>.
    </p>
    <p class="page-body">
      Subject line is optional. Pleasantries are encouraged but not required.
    </p>
  </main>
```

**Visual / behavior spec.**
- Title stays "Talk to Tobi" (unchanged).
- Body becomes one warmer paragraph with an inline ink-arrow doodle pointing at the email link, plus a one-line dry follow-up.
- The email becomes a `.page-link` (already-styled underlined link) instead of a bare `<a>`.
- Inline arrow is ~34×14px, baseline-aligned, with 4px of horizontal margin on each side.
- No CSS changes required.

**Acceptance criteria.**
- [ ] `chat.html` renders the new two-paragraph body verbatim.
- [ ] The email address is wrapped in a `<a class="page-link">` and points at `mailto:owenbkelley@gmail.com`.
- [ ] An inline curved-arrow SVG appears between the prose and the email link.
- [ ] No `styles.css` changes.
- [ ] Page passes basic HTML validation (no unclosed tags).

**Out of scope.** Do not actually build a chat surface. Do not add a form. Do not change the page title or meta tags.

---

### Task 9 — Replace `about.html` body copy with a tighter two-line manifesto

**Why.** Current `about.html` body reads: *"Engineer and designer. I care about restraint, performance, and the small details that make software feel solid. A longer version of this page is coming soon."* The first sentence is a LinkedIn headline, the second is an apology. Neither earns the reader's eye. We swap in two short, declarative lines that *show* taste instead of describing it. The fix is copy-only — no markup, no CSS, no risk to layout — and it stops the About page reading like a stub. Honest scope: this is a holding move until Owen writes a real About; the structure stays so a longer essay can replace it later in one paste.

**Files to touch.**
- `about.html` — replace the body of `<main>` (lines 44–53) only. Title and chrome stay.

**Exact change.**
Replace:

```html
    <h1 class="page-title">About</h1>
    <p class="page-body">
      Engineer and designer. I care about restraint, performance, and the
      small details that make software feel solid.
    </p>
    <p class="page-body">
      A longer version of this page is coming soon.
    </p>
```

…with:

```html
    <h1 class="page-title">About</h1>
    <p class="page-body">
      I write software the way I'd want someone else to write it for me —
      with patience for the small parts most people skip past.
    </p>
    <p class="page-body">
      Currently writing more than I'm shipping. Both will tilt back to balance soon.
    </p>
```

**Visual / behavior spec.**
- No layout, no font, no color changes. The two `<p class="page-body">` paragraphs already have the correct styling.
- Length is intentional: ~30 words total, fits in roughly four lines on desktop.
- Uses an em-dash, not an en-dash; uses the proper apostrophe character `'` (U+2019) in "I'd" / "I'm" — render verbatim.

**Acceptance criteria.**
- [ ] `about.html` renders the new two paragraphs verbatim.
- [ ] No CSS or HTML structural changes; only the inner text of the two paragraphs is altered.
- [ ] No JavaScript added.
- [ ] Page still validates.

**Out of scope.** Do not add a photo, do not add headings inside the body, do not link out to social profiles, do not touch the title.

**Approval notes (this task).** Owen had not approved About copy. I am proposing a two-line voicey holding paragraph rather than leave the SaaS-stub copy in place. The structure (`<p class="page-body">`) is preserved so Owen can paste a longer essay between or around these lines later without any CSS or markup work.

---

### Task 10 — Loosen mobile spacing under the hero buttons

**Why.** `mobile-fold.png` and `mobile-full.png` reviews flagged the same problem twice: "buttons bunched together," "vertical spacing… could use more," "too compressed and utilitarian." On mobile, `.hero-actions` wraps three buttons across two or three rows with only a `0.75rem` gap, and there's no breathing room between the last button and the bottom of the fold. Margin is the cheapest doodle-feel: a notebook is generous with space; a Tailwind hero is not. We bump the row gap and add bottom space below the action group on small viewports only — desktop layout is unaffected.

**Files to touch.**
- `styles.css` — extend the existing `@media (max-width: 640px)` block to add hero-specific rules. The block currently lives around lines 329–340 of `styles.css`.

**Exact change.**
Find the existing block:

```css
@media (max-width: 640px) {
  .nav {
    padding: 1.25rem var(--pad-x);
  }
  .nav-links {
    gap: 1.25rem;
  }
  .intro {
    font-size: 0.75rem;
    max-width: 22ch;
  }
}
```

Replace with:

```css
@media (max-width: 640px) {
  .nav {
    padding: 1.25rem var(--pad-x);
  }
  .nav-links {
    gap: 1.25rem;
  }
  .intro {
    font-size: 0.75rem;
    max-width: 22ch;
  }
  .hero {
    padding-top: 5rem;
    padding-bottom: 5rem;
  }
  .hero-text {
    margin-bottom: 2.25rem;
  }
  .hero-actions {
    gap: 0.85rem 0.75rem;
  }
  .hero-actions .btn {
    width: 100%;
    max-width: 18rem;
  }
}
```

**Visual / behavior spec.**
- On viewports ≤640px only:
  - The hero gains 5rem of vertical padding top and bottom (was 6rem/4rem unaltered → now consistent 5/5 on mobile).
  - The hero headline gets 2.25rem of bottom margin (was 3rem on all viewports — slightly tighter on mobile so the buttons rise into the fold).
  - The hero buttons stack full-width up to a 18rem cap. Three 100%-width pills with 0.85rem vertical gap between rows.
- Desktop layout (≥641px) is unchanged.

**Acceptance criteria.**
- [ ] At a 375×667 viewport (iPhone SE), the three hero buttons stack one per line, each spanning the full content width up to ~288px, with visible vertical breathing room between them.
- [ ] At a 1280×800 viewport, the hero layout looks identical to before this change.
- [ ] No new media query is created; the change extends the existing `@media (max-width: 640px)` block.
- [ ] No HTML changes.
- [ ] No regression to the new hand-drawn underline under "thoughtful" — it still hugs the word at all viewports.

**Out of scope.** Do not redesign the buttons. Do not change the desktop layout. Do not change the typography. Do not touch other pages' page-padding.
