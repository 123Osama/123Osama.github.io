# Osama — Portfolio (multi-page version)

Each nav item is now its own real HTML file — clicking "Research" loads `research.html`,
not just an anchor-scroll on one long page. This makes editing far simpler: open the one
file for the page you want to change, and the sidebar/nav are identical across all of them.

## File structure

```
├── index.html          ← Home (hero, morpheme demo, bio, scrollable Updates window)
├── research.html        ← Research / thesis
├── projects.html        ← Projects
├── publications.html    ← Publications
├── skills.html           ← Skills
├── thoughts.html         ← My Thought (blog-style entries)
├── contact.html          ← Contact
├── css/style.css        ← shared styling for all pages
├── js/script.js         ← shared behavior (footer year, morpheme demo) for all pages
├── images/profile.jpg   ← your photo (add this yourself)
└── cv.pdf               ← your CV (add this yourself)
```

## How to edit each page

Every page has the **same two sections**:
1. `<aside class="sidebar">` — identical on all 7 files. If you change anything here
   (your name, email, links, tagline), you need to copy that same change into **all 7**
   HTML files, since there's no shared template engine — this is plain static HTML.
2. `<main class="content">` — this is what's unique per page. Only edit the content
   inside `<main>` for the page you're working on.

**The Updates window lives only on `index.html`** (inside the `.updates-box` div), exactly
as you asked — it doesn't appear on any other page, and it scrolls independently inside its
own small box rather than scrolling the whole page.

## Nav bar

The nav bar at the top of `<main>` is the same 7 links on every page:
```html
<nav class="topnav" aria-label="Section navigation">
  <a href="index.html">Home</a>
  <a href="research.html">Research</a>
  <a href="projects.html">Projects</a>
  <a href="publications.html">Publications</a>
  <a href="skills.html">Skills</a>
  <a href="thoughts.html">My Thought</a>
  <a href="contact.html">Contact</a>
</nav>
```
The current page's link has `class="active"` added to it (so it's highlighted) — that's
the only difference in the nav block between files.

## If you'd rather not hand-edit 7 files for sidebar changes

There's a `build.py` script included that generates all 7 pages from one shared sidebar
template and per-page content blocks — if you have Python installed, edit `build.py`
instead of the HTML files directly, then run:
```bash
python3 build.py
```
This regenerates all 7 HTML files at once so the sidebar only needs to change in one
place. This is optional — plain HTML editing works fine too, it's just more repetitive.

## Publishing

Same as before — push all files (including the `css/` and `js/` folders) to your
`123Osama.github.io` repo and enable GitHub Pages from Settings → Pages.
