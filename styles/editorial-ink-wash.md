# 风格档案 · 报刊淡彩（Editorial Ink Wash）

参考图：`assets/p718126702.jpg`（1080×1080，报刊头版式钢笔淡彩人物群像）。

## 负一、溯源识人（第 0 步产物）

| 项 | 结论 |
|----|------|
| 作者判断 | **高置信：Barry Blitt（巴里·布里特）** —— 《纽约客》御用讽刺漫画家 |
| 判断依据 | ①媒介：钢笔细线 + 淡水彩，纸本；②手法：头部放大的漫画式名人肖像；③版式：报刊头版戏仿（masthead + 小框插图 + 手写标注）；④题材：传媒大亨家族群像（Rupert / Lachlan / James / Sir Keith = 默多克家族），正是 Blitt 擅长的政治/媒体讽刺领域 |
| 风格谱系 | **纽约客编辑讽刺插画传统（New Yorker editorial caricature）**：钢笔淡彩 + 漫画式夸张 + 报刊版面叙事 + 克制的幽默 |
| 谱系通用特征 | 贯穿 Blitt 所有作品：发丝细线、淡水彩平涂、高调留白、头部放大夸张、报刊/书籍版式戏仿、手写标注字——**这些才是可复用的风格资产** |
| 内容特征（禁止进档案） | "NEW YORK POST" 报头、默多克家族人物、Page Six 栏目——只对这张图成立 |
| 名字纪律 | 作者名仅留档研究用，锚定段与提示词中**绝不出现**（触发出图审核，实测 HTTP 403） |

## 〇、量化指纹（脚本实测，可复核）

| 指标 | 实测值 | 含义 |
|------|--------|------|
| 明度分布 | 亮部(≥180) **84.2%**，中间 8.3%，暗部(<80) 仅 **7.6%** | 极端高调：画面近九成是浅色 |
| 明度中位数 | 233 / 255 | 纸白主导 |
| 饱和度中位数 | **0.09**（p90=0.29） | 极低保和，颜色几乎全是"淡了三分"的 |
| 暗部去向 | 几乎全部来自 ①墨线 ②报头实心字 ③西装色块 | 不存在"阴影"，只存在"线与小色块" |

**主色板（量化提取，按占比）**：

| 色 | HEX | 占比 | 角色 |
|----|-----|------|------|
| 纯白 | `#ffffff` | 17.7% | 纸张留白 |
| 纸米白 | `#eeeadf` / `#e6e1d5` | 27.3% | 报纸底色、西装灰的淡化区 |
| 淡桃肤 | `#f4e2ca` / `#f7eedc` | 24.1% | 肤色、暖背景 wash |
| 浅灰褐 | `#cab9a8` | 9.7% | 水彩晕斑积色、淡阴影 |
| 墨褐黑 | `#433931` | 10.9% | 墨线 + 报头实心字 + 西装深色区 |
| 点缀色（微量） | 领带亮蓝、国旗灰红、插图框底淡橙/淡蓝 | 各 <2% | **全画最艳的颜色只占极小面积** |

## 一、风格要素拆解（逐区域放大目检，带证据）

| 维度 | 特征 | 证据（图中位置） |
|------|------|------------------|
| 明度基调 | **极端高调**：84% 亮部；无任何"画的阴影"，暗色只以线和独立小色块存在 | 全图量化；面部受光/背光无差异（主肖像面部） |
| 媒介 | 针管笔/细钢笔黑线 + 透明水彩，纸本 | 线条起笔有针管笔顿挫（面部轮廓） |
| 线条 | **发丝级细线**，粗细均匀（1080px 图幅下约 1–2px），略带手抖；**几乎零排线**——下巴下、发际仅 3–5 根发线暗示 | 主肖像下颌、耳后（区域 x420,y270） |
| 实心黑 | **只允许出现在指甲盖大小的装饰块**：报头字母、"Page Six" 小框；且带白色飞白高光 | 报头区（x180,y70） |
| 上色 | 每个色块**一层平涂**即止，可见水彩晕斑边缘；颜色基本不出墨线；西装=一层青灰蓝平涂 | 西装与领带区（x330,y680） |
| 色板 | 纸白/米白 + 淡桃肤 + 青灰蓝 + 淡橙/淡蓝小色块；**全画只有一个高饱和点缀色**（领带亮蓝），面积 <2% | 量化色板 + 领带区 |
| 构图 | **报刊头版版面**：顶部报头横条；右侧大主肖像（约占版面 60% 宽）；左侧纵向叠 2–3 个小方框插图；每个头像下方一行手写标注；整版微倾斜，四周露出下层报纸边缘 | 全图 |
| 夸张度 | **头部显著放大**（主肖像头占人物高度约 45%），五官漫画式夸张（大鼻、深笑纹、眯眼），身体画法保持常规 | 主肖像（x420,y270） |
| 手写文字 | 两种：①标注字=细衬线全大写手写字（"RUPERT"）②报头=粗体实心手写字；背景栏文字用**假文字线条**表示 | 标注区（x330,y680）、左栏（x0,y380） |
| 质感 | 米色新闻纸，可见纸纤维与水彩水痕；无噪点、无胶片颗粒 | 纸米白区量化 + 背景区 |
| 题材 | 报刊人物群像/时事讽刺插画；版面化叙事 | 全图 |
| 画幅 | 1:1（参考图）；出图默认 1:1，可按需 16:9 | — |

**参考图里看不到的东西（负面约束反推依据）**：无渐变、无投影、无排线阴影、无大面积深色、无照片感细节、无 3D 体积感、无光滑数字填色、无霓虹高饱和色（除领带小点缀）。

## 二、风格锚定段

```anchor-en
Extremely high-key editorial ink-and-watercolor illustration on cream newsprint,
hand-drawn for a newspaper feature page, bright and airy. Delicate hairline-thin
black pen outlines of uniform weight, slightly wobbly; shading only hinted at
with three to five sparse hairline strokes, never filled in. Each color shape
receives a single flat watercolor wash, visible blotchy wash edges, colors stay
inside the ink lines. Palette of faded newsroom tints: paper white and cream,
pale peach skin, slate blue-grey, pale orange, washed navy; one small
high-saturation accent at most (e.g. a bright blue tie), under two percent of
the image. Solid black fills appear only in thumbnail-size decorative blocks.
Caricature proportions: oversized heads, exaggerated noses and smile lines,
conventionally drawn bodies. Composition like a newspaper front page: a large
main portrait beside stacked small framed inset portraits, thin hand-lettered
slab-serif capital captions beneath each figure, background columns shown as
meaningless hand-drawn text squiggles. No cast shadows, no gradients, no tonal
modeling. No readable artist signature and no dates or timestamps anywhere in
the image. {ratio} composition.
```

```anchor-cn
极端高调的报刊编辑插画，米色新闻纸上的钢笔淡彩手绘，明亮透气。发丝级纤细的
黑色钢笔轮廓线，粗细均匀、略带手抖；阴影只用三五根发线点到为止，绝不填死。
每个色块只平涂一层水彩，可见晕斑边缘，颜色不出墨线。褪色报刊色板：
纸白与米白、淡桃肤色、青灰蓝、淡橙、浅藏蓝；全画至多一个高饱和点缀色
（如亮蓝领带），面积不超过百分之二。实心黑只出现在指甲盖大小的装饰块中。
漫画比例：头部显著放大，鼻子与笑纹夸张，身体画法保持常规。
报刊头版式构图：大主肖像旁纵向叠小方框插图，每个头像下方一行细衬线
全大写手写字，背景文字栏用无意义的手写波浪线表示。无投影、无渐变、
无明暗塑造。不出现任何画师签名、日期或时间。{ratio} 构图。
```

```negative
no photorealism, no photography, no 3D render, no CGI, no digital smooth gradients,
no anime or manga style, no oil painting, no thick impasto, no neon colors,
no sharp vector lines, no flat cartoon fill, no glossy airbrush,
no dense cross-hatching, no heavy ink, no dark shadows, no dramatic lighting,
no chiaroscuro, no gritty texture, no graphic-novel shading, no moody darkness,
no cast shadows, no smooth digital fills, no large dark areas,
no artist signature, no readable signature, no dates, no timestamps, no watermark
```

## 三、场景描述写法

锚定段之后接场景段，只写变量：人物 + 动作 + 环境 + 氛围，英文 1–3 句。可选：
在场景末尾加 `Caption: "<手写标注文字>"` 让画面带报刊式标题字。
**场景必须与极端高调基调兼容**：不选夜景、暗房、单一强光源场景；叙事场景
用均匀 daylight 或明亮室内光改写。

## 四、抽象概念 → 场景转译速查（本风格）

| 文章主题 | 场景化写法示例 |
|----------|----------------|
| 人物自述/访谈 | 当事人做一件最有代表性的小事 + 手写人名标注，或小框分格画不同人生阶段 |
| 回忆/往事 | 同版分格：大格现状、小格往事，如同报纸人物版 |
| 转折/顿悟 | 单人物近景漫画肖像 + 一个象征物（画架、蝴蝶、扔掉的刷子） |
| 日常/回归 | 明亮群像小场景（教室、街角、市集），均匀 daylight |
