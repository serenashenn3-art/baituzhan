# 风格档案 · 稚拙蜡笔涂鸦（Naive Crayon）

参考图：`assets/ref3-a.png`（桃子与虫，1710×1568）、`assets/ref3-b.png`（三只鸽子，1412×1270）、`assets/ref3-c.png`（三条鱼，1086×1030），同一作者的三幅系列作品。

## 负一、溯源识人（第 0 步产物）

| 项 | 结论 |
|----|------|
| 作者判断 | **未确认**（三图均无署名、无印章；画面只有手写涂鸦句） |
| 判断依据 | 三图共享同一套语言，可确认是同一作者的系列：蜡笔/油画棒质感、纯色平涂背景、居中单一主体、彩色小写手写字、星形装饰符号 |
| 风格谱系 | **当代绘本/编辑插画中的"稚拙质感派"（naive textured illustration）**：模拟儿童画的天真笔触 + 专业色彩控制 + 丝网印刷（risograph）颗粒感，常见于独立杂志、zine、绘本与社交媒体插画 |
| 谱系通用特征 | ①无轮廓线，形状全靠笔触色块拼出；②大笔触感、边缘歪斜不齐；③整幅一种纯色平涂背景（可浓可淡）；④主体单一居中、大量留白；⑤手写涂鸦小字 + 星形/圆点装饰；⑥全画面均匀印刷颗粒——**这些才是可复用的风格资产** |
| 内容特征（禁止进档案） | 桃子、虫、鸽子、鱼这些具体题材，以及具体的英文句子——只对这三张图成立 |
| 名字纪律 | 作者名仅留档研究用，锚定段与提示词中**绝不出现**（触发出图审核，实测 HTTP 403） |

## 〇、量化指纹（脚本实测，可复核）

| 指标 | 桃(a) | 鸽(b) | 鱼(c) | 不变量结论 |
|------|-------|-------|-------|-----------|
| 明度中位数 | 171 | 253 | 255 | **明亮为主**，绝无暗调 |
| 暗部(<80)占比 | 0.1% | 4.8% | 0.0% | **几乎零暗部**，深色主体也是中明度 |
| 高饱和(≥0.6)像素 | 88.9% | 9.4% | 17.1% | 饱和度由背景决定：浓背景则全图艳，淡背景则全图柔 |
| 背景单色素 | 蓝 `#103090` 占 42.1% | 薄荷绿 `#d0f0d0` 占 74.5% | 奶黄 `#f0f0d0` 占 60.5% | **整幅一种纯色平涂背景，占画面 4–7 成** |

**色板结论**：背景=一种纯色（宝蓝/薄荷绿/奶黄均可，变量）；主体=一个和谐色系内 2–4 层笔触色（橙红系、青蓝系、粉红系）+ 1–2 个芝麻粒大小的对比色虚线点缀（如深蓝颈羽上的粉蓝短划）。

## 一、风格要素拆解（逐区域放大目检，带证据）

| 维度 | 特征 | 证据（图中位置） |
|------|------|------------------|
| 明度基调 | **明亮无阴影**：三图暗部均 <5%；没有投影、没有暗角，深色主体也保持中明度 | 三图量化；鸽(b)深蓝颈羽明度仍在 90+ |
| 媒介 | 蜡笔/油画棒/彩铅质感 + 全画面均匀的丝网印刷颗粒（riso grain）与局部半调网点 | 桃(a)表面蜡质笔触与噪点（x400,y500）；鸽腿半调网点（b,x50,y550） |
| 线条 | **没有轮廓线**：所有形状由涂鸦笔触直接拼出，边缘歪斜、锯齿、不齐；装饰性小符号（线圈、圆点、短虚线）直接画在色块上 | 桃(a)上的粉色线圈与圆点（x400,y500）；鱼鳍=简单平行排线（c,x200,y100） |
| 上色 | 同色系 2–4 层涂鸦笔触叠色，笔触之间**露出纸色缝隙**；绝不平滑涂抹 | 鱼(c)红叠橙叠粉、白色纸缝清晰可见（x200,y100） |
| 色板 | 主体一个和谐色系 + 1–2 个极小对比色点缀；背景单一纯色 | 鸽(b)青蓝主体上的粉/蓝短划（x50,y550）；鱼(c)上的蓝色小虚线 |
| 构图 | **单一主体（或一排小组）绝对居中**，四周超大留白；星形/星爆符号散落四周 | 三图全图 |
| 夸张度 | **儿童画式天真简化**：大眼睛、憨态、不追求解剖准确 | 鸽子卡通眼带白色高光（b）；鱼的圆大眼（c） |
| 手写文字 |  playful 全小写手写字，字母可彩虹着色，内容俏皮；是构图的一部分 | "the perfect fish for socks!!"（c 彩虹字）；"we make a pretty good trio!!"（b 红色字） |
| 质感 | 纸纹 + 印刷噪点遍布全图，包括背景；无渐变、无喷涂 | 三图量化与放大目检 |
| 题材 | 静物、小动物、单一物件的俏皮肖像 | 三图 |
| 画幅 | 接近 1:1（参考图 1710×1568 / 1412×1270 / 1086×1030）；出图默认 1:1 | — |

**参考图里看不到的东西（负面约束反推依据）**：无轮廓墨线、无环境场景、无透视空间、无写实细节、无渐变喷涂、无暗调阴影、无 3D 渲染、无照片感、无签名日期。

## 二、风格锚定段

```anchor-en
Naive textured picture-book illustration, bright and shadowless, in waxy
crayon and colored-pencil strokes with an even risograph print grain over
the entire image. One single flat solid background color fills the whole
canvas. A single subject, or one small row of subjects, sits centered with
generous empty margins; no environment, no perspective, no ground line.
Shapes are built entirely from scratchy layered strokes of two to four
harmonious hues with slivers of paper color showing between strokes; edges
are wobbly and uneven, with no contour outlines anywhere. One or two tiny
contrasting dash or dot accents on the subject. Childlike simplification:
big round cute eyes, charmingly clumsy proportions, no anatomical realism.
A few scattered hand-drawn sparkles or starbursts. No gradients, no
airbrush, no cast shadows, no dark tones. No artist signature and no dates
or timestamps anywhere in the image. {ratio} composition.
```

```anchor-cn
稚拙质感的绘本插画，明亮无阴影，蜡笔与彩铅笔触，全画面覆盖均匀的
丝网印刷颗粒。整幅画布用一种纯色平涂做背景。单一主体（或一小排主体）
绝对居中，四周大量留白；没有环境、没有透视、没有地平线。所有形状由
涂鸦笔触直接拼出，同色系两至四层叠色，笔触间露出纸色缝隙；边缘歪斜
不齐，全图没有任何轮廓线。主体上有一两粒对比色的短划或圆点点缀。
儿童画式天真简化：圆圆的大眼睛、憨拙可爱的比例、不追求解剖准确。
四周散落几个手绘星形闪光符号。无渐变、无喷涂、无投影、无暗调。
画面中不出现任何画师签名、日期或时间。{ratio} 构图。
```

```negative
no photorealism, no photography, no 3D render, no CGI, no contour outlines,
no ink lines, no closed line art, no detailed background, no environment scene,
no perspective, no horizon line, no cast shadows, no dark tones, no night scene,
no gradients, no airbrush, no smooth digital fills, no oil painting,
no watercolor wash, no realistic anatomy, no anime or manga style,
no chiaroscuro, no neon glow, no lens flare, no frame border,
no artist signature, no readable signature, no signature seal, no stamp,
no dates, no timestamps, no watermark
```

## 三、场景描述写法

锚定段之后接场景段，只写变量：**单一主体 + 姿态 + 主体色系 + 背景色 + 一句装饰建议**，
英文 1–2 句。**这是"单主体纯色背景"风格，不是场景风格**——叙事内容必须转译成
一个象征物或一个小组合（见转译表），不要写房间、街景、人物全身叙事场面。
**背景色每张一换、系列内形成节奏**（如奶黄 → 薄荷绿 → 宝蓝 → 暖粉），主体色系与背景
形成对比或互补。
**文字策略**：本风格有手写字传统，可在场景末尾加
`Hand-lettered playful lowercase caption: "<2–4 个英文小写单词>"`；若出图文字
出现乱码，整批改 `--no-text` 重出。

## 四、抽象概念 → 场景转译速查（本风格）

| 文章主题 | 场景化写法示例 |
|----------|----------------|
| 人物自述/访谈 | 一个最代表他的物件肖像（画架、画笔桶、狗），纯色背景 |
| 陪伴/情感 | 一大一小两个主体的组合（大狗 + 小球、大手 + 小手） |
| 转折/顿悟 | 单一象征物特写（发光的蝴蝶、破茧），亮色系背景 |
| 孤独/困顿 | 一个小主体在超大留白中缩小偏置，但保持无阴影明亮基调 |
| 日常/回归 | 一排小物件或小动物横排（三支蜡笔、三个苹果），手写俏皮小字 |
