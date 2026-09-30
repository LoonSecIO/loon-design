# LoonSec design foundations

The shared brand source for LoonSec's marketing site, LoonInspect, LoonVD, and future native agent interfaces.

Version **0.1.0** established the existing marketing identity and the selected Lakeside Console application direction; **0.2.0** adds the working loon, the one sanctioned motion of the mark; **0.3.0** adds the readability rules and per-theme accent text tokens. It is a foundation, not a complete component library. Product features and availability remain documented by their respective repositories.

- [Brand guide](guide/brand.md): identity, assets, typography, voice, integration examples.
- [Interface patterns](guide/interfaces.md): web and native behavior, states, accessibility.
- [Tokens](tokens/design.json): platform-neutral values; generated CSS is in `dist/` after building.
- [Assets](assets/): existing vector mark, reverse variant, PNG, favicon, lake illustration, and the working loon's motion files (`assets/motion/`).
- [Usage terms](BRAND-USAGE.md) and [asset provenance](ASSETS.md).

## Build and validate

Python 3.12+, no dependencies:

```sh
python3 tools/build.py
python3 -m unittest discover -s tests -v
```

The build produces `dist/tokens.css` and `dist/loon-design-0.3.0.zip`. `python3 tools/motion.py` regenerates `assets/motion/` from the supplied artwork. JSON is the source of truth; do not edit generated CSS. Release bundles contain source guides, tokens, assets, and usage terms. Tag releases after reviewing the output.

## Consumers

Marketing publishes the guide at `/brand/` from a pinned revision of this repository. Its sync tool copies a reviewed checkout into the site; builds and visitors need no GitHub access. Do not hand-edit the vendored guide or assets. Updating the pin is a marketing pull request.

Web products can consume generated CSS; native agents should map semantic JSON tokens to native dynamic colors and use platform controls. No React dependency is required. Pin a release or commit rather than pulling `main` at build time. Adopting these foundations in existing products is separate work.

## Contributions

Propose changes with a pull request, rationale, screenshots in both themes, and applicable contrast/keyboard checks. Kyle owns brand decisions; an independent reviewer approves changes before merge. Breaking token removals need a major version and migration notes. Additive changes use a minor version; corrections use a patch version. See [CHANGELOG](CHANGELOG.md).

Code, tokens, and guide text use the MIT license. Logos and illustrations have separate terms in BRAND-USAGE.md. Fonts are named but not redistributed in this release.
