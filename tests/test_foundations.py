import hashlib
import json
from pathlib import Path
import runpy
import unittest
import xml.etree.ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def luminance(value):
    rgb = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in rgb]
    return sum(a*b for a, b in zip(linear, (.2126, .7152, .0722)))


class Foundations(unittest.TestCase):
    def test_semantic_pairs_have_aa_contrast(self):
        themes = json.loads((ROOT / 'tokens/design.json').read_text())['themes']
        self.assertEqual(themes['light'].keys(), themes['dark'].keys())
        for theme, t in themes.items():
            pairs = [('text', 'surface'), ('text', 'surface-raised'), ('text-secondary', 'surface'), ('text-secondary', 'surface-raised'), ('navigation-text', 'navigation'), ('selected-text', 'selected'), ('action-text', 'action'), ('danger', 'danger-surface'), ('warning', 'warning-surface'), ('success', 'success-surface'), ('accent-red-text', 'surface'), ('accent-red-text', 'surface-raised'), ('accent-green-text', 'surface'), ('accent-green-text', 'surface-raised')]
            for fg, bg in pairs:
                lo, hi = sorted([luminance(t[fg]), luminance(t[bg])])
                self.assertGreaterEqual((hi+.05)/(lo+.05), 4.5, (theme, fg, bg))
            for fg in ('focus', 'border'):
                for bg in ('surface', 'surface-raised'):
                    lo, hi = sorted([luminance(t[fg]), luminance(t[bg])])
                    self.assertGreaterEqual((hi+.05)/(lo+.05), 3, (theme, fg, bg))

    def test_brand_hues_keep_their_roles(self):
        data = json.loads((ROOT / 'tokens/design.json').read_text())
        brand, themes = data['brand'], data['themes']
        def ratio(a, b):
            lo, hi = sorted([luminance(a), luminance(b)])
            return (hi + .05) / (lo + .05)
        # Sun always carries Ink, and Sun is the same in both themes.
        self.assertGreaterEqual(ratio(brand['ink'], brand['sun']), 4.5)
        for theme, t in themes.items():
            self.assertEqual(t['selected'], brand['sun'], theme)
            self.assertEqual(t['selected-text'], brand['ink'], theme)
            # Eye is an accent: 3:1 on the page ground is enough for display
            # headings and marks. It is 2.7:1 on the dark raised surface, so
            # there it is decorative only; red that carries meaning uses
            # accent-red-text. The guide says so.
            self.assertGreaterEqual(ratio(brand['eye'], t['surface']), 3, theme)

    def test_guide_states_the_readability_rules(self):
        guide = (ROOT / 'guide/brand.md').read_text()
        for phrase in ('WCAG 2.2 Level AA', '4.5:1', 'Sun always carries Ink', 'accent-red-text', 'never by fading'):
            self.assertIn(phrase, guide)

    def test_vector_geometry_and_eye_preserved(self):
        original = ET.parse(ROOT / 'assets/logos/loon-mark.svg').getroot()
        reverse = ET.parse(ROOT / 'assets/logos/loon-mark-reversed.svg').getroot()
        self.assertEqual(original.attrib['viewBox'], reverse.attrib['viewBox'])
        self.assertEqual([e.get('d') for e in original.iter()], [e.get('d') for e in reverse.iter()])
        self.assertIn('#c30000', (ROOT / 'assets/logos/loon-mark-reversed.svg').read_text())

    def test_bundle_is_reproducible_and_includes_terms(self):
        build = runpy.run_path(str(ROOT / 'tools/build.py'))['build']
        out = build()
        version = json.loads((ROOT / 'tokens/design.json').read_text())['version']
        bundle = out / f'loon-design-{version}.zip'
        before = hashlib.sha256(bundle.read_bytes()).hexdigest()
        build()
        self.assertEqual(before, hashlib.sha256(bundle.read_bytes()).hexdigest())
        with ZipFile(bundle) as z:
            for name in ('LICENSE', 'BRAND-USAGE.md', 'ASSETS.md', 'tokens/design.json', 'tokens/tokens.css', 'guide/brand.md'):
                self.assertIn(name, z.namelist())


if __name__ == '__main__':
    unittest.main()
