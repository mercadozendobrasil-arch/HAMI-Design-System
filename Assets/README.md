# Assets

HAMI 的受控品牌资产。所有文件必须通过版本控制引用，禁止由生成模型重绘、补全或替换。

## Purpose
集中保存经验证的品牌源资产与统一图标。

## Usage
按下方目录和对应品牌文档引用；不得复制到 Product Library。

```text
Assets/
├── logo/          经验证的 HAMI Logo 源文件
├── icons/         统一 64×64 outline SVG 图标
├── backgrounds/   背景实现说明；颜色取自 Tokens
└── products/      产品透明 PNG（产品正式入库后使用）
```

## 使用规则

- Logo 只能使用 `logo/` 中的原始文件，并遵循 `Brand/LogoSystem.md`。
- 图标只能使用 `icons/` 中的 SVG，并遵循 `Brand/IconSystem.md`。
- 背景必须由 `Tokens/background.tokens.json` 定义，不保存随机生成的背景图。
- 产品图片的唯一正式来源是 `HAMI-Product-Library`；本目录不复制或修改产品像素。

## Dependencies / Related Modules / Version
Depends on `../Brand/` and `../Tokens/`; related to components and templates. Version `2.0.0`.
