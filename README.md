# portfolio-site

Personal portfolio site for Owen Kelley. A small, deliberately plain set of pages introducing him, his work, and how to get in touch.

Live: https://tobi-bot1234.github.io/portfolio-site/

## Stack

Plain static HTML and CSS with a small amount of vanilla JavaScript for the typewriter intro. No framework, no build step, no dependencies. Deployed via GitHub Pages from `main`.

## Pages

- `index.html` — landing
- `work.html` — selected work
- `about.html` — about Owen
- `contact.html` — contact
- `404.html` — not found

## Running locally

Open `index.html` directly in a browser, or serve the directory:

```sh
python3 -m http.server 8000
```

Then visit http://localhost:8000.

## Deploying

Push to `main`. GitHub Pages picks it up automatically.
