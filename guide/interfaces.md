# Interface foundations

These are shared rules for implementation, not a shipped component library.

## Components to establish first

- Buttons: one primary action per task, visible labels, explicit disabled/busy state; destructive actions say what they delete.
- Forms: persistent labels, help beside the relevant field, errors that preserve entered values. No placeholder-only labels.
- Navigation: visible active location, keyboard operation, responsive disclosure. Preserve permissions and all existing destinations.
- Tables: semantic headers, readable row density, tabular numerals, clear sorting, and horizontal scroll confined to the table on narrow screens. Unknown values use a labeled unknown state, never zero.
- Status: loading, empty, failed, stale, and complete are separate states. Color is supplemental. Timestamps state their timezone.
- Dialogs: labeled purpose, focus containment, Escape where safe, and focus returned to the trigger.

## Accessibility and themes

Target WCAG 2.2 AA text contrast (4.5:1 normal text, 3:1 large text), visible focus, and 3:1 contrast for essential control boundaries. The token tests check the supplied foreground/background pairs; they do not certify an entire interface. Verify composed screens, keyboard flow, zoom, both themes, reduced motion, and touch targets. Aim for 44px effective touch targets without forcing desktop table rows to that height.

Two failures that have already happened, so they are rules: a surface token that changes between themes must change its text tokens with it, and a container must never be dimmed with opacity, which drags every colour inside it below AA. See “Readable by rule” in the brand guide.

On the web, apply generated variables with `[data-loon-theme="dark"]` for an explicit dark selection. The host controls system-preference resolution. Use `--loon-text` on `--loon-surface`, not arbitrary brand colors.

For a native agent, map the JSON semantic names to light/dark color assets. Use system typography, native buttons, accessibility labels, high-contrast settings, and the platform's focus and permission patterns. Example: `themes.dark.text` becomes the dark appearance of the agent's primary text color. CSS is an output, not the cross-platform contract.

## Verification and rollout

Start with tokens and the shared shell; adopt forms and tables where they are already used. Test existing search, filtering, pagination, authorization, and navigation after presentation changes. Keep the inventory-summary provider/consent behavior intact. Preserve the distinction between vulnerability publication age and first detection in a fleet.

The selected LoonInspect direction is B, Lakeside Console. Its implementation is coordinated separately with inventory summaries and the vulnerability-table work. A design release does not change those features or claim they have shipped.
