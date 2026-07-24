#!/usr/bin/env python3
"""build_prompt.py 的单元测试（stdlib unittest，无第三方依赖）。

运行方式（仓库根目录）：
    python tests/test_build_prompt.py
"""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "build_prompt.py"

spec = importlib.util.spec_from_file_location("build_prompt", SCRIPT)
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

SCENE_CN = "深夜办公室里，两名交易员隔着堆满报表的桌子争论"
SCENE_EN = "Two traders arguing across a desk stacked with paper reports"


class AnchorTest(unittest.TestCase):
    """内置 fallback 锚定段内容完整性约束。"""

    def test_en_anchor_core_phrases(self):
        for phrase in ("ink", "watercolor", "Pastel palette", "{ratio}"):
            self.assertIn(phrase, bp.EN_ANCHOR)

    def test_cn_anchor_core_phrases(self):
        for phrase in ("水彩", "速写", "{ratio}"):
            self.assertIn(phrase, bp.CN_ANCHOR)

    def test_no_real_artist_names(self):
        # 真实画师姓名会触发出图工具版权审核，锚定段必须保持通用描述
        joined = (bp.EN_ANCHOR + bp.CN_ANCHOR).lower()
        for name in ("behringer", "picasso", "van gogh", "vangogh", "monet"):
            self.assertNotIn(name, joined)

    def test_negative_constraints_present(self):
        for phrase in ("no photorealism", "no 3D render", "no artist signature"):
            self.assertIn(phrase, bp.NEGATIVE)


class StyleArchiveTest(unittest.TestCase):
    """风格档案解析器约束。"""

    def test_load_watercolor_sketch_archive(self):
        archive = bp.load_style_archive(ROOT / "styles" / "watercolor-sketch.md")
        self.assertIn("Reportage sketch illustration", archive["anchor-en"])
        self.assertIn("新闻速写水彩插画", archive["anchor-cn"])
        self.assertIn("no artist signature", archive["negative"])

    def test_missing_file_errors(self):
        with self.assertRaises(SystemExit):
            bp.load_style_archive(ROOT / "styles" / "no-such-style.md")

    def test_missing_block_errors(self):
        with tempfile.NamedTemporaryFile(
            "w", suffix=".md", delete=False, encoding="utf-8"
        ) as f:
            f.write("# 残缺档案\n\n```anchor-en\nsome anchor\n```\n")
            tmp = f.name
        try:
            with self.assertRaises(SystemExit) as ctx:
                bp.load_style_archive(tmp)
            self.assertIn("anchor-cn", str(ctx.exception))
            self.assertIn("negative", str(ctx.exception))
        finally:
            Path(tmp).unlink()


class CliTest(unittest.TestCase):
    """CLI 端到端输出约束。"""

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True, text=True, check=True,
        ).stdout

    def test_full_output_with_translation(self):
        out = self.run_cli("--scene", SCENE_CN, "--scene-en", SCENE_EN)
        self.assertIn("EN PROMPT", out)
        self.assertIn("CN PROMPT", out)
        self.assertIn("NEGATIVE", out)
        self.assertIn("Scene: " + SCENE_EN, out)
        self.assertIn("场景：" + SCENE_CN, out)
        self.assertIn("16:9", out)
        self.assertNotIn("未提供 --scene-en", out)

    def test_style_flag_loads_archive(self):
        out = self.run_cli("--scene", SCENE_CN, "--style", "watercolor-sketch")
        self.assertIn("styles/watercolor-sketch.md", out)
        self.assertIn("Reportage sketch illustration", out)

    def test_list_styles(self):
        out = self.run_cli("--list-styles")
        self.assertIn("watercolor-sketch", out)

    def test_ratio_override(self):
        out = self.run_cli("--scene", SCENE_CN, "--scene-en", SCENE_EN, "--ratio", "3:2")
        self.assertIn("3:2", out)
        self.assertNotIn("16:9 composition", out)

    def test_missing_translation_warns(self):
        out = self.run_cli("--scene", SCENE_CN)
        self.assertIn("未提供 --scene-en", out)

    def test_scene_required(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], capture_output=True, text=True
        )
        self.assertNotEqual(result.returncode, 0)

    def test_style_flag_missing_archive_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--scene", SCENE_CN, "--style", "no-such-style"],
            capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--list-styles", result.stderr)

    def test_character_anchor_series_consistency(self):
        char = "a lean Chinese male artist in his late twenties, short messy black hair"
        out = self.run_cli("--scene", SCENE_CN, "--scene-en", SCENE_EN,
                           "--character", char)
        # 角色锚定必须出现在 Scene 之前，且逐字保留
        self.assertIn("Protagonist (identical across the whole series): " + char, out)
        self.assertLess(out.index(char), out.index("Scene: " + SCENE_EN))

    def test_no_text_flag(self):
        out = self.run_cli("--scene", SCENE_CN, "--scene-en", SCENE_EN, "--no-text")
        self.assertIn("No legible text", out)
        self.assertIn("no text, no lettering", out)
        self.assertIn("不要任何可读文字", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
