# Product Lock

本规则优先级高于所有美学要求。

## Purpose

保护 Product Library 中真实产品的像素、结构、比例和透视。

## Usage

每张图在组合前记录源路径和 SHA-256，组合后逐项执行 `../QA/ProductLock-QA.md`。

## Must Preserve

- 外形与比例
- 摄像头孔位
- 按键、接口、扬声器孔
- 扣子、绑带、支架及连接结构
- 边角弧度与厚度
- 透明区域与材质边界
- 纹理、缝线和真实颜色
- 原始透视关系

## Allowed Changes

- 去除原图背景
- 清理非产品灰尘或压缩噪点
- 等比例缩放
- 不改变结构的整体旋转和位置调整
- 添加背景、自然阴影、文字和图标

## Forbidden

- 生成式重绘产品
- 补画不存在的结构
- 为适配构图而拉伸、压扁或液化
- 改变孔位方向、扣子数量或支架形状
- 擅自把产品改成另一种颜色
- 用相似产品替代真实产品

## Pixel Integrity

只要输入素材清晰，产品主体应尽可能保持像素级一致。无法确定的结构不得推断，必须保留原图或请求补充素材。

## Dependencies

HAMI Product Library canonical assets and metadata.

## Related Modules

`../Components/ProductCard.md`, `../QA/ProductLock-QA.md`, all templates.

## Version

`2.0.0`
