# HAMI Design System

HAMI 电商视觉的唯一设计事实源。该仓库让 Codex、ChatGPT、Claude Code、Cursor、Gemini 与后续 AI 系统以同一套品牌、token、组件、模板和 QA 规则生成 Shopee Official Store 商品图。

Purpose: 统一 HAMI 商品图的所有视觉与执行契约。
Usage: 从下方 Mandatory loading order 开始，禁止跳过模块。
Dependencies: 运行时依赖兼容的 HAMI Product Library。
Related Modules: 本仓库全部受治理目录与 Product Library。
Version: `2.0.0`。

## Mandatory loading order

任何读取、规划、生成或修改商品图片的动作开始前，必须完整加载：

`README.md` → `CODEX.md` → `Brand/` → `Tokens/` → `Components/` → `Templates/` → `Rules/` → `QA/` → `HAMI-Product-Library`

不得跳过、并行猜测或用模型记忆替代当前文件。详见 [`Documentation/AI-Loading-Protocol.md`](Documentation/AI-Loading-Protocol.md)。

## Non-negotiable output contract

- 800×800 px、RGB、PNG、Shopee Official Store。
- 产品视觉占比 72%–75%，银灰渐变背景，Montserrat only。
- 每张图最多四个卖点；每个文案块最多两行；outline icons only。
- 所有布局值来自 token；8pt grid，safe area、Logo、spacing 与 margins 固定。
- 产品像素来自 `HAMI-Product-Library`，不得重绘、变形、推断或补全。

## Repository map

| Module | Responsibility |
| --- | --- |
| [`Brand/`](Brand/) | 品牌身份、Logo、字体、颜色、图标、语气 |
| [`Tokens/`](Tokens/) | 可复用机器可读设计值 |
| [`Components/`](Components/) | 十个可复用视觉组件 |
| [`Templates/`](Templates/) | Template001–009 永久版式规范 |
| [`Rules/`](Rules/) | Product Lock、布局和文案约束 |
| [`Prompts/`](Prompts/) | 只做路由、不复制规则的薄提示词 |
| [`QA/`](QA/) | 自动检查器、schema 与人工检查表 |
| [`Assets/`](Assets/) | 经验证的 Logo 与统一 outline SVG |
| [`Examples/`](Examples/) | 命令解析示例，不存伪造产品图 |
| [`Documentation/`](Documentation/) | 加载、选模、版本和贡献协议 |

## Command example

```text
Generate QT Redmi Pad 2 Shopee Cover
```

系统将解析产品记录、调用 `Template001-Cover`、执行 QA 并导出；如果产品记录或必需真实素材不存在，则明确拒绝生成，不会用占位图冒充商品。详见 [`Documentation/Automation-Contract.md`](Documentation/Automation-Contract.md)。

## Repository boundary

- `HAMI-Design-System`：品牌、token、组件、布局、模板、prompt、QA、资产与文档。
- `HAMI-Product-Library`：真实产品像素、产品元数据和产品专属备注。

两仓库不得复制对方职责内的文件。当前稳定版本：`2.0.0`。
