# Hogwarts Castle 71043 — version 0 reconstruction

## Source and scope

The supplied booklet PDFs are treated as segments of the 71043 instructions; filename digits are not interpreted as printed page or step numbers. Image review of `6607901-50.pdf`, booklet 22, maps PDF pp.6–14 to printed pp.10–18 and steps 1–18. Steps 8–18 appear on printed pp.13–18. Circular side builds shown earlier in this booklet remain a separate unresolved assembly. Minifigures are excluded.

The 64179 frame geometry and recursive dependencies came from the official `ldraw-org/official-library` repository at commit `894bbba5e696b1554800d8e45134c57163dba905`. Its header identifies a Technic Beam 7 x 5 with Open Center 5 x 3, CC BY 4.0. Source, license, dependency paths, and hashes are recorded in `assets/policy.md`. No GoBricks offer or SKU is asserted.

## Written geometry

The root `hogwarts-frame.ldr` contains 25 physical references for steps 1–7. The 64179 frame at `[-40,20,0]` aligns four local through-hole centers `(40,0,z)`, z=−60,−20,20,60, with the four 2780 pins from step1. Center and axis residuals are 0 LDU. The nominal pin spans both adjacent 20-LDU layers; real fit and friction are untested.

Root `part-0006` (32278, step2) currently has an end-face datum against the frame side, but its first hole is 9 LDU beyond the frame side-hole center. The step3 retaining joint remains unverified. `part-0012` and three tan supports form a provisional underside contact at y=38; the overhang and exact step5 support pattern remain unverified. Steps6–7 are candidate placements and remain subject to correction from later attachment evidence.

Printed p.13 step8 is now a partial local assembly in `hogwarts-step8.ldr`. It contains one 64179 frame, two purple 2420 corner plates, one 32278 rail and two 2780 pins. The rail is rotated so its local +Y hole axis maps to +X and its local Z hole centers map to the frame side row. At z=−60 and +60, both pin axes and centers match the 64179 and 32278 holes; the pin length nominally spans both adjoining parts. These contacts are geometry-derived and not physically tested. The callout also shows one lime 2x2 axle-hole plate, one gray 1x2 side-connector and two gray 2x2 side-pin blocks; those three gray blocks and the center plate have not been placed because their precise shape/seat is unresolved. This module is partial and not root reachable.

Printed p.17 steps14–15 are a seven-reference local module (`hogwarts-step14.ldr`): a 32524 beam with four pins, a 64179 frame aligned to those pins and a 32278 rail. The beam/frame pin contacts align. The rail end datum is provisional; its first hole differs from the frame side-hole center by 9 LDU. The module is not root reachable. Printed p.18 step17 is a local 64179 frame with four 2780 pins at its side holes (`hogwarts-step17.ldr`); the pin contacts align, but no root placement is claimed without the step16 mating relation.

Steps9–13 and16 have been image-reviewed but are not yet reconstructed. Their callouts/sequence show additional beams and wall/base details, plus four step16 pins and two side-pin blocks. Step18 now has a tentative local `hogwarts-step18.ldr` with candidate 32140 and two 2780 pins. The candidate DAT has +Y holes at the two selected pin centers, but the callout has no element number; part identity and exact selected holes remain unconfirmed. This module is not root reachable. Model state keeps local definitions separate from root placed-piece counts.

## Validation status

- MPD physical Type-1 references, unique IDs, per-instance transforms, and state records are checked separately for root and unplaced local modules.
- Root placements: 25. Local partial modules: 21 references total. Unplaced definitions are not counted as assembled root pieces.
- 64179 source asset hashes and recursive dependencies are recorded in the shared asset manifest.
- The repository validator reaches the commercial catalog lookup, then stops on empty `gobricks_id` (`KeyError: ''`). This is a catalog-mapping failure, not a geometry pass. Structural/shape checks continue independently; no placeholder offer data is used.
