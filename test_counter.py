import os
import tempfile
import unittest

import counter


class CounterTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        with open(os.path.join(self.dir, "a.py"), "w") as f:
            f.write("# comment\nx = 1\n\nprint(x)\n")
        with open(os.path.join(self.dir, "b.js"), "w") as f:
            f.write("// note\nconsole.log(1);\n")
        with open(os.path.join(self.dir, "readme.txt"), "w") as f:
            f.write("ignored\n")

    def test_count_file(self):
        self.assertEqual(counter.count_file(os.path.join(self.dir, "a.py"), "#"), (2, 1, 1))

    def test_scan_languages(self):
        stats = counter.scan(self.dir)
        self.assertEqual(set(stats), {"Python", "JavaScript"})
        self.assertEqual(stats["Python"]["code"], 2)

    def test_table_has_total(self):
        self.assertIn("TOTAL", counter.format_table(counter.scan(self.dir)))


if __name__ == "__main__":
    unittest.main()
