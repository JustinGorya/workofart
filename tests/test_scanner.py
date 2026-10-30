"""Exercise the packaged CLI independently of its working directory."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCANNER = Path(__file__).resolve().parents[1] / "skills" / "workofart" / "scripts" / "scan.py"


class ScannerTests(unittest.TestCase):
    def test_reports_source_locations_and_skips_dependencies(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "site.css").write_text(
                "/* fixture */\n:root { --bg: #f6f8fb; --radius:16px; }\n"
                ".card:hover { transform: translateY(-4px); }\n", encoding="utf-8")
            deps = project / "node_modules"
            deps.mkdir()
            (deps / "ignored.css").write_text("body { color: #ff6b35; }", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCANNER), str(project), "--json"],
                                    cwd=tmp, capture_output=True, check=True)
            report = json.loads(result.stdout)
            self.assertEqual(report["files"], 1)
            hits = report["hits"]
            self.assertTrue({"PAL-1", "TOK-1", "TOK-2", "HOV-1"} <= {h["tell"] for h in hits})
            hover = next(h for h in hits if h["tell"] == "HOV-1")
            self.assertEqual(hover["line"], 3)
            self.assertEqual(Path(hover["file"]).name, "site.css")

    def test_text_output_does_not_modify_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "site.css"
            content = "/* café — review */\n.card:hover { transform: translateY(-4px); }\n".encode("utf-8")
            path.write_bytes(content)
            result = subprocess.run([sys.executable, str(SCANNER), str(path), "--max", "1"],
                                    cwd=tmp, capture_output=True, check=True)
            text = result.stdout.decode("utf-8")
            self.assertIn("HOV-1", text)
            self.assertIn("site.css:2", text)
            self.assertEqual(path.read_bytes(), content)

    def test_baseline_reset_alone_is_not_a_template_signal(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "reset.css"
            path.write_text("*, *::before, *::after { box-sizing: border-box; }\n"
                            ":focus-visible { outline: 3px solid blue; }\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCANNER), str(path), "--json"],
                                    cwd=tmp, capture_output=True, check=True)
            report = json.loads(result.stdout)
            self.assertFalse(any(h["sev"] == "H" for h in report["hits"]))


if __name__ == "__main__":
    unittest.main()
