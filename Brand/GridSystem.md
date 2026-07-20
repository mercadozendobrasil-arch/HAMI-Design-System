# Grid System

> Purpose: define the 800×800 spatial system.  
> Usage: consume coordinates through layout and component tokens.  
> Dependencies: `BrandIdentity.md`.  
> Related: `../Rules/LayoutRules.md`, `../Templates/`.  
> Version: `2.0.0`.

## Base Canvas

- 800 × 800 px
- 8 px 基础网格
- 安全边距：40 px
- 核心内容不得进入 32 px 外沿区域

## Cover Grid

- 左侧信息区：X 40–310 px
- 右侧产品区：X 300–780 px
- Logo 起点：X 40 px / Y 36 px
- 标题起点：X 40 px / Y 175–210 px
- 卖点区：X 40–285 px / Y 390–690 px
- 产品视觉中心：X 565 px / Y 420 px

## Spacing Tokens

`8 / 16 / 24 / 32 / 40 / 56 / 72 px`

不得使用无规律间距。相邻信息组至少间隔 24 px。

## Alignment

- 左侧文案统一左对齐。
- 图标与标签按同一垂直轴对齐。
- 产品可以越过产品区边界，但不得裁切关键结构。
- 产品底部应保持统一视觉基线。
