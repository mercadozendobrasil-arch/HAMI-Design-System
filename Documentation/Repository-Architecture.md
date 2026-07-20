# Repository Architecture

## Purpose

定义 HAMI Design System 与 Product Library 的所有权边界，避免规则和产品像素重复。

## Usage

| Repository | Owns | Must not own |
| --- | --- | --- |
| HAMI-Design-System | Brand, tokens, components, layouts, templates, prompts, QA, approved brand assets, examples | SKU product pixels or product-specific facts |
| HAMI-Product-Library | Product PNGs, product metadata, asset hashes, series notes | Brand values, layout values or copied template rules |

依赖方向：Design System 在运行时读取 Product Library 的稳定记录；Product Library 只声明兼容的 Design System 版本，不复制其文件。生成结果通过版本号和 SHA-256 关联两端。

## Dependencies

`../design-system.manifest.json`, Product Library manifest.

## Related Modules

`AI-Loading-Protocol.md`, `Versioning.md`.

## Version

`2.0.0`
