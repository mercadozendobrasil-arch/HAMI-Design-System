# Background Assets

HAMI 的银灰背景是确定性的设计 token，不使用随机位图。

## Purpose
规定背景只由受控 token 渲染。

## Usage
解析 background token 的颜色、角度和停靠点，在 800×800 RGB canvas 上确定性绘制。

- Source: `../../Tokens/background.tokens.json`
- Canvas: 800×800 px
- Rendering: 按 token 中定义的颜色、角度和停靠点生成
- Prohibited: 随机纹理、噪点、场景化背景、未经定义的渐变

## Dependencies / Related Modules / Version
Depends on `../../Tokens/background.tokens.json`; related to all templates and Final QA. Version `2.0.0`.
