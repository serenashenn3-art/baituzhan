#!/usr/bin/env python3
"""百图斩 · 通用风格复刻配图提示词组装器（中英双语，零依赖 stdlib）。

用法:
    python build_prompt.py --scene "深夜办公室里，两名交易员隔着堆满报表的桌子争论"
    python build_prompt.py --scene "..." --scene-en "Two traders arguing across a desk..."
    python build_prompt.py --scene "..." --style watercolor-sketch --ratio "3:2"
    python build_prompt.py --scene "..." --anchor-file /path/to/my-style.md
    python build_prompt.py --list-styles

--scene        场景中文描述（必填，--list-styles 除外）：谁、在哪、做什么、什么情绪
--scene-en     场景英文描述（可选，缺省时英文提示词内嵌中文原文并提示补译）
--ratio        画幅，默认 16:9
--style        加载 styles/<名称>.md 风格档案
--anchor-file  加载任意路径的风格档案（尚未存入 styles/ 时使用）
--character    系列一致性角色锚定（英文）：同一套配图中逐字复用，保证主角是同一个人
--character-cn 角色锚定中文版（可选，缺省时复用 --character 原文）
--no-text      画面不出现任何可读文字（封面/海报/标注字一律禁止，贴合中文文章场景）
--list-styles  列出 styles/ 下所有可用风格档案并退出

风格档案格式：普通 Markdown，内含三个带语言标记的代码块
（```anchor-en / ```anchor-cn / ```negative），锚定段可含 {ratio} 占位符。
"""
import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
STYLES_DIR = SCRIPT_DIR.parent / "styles"

# ---------------------------------------------------------------------------
# 内置默认风格锚定（watercolor-sketch）：与 styles/watercolor-sketch.md 保持一致，
# 未指定 --style / --anchor-file 时作为 fallback 使用。
# ---------------------------------------------------------------------------
EN_ANCHOR = (
    "Reportage sketch illustration, traditional news sketch artist's hand-drawn ink "
    "and watercolor on paper. "
    "Loose black ink pen outlines with visible hand-drawn sketchy strokes, contour lines "
    "not fully closed, occasional searching repeat lines. Transparent watercolor washes "
    "layered over the ink, thin color layers with visible paper texture and soft bleeding "
    "edges. Pastel palette: pale yellow, dusty pink, lavender purple, sky blue, warm wood "
    "brown, rosy skin tones. Background rendered as a soft monochrome watercolor wash with "
    "generous white space. Figures slightly exaggerated in a lively reportage manner, "
    "expressive faces and captured gestures, on-the-spot documentary journalism feel. "
    "Handwritten-style scene annotations, but no readable artist signature and no dates "
    "or timestamps anywhere in the image. "
    "Horizontal {ratio} composition, observer's viewpoint."
)

CN_ANCHOR = (
    "新闻速写水彩插画，传统新闻速写画师的纸本钢笔水彩手绘。黑色墨水钢笔松动勾线，速写笔触明显，"
    "轮廓线不完全闭合，偶有试探性重复线。墨线上罩透明水彩薄涂，色层轻薄可见纸纹，"
    "边缘自然洇开。粉彩色板：淡黄、灰粉、薰衣草紫、天蓝、暖木棕、玫瑰肤色。背景为"
    "单色水彩大面积晕染并大量留白。人物略带速写式夸张，表情生动、动作有抓拍感，"
    "现场新闻纪实气质。画面可有手写体场景标注，但不出现任何画师签名、日期或时间。"
    "横版 {ratio}，旁观者视角。"
)

NEGATIVE = (
    "no photorealism, no photography, no 3D render, no CGI, no digital smooth gradients, "
    "no anime or manga style, no oil painting, no thick impasto, no neon colors, "
    "no sharp vector lines, no flat cartoon fill, "
    "no artist signature, no readable signature, no dates, no timestamps, no watermark"
)

CN_NEGATIVE = (
    "不要照片写实、不要摄影感、不要 3D 渲染、不要数码平滑渐变、"
    "不要动漫风、不要厚涂油画、不要霓虹色、不要矢量锐线、不要平涂卡通、"
    "不要画师签名、不要日期时间、不要水印"
)

FALLBACK_ARCHIVE = {
    "anchor-en": EN_ANCHOR,
    "anchor-cn": CN_ANCHOR,
    "negative": NEGATIVE,
}

# 风格档案中三个带语言标记的代码块
BLOCK_PATTERNS = {
    "anchor-en": re.compile(r"```anchor-en\s*\n(.*?)```", re.DOTALL),
    "anchor-cn": re.compile(r"```anchor-cn\s*\n(.*?)```", re.DOTALL),
    "negative": re.compile(r"```negative\s*\n(.*?)```", re.DOTALL),
}

LIST_STYLES_HINT = "可用 --list-styles 查看 styles/ 下所有可用风格档案。"


def load_style_archive(path):
    """解析风格档案 Markdown，提取 anchor-en / anchor-cn / negative 三个代码块。

    文件不存在或缺失任一代码块时，给出清晰报错并以非零码退出。
    返回 dict：{"anchor-en": str, "anchor-cn": str, "negative": str}
    """
    path = Path(path)
    if not path.is_file():
        raise SystemExit(
            f"[错误] 风格档案不存在：{path}\n{LIST_STYLES_HINT}"
        )
    text = path.read_text(encoding="utf-8")
    archive = {}
    missing = []
    for key, pattern in BLOCK_PATTERNS.items():
        m = pattern.search(text)
        if m:
            archive[key] = m.group(1).strip()
        else:
            missing.append(key)
    if missing:
        raise SystemExit(
            f"[错误] 风格档案 {path} 缺少代码块：{', '.join('```' + k for k in missing)}\n"
            f"风格档案必须包含 anchor-en / anchor-cn / negative 三个带语言标记的代码块，"
            f"格式见 references/style-guide.md。\n{LIST_STYLES_HINT}"
        )
    return archive


def list_styles():
    """列出 styles/ 下所有可用风格档案。"""
    print("【可用风格档案 · styles/】")
    if not STYLES_DIR.is_dir():
        print(f"（styles/ 目录不存在：{STYLES_DIR}）")
        return
    found = sorted(STYLES_DIR.glob("*.md"))
    if not found:
        print("（暂无风格档案，按 references/style-guide.md 的建档流程新建一个吧）")
        return
    for f in found:
        print(f"  - {f.stem}    ({f})")
    print()
    print("用法：python scripts/build_prompt.py --style <名称> --scene \"<场景描述>\"")


def main() -> None:
    ap = argparse.ArgumentParser(description="百图斩 · 通用风格复刻配图提示词组装器")
    ap.add_argument("--scene", default=None, help="场景中文描述（必填，--list-styles 除外）")
    ap.add_argument("--scene-en", default=None, help="场景英文描述")
    ap.add_argument("--ratio", default="16:9", help="画幅比例，默认 16:9")
    ap.add_argument("--style", default=None, help="加载 styles/<名称>.md 风格档案")
    ap.add_argument("--anchor-file", default=None, help="加载任意路径的风格档案")
    ap.add_argument("--list-styles", action="store_true", help="列出所有可用风格档案并退出")
    ap.add_argument("--character", default=None,
                    help="系列一致性角色锚定（英文），同一套配图逐字复用")
    ap.add_argument("--character-cn", default=None, help="角色锚定中文版（可选）")
    ap.add_argument("--no-text", action="store_true",
                    help="画面不出现任何可读文字（海报/标注/招牌一律禁止）")
    args = ap.parse_args()

    if args.list_styles:
        list_styles()
        return

    if not args.scene:
        ap.error("--scene 为必填参数（仅 --list-styles 时省略）")

    # 确定锚定来源：--anchor-file > --style > 内置 fallback
    if args.anchor_file:
        archive = load_style_archive(args.anchor_file)
        style_label = f"自定义档案 {args.anchor_file}"
    elif args.style:
        archive = load_style_archive(STYLES_DIR / f"{args.style}.md")
        style_label = f"styles/{args.style}.md"
    else:
        archive = FALLBACK_ARCHIVE
        style_label = "内置默认 watercolor-sketch（fallback）"

    scene_en = args.scene_en or args.scene
    warn = "" if args.scene_en else (
        "\n[提示] 未提供 --scene-en，英文提示词的场景段为中文原文；"
        "用于英文出图工具前请先补译。\n"
    )

    en_prompt = archive["anchor-en"].replace("{ratio}", args.ratio)
    cn_prompt = archive["anchor-cn"].replace("{ratio}", args.ratio)

    # 系列一致性：角色锚定逐字复用，保证一套图里主角是同一个人
    if args.character:
        en_prompt += f"\nProtagonist (identical across the whole series): {args.character}"
        cn_prompt += f"\n主角（整套图保持同一人）：{args.character_cn or args.character}"

    en_prompt += f"\nScene: {scene_en}"
    cn_prompt += f"\n场景：{args.scene}"

    negative = archive["negative"]
    cn_negative = CN_NEGATIVE
    if args.no_text:
        en_prompt += "\nNo legible text, lettering, signs, posters or captions anywhere in the image."
        cn_prompt += "\n画面中不出现任何可读文字、招牌、海报或标注。"
        negative += ", no text, no lettering, no captions, no signage, no posters with words"
        cn_negative += "、不要任何可读文字、不要招牌海报上的字"

    print(f"[风格档案] {style_label}")
    print("=" * 60)
    print("【英文提示词 · EN PROMPT】")
    print("=" * 60)
    print(en_prompt)
    print()
    print("【负面约束 · NEGATIVE】")
    print(negative)
    print()
    print("=" * 60)
    print("【中文提示词 · CN PROMPT】")
    print("=" * 60)
    print(cn_prompt)
    print()
    print("【负面约束 · 中文工具同样适用】")
    print(cn_negative)
    print(warn)


if __name__ == "__main__":
    main()
