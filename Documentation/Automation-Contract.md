# Automation Contract

## Purpose

把简短自然语言命令确定性地解析为产品、模板、输入资产、QA 与输出，避免追问和随机设计。

## Usage

命令语法：

```text
Generate <SERIES> <PRODUCT NAME> <CHANNEL> <OUTPUT TYPE>
```

示例：

```text
Generate QT Redmi Pad 2 Shopee Cover
```

确定性解析结果：

```json
{
  "series": "QT",
  "productQuery": "Redmi Pad 2",
  "channel": "Shopee",
  "template": "Template001-Cover"
}
```

执行器必须：

1. 完成 `AI-Loading-Protocol.md`。
2. 在 `Products/QT/` 中以规范化名称、SKU 和 `compatibleModels` 查找唯一记录。
3. 验证 `metadata.json`、`metadata.md`、`notes.md` 与模板要求的真实 PNG。
4. 加载 `Template001-Cover.md` 及其声明的 token、组件和 icon。
5. 生成 image manifest，执行 `QA/validate.py` 和全部适用人工检查。
6. 仅在全部通过后输出 800×800 RGB PNG。

若 `QT Redmi Pad 2` 尚未入库，正确结果是 `BLOCKED_MISSING_PRODUCT_RECORD` 并返回缺失路径，不得伪造产品图、metadata 或卖点。只在存在多个真实匹配或用户命令缺少不可推导的产品身份时才需要用户选择。

## Dependencies

`AI-Loading-Protocol.md`, `Template-Selection.md`, `../Prompts/PromptContract.md`, Product Library metadata schema.

## Related Modules

`../QA/validate.py`, `../QA/image-manifest.schema.json`, `../Rules/ProductLock.md`.

## Version

`2.0.0`
