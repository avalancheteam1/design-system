# Source provenance and audit facts

## Authority

- Source presentation: `Team1 Overview.pptx`.
- Source SHA-256: `8af6803b1342e8c40ebc41fc5a382d21816c33bd329223c393731e1ef35ef4e0`.
- Inspection method: read-only review of presentation XML, relationships, theme/master/layout data, embedded media, and rendered slides.
- The source file was not edited during extraction.

## Document structure

- 20 source slides, one slide master, 19 slide layouts.
- 16:9 geometry: 10 × 5.625 inches, equivalent to 960 × 540 px at the inspection scale.
- All visible source slides use dark layouts. Light variants exist in the file but were unused.
- The visible grid/glow/background is an opaque full-slide PNG. The master’s fallback fill is white.
- The recurring footer/chrome is inherited from layouts, not independently rebuilt on each slide.

## Source typography

The presentation contains subset embedded data for Inter, Inter SemiBold, Kanit Medium, and Helvetica Neue. Visible narrative runs use Kanit/Inter in the early overview section and Helvetica Neue in later editorial/case-study slides. Theme/default Arial is not evidence of a visible brand face.

Because the font data is subsetted, it may not cover every new character or language. New work must verify installed fonts and final rendering.

## Asset handling

Bundled assets were extracted from the source presentation and renamed descriptively. `assets/asset-index.json` records each renamed path, original media filename, category, and use warning. Authentic marks and raster backgrounds must not be recreated.

The source’s legacy QR image and a QR-bearing legacy poster were intentionally not included. Their destination and current approval were not established.

## Time-sensitive content

Metrics, chapter tiles, program names, application links, social handles, partners, and calls to action reflect the source at an unknown historical moment. Their presence is evidence of visual treatment, not proof that the claim is current. Verify live status before publication.
