"""Contract checks for the dependency-free Pages source; run with unittest."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SiteTests(unittest.TestCase):
    def test_single_source_plan(self):
        page = (ROOT / 'index.html').read_text()
        self.assertIn('include_relative plan_directo/plan_director.md', page)
        self.assertIn('markdownify', page)
        self.assertNotIn('<script', page)

    def test_navigation_targets_exist(self):
        page = (ROOT / 'index.html').read_text()
        plan = (ROOT / 'plan_directo/plan_director.md').read_text()
        targets = re.findall(r'href="#([a-z-]+)"', page)
        self.assertGreaterEqual(len(targets), 8)
        for target in targets:
            self.assertTrue(f'{{#{target}}}' in plan or f'id="{target}"' in page, target)

    def test_project_subpath_and_publication_scope(self):
        config = (ROOT / '_config.yml').read_text()
        self.assertIn('baseurl: /hito-celulaia-proyectos2026', config)
        for path in ['odd/', 'tests/', 'README.md']:
            self.assertIn(path, config)
        page = (ROOT / 'index.html').read_text()
        self.assertIn("'/assets/style.css' | relative_url", page)
        self.assertIn('name="viewport"', page)
        self.assertIn('lang="es"', page)
        self.assertIn('aria-label=', page)

    def test_responsive_and_keyboard_styles(self):
        css = (ROOT / 'assets/style.css').read_text()
        for rule in ['@media', ':focus-visible', 'overflow-x: auto', 'prefers-reduced-motion']:
            self.assertIn(rule, css)


if __name__ == '__main__':
    unittest.main()
