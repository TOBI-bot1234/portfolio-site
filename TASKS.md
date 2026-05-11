# Tasks

Single source of truth for portfolio-site work. See "Task tracker" in Bob's instructions for the workflow.

## In progress

(none)

## Backlog

### 1. Rewrite thin meta descriptions to be actual descriptions

**Why.** All 6 pages have meta descriptions under 35 characters — they're stubs, not descriptions. Google shows 120-160 chars. The current ones read like file names, not summaries. `about.html` says "About Owen Kelley." (18 chars). `work.html` says "Selected work by Owen Kelley." (29 chars). This doesn't help SEO and it doesn't help social previews (though og:description is separate, the HTML meta description is still the canonical summary).

**Scope.** Update `<meta name="description">` on all 6 pages with 100-140 character descriptions that actually say something. Also update the corresponding `<meta property="og:description">` to match on each page (they should be in sync, since the site uses the same description for both).

**Files to touch.** `index.html`, `work.html`, `about.html`, `contact.html`, `chat.html`, `404.html`

**Proposed descriptions.** (100-135 chars each, written in the same voice as the page body)

| Page | Description |
|------|-------------|
| `index.html` | Owen Kelley — software engineer who writes the kind of code he'd want someone else to write for him. Personal portfolio and landing page. |
| `work.html` | Projects Owen has shipped or is currently shipping. Each item is a short summary, no lorem ipsum. |
| `about.html` | How Owen got here and what he cares about. Two paragraphs, no fluff — patience for the small parts most people skip. |
| `contact.html` | Email is the front door. Owen reads everything and writes back on purpose, usually within a day or two. |
| `chat.html` | Chat isn't built yet. Email works. Easter-egg page reached from the hero typing animation. |
| `404.html` | That page either moved, broke, or never existed. Sorry about it — try home or just email me directly. |

**Acceptance criteria.**
- [ ] All 6 `<meta name="description">` tags updated to 100-135 chars
- [ ] All 6 `<meta property="og:description">` tags updated to match
- [ ] `<title>` tags untouched on every page
- [ ] No other HTML or CSS changes

## Needs Owen's input

(none)

## Done (last 12)

- 2026-05-11 — Remove dead .icon-squiggle-inline CSS class — 7450b58
- 2026-05-11 — Mark all backlog items done, backlog empty — 65ede1f
- 2026-05-11 — Document Chat-not-in-nav decision, close aria-current loophole — 5f53387
- 2026-05-11 — Add corner doodle to 404.html + loosen mobile hero rhythm — ba9063e
- 2026-05-11 — Rewrite contact.html body with voice and inline ink underline — 9e5a9b3
- 2026-05-10 — Trim redundant Person JSON-LD from sub-pages — 2fc79cd
- 2026-05-10 — Consolidate repeated footer SVG into assets/footer.js — fe50af3
- 2026-05-10 — Add noreferrer to resume link rel attribute — 2ae3f45
- 2026-05-09 — Update structured data canonical URLs on sub-pages — 796c808
- 2026-05-09 — Extract inline SVG styles to CSS classes — b4deec4
- 2026-05-08 — Audit: add missing twitter:image meta to all 6 pages — 50174cf
- 2026-05-08 — Clean up stale task briefs in TASKS.md (~495 lines removed) — 0fdee2c
