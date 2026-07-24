# 样张对图核验清单 · Style Audit Checklist

用法：新档案出样张后，把**样张与参考图并排**，逐项对照打分。任何一项「跑偏」都必须回修锚定段对应句并重出样张；全绿才允许批量出图。把核验记录附在提示词清单（examples/*-prompts.md）里。

| # | 核验项 | 看什么 | 一致 | 偏一点 | 跑偏 | 偏差描述 |
|---|--------|--------|:----:|:------:|:----:|----------|
| 1 | 明度基调 | 样张整体亮度 vs 参考图；最深色有多深；阴影面积 | ☐ | ☐ | ☐ | |
| 2 | 线条密度 | 排线/发线数量是否相当；有无样张过密或过疏 | ☐ | ☐ | ☐ | |
| 3 | 线条粗细 | 发丝级 / 常规 / 粗，是否与参考图一致 | ☐ | ☐ | ☐ | |
| 4 | 色块层数 | 每个色块叠色层数是否相当（一两层 vs 多层） | ☐ | ☐ | ☐ | |
| 5 | 色板 | 主色是否落在参考图色板家族内；饱和度/明度倾向 | ☐ | ☐ | ☐ | |
| 6 | 留白比例 | 空白/浅色区域占比是否相当 | ☐ | ☐ | ☐ | |
| 7 | 夸张度 | 人物比例与五官：写实 / 温和夸张 / 强漫画 | ☐ | ☐ | ☐ | |
| 8 | 质感 | 纸纹/水痕/噪点等表面特征是否一致 | ☐ | ☐ | ☐ | |
| 9 | 禁忌项 | 无签名、无日期、无水印、无可读文字（除非风格要求标注字） | ☐ | ☐ | ☐ | |
| 10 | 系列一致 | （批量时）主角外貌连贯、色温情绪统一 | ☐ | ☐ | ☐ | |

## 回修速查

| 跑偏方向 | 改哪里 |
|----------|--------|
| 样张太暗 / 对比太强 | 锚定段「明度基调句」加强 + 负向形态句补 `no dark shadows, no dramatic lighting, no chiaroscuro`；检查场景是否与明度基调打架（夜景/孤灯场景换白天/均匀光） |
| 排线过密、像素描 | 「线条定量句」写明排线密度上限，如 `shading only hinted at with a few sparse hairline strokes, never filled in` + 负面约束加 `no dense cross-hatching` |
| 色太浓、层太厚 | 「色块层数句」写明 `only one or two thin tones per shape` + 负面约束加 `no heavy saturated color` |
| 留白不够、画面太满 | 锚定段补 `large areas of untouched white paper / generous negative space` |
| 太写实 | 锚定段「夸张度」改写，如 `gentle caricature proportions` 或 `strong caricature exaggeration with oversized heads` |
| 风格完全不同 | 检查是否把可变特征写进了锚定段、或骨架特征漏写；回到 style-guide.md 第一节重走来图识别三步 |
