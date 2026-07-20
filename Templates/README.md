# Template Library

## Purpose

定义 Shopee Official Store 的九个永久页面模板。模板负责布局契约，不复制 token、组件或产品事实。

## Usage

| ID | Output |
| --- | --- |
| Template001 | Cover |
| Template002 | Selling Points |
| Template003 | Stand |
| Template004 | Material |
| Template005 | Protection |
| Template006 | Details |
| Template007 | Colors |
| Template008 | Compatibility |
| Template009 | Package |

必须使用 `Documentation/Template-Selection.md` 选择唯一模板，并执行模板声明的 QA。不得改版或创建临时布局。

## Dependencies

`../Tokens/`, `../Components/`, `../Rules/`.

## Related Modules

`../Prompts/`, `../QA/`, `../Documentation/Template-Selection.md`.

## Version

`2.0.0`
