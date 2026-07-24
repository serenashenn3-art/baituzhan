# examples · 实测案例

同一篇文章 × 三种斩来的风格，各配 4 张，演示「任意来图 × 任意文章」通用流程：

| 案例 | 风格档案 | 参考图 | 成品 | 提示词清单 |
|------|----------|--------|------|-----------|
| 报刊淡彩 | `styles/editorial-ink-wash.md` | `assets/p718126702.jpg` | `butterfly-boy-fig1~4.png` | [butterfly-boy-prompts.md](butterfly-boy-prompts.md) |
| 明线派 | `styles/ligne-claire.md` | `assets/example-ligne-claire.png` | `butterfly-boy-moebius-fig1~4.png` | [butterfly-boy-moebius-prompts.md](butterfly-boy-moebius-prompts.md) |
| 稚拙蜡笔 | `styles/naive-crayon.md` | `assets/ref3-a/b/c.png` | `butterfly-boy-crayon-fig1~4.png` | [butterfly-boy-crayon-prompts.md](butterfly-boy-crayon-prompts.md) |

> 每套图共用同一锚定段、同一画幅，翻阅时风格连贯。
> 新案例按 `<任务名>-figN.png` + `<任务名>-prompts.md` 组织；完整锚定段可由
> `python scripts/build_prompt.py --style <风格名> --scene "<场景>"` 逐条生成。

## prompts 清单模板（`<文章名>-prompts.md`）

```markdown
# 《<文章名>》配图提示词

风格：<风格名>（styles/<风格名>.md） · N 张 · 横版 16:9
用法：将英文提示词粘贴到 GPT image2 / nano banana / Midjourney / 即梦等出图工具，
负面约束一并附上（支持负面词的工具）。

---

## 图 1 · 头图｜<场景标题>（对应文章第 X–Y 段）

**EN：**

```
<锚定段逐字复用>
Scene: <英文场景描述>
```

**负面约束：** `<英文负面约束>`

**CN 场景：** <中文场景描述>

---

## 图 2｜<场景标题>（对应第 Z 段）

**EN：**

```
（同上锚定段）
Scene: <英文场景描述>
```

**CN 场景：** <中文场景描述>

---

> N 张图共用同一锚定段、色板与画幅，翻阅时风格连贯。
> 完整锚定段可由 `python scripts/build_prompt.py --style <风格名> --scene "<场景>"` 逐条生成。
```
