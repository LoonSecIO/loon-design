# One LoonSec. Wherever it shows up.

Brand foundations · v0.3.0

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
| Sun | #EFC15A | Selected navigation and occasional emphasis. Always carries Ink; never light text on Sun |
| Eye | #C6342A | The loon eye, small accents, and display-size headings. Not a body-text color |
| Mist | #A7C3CE | Supporting color on dark surfaces |

Use semantic tokens in interfaces. A brand hue is not automatically a readable text color. Status colors always carry a label or icon; yellow navigation does not mean warning, and a decorative red accent does not mean an error. Never use a success treatment for missing data.

### Readable by rule

The target is WCAG 2.2 Level AA: 4.5:1 for text, 3:1 for large text (24px, or 18.66px bold), control boundaries, and focus indicators. The semantic pairs in `tokens/design.json` are the checked ones; the token tests fail below those ratios in both themes. Any other pairing is unchecked until you measure it.

- **A ground that changes between themes changes its text with it.** Pine lightens in dark mode, so text tuned for Pine on paper fails on Pine in the dark. Either the ground holds still across themes or the text token moves with it. Never assume a pairing survives because the ground is "always dark" or "always yellow"; check that the ground token really is fixed.
- **Sun always carries Ink.** Sun is the same in both themes, so what sits on it is the same in both themes. Light text on Sun is 1.4:1.
- **Eye is an accent, not a text color.** Use it for the loon's eye, display headings on the page ground, focus on light surfaces, and marks. On dark raised surfaces it measures 2.7:1, so there it is decorative only. Body-size red text, and any red that carries meaning on a raised dark surface, uses `accent-red-text`; green uses `accent-green-text`. Both are tuned per theme.
- **De-emphasize with size, weight, and spacing, never by fading.** `text-secondary` is the lightest text color. Nothing carries text below 4.5:1 to look quieter, and nothing inside a dimmed container inherits an opacity that drags its text below AA.
- **Type has a floor.** Monospace labels are 12px or larger; nothing is set below 11px. Small and faded is how labels fail.
- **Focus is the `focus` token**, Eye on light surfaces and Sun on dark ones, drawn as a 3px ring with a 3px offset. Do not restyle it per component.

## Type with a job to do

**Archivo** gives headings and product identity their compact, confident shape. **Public Sans** carries paragraphs and controls. **JetBrains Mono** identifies versions, serials, timestamps, and code. Keep all-caps display type to short labels and marketing headings. Dense application copy uses sentence case.

Self-host web fonts with their license notices. No font binaries are included in this kit. Native interfaces may use the platform font for controls, dynamic text, and accessibility sizing. Use system sans-serif and monospace fallbacks when branded fonts are unavailable.

## Four surfaces, one identity

- **Marketing:** warm paper, expansive Archivo headings, lake illustrations, generous spacing. Publishes an accessibility statement at `/accessibility/` that says what was checked and what was not.
- **LoonInspect:** Lakeside Console. Lake-blue navigation, yellow selection, compact tables, quiet content surfaces. No decorative illustration or brand tagline at the bottom of the sidebar.
- **Vulnerability service:** the same foundations with clear coverage and assessment states. Distinguish “No findings”, “Outside the corpus”, and “Not assessed”.
- **Native agent:** platform controls and behavior, shared assets and semantic colors. Support system appearance and text sizing. Do not force a web sidebar into a native settings panel.

Illustrations belong in introductions, onboarding, and appropriate empty states. Keep them away from data rows and urgent error messages. Avoid looping decorative motion; honor reduced-motion preferences. The working loon, below, is the one exception, and it moves only while work is in flight.

## The loon at work

When LoonSec is busy on someone's behalf, the loon can show it. It lifts its checkered back about the shoulder twice and settles, the way a loon shakes out on open water. The motion files in `assets/motion/` copy the supplied geometry and move whole pieces of it. Nothing is redrawn, and the eye stays red.

| File | Size | Use it for |
| --- | --- | --- |
| `loon-working-small.svg` | 16–31 px | A busy button or control. It uses the simplified loon, like the favicon. |
| `loon-working.svg` | 32–64 px | A panel or table waiting on its first read, beside words that say what is loading. |
| `loon-working-page.svg` | 96–200 px | A whole page that waits, with the words below it. The ripples drift. |
| `loon-diving.svg` | 96–200 px | Long work of unknown length, such as a first sync. The loon dives, swims out of sight, surfaces and shakes off. |
| `lake-working.svg` | Full width | Onboarding and a first run. The lake illustration, with the loon riding the swell. |

Every file except the lake has a `-reversed` twin for dark surfaces. The lake keeps its own palette.

- **Motion means working.** Stop it when the work ends. A finished, empty, failed or stale state never shows a moving loon, and the loon never loops as decoration in a header, footer or hero.
- **Pair it with words.** "Reading the observation ledger…" is the status. To assistive technology the loon is decoration: `alt=""` on an image, `aria-hidden="true"` inline.
- **Let quick answers stay quiet.** Show the loon only once a wait passes about 300 ms, so a fast response never flashes it. The files start at rest and fully visible, so they also work as still images.
- **Honor reduced motion.** Every file stands still under `prefers-reduced-motion: reduce`, and the words carry the state.
- **Keep the play to waiting.** The dive is lighthearted. It never sits beside a failure or a security finding.
- **The mark's rules still apply.** Keep its clear space, and below 32 px use the small loon.

### Known progress: the swimming loon

When the work has a count, show the count. The small loon swims along a waterline to the share that is done, and the numbers stay in words beside it.

```html
<div class="loon-swim" role="progressbar" aria-label="Importing Macs"
     aria-valuemin="0" aria-valuemax="14000" aria-valuenow="5880" style="--done: 0.42">
  <img src="loon-working-small.svg" alt="">
</div>
<p>5,880 of 14,000 Macs imported</p>
```

```css
.loon-swim {
  position: relative;
  height: 28px;
  background:
    linear-gradient(var(--loon-action), var(--loon-action)) 0 100% / calc(var(--done) * 100%) 3px no-repeat,
    linear-gradient(var(--loon-border), var(--loon-border)) 0 100% / 100% 1px no-repeat;
}
.loon-swim img {
  position: absolute;
  bottom: -4px;
  width: 28px;
  left: calc(var(--done) * (100% - 28px));
  transition: left .4s ease-out;
}
@media (prefers-reduced-motion: reduce) { .loon-swim img { transition: none; } }
```

Use the reversed small loon on dark surfaces. When the count completes, show the finished state in its place; the loon doesn't keep beating at 100%.

Regenerate the motion files with `python3 tools/motion.py` after any change to the supplied artwork. The tests hold every path in them to the originals.

Brand illustrations are authored and reproducible from source: the lake scene is hand-drawn vector art, and the background tiles and social card are rendered by committed code with a fixed seed. Nothing in the kit is AI-generated. If AI imagery is ever used in a Field Note or a product screen, the caption says so.

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
