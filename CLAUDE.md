# CLAUDE.md — Baituzhan (百图斩) Skill

This repository is a **style-agnostic illustration-replication** skill package: harvest any visual style from 1–3 reference images into a style archive (`styles/<name>.md`), then produce unified-style illustrations for an article or a one-line brief.

## Read first

1. `SKILL.md` — canonical workflow (style harvesting + article mode + brief mode + generation/fallback rules).
2. `references/style-guide.md` — 8-dimension breakdown framework, anchor-writing rules, universal negatives, archiving SOP, and the `styles/<name>.md` format contract (three fenced blocks: `anchor-en` / `anchor-cn` / `negative`).
3. `AGENTS.md` — backend priority, hard rules, conventions (applies to you too).

## Quick path

- List styles: `python scripts/build_prompt.py --list-styles`
- Assemble a prompt: `python scripts/build_prompt.py --style <name> --scene "<场景中文描述>" [--scene-en "<English scene>"] [--ratio 16:9]`
- Archive not yet in `styles/`? Use `--anchor-file <path>`.
- Slash command available: `/baituzhan` (see `.claude/commands/baituzhan.md`).
- Run tests: `python tests/test_build_prompt.py`.

## Non-negotiables

- Anchor verbatim on every image; same archive + ratio across a batch; negative constraints always appended (signature/date/timestamp/watermark bans never removed).
- No real artist names in prompts or anchors (copyright moderation, HTTP 403). Lock style with the archive's reference image from `assets/` instead.
- If no image-generation backend is available, output the full detailed bilingual prompt list for the user — never fake a generated image.
