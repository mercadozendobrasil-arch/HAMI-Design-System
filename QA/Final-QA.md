# Final QA

## Purpose
Provide the final export gate after all template-specific checks.

## Usage
Run the automated gate, then complete the human gate against the rendered PNG and source product.

## Automated gate

Run `python QA/validate.py <manifest.json>` and require exit code 0.

## Human gate

- [ ] ProductLock-QA passes against source pixels.
- [ ] Template-specific QA passes.
- [ ] Montserrat, silver gradient, outline icons, Logo and shadow are consistent.
- [ ] Brazilian Portuguese is correct and every text block is within two lines.
- [ ] No misleading claim, item, model, certification or third-party Logo appears.
- [ ] Final output is a clean 800×800 RGB PNG suitable for Shopee Official Store.

Any failed item rejects export.

## Dependencies / Related Modules / Version
All QA modules and the image manifest schema. Related to every template and Product Lock. Version `2.0.0`.
