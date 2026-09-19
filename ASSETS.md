# Asset provenance

- `assets/logos/loon-mark.svg`: existing LoonInspect `frontend/public/loon.svg`; geometry preserved.
- `assets/logos/loon-mark-reversed.svg`: same geometry; dark ink replaced with paper (#F6F2E7), red eye preserved. Use on lake-blue or similarly dark backgrounds.
- `assets/logos/loon-favicon.svg`: existing LoonInspect simplified favicon. Deliberately different from the full hexagonal mark at small sizes.
- `assets/logos/loon-mark.png`: existing LoonMarketing `static/img/loon-mark.png`.
- `assets/illustrations/lake-scene.svg`: existing LoonMarketing homepage illustration extracted without changing geometry.

The existing vector and raster sources have small palette differences. They are recorded as supplied; this release does not silently redraw or recolor the original files. Future normalization requires visual review.

Source repositories: https://github.com/LoonSecIO/LoonInspect and https://github.com/LoonSecIO/LoonMarketing. Exact source revisions are recorded in `sources.json`.

Typography: Archivo (headings), Public Sans (body), JetBrains Mono (identifiers). Fonts are not bundled here. Consumers must obtain the fonts with their licenses, or use the system fallbacks documented in the guide. Existing marketing fonts continue to be self-hosted by that site.
