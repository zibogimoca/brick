# Notre-Dame de Paris v0

## Reconstruction status

The v0 model is in progress in [`notre-dame-v0.mpd`](notre-dame-v0.mpd). Steps 1–22 from the first uploaded booklet are represented as a mixture of dimensioned base work and diagram-derived drafts. Later pages through printed page 37 (step 44) were inspected to constrain the choir arc. The remaining pages and the other five booklets are not yet reconstructed.

Current project policy excludes minifigures, signs and nameplates from modeling and manual-reconstruction scope. No such items have been included in the current MPD. This exclusion does not apply to the building, base, structural connections or other ornament.

GoBricks product correspondence and sales status remain unverified. No product IDs or SKUs have been inferred. The automatic `tools/validate_model.py` check stops at its required `gobricks_id` field; this is a product-metadata failure. It is not reported as a geometry pass. Physical clutch/fit remains unverified.

## Geometry evidence and provisional placements

- Step 20 (printed page 23) callout counts are white 5/5/8 and black 5/5/10. Five complementary 42862/48165 pairs per color represent the two small wedge silhouettes. The broad silhouettes map to eight white 43710 and ten black 43711 4x2 double wedges. Later step 44 shows 13 repeated three-stud modules on the choir semicircle: 13 × 60 LDU over a half-circle implies about 248 LDU radius, supporting the step-20 outer radius of 250 LDU. The outer and inner arcs are centered provisionally at `(0, 420)` with radii 250 and 200 LDU. Their endpoints and exact base contact remain provisional.
- Backward placement from the later choir view moves the step-20 arc center 200 LDU east of the 4x6 mosaic center `(-200, 420)`. Step 18's mosaic right edge at `x=-80` meets the step-14 69729 tile field's left edge at `x=-80`; the choir arc then sits beside the shared floor edge. The tile-field z boundary and wall contact remain provisional.
- Step 21 (printed page 24) maps to two 87544 reinforced 1x2x3 panels, one 3021 2x3 plate and one 3023b 1x2 plate. The panels occupy successive one-stud tangent rows under the 2x3 plate; the 1x2 plate sits on its exposed third row. Positions use y levels `-88`, `-96`, `-104`. Relative sequencing follows the exploded diagram; the global anchor and physical clutch remain provisional.
- Step 22 (printed page 25) maps three each of 3021, 15573 (1x2 plate with grooved center stud) and 18674 (round 2x2 plate with center stud). Three stacks at radius 200 LDU and angles -60/0/+60 degrees are symmetric diagram-derived drafts, with y levels `-16`, `-24`, `-32`. Exact offsets and physical clutch remain unverified.

## Asset and verification record

Official LDraw parts 43710, 43711, 42862, 48165, 87544 and 18674 are shared under the licenses retained in `assets/policy.md`; 87544 and 18674 dependencies were resolved from the official 2026-09 `complete.zip` archive (SHA-256 `023083918da2d3697c794fb4267975509584f3611b993095874206a803fa610f`). Existing assets 3021, 3023b and 15573 were reused. Asset manifest file hashes were verified after registration. No GoBricks dictionary mapping was added because no product correspondence was verified.

Independent model checks cover instance/reference count and ID uniqueness, referenced part presence, finite coordinates, right-handed orthonormal rotations, per-step piece counts, and the step-20 arc radii/chord pitches. Step 21 panel/cap heights and stud-row spacing and step 22 stack order were checked separately. The full contact graph, physical fit and full-manual coverage remain in progress.
