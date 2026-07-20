# HAMI Design System

HAMI 的统一电商视觉规范仓库，供 Codex、设计师及其他 AI 工具生成 Shopee、Mercado Livre 和 TikTok Shop 商品图片时调用。

## 强制使用原则

1. 开始任何设计任务前，先读取 [`CODEX.md`](CODEX.md)。
2. 所有封面主图必须读取 [`Templates/Template001-Cover.md`](Templates/Template001-Cover.md)。
3. 产品必须遵守 [`Rules/ProductLock.md`](Rules/ProductLock.md)，不得重绘、变形或改变结构。
4. 非必要情况下，每个文案块不得超过两行，并尽量减少文字总量。
5. 输出前必须执行 [`QA/Image-QA.md`](QA/Image-QA.md)。

## 仓库结构

```text
Brand/          品牌身份与原则
Tokens/         设计令牌
Components/     可复用组件
Templates/      Shopee 九张图永久模板
Rules/          产品、文案、布局与素材规则
Prompts/        可复用任务提示词
QA/             自动检查与人工检查表
Assets/         固定品牌资产
Examples/       审核通过的标准案例
Documentation/  架构与使用文档
```

## 快速调用

向 Codex 输入：

```text
请先读取本仓库的 CODEX.md，然后使用 Template001-Cover 为以下产品制作 800×800 Shopee 封面图。
产品：<产品名称>
型号：<兼容型号>
颜色：<产品颜色>
素材：<产品图片路径>
```

## Canonical repositories

- `HAMI-Design-System`: reusable brand rules, tokens, components, layouts, templates, prompts, QA and documentation.
- `HAMI-Product-Library`: product pixels, product metadata and product-specific notes only.

Files must never be duplicated between the two repositories. Design files reference product-library paths; product records reference design-system versions.

## Required loading order

`README.md` → `CODEX.md` → `Brand/` → `Tokens/` → `Components/` → `Templates/` → `Rules/` → `QA/` → `HAMI-Product-Library`

当前版本：`v2.0.0-dev`
