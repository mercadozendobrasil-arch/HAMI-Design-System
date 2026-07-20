# Versioning

## Purpose

让设计规则、产品数据和生成结果可追溯、可兼容。

## Usage

采用 Semantic Versioning：

- MAJOR：破坏模板坐标、token 名、组件契约或产品库接口。
- MINOR：向后兼容地新增模板能力、token 或 QA 检查。
- PATCH：不改变契约的文案、示例或错误修复。

每张生成图的 manifest 必须记录 `designSystemVersion`、`productLibraryVersion`、`templateId`、`productSku` 和源图哈希。发布前同步更新根 manifest、README 和受影响模块版本。

## Dependencies

`../design-system.manifest.json`, Product Library manifest.

## Related Modules

`Release-Checklist.md`, `Contributing.md`.

## Version

`2.0.0`
