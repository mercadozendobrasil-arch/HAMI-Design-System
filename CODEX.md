# HAMI Codex Operating Instructions

本文件是 AI 执行 HAMI 商品图片任务的强制运行契约。

Purpose: 约束 AI 的加载、解析、生成与拒绝行为。
Usage: 每个新商品图片任务都从 Preflight gate 开始。

## Preflight gate

在做任何分析、选模、写 prompt、排版或生成之前，必须完整读取且按顺序完成：

1. `README.md`
2. `CODEX.md`
3. `Brand/` 全部文档
4. `Tokens/` 全部文档与 JSON
5. `Components/` 全部文档
6. `Templates/` 全部文档
7. `Rules/` 全部文档
8. `QA/` 全部文档、schema 和验证器契约
9. `HAMI-Product-Library/README.md`、manifest、schema、目标系列和目标产品记录

未完成 preflight 时，禁止开始工作。每次新的商品图片任务都必须重新执行，不能依赖上一次读取或模型记忆。

## Execution contract

1. 将自然语言命令解析为 `series`、`product`、`channel`、`template`。
2. 在 Product Library 中定位唯一产品记录并验证 metadata 与文件哈希。
3. 依据任务映射 Template001–009，不改变模板布局。
4. 只加载模板声明的 token、组件、icon 和规则依赖。
5. 保持真实产品像素锁定，只组合背景、文案、图标和版式。
6. 生成 800×800 RGB PNG 和 image manifest。
7. 运行模板 QA、Product Lock QA、Layout QA 和 Final QA；失败则修正或拒绝导出。

## Priority

1. 产品真实性与结构完整
2. 模板一致性
3. 手机端可读性
4. 产品视觉占比
5. 装饰美观

## Product Lock

不得重绘、推断或修改摄像头孔、扬声器孔、按键、接口、圆角、形状、透视、比例、透明 TPU、纹理与颜色边界。缺少真实素材时必须停止生成并报告缺失项。

## Fixed image rules

- 800×800 px、RGB、PNG。
- Montserrat only。
- 银灰渐变背景。
- 产品视觉占比 72%–75%。
- 每张图最多四个短卖点，每个文案块最多两行。
- outline icons only。
- 所有布局值由 token 提供；禁止硬编码新值。
- 默认输出语言为巴西葡萄牙语。

## Default routing

“Cover / 封面 / 主图”映射到 `Templates/Template001-Cover.md`。其他映射见 `Documentation/Template-Selection.md`。不得在模板之外发明布局或随机风格。

Version: `2.0.0`
Dependencies: `README.md`, all governed modules, `HAMI-Product-Library`.
Related: `Documentation/AI-Loading-Protocol.md`, `Documentation/Automation-Contract.md`.
