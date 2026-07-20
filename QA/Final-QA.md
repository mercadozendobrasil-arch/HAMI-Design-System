# Final QA

## Automated gate

Run `python QA/validate.py <manifest.json>` and require exit code 0.

## Human gate

- [ ] ProductLock-QA passes against source pixels.
- [ ] Template-specific QA passes.
- [ ] Montserrat, silver gradient, outline icons, Logo and shadow are consistent.
- [ ] Brazilian Portuguese is correct and every text block is within two lines.
- [ ] No misleading claim, item, model, certification or third-party Logo appears.
- [ ] Final output is a clean 800×800 RGB PNG suitable for Shopee Official Store.

Any failed item rejects export. Dependencies: all QA modules. Version `2.0.0`.
