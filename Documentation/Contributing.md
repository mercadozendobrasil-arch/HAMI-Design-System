# Contributing

## Purpose

定义不破坏 HAMI 单一事实源的变更流程。

## Usage

1. 先读取强制加载序列并确认变更归属仓库。
2. 修改前验证当前状态；不得覆盖无关用户变更。
3. 复用既有 token 和组件；不得在模板中硬编码新值。
4. 若修改视觉契约，同步依赖文档、schema、QA 与版本。
5. 运行 `python -m unittest discover -s QA -p "test_*.py" -v`、`python QA/validate_repository.py . ../HAMI-Product-Library` 和 `git diff --check`。
6. 每个独立模块单独提交，使用 `feat(module)` 或 `fix(module)`。

Product pixels、SKU facts 和产品备注只能提交到 Product Library。未经批准不得替换 Logo 或产品源图。

## Dependencies

`AI-Loading-Protocol.md`, `Versioning.md`, `Release-Checklist.md`.

## Related Modules

`../QA/README.md`, `Repository-Architecture.md`.

## Version

`2.0.0`
