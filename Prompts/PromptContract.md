# Prompt Contract

## Purpose
定义所有薄 prompt 共用的确定性执行和失败协议。

## Usage
输入 `productRecord`、`templateId`、`outputPath`，可选输入只有已验证的 `copyOverrides`。按强制顺序加载 Design System 和目标产品记录，解析模板依赖，组合画面，生成 QA manifest，运行适用 QA，仅在通过后导出。

缺少产品资产、声明未经验证、metadata 不兼容、Product Lock 失败或 QA 失败时拒绝导出。不得发明缺失数据。

## Dependencies
`../CODEX.md`, `../Templates/`, `../Rules/`, `../QA/`, Product Library.

## Related Modules
`../Documentation/Automation-Contract.md`, `../Documentation/AI-Loading-Protocol.md`.

## Version
`2.0.0`
