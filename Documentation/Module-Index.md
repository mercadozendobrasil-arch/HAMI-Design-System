# Module Index

## Purpose

提供人类与 AI 都可遍历的模块入口。

## Usage

| Order | Module | Entry | Depends on |
| ---: | --- | --- | --- |
| 1 | Root contract | `../README.md`, `../CODEX.md` | — |
| 2 | Brand | `../Brand/README.md` | Root contract |
| 3 | Tokens | `../Tokens/README.md` | Brand |
| 4 | Components | `../Components/README.md` | Brand, Tokens |
| 5 | Templates | `../Templates/README.md` | Components, Rules, Tokens |
| 6 | Rules | `../Rules/README.md` | Brand, Tokens |
| 7 | QA | `../QA/README.md` | Rules, Templates |
| 8 | Product Library | external repository manifest | All preceding modules |
| Runtime | Prompts | `../Prompts/PromptContract.md` | Loaded system |
| Runtime | Assets | `../Assets/README.md` | Brand, Tokens |

Machine-readable entry: `../design-system.manifest.json`.

## Dependencies

All governed HAMI modules.

## Related Modules

`AI-Loading-Protocol.md`, `Repository-Architecture.md`.

## Version

`2.0.0`
