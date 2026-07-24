# 风格档案 · 明线派科幻插画（Ligne Claire）

参考图：`assets/example-ligne-claire.png`（1648×2944 竖版，外星酒吧中的白发老者，密集机械背景）。

## 负一、溯源识人（第 0 步产物）

| 项 | 结论 |
|----|------|
| 作者判断 | **确认：Moebius（墨比斯，本名 Jean Giraud，1938–2012）** —— 法国国宝级漫画家 |
| 判断依据 | ①文件名自带署名 "Man at Alien Bar by Moebius"；②手法即其标志性语言：均匀闭合细轮廓线 + 平涂色块 + 色块内排线/点刻肌理；③密集繁复的机械管线背景（其科幻场景标志）；④紫蓝 + 橙红互补双色调打光；⑤左下角有其常用的红色印章式签名（区域 x0,y2544） |
| 风格谱系 | **法比漫画明线派（ligne claire / clear line）**：源自《丁丁历险记》Hergé 的闭合均匀线 + 平涂传统，Moebius 在此之上加入**极高密度细节**与**双色打光**，形成梦幻科幻一支（《阿扎克》《蓝莓上尉》《印加石》） |
| 谱系通用特征 | 贯穿 Moebius 所有作品：均匀闭合轮廓线、平涂色块、阴影=互补色离散色块（拒绝渐变）、点刻/排线肌理、密集机械细节、紫蓝橙红双色调——**这些才是可复用的风格资产** |
| 内容特征（禁止进档案） | 外星酒吧、白发白须老者、酒瓶蒸馏器、外星人——只对这张图成立；换题材时场景完全自由 |
| 名字纪律 | 作者名仅留档研究用，锚定段与提示词中**绝不出现**（触发出图审核，实测 HTTP 403）；也不要写 "in the style of" 任何在世或已故作者名 |

## 〇、量化指纹（脚本实测，可复核）

| 指标 | 实测值 | 含义 |
|------|--------|------|
| 明度分布 | 暗部(<80) **26.4%**，中间 **65.7%**，亮部(≥180) 仅 **8.0%** | 中间调偏暗：画面以中深色为主 |
| 明度中位数 | **118 / 255**（p10=44，p90=177） | 氛围感画面，绝非明亮高调 |
| 饱和度中位数 | **0.39**（p90=0.89） | 中高饱和：底色沉稳，局部很艳 |
| 暗部去向 | ①近黑墨线（11.2%）②藏蓝/深蓝背景色块 | 暗色是**有颜色的暗**（蓝紫系），不是纯黑阴影 |

**主色板（量化提取，按占比）**：

| 色 | HEX | 占比 | 角色 |
|----|-----|------|------|
| 紫粉 | `#b99cb8` | 17.1% | 肤色、亮部平涂 |
| 灰蓝 | `#717ca3` | 13.8% | 中间调底色 |
| 藏蓝 | `#4d5e91` | 12.0% | 背景机械主色 |
| 近黑 | `#16191d` | 11.2% | 全部轮廓墨线 |
| 暗红 | `#803632` | 9.7% | 暖色打光区（衬衫、吧台） |
| 深蓝 | `#2a4972` | 9.6% | 背景深处 |
| 粉 | `#b58799` | 8.1% | 肤色过渡、器物 |

**色板结论**：蓝紫冷色系为底（约占 6 成）+ 橙红暖色系做打光与点缀（约占 2 成）+ 近黑墨线，即**互补双色调**。

## 一、风格要素拆解（逐区域放大目检，带证据）

| 维度 | 特征 | 证据（图中位置） |
|------|------|------------------|
| 明度基调 | **中间调偏暗 + 双色调打光**：冷蓝紫为环境光，暖橙红为局部光源色；亮部极少且小 | 全图量化；面部受光（区域 x550,y700：左冷右暖） |
| 媒介 | 钢笔/针管笔墨线 + 平涂上色（原作为墨线 + 手绘色，数字复刻亦成立） | 全图 |
| 线条 | **均匀细致的闭合轮廓线**，粗细基本一致（1648px 宽图幅下约 2–3px），近黑色；**所有形状完全封闭**，为平涂做准备；轮廓线偶尔用同色系的更深色代替纯黑（蓝形上用深藏蓝线） | 面部皱纹与发丝（x550,y700）；背景机械（x0,y0，蓝上蓝线） |
| 肌理 | **色块内部用排线、点刻、短碎线做明暗与质感**，绝不涂抹：胡须=密集平行弧线；皮肤=细点 + 短皱线；布料=稀疏折线 + 细碎点 | 胡须（x750,y950）；外套（x100,y1100）；吧台（x900,y1400 台面碎点） |
| 阴影 | **阴影 = 互补色的离散平涂色块**，形状独立、边缘锐利、无渐变过渡：暖区里的影子是蓝紫色块，冷区里的影子是更深色块 | 外套亮橙面上的蓝紫影块（x100,y1100）；手部冷光区（x900,y1400 左下） |
| 上色 | 每形状**一层平涂**，色不出线；色彩平但有版画画感 | 全图 |
| 色板 | 紫粉/灰蓝/藏蓝/深蓝冷底 + 暗红/橙暖点缀 + 近黑墨线；最艳色集中在小面积（衬衫红、酒瓶） | 量化色板 |
| 细节密度 | **极高密度**：背景机械管线铆钉层层叠叠，每件器物都完整刻画，无省略无虚化 | 背景机械区（x0,y0）：管线、铆钉、刻度盘全部画出 |
| 构图 | 人物近景居中，环境细节充满全部背景，无留白 | 全图 |
| 夸张度 | **写实比例**，人物解剖准确；表情靠皱纹线条刻画，不卡通化 | 面部（x550,y700） |
| 文字/签名 | 左下角有红色印章式签名——**出图必须禁止模仿**：不要签名、不要印章、不要日期 | 签名区（x0,y2544） |
| 质感 | 平涂 + 线条肌理，画面干净；无噪点、无胶片颗粒、无纸纹 | 全图量化 |
| 题材 | 科幻/奇幻场景、人物肖像、密集环境；换题材后风格全部成立 | 全图 |
| 画幅 | 参考图 9:16 竖版；出图默认 1:1（配图），可按需 16:9 | — |

**参考图里看不到的东西（负面约束反推依据）**：无渐变、无喷涂柔边、无照片写实、无 3D 渲染体积光、无水彩晕斑、无厚涂笔触、无卡通粗描边、无大面积纯白留白、无胶片噪点。

## 二、风格锚定段

```anchor-en
Franco-Belgian ligne-claire comic illustration, mid-key and moody with two-tone
lighting: cool blue-violet ambient tones against warm orange-red accents.
Clean, fine, uniform closed contour lines in near-black, every shape fully
enclosed; occasional hue-matched darker lines on colored shapes. Each shape
receives one flat color fill, colors stay inside the lines; shading is drawn
as discrete flat shapes in the complementary hue with crisp edges, never
gradients. Interior texture built only from fine parallel hatching, stipple
dots and short dashed strokes. Palette of muted violet-blue base tones
(dusty mauve, slate blue, deep navy) with small saturated warm accents
(brick red, orange) and near-black ink. Extremely dense intricate detail:
every object, pipe and rivet fully drawn, no blur, no empty background.
Realistic human proportions, no caricature. No painterly gradients, no
photorealism, no 3D rendering, no airbrush softness, no watercolor blotches.
No artist signature, no signature seal or stamp, no dates or timestamps
anywhere in the image. {ratio} composition.
```

```anchor-cn
明线派法比漫画插画，中间调偏暗、双色调打光：冷蓝紫环境光对撞暖橙红点缀。
干净细致的均匀闭合轮廓线，近黑色，所有形状完全封闭；彩色形状上偶尔用
同色系的更深色勾线。每个形状只平涂一层颜色，色不出线；阴影画成互补色的
离散平涂色块，边缘锐利，绝无渐变。块面内部肌理只用细排线、点刻和
短碎线表现。色板：沉稳的蓝紫冷底（灰紫粉、石板蓝、深藏蓝）+ 小面积
高饱和暖色点缀（砖红、橙）+ 近黑墨线。细节密度极高：每件器物、管线、
铆钉都完整刻画，不虚化、不留空背景。人物写实比例，不卡通化。
无绘画性渐变、无照片写实、无 3D 渲染、无喷涂柔边、无水彩晕斑。
画面中不出现任何画师签名、签名印章、日期或时间。{ratio} 构图。
```

```negative
no photorealism, no photography, no 3D render, no CGI, no cinematic lighting,
no airbrush, no soft gradients, no painterly blending, no watercolor,
no wash blotches, no oil painting, no thick impasto, no anime or manga style,
no chibi, no thick cartoon outlines, no sketchy unfinished lines, no cross-hatched
shadow fills, no neon cyberpunk glow, no lens flare, no film grain, no noise,
no paper texture, no large empty white areas, no blurry background, no bokeh,
no caricature, no chiaroscuro, no heavy black shadow masses,
no artist signature, no readable signature, no signature seal, no stamp,
no red seal stamp, no dates, no timestamps, no watermark
```

## 三、场景描述写法

锚定段之后接场景段，只写变量：人物 + 动作 + 环境 + 氛围，英文 1–3 句。
**场景必须与中间调偏暗的双色调基调兼容**：优先室内灯光、夜晚、台灯/炉火/
发光体等"有理由的暖光源 + 冷环境"场景；明亮户外大白天与本风格相悖，
如需白天场景改写成"冷天光为主 + 一处暖色点缀"。
**每张图都要写清暖光源在哪里**（台灯、炉火、发光物），这是双色调的锚。
本风格无文字传统：默认 `--no-text`，不要标题字、标注字。

## 四、抽象概念 → 场景转译速查（本风格）

| 文章主题 | 场景化写法示例 |
|----------|----------------|
| 人物自述/访谈 | 人物近景居中做一件手上的事（画画、修东西），环境细节充满背景，一盏暖光源 |
| 回忆/往事 | 同一场景的"深夜版"：冷蓝环境 + 单一暖光源，象征物置于光下 |
| 转折/顿悟 | 人物与发光象征物对视（发光体本身就是暖光源，天然双色调） |
| 孤独/困顿 | 小空间全景：密集杂物充满画面，人物缩在暖光一角 |
| 日常/回归 | 群像小场景（教室、作坊），暖色灯光 + 冷色环境，细节全刻画 |
