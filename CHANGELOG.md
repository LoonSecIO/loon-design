# Changelog

## 0.3.0

- Add “Readable by rule” to the brand guide: WCAG 2.2 AA as the target, grounds that change between themes change their text with them, Sun always carries Ink, Eye is an accent not a text colour, no fading below AA, a type-size floor, and the focus token.
- Add `accent-red-text` and `accent-green-text` per theme for body-size red and green text; `eye` and `pine-light` stay accents.
- Extend the foundation tests to the new tokens, to Ink on Sun, and to Eye as a 3:1 accent on the page ground.
- State that brand illustrations are authored and reproducible, and that AI imagery would be captioned.
- Prompted by the first report against loonsec.io: the dark-mode call-to-action rendered near-white on Sun at 1.4:1 (LoonMarketing #29, #30, #31).

## 0.2.0

- Add the working loon: small, inline, page, diving and lake motion files, with reversed twins, generated from the supplied artwork by `tools/motion.py`.
- Add "The loon at work" to the brand guide: when the loon may move, how it pairs with words, reduced motion, and the swimming-loon progress pattern.
- Tests hold every motion file to the supplied geometry and eye, require a reduced-motion rule, and regenerate the files byte for byte.

## 0.1.0

- Establish brand guide, integration examples, interface conventions, shared color/spacing/type tokens, and downloadable assets.
- Record Lakeside Console as LoonInspect's selected direction, without decorative sidebar footer branding.
- Provide web CSS generated from platform-neutral tokens and a reproducible source bundle.
- Existing product implementations are not automatically migrated by this release.
