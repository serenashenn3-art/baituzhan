# assets · 参考图目录

每个风格档案（`styles/<风格名>.md`）对应的参考图放这里，命名与档案对应：

```
styles/watercolor-sketch.md      →  assets/example-watercolor-sketch.jpeg
styles/<你的风格名>.md            →  assets/example-<你的风格名>.jpeg（1–3 张可加 -1 -2 后缀）
```

参考图的两个用途：

1. **斩风格**：Agent 建档时的分析对象；
2. **出图锁风格**：作为参考图传入出图工具（如 Kimi image_generation 插件的 `--reference-image`），让整套图风格高度统一。

注意：参考图若带有画师签名、日期，属正常现象——锚定段与负面约束已内置禁令，生成图不得模仿出这些信息，生成后需目检。
