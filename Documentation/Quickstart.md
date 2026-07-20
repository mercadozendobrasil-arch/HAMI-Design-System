# Quickstart

## Purpose

提供最短但完整的 HAMI 自动生成入口。

## Usage

1. Clone `HAMI-Design-System` 与 `HAMI-Product-Library` 到同一工作区。
2. 按 `AI-Loading-Protocol.md` 完成全部预加载。
3. 确认目标产品目录包含真实 PNG、`metadata.json`、`metadata.md` 和 `notes.md`。
4. 输入 `Generate <SERIES> <PRODUCT> Shopee <OUTPUT TYPE>`。
5. 生成器按 `Template-Selection.md` 选模并输出 image manifest。
6. 在仓库根目录运行：

```powershell
python -m unittest discover -s QA -p "test_*.py" -v
python QA/validate.py <image-manifest.json>
```

只有自动 QA 和适用人工 QA 全部通过后才发布 PNG。

## Dependencies

`AI-Loading-Protocol.md`, `Automation-Contract.md`, Product Library onboarding docs.

## Related Modules

`../QA/README.md`, `Template-Selection.md`.

## Version

`2.0.0`
