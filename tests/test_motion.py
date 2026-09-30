import re
import runpy
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOTION = ROOT / 'assets/motion'
SOURCES = [ROOT / 'assets/logos/loon-mark.svg', ROOT / 'assets/logos/loon-favicon.svg', ROOT / 'assets/illustrations/lake-scene.svg']
SVG = '{http://www.w3.org/2000/svg}'


def paths(text):
    return re.findall(r'\sd="([^"]*)"', text)


def circles(text):
    return [(c.get('cx'), c.get('cy'), c.get('r'), c.get('fill')) for c in ET.fromstring(text).iter(f'{SVG}circle')]


class WorkingLoon(unittest.TestCase):
    def files(self):
        found = sorted(MOTION.glob('*.svg'))
        self.assertTrue(found)
        return found

    def test_files_are_generated_from_the_supplied_artwork(self):
        generate = runpy.run_path(str(ROOT / 'tools/motion.py'))['generate']
        with tempfile.TemporaryDirectory() as out:
            written = generate(Path(out))
            self.assertEqual(sorted(p.name for p in written), [p.name for p in self.files()])
            for p in written:
                self.assertEqual(p.read_bytes(), (MOTION / p.name).read_bytes(), f'{p.name}: run python3 tools/motion.py')

    def test_geometry_is_copied_never_redrawn(self):
        supplied = {d for s in SOURCES for d in paths(s.read_text())}
        # Every circle is a supplied one, fill included: the eye is never moved, enlarged or
        # recoloured, and the lake keeps its sun.
        supplied_circles = {c for s in SOURCES for c in circles(s.read_text())}
        for p in self.files():
            text = p.read_text()
            self.assertTrue(paths(text), p.name)
            self.assertEqual([d for d in paths(text) if d not in supplied], [], p.name)
            self.assertEqual([c for c in circles(text) if c not in supplied_circles], [], p.name)
            if p.name.startswith('loon-'):
                self.assertIn(('525.22', '374.58', '5.40', '#c30000'), circles(text), f'{p.name} keeps the eye')

    def test_every_file_stands_still_under_reduced_motion(self):
        for p in self.files():
            text = p.read_text()
            self.assertIn('@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }', text, p.name)
            self.assertNotIn('<script', text, p.name)
            self.assertNotRegex(text, r'(href|src)="https?:', p.name)

    def test_reversed_twins_change_only_the_ink(self):
        twins = sorted(MOTION.glob('*-reversed.svg'))
        self.assertEqual(len(twins), 4)
        for p in twins:
            original = (MOTION / p.name.replace('-reversed', '')).read_text()
            reversed_ = p.read_text()
            self.assertEqual(paths(original), paths(reversed_), p.name)
            self.assertEqual(circles(original), circles(reversed_), p.name)
            fills = set(re.findall(r'fill="(#[0-9A-Fa-f]{6})"', reversed_))
            self.assertEqual(fills, {'#F6F2E7', '#c30000'}, p.name)

    def test_the_lake_keeps_its_illustration(self):
        scene = (ROOT / 'assets/illustrations/lake-scene.svg').read_text()
        working = (MOTION / 'lake-working.svg').read_text()
        self.assertEqual(paths(scene), paths(working))
        self.assertEqual(circles(scene), circles(working))


if __name__ == '__main__':
    unittest.main()
