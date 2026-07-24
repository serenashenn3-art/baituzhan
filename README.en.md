<sub>🌐 [中文](README.md) · English</sub>

<div align="center">

# baituzhan · 百图斩

> *A style-agnostic illustration-replication skill: harvest any style from 1–3 reference images, then illustrate any article in it.*
> *风格无关的通用复刻配图技能 —— 斩风格建档，再为文章批量配统一风格插图。*

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet.svg)](#)
[![skills.sh Compatible](https://img.shields.io/badge/skills.sh-Compatible-green.svg)](#)

**Harvest → Archive → Generate, in two moves:**  
Feed it 1–3 reference images of ANY visual style, and it carves out a reusable **style archive** (EN/CN anchor paragraphs + negative constraints).  
Then hand it an article or a one-line brief, and it produces a full set of unified-style illustrations.  
Harvested so far: watercolor sketch · editorial ink wash · ligne claire · naive crayon — more styles are one harvest away.

```bash
npx skills add serenashenn3-art/baituzhan
```

Works with Claude Code, Codex, Kimi, Hermes — any AI agent that supports a skills directory.

[Install](#install) · [What it does](#what-it-does) · [How it works](#how-it-works) · [Project layout](#project-layout)

</div>

---

<p align="center">
  <img src="assets/example-watercolor-sketch.jpeg" width="100%" alt="Reference image of the built-in example style: a live news reportage sketch">
</p>

<sub>Reference image of the built-in `watercolor-sketch` style. Baituzhan is not bound to any single style — give it reference images and it harvests a new archive.</sub>

## Gallery

One article (a painter interview) × three harvested styles, 4 illustrations each — the generic "any image × any article" pipeline at work. Anchors are reused verbatim within each set (no signatures, no dates):

### Case 1 · Editorial Ink Wash `editorial-ink-wash`

Reference `assets/p718126702.jpg` (newspaper-front-page pen-and-wash caricature) → archive → 4 key scenes:

<table><tr>
<td><img src="examples/butterfly-boy-fig1.png" alt="the glowing dog"></td>
<td><img src="examples/butterfly-boy-fig2.png" alt="twenty square meters"></td>
<td><img src="examples/butterfly-boy-fig3.png" alt="butterfly boy"></td>
<td><img src="examples/butterfly-boy-fig4.png" alt="back to life"></td>
</tr><tr>
<td align="center"><sub>the glowing dog</sub></td>
<td align="center"><sub>20 m² in Songzhuang</sub></td>
<td align="center"><sub>butterfly boy</sub></td>
<td align="center"><sub>back to life</sub></td>
</tr></table>

### Case 2 · Ligne Claire `ligne-claire`

Reference `assets/example-ligne-claire.png` (Franco-Belgian clear line: closed contours + flat fills + two-tone lighting) → same article, re-illustrated:

<table><tr>
<td><img src="examples/butterfly-boy-moebius-fig1.png" alt="night studio"></td>
<td><img src="examples/butterfly-boy-moebius-fig2.png" alt="tiny rented room"></td>
<td><img src="examples/butterfly-boy-moebius-fig3.png" alt="rooftop butterfly"></td>
<td><img src="examples/butterfly-boy-moebius-fig4.png" alt="teaching kids"></td>
</tr><tr>
<td align="center"><sub>night studio · desk lamp</sub></td>
<td align="center"><sub>20 m² room · heater</sub></td>
<td align="center"><sub>rooftop · glowing butterfly</sub></td>
<td align="center"><sub>classroom · hanging bulb</sub></td>
</tr></table>

### Case 3 · Naive Crayon `naive-crayon`

References `assets/ref3-a/b/c.png` (a 3-image series by one artist; cross-image invariants only) → single-subject flat-background style, scenes translated into symbolic subjects:

<table><tr>
<td><img src="examples/butterfly-boy-crayon-fig1.png" alt="good dog"></td>
<td><img src="examples/butterfly-boy-crayon-fig2.png" alt="my tiny studio"></td>
<td><img src="examples/butterfly-boy-crayon-fig3.png" alt="butterfly boy"></td>
<td><img src="examples/butterfly-boy-crayon-fig4.png" alt="draw with me"></td>
</tr><tr>
<td align="center"><sub>good dog</sub></td>
<td align="center"><sub>my tiny studio</sub></td>
<td align="center"><sub>butterfly boy</sub></td>
<td align="center"><sub>draw with me</sub></td>
</tr></table>

Full prompt sheets for every set live in [examples/](examples/).

## Install

### Option 1: skills.sh (recommended)

```bash
npx skills add serenashenn3-art/baituzhan
```

### Option 2: manual

Clone or download this repo, then copy the whole `baituzhan/` directory to one of:

| Agent | Install path |
|---|---|
| Claude Code / Codex / generic | `~/.config/agents/skills/` |
| Kimi | `~/.kimi/skills/` |
| Project-level (any agent) | `.agents/skills/` in your project root |

Then say *"harvest this style from my reference images"* or *"illustrate this article in my archived style"* to trigger it.

## What it does

| Input | Output |
|---|---|
| 🎨 1–3 reference images | Style harvest: 8-dimension breakdown → a style archive at `styles/<name>.md` (EN/CN anchors + negatives + scene-translation hints + default ratio), reusable forever |
| 📄 An article (upload or paste) | Article mode: reads it → picks 2–4 key scenes → generates unified-style illustrations one by one (with suggested insert positions) |
| ✏️ A one-line brief | Brief mode: one same-style illustration |
| 🧩 No image backend available | Complete, ready-to-paste bilingual (EN/CN) prompt sheets you can edit and feed to any image tool |

Image backends adapt automatically (user-named tools first): GPT image2 / gpt-image, nano banana (Gemini), Kimi `image_generation` plugin (with `--reference-image` style locking), 即梦, Midjourney — uses whatever is available; if none, it degrades gracefully to prompts.

Want to fork this into your own style skill? See [HOW-TO-CREATE-A-STYLE-SKILL.md](HOW-TO-CREATE-A-STYLE-SKILL.md) — change the style name, attach reference images, send one paragraph to any AI.

## How it works

**Three rules keep every batch visually unified:**

1. **Style anchor reused verbatim** — every generation carries the full anchor paragraph from `styles/<name>.md`, never abbreviated, never rewritten from memory; anchors **never contain real artist names** (copyright moderation);
2. **Reference image locks the style** — the matching image from `assets/` is passed to the generation tool, keeping a whole batch unified;
3. **Built-in negative constraints** — appended on every run; `no artist signature / no dates / no timestamps / no watermark` are never removed: **no signature, date, timestamp, or watermark ever appears in generated images**.

**Prompt assembler** (stdlib only, zero dependencies):

```bash
python scripts/build_prompt.py --list-styles          # browse all style archives
python scripts/build_prompt.py --style watercolor-sketch \
  --scene "Two traders arguing across a desk stacked with reports in a late-night office"
```

Output = English main prompt + negative constraints + Chinese prompt, ready to paste. Tests:

```bash
python tests/test_build_prompt.py
```

## Project layout

```
baituzhan/
├── SKILL.md                        # Canonical workflow (generic pipeline: harvest + article analysis + article/brief modes + fallback)
├── AGENTS.md                       # Operating guide for AI coding agents (Codex, Hermes, …)
├── CLAUDE.md                       # Claude Code quick guide
├── HOW-TO-CREATE-A-STYLE-SKILL.md  # Reusable prompt template for forking new style skills
├── .claude/commands/baituzhan.md   # Claude Code slash command: /baituzhan
├── references/
│   ├── style-guide.md              # Recognition SOP (provenance / quantitative fingerprint / multi-ref invariants), anchor rules, compatibility constraints
│   └── style-audit-checklist.md    # Sample-audit checklist
├── styles/                         # Harvested style archives (reusable case cache)
│   ├── watercolor-sketch.md        # Watercolor reportage sketch
│   ├── editorial-ink-wash.md       # Editorial ink wash
│   ├── ligne-claire.md             # Ligne claire (Franco-Belgian clear line)
│   └── naive-crayon.md             # Naive crayon
├── scripts/
│   └── build_prompt.py             # Prompt assembler (bilingual, stdlib only, --style/--list-styles)
├── tests/
│   └── test_build_prompt.py        # Stdlib unittest suite
├── assets/                         # All reference images (with naming README)
└── examples/                       # Three field-test cases (4 outputs + prompt sheets each)
```

## License

MIT — use, modify, and distribute freely.
