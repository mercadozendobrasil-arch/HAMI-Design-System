# AI Loading Protocol

## Purpose

确保每个 AI 在接触任务前使用当前、完整、同序的 HAMI 事实源。

## Usage

每个新的商品图片任务都执行一个阻塞式 preflight：

1. 读取根 `README.md` 和 `CODEX.md`。
2. 按文件名字典序完整读取 `Brand/`。
3. 完整读取并解析 `Tokens/` 的 Markdown 与 JSON。
4. 按文件名字典序完整读取 `Components/`。
5. 完整读取 `Templates/`，但只执行命令映射到的模板。
6. 完整读取 `Rules/`。
7. 完整读取 `QA/`；源代码按接口读取，不执行不可信输入。
8. 打开 Product Library 的 `README.md`、manifest、metadata schema、目标系列和唯一目标产品记录。
9. 记录 design-system version、product-library version、template id、product SKU 与源图 SHA-256，随后才可开始。

## Failure behavior

- 任一模块、JSON、目标产品或必需图片缺失：停止生成并列出精确缺失项。
- 同一产品出现多个匹配：停止并列出冲突记录，不猜测。
- metadata、文件哈希或 Product Lock 无效：拒绝输出。
- 旧缓存与仓库文件冲突：以当前仓库文件为准。

## Dependencies

`../README.md`, `../CODEX.md`, `../design-system.manifest.json`, `HAMI-Product-Library/product-library.manifest.json`.

## Related Modules

`Automation-Contract.md`, `Template-Selection.md`, `../QA/Final-QA.md`.

## Version

`2.0.0`
