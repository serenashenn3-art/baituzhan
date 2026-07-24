<sub>🌐 中文 · [English](README.en.md)</sub>

<div align="center">

# 百图斩 · baituzhan

> *风格无关的通用复刻配图技能 —— 给它 1–3 张参考图斩出风格档案，再给文章批量配统一风格插图*
> *A style-agnostic illustration-replication skill: harvest any style from reference images, then illustrate any article in it.*

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet.svg)](#)
[![skills.sh Compatible](https://img.shields.io/badge/skills.sh-Compatible-green.svg)](#)

**斩风格 → 建档 → 出图，两步走完：**  
上传 1–3 张任意风格参考图，斩成一份可复用的「风格档案」（中英锚定段 + 负面约束）；  
再丢给它一篇文章或一句话，就能产出一整套该风格的统一插图。  
已斩案例档案：水彩速写 · 报刊淡彩 · 明线派 · 稚拙蜡笔 —— 更多风格，随斩随有。

```bash
npx skills add serenashenn3-art/baituzhan
```

Claude Code / Codex / Kimi / Hermes —— 任何支持 Skill 目录的 AI Agent 都能用。

[安装](#安装) · [能做什么](#能做什么) · [核心机制](#核心机制) · [项目结构](#项目结构)

</div>

---

<p align="center">
  <img src="assets/example-watercolor-sketch.jpeg" width="100%" alt="内置示例风格参考图：新闻纪实水彩速写">
</p>

<sub>内置示例风格 `watercolor-sketch` 的参考图：一张现场新闻速写。百图斩不限于任何单一风格 —— 你给参考图，它斩新档案。</sub>

## 案例画廊

同一篇文章（画家访谈）× 三种斩来的风格，各配 4 张 —— 演示「任意来图 × 任意文章」的通用流程。每套图锚定段逐字复用，风格严格统一（无签名、无日期）：

### 案例一 · 报刊淡彩 `editorial-ink-wash`

参考图 `assets/p718126702.jpg`（报刊头版式钢笔淡彩人物群像）→ 斩出档案 → 提取 4 个关键场景逐张生成：

<table><tr>
<td><img src="examples/butterfly-boy-fig1.png" alt="发光的狗"></td>
<td><img src="examples/butterfly-boy-fig2.png" alt="坐井观山"></td>
<td><img src="examples/butterfly-boy-fig3.png" alt="蝴蝶少年"></td>
<td><img src="examples/butterfly-boy-fig4.png" alt="下凡"></td>
</tr><tr>
<td align="center"><sub>发光的狗</sub></td>
<td align="center"><sub>坐井观山</sub></td>
<td align="center"><sub>蝴蝶少年</sub></td>
<td align="center"><sub>下凡</sub></td>
</tr></table>

提示词清单：[examples/butterfly-boy-prompts.md](examples/butterfly-boy-prompts.md)

### 案例二 · 明线派 `ligne-claire`

参考图 `assets/example-ligne-claire.png`（法比漫画明线派：闭合细线 + 平涂 + 双色调打光）→ 同一篇文章重配 4 张：

<table><tr>
<td><img src="examples/butterfly-boy-moebius-fig1.png" alt="深夜画室"></td>
<td><img src="examples/butterfly-boy-moebius-fig2.png" alt="宋庄二十平米"></td>
<td><img src="examples/butterfly-boy-moebius-fig3.png" alt="天台的蝴蝶"></td>
<td><img src="examples/butterfly-boy-moebius-fig4.png" alt="教孩子画画"></td>
</tr><tr>
<td align="center"><sub>发光的狗 · 台灯</sub></td>
<td align="center"><sub>宋庄二十平米 · 电暖器</sub></td>
<td align="center"><sub>蝴蝶少年 · 发光蝶</sub></td>
<td align="center"><sub>下凡 · 吊灯</sub></td>
</tr></table>

提示词清单：[examples/butterfly-boy-moebius-prompts.md](examples/butterfly-boy-moebius-prompts.md)

### 案例三 · 稚拙蜡笔 `naive-crayon`

参考图 `assets/ref3-a/b/c.png`（同作者三幅：桃子与虫 / 三只鸽子 / 三条鱼，跨图互证取不变量）→ 单主体纯色背景风格，叙事场景按档案转译为象征物：

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

提示词清单：[examples/butterfly-boy-crayon-prompts.md](examples/butterfly-boy-crayon-prompts.md)

## 安装

### 方式一：skills.sh（推荐）

```bash
npx skills add serenashenn3-art/baituzhan
```

### 方式二：手动安装

克隆或下载本仓库，把整个 `baituzhan/` 目录复制到以下任一位置：

| Agent | 安装路径 |
|---|---|
| Claude Code / Codex / 通用 | `~/.config/agents/skills/` |
| Kimi | `~/.kimi/skills/` |
| 项目级（任何 Agent） | 项目根目录 `.agents/skills/` |

装好后直接说「按这几张参考图的风格给这篇文章配插图」或「百图斩，斩这个风格」即可触发。

## 能做什么

| 输入 | 输出 |
|---|---|
| 🎨 1–3 张参考图 | 斩风格：八维度拆解 → 落成 `styles/<风格名>.md` 风格档案（中英锚定段 + 负面约束 + 场景转译 + 默认画幅），永久复用 |
| 📄 一篇文章（上传或粘贴全文） | 模式A：通读全文 → 提取 2–4 个关键场景 → 逐张生成风格统一的插图（含建议插入位置） |
| ✏️ 一句话简短需求 | 模式B：直接生成一张同风格插画 |
| 🧩 没有出图工具时 | 输出完整、可直接粘贴的中英双语提示词清单，方便你自行修改后丢给任何出图工具 |

出图后端自动适配（用户指定的优先）：GPT image2 / gpt-image、nano banana（Gemini）、Kimi `image_generation` 插件（支持 `--reference-image` 参考图锁风格）、即梦、Midjourney —— 有什么用什么，一个都没有就优雅降级为提示词清单。

想把它复制成你自己的风格技能？看 [HOW-TO-CREATE-A-STYLE-SKILL.md](HOW-TO-CREATE-A-STYLE-SKILL.md) —— 改个风格名、附几张参考图，一段话发给任何 AI 即可走完全流程。

## 核心机制

**风格统一靠三条铁律：**

1. **锚定段逐字复用** —— 每次生成都带完整风格锚定段（存于 `styles/<风格名>.md`），绝不缩写、不凭记忆改写；锚定段**严禁出现真实画师姓名**（防出版权审核）；
2. **参考图锁风格** —— 以 `assets/` 中对应参考图传入生成工具，整套图风格高度统一；
3. **负面约束内置** —— 每次必带，其中 `no artist signature / no dates / no timestamps / no watermark` 四条永不移除：**生成图中永远不会出现画师签名、日期、时间、水印**。

**提示词组装脚本**（零依赖，标准库即可运行）：

```bash
python scripts/build_prompt.py --list-styles            # 查看全部风格档案
python scripts/build_prompt.py --style watercolor-sketch \
  --scene "深夜办公室里，两名交易员隔着堆满报表的桌子争论"
```

输出 = 英文主提示词 + 负面约束 + 中文提示词，可直接粘贴使用。测试：

```bash
python tests/test_build_prompt.py
```

## 项目结构

```
baituzhan/
├── SKILL.md                        # 技能主入口（通用流水线：斩风格 + 文章分析 + 模式A/B + 降级规则）
├── AGENTS.md                       # AI Agent 操作指南（Codex / Hermes 等）
├── CLAUDE.md                       # Claude Code 速查
├── HOW-TO-CREATE-A-STYLE-SKILL.md  # 复用话术模板：改风格名+参考图即可造新技能
├── .claude/commands/baituzhan.md   # Claude Code 斜杠命令：/baituzhan
├── references/
│   ├── style-guide.md              # 来图识别 SOP（溯源/量化指纹/多图互证）、锚定段规范、兼容硬规则
│   └── style-audit-checklist.md    # 样张核验清单
├── styles/                         # 已斩风格档案（案例缓存，可复用）
│   ├── watercolor-sketch.md        # 水彩速写 · 新闻纪实
│   ├── editorial-ink-wash.md       # 报刊淡彩
│   ├── ligne-claire.md             # 明线派（法比漫画）
│   └── naive-crayon.md             # 稚拙蜡笔
├── scripts/
│   └── build_prompt.py             # 提示词组装器（双语输出，零依赖，支持 --style/--list-styles）
├── tests/
│   └── test_build_prompt.py        # 标准库测试套件
├── assets/                         # 全部参考图（含命名说明 README）
└── examples/                       # 三套实测案例（各 4 张成品图 + 提示词清单）
```

## License

MIT —— 随意使用、修改、分发。
