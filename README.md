# HAMI Design System

HAMI 的统一电商视觉规范仓库，供 Codex、设计师及其他 AI 工具生成 Shopee、Mercado Livre 和 TikTok Shop 商品图片时调用。

## 强制使用原则

1. 开始任何设计任务前，先读取 [`CODEX.md`](CODEX.md)。
2. 所有封面主图必须读取 [`templates/Template001-Cover.md`](templates/Template001-Cover.md)。
3. 产品必须遵守 [`rules/ProductLock.md`](rules/ProductLock.md)，不得重绘、变形或改变结构。
4. 非必要情况下，每个文案块不得超过两行，并尽量减少文字总量。
5. 输出前必须执行 [`checklists/Image-QA.md`](checklists/Image-QA.md)。

## 仓库结构

```text
brand/       品牌、颜色、字体、图标与网格规范
rules/       产品锁定、文案、布局及素材规则
templates/   Shopee 九张图永久模板
prompts/     Codex 可直接调用的任务提示词
checklists/  输出前质量检查
assets/      Logo、背景、图标及产品素材目录说明
examples/    审核通过的标准案例
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

当前版本：`v1.0.0`
