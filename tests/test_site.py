"""Smoke checks against the actual Jekyll output; no browser dependencies."""

import os
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = Path(os.environ.get("ACADEMIC_SITE_DIR", ROOT / "_site"))
BASEURL = os.environ.get("ACADEMIC_BASEURL", "")


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def elements(self, tag):
        return [attrs for name, attrs in self.tags if name == tag]


class SiteTests(unittest.TestCase):
    def page(self, route=""):
        path = SITE / route / "index.html"
        self.assertTrue(path.is_file(), f"Missing rendered page: {route or '/'}")
        return Page(path)

    def test_research_and_software_are_reachable_from_home(self):
        home = self.page()
        hrefs = {a.get("href") for a in home.elements("a")}
        for route in ("research", "publications", "software"):
            self.assertIn(f"{BASEURL}/{route}/", hrefs)
            self.page(route)

    def test_home_has_keyboard_navigation_and_main_landmark(self):
        home = self.page()
        main = home.elements("main")
        self.assertEqual(len(main), 1)
        self.assertEqual(main[0].get("id"), "main-content")
        self.assertTrue(any(a.get("href") == "#main-content" for a in home.elements("a")))

    def test_complete_bibliography_is_preserved(self):
        keys = set(re.findall(r"@\w+\s*\{\s*([^,]+),", (ROOT / "_bibliography/papers.bib").read_text()))
        ids = {attrs["id"] for _, attrs in self.page("publications").tags if "id" in attrs}
        self.assertEqual(keys - ids, set(), "A bibliography entry was omitted")

    def test_home_images_are_accessible_and_exist(self):
        images = [i for i in self.page().elements("img") if "publication_preview" in i.get("src", "")]
        self.assertGreaterEqual(len(images), 3, "Selected research should include previews")
        for image in images:
            self.assertTrue(image.get("alt"), f"Missing image alternative text: {image.get('src')}")
            src = image.get("src", "")
            if src.startswith("/"):
                self.assertTrue((SITE / unquote(src.removeprefix(BASEURL)).lstrip("/")).is_file(), src)

    def test_new_pages_have_no_duplicate_ids_or_broken_internal_links(self):
        for route in ("", "research", "software"):
            page = self.page(route)
            ids = [attrs["id"] for _, attrs in page.tags if "id" in attrs]
            self.assertEqual([key for key, count in Counter(ids).items() if count > 1], [])
            for link in page.elements("a"):
                url = urlsplit(link.get("href", ""))
                if url.scheme or url.netloc or not url.path.startswith("/"):
                    continue
                if BASEURL:
                    self.assertTrue(url.path.startswith(BASEURL + "/"), url.path)
                path = SITE / unquote(url.path.removeprefix(BASEURL)).lstrip("/")
                self.assertTrue(path.is_file() or (path / "index.html").is_file(), str(path))
                if url.fragment:
                    target = path / "index.html" if path.is_dir() else path
                    target_ids = {a.get("id") for _, a in Page(target).tags}
                    self.assertIn(url.fragment, target_ids)

    def test_cv_remains_a_pdf(self):
        path = SITE / "assets/pdf/JJ_CV.pdf"
        self.assertTrue(path.is_file())
        self.assertEqual(path.read_bytes()[:5], b"%PDF-")

    def test_dark_default_is_rendered_before_javascript_loads(self):
        page = self.page()
        self.assertEqual(page.elements("html")[0].get("data-theme"), "dark")
        self.assertEqual(page.elements("html")[0].get("data-default-theme"), "dark")
        toggle = next((b for b in page.elements("button") if b.get("id") == "light-toggle"), {})
        self.assertTrue(toggle.get("aria-label"), "The theme switch needs an accessible label")


if __name__ == "__main__":
    unittest.main()
