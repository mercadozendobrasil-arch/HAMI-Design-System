# Product Lock QA

## Purpose
Prove that rendered product pixels preserve the canonical source.

## Usage
Compare the output against the recorded source asset and hash for every image.

- [ ] Source path and SHA-256 are recorded.
- [ ] Product pixels are not generated or reconstructed.
- [ ] Scale is uniform and aspect ratio unchanged.
- [ ] Camera holes, ports, buttons, speakers, straps, stands, corners, materials and perspective match the source.
- [ ] No key structure is cropped, covered or inferred.

Any failure rejects export.

## Dependencies / Related Modules / Version
Depends on `../Rules/ProductLock.md` and Product Library hashes. Related to Final-QA. Version `2.0.0`.
