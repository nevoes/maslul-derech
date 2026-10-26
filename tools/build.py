#!/usr/bin/env python3
"""Stamps the shared parts of the site into every page.

The pages stay plain HTML files (GitHub Pages serves them as-is). The parts that
are the same on every page live once, in partials/, and this script copies them
into each page between marker comments:

    partials/nav.html     -> <!-- nav:start --> ... <!-- nav:end -->        (Hebrew pages)
    partials/footer.html  -> <!-- footer:start --> ... <!-- footer:end -->  (Hebrew pages)
    partials/icons.svg    -> <!-- icons:start --> ... <!-- icons:end -->    (all pages)

Shared CSS is not stamped: it lives in site.css, which every page links to.

Usage, after editing anything in partials/:   python3 tools/build.py
A new page: copy an existing page (it already has the markers), then run the script.
english.html has its own English menu and footer, so it only gets the icons.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PART = ROOT / "partials"
SKIP = re.compile(r"^(404|review)")
ENGLISH = {"english.html"}


def stamp(html, name, content):
    pat = re.compile(r"(<!-- %s:start -->)(.*?)(<!-- %s:end -->)" % (name, name), re.S)
    if not pat.search(html):
        return html, False
    return pat.sub(lambda m: m.group(1) + content + m.group(3), html, count=1), True


def main():
    nav = (PART / "nav.html").read_text(encoding="utf-8").strip("\n")
    footer = (PART / "footer.html").read_text(encoding="utf-8").strip("\n")
    icons = (PART / "icons.svg").read_text(encoding="utf-8").strip("\n")
    missing = []
    for page in sorted(ROOT.glob("*.html")):
        if SKIP.match(page.name):
            continue
        html = page.read_text(encoding="utf-8")
        parts = [("icons", icons)]
        if page.name not in ENGLISH:
            # On the home page the "בית" link points to the top of the page itself.
            page_nav = nav.replace('class="nav-home" href="index.html"', 'class="nav-home" href="#"') if page.name == "index.html" else nav
            parts += [("nav", page_nav), ("footer", footer)]
        new = html
        for name, content in parts:
            new, ok = stamp(new, name, content)
            if not ok:
                missing.append(f"{page.name}: no {name} markers")
        if new != html:
            page.write_text(new, encoding="utf-8")
            print("updated", page.name)
    if missing:
        print("\n".join(missing))
        sys.exit(1)


if __name__ == "__main__":
    main()
