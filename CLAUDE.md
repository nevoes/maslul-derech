# מסלול ודרך – maslul-derech.co.il

Static site on GitHub Pages (custom domain www.maslul-derech.co.il, see CNAME). Every page is a plain, complete HTML file.

## Shared parts – edit once, not in every page
- **Menu, footer, SVG icons:** edit `partials/nav.html`, `partials/footer.html`, `partials/icons.svg`, then run `python3 tools/build.py`. The script copies them into every page between `<!-- nav:start -->`/`<!-- nav:end -->` (same for `footer`, `icons`). Never edit the content between those markers inside a page; it is overwritten on the next build.
- **Shared CSS:** `site.css`, linked from every page. Page-specific CSS stays in the page's own `<style>` blocks, which come after `site.css`, so a page can override shared rules.
- `english.html` has its own English menu and footer (no nav/footer markers); it only shares the icons and `site.css`.

## Adding a page
Copy an existing Hebrew page (it already has the markers and the `site.css` link), change its content and `<head>` meta (title, description, og:*, canonical with `https://www.`), run `python3 tools/build.py`, and add the page to `sitemap.xml`. Add it to `partials/nav.html` if it belongs in the menu.

## Already in place – keep when editing
- Skip link `<a class="skip" href="#main">` right after `<body>` and `id="main"` on `<main>`.
- GoatCounter script before `</body>` (`maslul-derech.goatcounter.com`).
- Contact form (`contact.html`) posts to a Google Form; field IDs are in the script under the form.
- Accessibility statement: `accessibility.html`, small link under the footer icons. Keep text contrast at WCAG AA (e.g. `--orange-ink` is `#A85200` for that reason).
- Canonical / og:url always use `https://www.maslul-derech.co.il/...`.

## Before publishing a visual-neutral change
Compare full-page screenshots before/after at 1280px and 390px; the owner wants the look unchanged unless he approved a change.
