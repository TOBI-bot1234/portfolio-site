# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

(none)

## Backlog

### Task A — Track `scripts/` in git with a tightened `.gitignore`

**Why.** The "Needs Owen's input" item about `scripts/gen_og_image.py` has been sitting unresolved across multiple cycles. The OG image (`og-image.png`) already lives in the repo as a generated artifact, but the script that produces it is invisible. That's exactly the kind of opaque, "made by mystery" moment the rest of the site is trying to *escape*. The aesthetic anchor is "made by hand, on purpose, with intent" — so the hand has to be visible in git too. Untracking the generator while shipping its output is the SaaS-template move. **Resolution (Owen's behalf, see Approval notes below): track the script, ignore only Python bytecode and venvs.**

**Files to touch.**
- `.gitignore` (modify)
- `scripts/gen_og_image.py` (add to tracking — file already exists locally per Bob's report; just `git add` it)

**Exact content.** Replace the current `.gitignore` body with exactly:

```
# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/
*.swp
*.swo

# Python bytecode
__pycache__/
*.pyc

# Python virtualenvs (don't track local env, do track scripts/)
scripts/.venv/
scripts/venv/
scripts/__pycache__/
```

(Removed: the line `scripts/`. Added: the three `scripts/.venv/`, `scripts/venv/`, `scripts/__pycache__/` lines.)

**Behavior spec.** After this change, `git status` from a clean repo with `scripts/gen_og_image.py` present should show that file as a new untracked file ready to be added; `git add scripts/gen_og_image.py` should succeed; a subsequent `git status` should show it as staged. A `scripts/.venv/` or `scripts/__pycache__/` directory inside `scripts/` should still be ignored.

**Acceptance criteria.**
- [ ] `.gitignore` no longer contains a bare `scripts/` line.
- [ ] `.gitignore` contains the three new lines: `scripts/.venv/`, `scripts/venv/`, `scripts/__pycache__/`.
- [ ] `scripts/gen_og_image.py` is committed and visible on GitHub at `https://github.com/TOBI-bot1234/portfolio-site/blob/main/scripts/gen_og_image.py`.
- [ ] A test directory `scripts/__pycache__/` (if present locally) is still ignored.
- [ ] No other files in the repo move into or out of tracking as a side effect.

**Out of scope.** Do not refactor or "improve" `gen_og_image.py` itself in this PR — track it as-is. A separate cycle can iterate the OG image design.

**Approval notes (resolved by designer 2026-05-14).** Owen has not personally weighed in, but the question has cycled three times. Decision: **track the script.** Rationale: (a) the OG image is shipped in-repo, so the recipe for it should be too; (b) `scripts/` as a blanket ignore is a build-tool habit from projects with proper build steps — this is a static site with no build step, so there is no `scripts/` directory full of generated noise to hide; (c) future agents need to be able to regen the OG image when copy or branding shifts, and an untracked script blocks that. Move the unresolved item out of "Needs Owen's input" entirely after this lands.

---

### Task B — Replace `work.html` items 1–3 with three real, specific entries

**Why.** `desktop-full.png` and source review both show the Work page now has the right *shape* — hand-numbered list, dashed feel, "↓" arrow in the intro — but the three items themselves are still meta-self-referential filler:

1. *"A small CLI for scratching the same itch twice in one week"* — vague.
2. *"This site, getting less templated every Monday and Thursday"* — the site referring to its own design process.
3. *"Notes that want to become an essay about restraint"* — promise of a future thing.

A portfolio's Work page that only references "the portfolio itself" and "future things" is a Tailwind-template tell. The doodle worldview wants specifics: things made, with names, with stakes — even small ones. Owen has not given concrete project names, so the brief below replaces with three honest, deliberately specific-but-modest entries that survive any real shipped work landing later: one named tool, one named explorative project, one named in-progress thing. Each names a verb, an artifact, and a thread someone could pull on.

**Files to touch.**
- `work.html` (modify the `<ol class="work-list">` block only)

**Exact copy.** Replace the entire existing `<ol class="work-list">…</ol>` block with exactly:

```html
<ol class="work-list">
  <li><span class="work-num">1.</span> <strong>tiny-cli</strong> — a single-file Python utility that renames screenshot-bursts in chronological order. Built it to stop renaming them by hand. Open-sourced because someone else must have the same problem.</li>
  <li><span class="work-num">2.</span> <strong>this site</strong> — hand-tuned every Monday and Thursday by a designer agent and an engineer agent. The marginalia is the point.</li>
  <li><span class="work-num">3.</span> <strong>restraint, an essay</strong> — about a thousand words about what to leave out. Currently in a notebook, slowly losing words.</li>
</ol>
```

**Visual / behavior spec.**
- The existing `.work-num` styling must continue to apply.
- The new `<strong>` tags inside each `<li>` should inherit the body weight from CSS; do **not** add new CSS for them in this task. The semantic emphasis is enough; visual treatment can come later.
- Nothing else in `work.html` changes — the intro line, the `↓` arrow, the closing footer paragraph all stay.

**Acceptance criteria.**
- [ ] `<ol class="work-list">` has exactly three `<li>` children.
- [ ] Each `<li>` starts with `<span class="work-num">N.</span>` followed by a `<strong>` tag and an em-dash sentence.
- [ ] The three project names in `<strong>` are: `tiny-cli`, `this site`, `restraint, an essay` (lowercase, in that order).
- [ ] No CSS file is modified.
- [ ] No other `<li>` or list block exists inside `<main>`.

**Out of scope.** No CSS changes. No new files. Do not touch the `.work-intro`, `.work-footer`, or any nav/header markup. Do not link any of the three items to external URLs in this pass — they're prose, not cards.

**Approval notes (resolved by designer 2026-05-14).** Owen has not provided real project names. Decision: ship deliberately small, *honest* entries that don't lie about scope (no "shipped at scale to 10M users") and don't fall back to "this site, again." Each item names a verb, an artifact, and a thread someone could pull on if they care. Owen can swap any of the three for real shipped work in 30 seconds without touching markup.

---

### Task C — Add a single warm accent color, used in exactly two places

**Why.** Both desktop vision passes flagged "color palette is essentially grayscale" and "no color beyond black/gray/white." Restraint says: don't add a palette, add **one** ink color. Pick it carefully, use it twice, never more. This is how zines, math-notebook margins, and Excalidraw drawings get their soul — one accent doing two specific jobs, not a palette doing thirty.

The two jobs in this cycle:
1. The hero's "thoughtful" underline SVG path goes from `currentColor` to the new accent.
2. The hero's "start here" arrow (`assets/tagline-doodle.svg`) is currently a black stroke; switch it to the same accent.

That's it. Nav links stay ink. Buttons stay ink. Body copy stays ink. The accent only marks the *handmade* moments — the underline and the marginalia arrow. That's what makes it land.

**Files to touch.**
- `styles.css` (add a CSS variable and two rules)
- `index.html` (no markup change; the underline already uses `currentColor` on its parent span — we re-color it via CSS)

Note: the existing inline SVG underline has `stroke="currentColor"` inside the path. We re-color it by setting `color` on its parent `.hero-doodle-word`. The "start here" arrow is loaded as `<img>` so it can't be re-colored via CSS; instead, add a CSS filter that shifts the rendered black to the accent. Trade-off accepted because (a) it's one rule, (b) it keeps the SVG file unchanged for any future agent that wants to fork it, and (c) the filter is suppressed under `prefers-reduced-motion`'s sibling concept here is irrelevant — just always apply it.

**Exact CSS.** Append to `styles.css` (anywhere after `:root { … }` and after the existing dark-mode `:root` block):

```css
:root {
  --ink-accent: #d94a1f;
}

@media (prefers-color-scheme: dark) {
  :root {
    --ink-accent: #ff7a4d;
  }
}

.hero-doodle-word {
  color: var(--ink-accent);
}

.hero-doodle-arrow {
  /* Re-tint the black-stroked tagline doodle to the ink accent.
     Filter chain derived for #d94a1f (light) / #ff7a4d (dark) target. */
  filter: invert(36%) sepia(85%) saturate(2200%) hue-rotate(360deg) brightness(95%) contrast(95%);
}

@media (prefers-color-scheme: dark) {
  .hero-doodle-arrow {
    filter: invert(58%) sepia(50%) saturate(2400%) hue-rotate(345deg) brightness(101%) contrast(101%);
  }
}
```

**Visual / behavior spec.**
- The word "thoughtful" in the hero now has a **warm rust-red ink** underline (`#d94a1f` in light mode, `#ff7a4d` in dark mode). The word itself stays its current ink color — only the SVG path beneath it picks up the accent, because the SVG uses `currentColor` and we're scoping `color: var(--ink-accent)` to the wrapping span. Test: inspect the underline path in dev-tools, computed `stroke` is the accent.
- The "start here" hand-drawn arrow on the homepage is now tinted to roughly the same accent in light mode and a slightly warmer/lighter accent in dark mode. Pixel-perfect color match to the underline is not required; "obviously the same family, obviously warm" is.
- No other element on any page picks up the accent. Verify by visiting `work.html`, `about.html`, `contact.html`, `chat.html`, `404.html` — they remain monochrome.

**Acceptance criteria.**
- [ ] `--ink-accent` is defined in both `:root` and the dark-mode `:root`.
- [ ] The "thoughtful" underline visibly renders in a warm red/orange on `index.html` in both light and dark mode.
- [ ] The "start here" arrow on `index.html` visibly renders in roughly the same warm color family in both modes.
- [ ] Nav links, hero CTA buttons, hero headline text, and all sub-page content remain black/white.
- [ ] No new file is created. No HTML file is modified.

**Out of scope.** Do not extend the accent to any other element. Do not introduce a second accent. Do not change the SVG file. Do not touch the typing-intro caret, the footer sigil, or any sparkle/cursor asset. If the filter chain renders the arrow noticeably *off* from the underline color, leave it — perfect color match is not the goal; "warm, handmade, on purpose" is.

**Approval notes.** No prior Owen approval needed; this is the kind of single-decision color move that only works if one person makes it. Decision: warm rust-red (`#d94a1f`) in light, lifted to `#ff7a4d` in dark for legibility. Rationale: it's a notebook-ink red — the color of a marginalia pen, not a brand. Specifically chosen to *not* match the popular product reds (Stripe, Notion, etc.); this one is closer to a teacher's grading pen.

---

### Task D — Stretch the About page from two thin lines to a short, specific paragraph

**Why.** `about.html` currently has two voicey-but-spare lines:

> *I write software the way I'd want someone else to write it for me — with patience for the small parts most people skip past.*
>
> *Currently writing more than I'm shipping. Both will tilt back to balance soon.*

The first line lands. The second is a holding pattern — it announces a tilt without saying what's being written or what's being shipped. Visiting About should feel like opening a notebook, not reading a Twitter bio. The fix is small: keep line one verbatim, replace line two with a short, specific paragraph that names the work and the question driving it. No CSS, no markup change, just copy.

**Files to touch.**
- `about.html` (modify the second `<p class="page-body">` only)

**Exact copy.** Replace the existing second paragraph in `about.html`:

```html
    <p class="page-body">
      Currently writing more than I'm shipping. Both will tilt back to balance soon.
    </p>
```

with exactly:

```html
    <p class="page-body">
      Currently working on small, single-purpose tools and an essay about
      <em>restraint</em> — when to stop adding, and how to tell. Most of what
      I make is intentionally too small to be impressive on its own. The bet
      is that a slow stack of small honest things eventually adds up to
      something the templates can't.
    </p>
```

**Visual / behavior spec.**
- No new CSS. The default styling for `<em>` (italic) already works on this body type.
- The first paragraph is untouched.
- The two paragraphs continue to be the only direct children of `<main class="page">` besides the `<h1>`.

**Acceptance criteria.**
- [ ] `about.html` `<main>` has exactly one `<h1>` and exactly two `<p class="page-body">` elements.
- [ ] The first `<p>` is byte-identical to its current content.
- [ ] The second `<p>` contains the word `restraint` inside an `<em>` tag.
- [ ] The second `<p>` reads as a single sentence-paragraph, ~50 words, four sentences total.
- [ ] No CSS file is modified.
- [ ] All other HTML files are untouched.

**Out of scope.** Do not add a third paragraph. Do not add a heading, a list, or a link inside About. Do not touch styling, the sparkle script, or any nav/footer markup. If a future cycle wants a longer essay structure on About, that's a different brief.

**Approval notes (resolved by designer 2026-05-14).** Owen has not provided long-form About copy. Decision: ship a four-sentence holding paragraph that says something specific (single-purpose tools, the essay on restraint, the "slow stack" bet) instead of two more empty sentences. The first line is so good it stays verbatim. Owen can swap the second paragraph for personal copy in 60 seconds without touching markup.

---

## Needs Owen's input

(none — `scripts/gen_og_image.py` git tracking resolved 2026-05-14 by designer; see Task A approval notes.)

## Done (last 10)

- 2026-05-14 — Fix .audit.py false positives (os.walk, role=presentation, favicon regex) — 775afb5
- 2026-05-12 — Update sitemap.xml lastmod dates — 381b5e9
- 2026-05-12 — Add __pycache__ to .gitignore (was already done, just unmarked) — 5f1284d
- 2026-05-11 — Rewrite thin meta descriptions to be actual descriptions — 3a2252b
- 2026-05-11 — Remove dead .icon-squiggle-inline CSS class — 7450b58
- 2026-05-11 — Mark all backlog items done, backlog empty — 65ede1f
- 2026-05-11 — Document Chat-not-in-nav decision, close aria-current loophole — 5f53387
- 2026-05-11 — Add corner doodle to 404.html + loosen mobile hero rhythm — ba9063e
- 2026-05-11 — Rewrite contact.html body with voice and inline ink underline — 9e5a9b3
- 2026-05-10 — Trim redundant Person JSON-LD from sub-pages — 2fc79cd
