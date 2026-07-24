---
description: 百图斩 · 风格复刻配图：斩风格建档，或为文章/一句话需求生成统一风格插图（或出图提示词）
---

Use the baituzhan skill in this repository.

1. Read `SKILL.md` and `references/style-guide.md`.
2. Determine the task:
   - If the user supplied 1–3 reference images and wants a new style → Style harvesting: analyze with the 8-dimension framework, write a style archive to `styles/<style-name>.md` (must contain `anchor-en` / `anchor-cn` / `negative` fenced blocks; no real artist names; signature/date/timestamp/watermark bans included), copy reference images to `assets/`.
   - If the user supplied an article → Article mode: pick 2–4 key scenes, then for each scene run `python scripts/build_prompt.py --style <name> --scene "<场景中文描述>" --scene-en "<English scene description>"` (omit `--style` to use the built-in default; `--list-styles` to browse).
   - If the user supplied a one-line story/request → Brief mode: assemble a single prompt the same way.
3. Generate images with an available backend (user-named tool first: GPT image2, nano banana, etc.; then the Kimi image_generation plugin with `--reference-image` pointing to the style's uploaded reference image). Reuse the style anchor verbatim and append the negative constraints on every image.
4. If no backend is available, output the complete detailed bilingual prompt list (anchor + scene + negative constraints per image) so the user can edit and paste it into any image tool.

User input: $ARGUMENTS
