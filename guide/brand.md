# One LoonSec. Wherever it shows up.

Brand foundations · v0.1.0

LoonSec is built in Minnesota for people who manage Apple devices and have to answer for them. The identity takes its character from the lake, the loon, and clear, practical language. Use this guide when building an integration, writing about a product, or designing a new surface.

## The mark

Use the supplied artwork. The hexagonal loon is the full mark; the simplified loon is for favicons and other very small contexts. Use the original on light surfaces and the reversed mark on dark ones. Keep the red eye.

Allow clear space of at least one quarter of the mark's height on every side. Use the full mark at 32 CSS pixels or larger. Below that, use the supplied favicon and check legibility at the actual size. These are v1 working minimums, not permission to stretch the art.

Do not redraw, distort, rotate, add shadows, place the mark inside another badge, or use a CSS inversion filter. Do not place it on a busy illustration. The supplied reversed asset changes the ink while preserving the eye.

Pair the mark with the exact product name in text. A combined graphic must use reviewed artwork; do not invent a new product symbol. LoonSec is the company; LoonInspect and LoonVD are product names. Describe the future agent by its approved name when that name and availability are settled.

## A palette from the lakeshore

| Color | Value | Use |
| --- | --- | --- |
| Paper | #F6F2E7 | Warm light background |
| Ink | #12212E | Primary light-theme text |
| Lake | #173A52 | Navigation and strong dark surfaces |
| Deep lake | #0C1E2C | Dark-theme background |
| Pine | #1F4A3A | Actions and restrained accents |
| Sun | #EFC15A | Selected navigation and occasional emphasis |
| Eye | #C6342A | The loon eye and small brand accents |
| Mist | #A7C3CE | Supporting color on dark surfaces |

Use semantic tokens in interfaces. A brand hue is not automatically a readable text color. Status colors always carry a label or icon; yellow navigation does not mean warning, and a decorative red accent does not mean an error. Never use a success treatment for missing data.

## Type with a job to do

**Archivo** gives headings and product identity their compact, confident shape. **Public Sans** carries paragraphs and controls. **JetBrains Mono** identifies versions, serials, timestamps, and code. Keep all-caps display type to short labels and marketing headings. Dense application copy uses sentence case.

Self-host web fonts with their license notices. No font binaries are included in this kit. Native interfaces may use the platform font for controls, dynamic text, and accessibility sizing. Use system sans-serif and monospace fallbacks when branded fonts are unavailable.

## Four surfaces, one identity

- **Marketing:** warm paper, expansive Archivo headings, lake illustrations, generous spacing.
- **LoonInspect:** Lakeside Console. Lake-blue navigation, yellow selection, compact tables, quiet content surfaces. No decorative illustration or brand tagline at the bottom of the sidebar.
- **Vulnerability service:** the same foundations with clear coverage and assessment states. Distinguish “No findings”, “Outside the corpus”, and “Not assessed”.
- **Native agent:** platform controls and behavior, shared assets and semantic colors. Support system appearance and text sizing. Do not force a web sidebar into a native settings panel.

Illustrations belong in introductions, onboarding, and appropriate empty states. Keep them away from data rows and urgent error messages. Avoid looping decorative motion; honor reduced-motion preferences.

## Sound like a useful colleague

Lead with what happened, its scope, and the next useful step. Be direct and approachable. Do not promise certainty beyond the evidence. Keep humor out of failures and security findings.

| Prefer | Avoid |
| --- | --- |
| “No findings in the current corpus.” | “Your fleet is safe.” |
| “Could not load inventory. Try again.” | “Oops! Something went wrong.” |
| “Inventory as of 14:32 UTC.” | “Real-time fleet intelligence.” |
| “Connect to LoonInspect.” | “Activate your AI-powered security journey.” |

AI-generated prose is advisory. Show its source and time when available; deterministic evidence remains authoritative. Never invent a reassuring status because a request has not completed.

## Building an integration

**Directory tile:** use the supplied mark, the name “LoonInspect”, and a factual sentence such as “Send LoonInspect events to Example SIEM.” Keep the integration author's name visible. Do not imply certification.

**Connection screen:** title it “Connect to LoonInspect”. Use native labels and controls, explain required access, and keep the host application's navigation. Branding identifies the service; it does not replace the host's interaction patterns.

**Two brands together:** keep each logo intact, give each its required clear space, and separate them with neutral space or a rule. Use wording such as “Example integration for LoonInspect”. Do not fuse marks or use “official partner” without permission.

**Downloads:** choose SVG for interfaces and scalable layouts, PNG where vector files are unsupported, and the reversed SVG on dark surfaces. Read the included usage terms. Link to the version used so later maintainers can reproduce it.

## Keeping it consistent

The public source is [LoonSecIO/loon-design](https://github.com/LoonSecIO/loon-design). Update it through a reviewed pull request. Products pin a version and adopt changes deliberately. The website publishes this guide from that same source.

The code, tokens, and guide text are MIT-licensed. Logos, illustrations, and names follow the separate [brand-use terms](https://github.com/LoonSecIO/loon-design/blob/main/BRAND-USAGE.md). For other uses, contact [sales@loonsec.io](mailto:sales@loonsec.io).
