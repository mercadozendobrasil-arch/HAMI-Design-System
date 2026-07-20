# Template Selection

## Purpose

将用户意图映射到唯一永久模板。

## Usage

| Intent | Template |
| --- | --- |
| Cover, hero, 封面, 主图 | `Template001-Cover` |
| Selling points, benefícios, 卖点 | `Template002-SellingPoints` |
| Stand, suporte, 支架 | `Template003-Stand` |
| Material, construção, 材质 | `Template004-Material` |
| Protection, proteção, 防护 | `Template005-Protection` |
| Details, detalhes, 细节 | `Template006-Details` |
| Colors, cores, 颜色 | `Template007-Colors` |
| Compatibility, compatibilidade, 兼容性 | `Template008-Compatibility` |
| Package, conteúdo, 包装清单 | `Template009-Package` |

如果命令明确给出输出类型，不得改用其他模板。一个输出对应一个模板；组合图必须拆成明确页面，不得创造 Template010。

## Dependencies

`../Templates/`, `../Prompts/PromptContract.md`.

## Related Modules

`Automation-Contract.md`, `../QA/README.md`.

## Version

`2.0.0`
