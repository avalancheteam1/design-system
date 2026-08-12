# Digital and web

The conventions here are the current frontend profile. They are implementation rules for digital products, not universal print or presentation tokens.

## Foundation

- Dark is the default: background `#000000`, surface `#161617`, nested surface `#1A1B1C`, hover surface `#2A2B2C`, border `#2A2D31`.
- Dark text roles: white/high contrast, `#E5E7EB` secondary, `#9CA3AF` tertiary.
- Light mode: background `#FFFFFF`, surface `#F5F5F9`, variant `#E8E9EC`, hover/border `#D8D9DC`, `#161617` secondary, `#6C757D` tertiary.
- Ava Red `#E6212F` is for brand emphasis and primary interaction. Use `#DC2626` for errors, `#16A34A` for success, `#F59E0B` for warning, and `#2563EB` for information.
- The official brand accents are Ava Blue `#3055B3` and Secondary Blue `#058AFF`. They are accents, not substitutes for semantic status colors.

Use the complete spacing scale—2, 4, 6, 8, 12, 14, 16, 20, 24, 32, 40, 48, 64, and 80 px—rather than inventing near-duplicates. Use standard radii 4, 6, 8, 10, and 12 px; use 16 px for project-logo containers and 9999 px for pills/badges. Use z-index levels 0 through 90 in steps of 10 and the packaged motion tokens. Build mobile-first at 640, 768, 1024, 1280, and 1536 px; cap the main container at 1280 px with 24 px desktop and 16 px mobile padding.

## Identity mapping

An implementation handoff must map authentic indexed files to every live context: a dark-background wordmark, light-background wordmark, approved monochrome fallback, compact symbol, square app/social icon, PFP, and the complete favicon set. Do not derive one variant from another. Keep `Team1` at sentence starts, in titles, and in proper-name treatments; `team1` is acceptable in flowing copy; never write `TEAM1`.

## Components and interaction

- Preserve a visible text hierarchy with Kanit Medium 500 headings and Kanit Light 300 body. Aeonik Regular or Medium is a sparse secondary option, not a site-wide default. Do not substitute a decorative display face for UI copy.
- Use real buttons for actions and links for navigation. Provide hover, active, disabled, loading, validation, empty, and error states.
- Keep pointer targets at least 44 × 44 px with at least 8 px separation where practical.
- Show a visible keyboard focus indicator on every interactive control. Never remove the browser outline without an equally visible replacement.
- Standard transitions are 150, 200, and 300 ms. Entrance motion may use 400 ms `cubic-bezier(0.16, 1, 0.3, 1)` with a 20 px fade-up and 80 ms stagger.
- Honor `prefers-reduced-motion`; remove non-essential movement rather than merely speeding it up.
- Use current favicons and social preview assets. Keep logo files intrinsic and unmodified.

## Accessibility

- Use semantic headings, landmarks, lists, labels, and controls with a logical reading and tab order.
- Supply useful alt text for informative images and empty alt text for decoration. Captions and transcripts are required where the medium needs them.
- Test contrast for the actual size, weight, state, and background. In particular, never assume red text on a dark surface passes merely because both colors are approved. Brand approval does not imply accessible contrast.
- Do not communicate status through color alone. Associate errors with their fields and expose status changes to assistive technology.
- Test keyboard-only use, zoom/reflow, small screens, slow/loading states, and a screen reader before launch.
- Run responsive QA on the deployed candidate in supported real desktop and mobile browsers/devices; viewport emulation is useful but does not replace at least one physical mobile-device check.

## Project and launch governance

Before implementation, obtain project approval and name the content, design, technical, and operational owners. Team1 web properties should use the approved Team1 network domain pattern, shared navigation/header, responsive behavior, current favicon set, SEO metadata, and a 1200 × 630 px Open Graph image.

The launch path is: content walkthrough → design review → Team1 review skill when available → automated/source checks → final code review → go-live approval. Record the repository, deployment owner, analytics choice, data collection, and privacy implications. Never expose private operations data, internal contacts, credentials, or unapproved tracking in a public artifact.
