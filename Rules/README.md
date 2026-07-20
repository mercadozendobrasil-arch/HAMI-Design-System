# Rules

## Purpose

集中定义跨模板强制规则，防止模板或 prompt 各自复制并产生漂移。

## Usage

- `ProductLock.md`：保护产品真实像素、结构、比例与透视。
- `LayoutRules.md`：规定 8pt grid、safe area、Logo、margins、spacing 与产品占比。
- `TextRules.md`：规定文案行数、卖点数量、语言与字体。

任何模板都只能引用规则，不得弱化或覆盖规则。冲突优先级为 Product Lock → Layout → Text → 装饰。

## Dependencies

`../Brand/`, `../Tokens/`.

## Related Modules

`../Templates/`, `../QA/`.

## Version

`2.0.0`
