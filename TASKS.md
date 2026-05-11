# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

### Rewrite `contact.html` body — kill the support-ticket tone

**Why.** Contact is currently the most generic page on the site. The body is one line — *"The best way to reach me is by email."* — followed by a `mailto:`. That sentence could be on a Zendesk help center. The rest of the site (hero underline, "start here" arrow, About's voicey two paragraphs, Work's hand-numbered notebook list) is the opposite of this. `desktop-full.png` review across two cycles has consistently flagged inner pages as falling off a cliff vs the hero; Contact is the worst offender because it's the page where a real human is supposed to be on the other end and we sound like a form.

This is pure copy + one inline ink mark. No CSS work, no new files.

**Files to touch.**
- `contact.html`
- `styles.css` (append only)

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

## Backlog

### 2. Add a corner doodle to `404.html` only

Replace `<main>` with doodle SVG + updated copy. Append CSS to `styles.css`.

**Files.** `404.html`, `styles.css` (append only).

See original brief for full markup/CSS (kept in git history from Owen's TASKS.md push).

---

### 3. Mobile-only: loosen vertical rhythm under the hero buttons

Single `@media (max-width: 600px)` block appended to `styles.css`. No HTML changes.

See original brief for full CSS (kept in git history from Owen's TASKS.md push).

---

### 4. Document Chat-not-in-nav decision; close the aria-current loophole

Add HTML comment in `chat.html` inside `<nav class="nav-links">`, add `## Pages` section to `README.md`.

See original brief for exact comment/README text (kept in git history).

## Needs Owen's input

(none — see In Progress task approval notes above)

## Done (last 10)

- 2026-05-10 — Trim redundant Person JSON-LD from sub-pages — 2fc79cd
- 2026-05-10 — Consolidate repeated footer SVG into assets/footer.js — fe50af3
- 2026-05-10 — Add noreferrer to resume link rel attribute — 2ae3f45
- 2026-05-09 — Update structured data canonical URLs on sub-pages — 796c808
- 2026-05-09 — Extract inline SVG styles to CSS classes — b4deec4
- 2026-05-08 — Audit: add missing twitter:image meta to all 6 pages — 50174cf
