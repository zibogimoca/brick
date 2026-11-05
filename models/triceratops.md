# 트리케라톱스 설계·개선 기록

## 재구성 근거와 진행

`models/triceratops-v0.mpd` is a manual-based reconstruction. Earlier layouts are not used as evidence when part identity changes; affected transforms are recalculated from the current official LDraw DAT geometry. Latest policy and shared know-how from `origin/main` commit `8ca6bf3` were incorporated, including the 77985 reviewed-step candidates.

- Printed steps 4–6 are a display-base rock formation, separate from the fossil skull built much later. Step 4 uses the called 18980 rounded 2×6 plate. Its DAT stud grid projects onto three perimeter positions in the 60474 project platform proxy; because that proxy omits the underside locking geometry, only grid and layer registration are established.
- Step 5 uses 24316 stop axles, 32064a cross-axlehole bricks and 3713 bushes. The replaced 4519/3700 coordinate assumptions are not carried forward; see the instance notes for the DAT-based refit and remaining insertion uncertainty.
- Step 10 is the display plant branch (68211 stem, 4367 white flower, 22667 dark-azure fruit candidate). It is not fossil-skull material. Its local ornament module remains separate from the skull.
- Step 249 is a local sandwich core: two 6541 bricks between the 3023b layers. The 6141 stud bases now coincide with the outward +Z side-hole centers and their studs point into the holes. The 25264 outer cap mating remains provisional.
- Step 278 is rebuilt from 32056, 92907 and two 61332 parts. Their internal axes and pin spans are recalculated below. Step 279’s visible docking sequence does not identify the compatible skull-side male port or provide a final numeric transform, so only that external transform is withheld.
- Independent later body, skull and base fragments continue as local candidate assemblies. Their unconnected definitions are not counted as pieces attached to the final root.

## 검사 결과와 한계

Current state records 161 physical instance IDs across the MPD hierarchy. Structural checks compare every ID, part, color, composed transform and quantity with embedded state. SKU mapping remains separate from source-part identity. LDraw DAT axis/center tests are distinct from closed-solid Boolean or open-surface collision tests; neither collision method is treated as valid when its mesh assumptions fail.

## 장식·범위 확인 항목

- 공식 LDraw ZIP에서 `24855.dat` (Plant Flower Stem with Bar and Hole)와 `37695.dat` (Plant Stem with 3 Leaves with Bar and Pin Holes), 그리고 재귀 참조 primitive/subpart 28개를 확보했다. 내부 참조는 `parts/subparts/`와 `primitives/` 경로 규칙으로 변환했고 CC BY 4.0 및 저자 정보를 보존했다. 원본 부품 번호·명칭은 도해의 초록 줄기/파란 잎 형상과 대체로 맞지만, 설명서 특정 색상과의 GoBricks 대응은 미확인이다.
- 이 기록의 앞선 장식 미작성 문장은 후속 “장식 서브모델 작업” 항목에서 갱신되었다.
- 표지판은 사용자 지시에 따라 범위에서 제외한다.

## 범위 제외 지시

사용자 지시에 따라 미니피겨 및 표지판/명판은 모델 구성에서 제외한다. 13쪽 완성 장면에 보이는 표지판은 부품 배치 대상이 아니다.

## 단계 10 식물 장식 대조

The step10 callout and the latest product-inventory crosswalk support one white seven-petal flower `4367`, one bright-green three-prong stem `68211`, and one dark-azure fruit `22667`. The prior `24855` stem and `37695` leaf-spray assignments are withdrawn; no old coordinates are reused. The current ornament module keeps the three parts separate, and their relative fit remains provisional until the exact bar/prong contact is checked. This is display-formation foliage, not fossil-skull ornament. SKU availability is a separate unknown.

## 두개골 본체 조립 진행

- 인쇄 12쪽 6단계의 갈색 1×1 브릭을 두개골 서브모델 로컬 원점으로 삼고, 인접한 두 갈색 경사/날개 부품 후보 24299를 좌우로 배치했다. 형상 파일은 공용 에셋에서 확인했으나 설명서의 실제 금형 번호와 stud 접점은 잠정이다.
- 인쇄 13쪽 완성도와 11단계 그림에서 두개골 옆에 2×2 원형 스터드가 있는 판 2개가 세워지는 것을 확인했다. 아직 정확한 판 후보 및 브래킷 연결면을 특정하지 않아 접점만 보류한다. 기준 본체는 별도 서브모델로 기록했다.
- 두개골 서브모델의 몸체 기준 변환과 장식 모듈 연결 변환은 후속 시점 대조 대상으로 남겼다. SKU 미확인은 설계 선행 조건으로 사용하지 않았다.

## 별도 프레임 초안

- 인쇄 14쪽 14단계에서 별도 프레임의 기준 부품인 황갈색 2×16 판과 끝의 황갈색 테크닉 브릭을 확인해 `triceratops-frame.ldr` 내부 서브모델에 로컬 배치했다. 판 중심을 원점으로 하고 긴 축을 X로 둔다. 테크닉 브릭 구멍의 최종 방향과 두개골/몸체와의 조립체 변환은 다음 단계 도해로 보정한다.
- 15–21단계 도해는 두 개의 긴 보를 긴 판에 쌓고, 끝에서 교차 프레임으로 닫는 구조를 보여 준다. 15단계 검은 1×6 브릭 및 회색/흰색 테크닉 연결부는 실제 부품 ID와 구멍 간격을 확인한 뒤 추가한다. 미확인 부품을 치수 비슷한 형상으로 대체하지 않는다.

- 인쇄 14–15쪽 14–19단계를 프레임 로컬 좌표계에 추가했다: 황갈색 2×16 기준판, 검은 1×6 보 2개, 흰 2×2/테크닉 브릭, 두 핀, 황갈색 교차 보·판, 상층 흰 보, 2×16 덮개 판. 수량은 해당 단계 부품표와 맞췄다. 보 간격과 교차 위치는 그림에서 추정한 잠정값이며 후속 시점으로 보정해야 한다.
- 1×6 형상 3009와 공식 참조 하위 조각을 LDraw ZIP에서 가져와 공용에 추가하고 사전·매니페스트에 출처와 해시를 기록했다. GoBricks 금형·색상 SKU 대응은 미확인이다.
- 인쇄 16쪽 20–21단계에서 두 번째 긴 황갈색 판이 평행 레일을 만들고, 끝에 황갈색 1×2 브릭 및 파란 삼각 지지 후보가 붙는 것을 확인해 프레임 서브모델에 추가했다. 24299는 형상 후보일 뿐 도해의 파란 몰드와 동일하다고 확정하지 않았다. 레일 간격과 교차 조인트의 정확한 stud/축 좌표는 원근도 기반 잠정값이며, 후속 프레임 시점과 두개골 결합을 기준으로 조정해야 한다.

## 후속 완성도에서 확인한 결합 관계

- 제공된 두 번째 PDF 인쇄 86–87쪽 완성 시점에서 두개골은 골격의 앞/상부에, 긴 프레임은 바닥의 평행 레일로 배치된다. 이 개요도는 위치 관계만 확인하며, 연결 브릭·구멍 중심을 가려 상대 변환을 수치화할 근거가 되지 않는다.
- `24299.dat` 헤더/형상은 실제로 Wedge Plate 2×2 Left이다. 따라서 단순 색상 유사 후보가 아니라 쐐기 평판 후보로 형상 기능은 설명서 6단계 쐐기 실루엣과 부합한다. 좌우 쌍의 몰드·회전은 단계별 호출 그림상 확정하지 못했으므로 현재 모델 배치는 후보로 유지한다.
- 현재 스켈레톤 지지 프레임과 페이지 14–21 로컬 프레임은 서로 다른 조립 구조일 수 있다. 86쪽 개요만으로 이를 같은 프레임으로 간주해 변환하지 않는다. 연결점 기준이 드러나는 단계별 도해가 확인될 때까지 두 서브모델의 상대 변환은 보류한다.


## 단계 249 및 278–279 형상 기반 재검산

- Step 247’s local receiver remains the p.136 47905 brick over two 6141 plates. It is a separate part group from the step249 tan support.
- On p.137, step249 builds the two 6541 one-hole bricks between lower and upper 3023b plates. With the 6541 DAT origins at y=-24, their side-hole centers are `(-10,-14,+/-10)` and `(10,-14,+/-10)`. The outward +Z hole centers used for the two 6141 candidates are `(-10,-14,10)` and `(10,-14,10)`, axes +Z. Each 6141 top-stud base is coincident with that center and its local stud axis is rotated from -Y to -Z. This is a center/axis fit to the candidate hole; manual mold identity and press-fit tolerance remain shape-candidate level. The 25264 caps are placed outside as candidates, but their receiving geometry and insertion are unverified.
- The parallel/orthogonal-axis question from the hidden view remains unresolved per the user’s “keep both candidates” answer. We do not infer both external ports must match the receiver, and no candidate is eliminated by that comparison.
- Step278’s current parts are 32056 + 92907 + 2×61332, per the latest reviewed inventory and p.148 callout. The old 32140/32184/11214 coordinates and all results derived from them are withdrawn.
- Step279 adds no pieces; p.149 shows docking of the completed skull onto the body. The current MPD has separate local fragments, not a physically assembled complete fossil skull. A compatible male port and its point/axis in the skull local frame have not been identified, so no docking transform is invented.

## 단계 6 전시용 바위 형상

The p.12 step6 pair is reddish-brown sloped rock trim in the display formation. The latest reviewed inventory identifies both as `28192` cutout slopes; the old `24299`/`24307` left/right wing interpretation is withdrawn. They remain inside `triceratops-display-formation-6.ldr`, a name explicitly distinct from the later fossil skull. Current positions follow the two opposed sides of the 3005 support; exact stud contact remains provisional.

## 단계 278 링크의 DAT 기반 좌표

`triceratops-step278-link.ldr` uses the 92907 local origin. The official DAT exposes the two positive-X axle-port lines at `(x,20,0)` and `(x,20,-20)`, each through x=0..20. The 32056 holes at `(0,0,0)` and `(0,0,20)` are mapped to those lines with translation `(25,20,0)` and rotation `[[0,1,0],[1,0,0],[0,0,-1]]`. The liftarm web spans x=20..30 and meets the crossblock face at x=20.

Each 61332’s DAT shaft envelope is 40 LDU along local X. Pins are placed on the two shared X-axis lines at `(20,20,0)` and `(20,20,-20)`, with their collar at the part-face boundary. This gives 20 LDU through the crossblock, 10 LDU into the liftarm and a nominal 10 LDU projection beyond its far face. These are computed geometry intervals, not proof of real-world tolerance or surface-interference clearance. The remaining 92907 center receiver points along +Z; its mating counterpart is not yet present as a verified feature in the local skull assembly.

## 독립 받침 조립 시작

- 인쇄 150쪽 단계 280에서 2×10 판을 stud grid로 확인해 새 `triceratops-base-280.ldr` 로컬 서브모델의 기준으로 배치했다. 두 studs와 옆 이중 힌지 fingers가 보이는 tan 부품은 공식 `50340` dual-finger hinge 후보로 배치했으며 힌지 방향은 잠정이다.
- 단계 281의 1×3 판 두 개는 두 행에 나란히 올린 보강 패치로 추가했다. 실제 부품 길이와 반복 수량은 도해와 맞지만 정확한 길이 방향/겹침은 다음 플랫폼 단계로 보정할 잠정 좌표다. 이 서브모델은 두개골·몸통 링크와 독립적으로 작성했다.



- 인쇄 151쪽 단계 282의 평평한 tan 2×4 타일을 `87079.dat` 형상 후보로 base 서브모델에 추가했다. 힌지 끝을 덮는 위치는 그림에서 추정한 잠정값이며 283단계 호출로 보정한다.



- 인쇄 151쪽 283단계 부품표에서 tan 1×2 판 1개, 1×2 테크닉 브릭 1개, 이중 손가락 힌지판 2개를 식별했다. `3023b`, `3700`, `50340` 후보를 282단계 타일 뒤의 드러난 두 행에 배치하고 공식 부품 높이에 맞춰 각 힌지판을 위에 놓았다. 행 선택과 손가락 방향은 도해 기반 잠정값이다.


## 포트 역할 보정 및 단계 284

- 단계 284 (인쇄 151쪽): 여섯 스터드 2×3 판은 `3021.dat`, 네 스터드 2×2 판은 `3022.dat` 도해 호출과 공식 형상이 일치한다. 두 부품을 독립 받침 서브모델에 추가했다. 길이 방향 회전·상대 중첩은 다음 플랫폼 시점에 맞춘 잠정 배치다. 기존 비다양체 Boolean/BVH 검사는 재실행하지 않았다.

- 단계 285 (인쇄 151쪽): 짧은 곡면 쐐기 두 개가 추가된다. 공식 `1762.dat` (“Slope Brick 31 2 x 2 Double, Curved”)은 호출의 이중 곡면 윤곽·수량과 맞는 형상 후보여서 양쪽에 하나씩 MPD에 배치했다. 이는 부품 식별 확정이 아니다. 곡면 진행 방향, 아래 스터드 footprint, 284단계 판과의 정확한 중첩은 286단계의 더 넓은 삼각판 조립과 함께 보정한다.

- 단계 286 (인쇄 152–153쪽): 양쪽의 큰 스터드형 삼각판이 옆으로 펼쳐지고 받침 측면에 연결되는 모습이 뒤쪽 시점에 보인다. 공식 LDraw `30355`/`30356` 6×12 좌우 Wing 형상은 스터드 격자·크기·좌우 외곽의 강한 후보라 MPD에 각각 하나씩 등록했다. 부품표는 형상 번호를 보이지 않으므로 실제 금형 배정은 미확정이며, 힌지 접촉면과 장착 높이도 다음 시점에 보정한다. 두 후보를 확인 부품 수량으로 보고하지 않는다.

- 단계 287 (인쇄 154쪽): 좌우 테이퍼 패널 한 개씩, 각각 큰 관통 구멍 네 개가 보인다. 공식 `67142`/`68196`은 5×13 곡면 좌우 패널이며 DAT가 구멍축과 외곽의 좌우 차이를 보존한다. 호출의 구멍 수·테이퍼 방향이 강하게 부합해 한 쌍을 후보로 배치했으나 부품 번호는 그림에 인쇄되지 않았다. 긴 축을 삼각판의 바깥 가장자리와 나란히 둔 잠정 좌표이며 실제 접점·삽입 깊이는 보류한다.

- 단계 288 (인쇄 154쪽): 작은 왼쪽·오른쪽 경사 날개 조각이 각각 두 개씩 호출된다. `24299` 왼쪽 Wing과 `24307` 오른쪽 Wing은 서로 다른 공식 금형이며 동일 부품의 단순 회전으로 취급하지 않았다. 후보 네 개를 외측 패널에 잠정 배치했으나, 평평한 면 방향과 스터드/클립 접점은 다음 289–290단계 호출과 후면 시점으로 보정한다. 후보 배치는 확정 BOM 수량으로 세지 않는다.


## 단계 278–279 외부 포트 상태

Step278 internal geometry is registered as described above. Its external +Z receiver is not yet matched to a verified skull-side male feature. Step279’s p.149 placement arrow and final view establish assembly order and broad orientation only; they do not expose the exact hidden point/axis. The verified step247 47905/6141 stack and step249 6541/6141/25264 candidates remain separate local fragments and are not claimed as the complete torso receiver. Older step247 spacer and step249 pin/joiner hypotheses were superseded by the newest product-inventory crosswalk; no withdrawn candidate remains counted as an instance.

## 단계 250 몸통 연장판

- 인쇄 137쪽 250단계 호출은 tan 네-스터드 1×4 판 한 개다. 공식 `3710.dat`의 네 스터드와 평판 윤곽이 호출과 일치한다. 실제 배치는 `triceratops-torso-250.ldr` 내부 로컬 조각으로 작성했고, 긴 축은 도해의 몸통 보 방향에 맞췄다. 루트의 X=1600은 미연결 조각을 보기 좋게 분리한 편집 좌표다. 스터드 행·겹침·몸통 최종 변환은 미확인이라 기존 247/249 수용부와 임의로 결합하지 않았다.


## 단계 251 소형 몸통 연결 조각

- 인쇄 138쪽 251단계 호출은 오프셋 구멍이 있는 단일 스터드 1×2 판 3개와 작은 경사 브릭 1개를 보여 준다. 공용 형상의 `11458.dat`와 `54200.dat`이 각각 구멍/단일 돌기 및 31도 1×1 경사 윤곽에 맞아 `triceratops-torso-251.ldr`에 잠정 등록했다. 세 판은 긴 축을 교차시킨 로컬 배열로 두어 호출 수량을 표시했으며, 이를 3710이나 6541에 억지로 접촉시키지 않았다. 스터드 행·구멍 방향·몸통 결합은 252–254단계 시점으로 보정할 항목이다. 네 후보 배치는 확정 BOM 수량으로 세지 않는다.

- 252단계의 긴 곡면 tan 조각은 공식 `50950` 형상 후보로 `triceratops-torso-251.ldr`에 실제 추가했다. 50950의 3×1 바닥 외곽(60×20 LDU)은 11458 세 개의 20-LDU 피치에 90° 회전 시 명목 정합한다. 이는 후보의 크기·곡률·배치가 도해와 양립한다는 근거이며 금형 번호, 숨은 보어, 삽입 깊이 또는 GoBricks SKU를 확인한 것은 아니다. 이 잠정 후보는 완료 수량에 포함하지 않는다.


## 단계 253–254 원형 부품 및 내부 쌍

- 인쇄 138쪽의 두 호출 그림은 모두 2스터드 1×2 판 한 개 위에 4스터드 원형 판 한 개를 두 개의 화살표로 내리는 구조다. 하부는 3023b 형상에 맞고, 상부 `4032a`는 중앙 십자 액슬 구멍·4개 스터드·8 LDU 두께·칼라 없는 원형 외곽이 호출과 부합하는 강한 후보다. 외곽 지름만으로 정하지 않았다. 실제 접점 그림의 20 LDU 쌍 스터드가 원형 판 하부의 한 안티스터드 행과 맞는다.
- 두 내부 쌍을 `triceratops-torso-side-253.ldr`와 `triceratops-torso-side-254.ldr`에 각각 작성했다. 4032a 후보의 중심 액슬 구멍은 로컬 +Y 방향으로 열려 있고 이 단계에서는 축을 추가하지 않는다. 3023b 윗면과 4032a 하부면은 8 LDU 판 두께 기준으로 맞닿는다. 이는 공용 DAT 피치·두께 등록이며 실물 공차나 부품 금형 확정은 아니다.
- 단계254의 회전 아이콘은 모델을 돌려 보여 주는 표시라 부품 자체의 월드 회전으로 사용하지 않았다. 두 번째 쌍의 몸통 상대 변환과 노출 구멍 방향은 후속 단계 접점에서 결정한다. 두 단계의 4032a 두 개는 각 단계에 실제로 호출된 별도 후보이며, 확정 완료 수량으로 세지 않는다.


## 단계 289–292 힌지축 추적

- 50340 후보의 공식 DAT와 `clh10` 도움말은 힌지 회전축을 부품 로컬 Z로 정의한다. 50340의 후보 기준선은 로컬 `(x=0,y=2)`를 지나며 두 끝의 손가락 중심은 `z=-16,+16`(32 LDU 간격)이다. 단계289·290의 현재 부품 회전은 항등이라 두 로컬 조립체 모두 축 `+Z`를 유지한다.
- 인쇄 157쪽 291–292의 화살표는 이미 만든 양쪽 큰 패널의 회전을 보여 주며 이 힌지 행과 양립한다. 이는 축 방향 후보 확인이지 결합된 다른 힌지 절반·동축 중심·삽입 범위·각도를 확인한 것은 아니다. 따라서 MPD의 독립 로컬 조립체는 보존하고, 확인되지 않은 접힘 변환을 추가하지 않았다.

- 4032a 후보를 같은 외곽의 공식 대안과 비교했다. `18674.dat`는 중심이 구멍이 아니라 추가 스터드 하나인 2×2 원판이므로 확대 호출도의 중앙 십자 개구와 불일치한다. `30000.dat`는 측면 핀이 달린 2×2 브릭이고 높이가 24 LDU인 반면, 호출은 낮은 2×2 원판을 두 스터드에 내리는 구조다. `4032a.dat`는 중앙 축 구멍(세로 로컬 Y), 주변 네 스터드, 칼라 없는 8 LDU 원판 두께가 그림과 가장 잘 맞지만, 부품 번호가 인쇄되지 않아 강한 형상 후보로 유지한다.
- 251–252의 높이도 역검사했다. 공식 50950의 바닥 기준 y=24를 MPD의 y=-24 이동에 놓으면 바닥이 y=0이 되고, 11458의 상면 기준 y=0과 명목 간격 0 LDU다. 따라서 기존 잠정 높이는 유지한다. 스터드/소켓의 실제 체결 깊이와 설명서의 금형 번호는 미검증이다.


## 단계 256–258 독립 갈비 보강 조각

- 인쇄 139쪽 256단계는 tan 1×4 판 두 개를 직각으로 놓고, 257단계는 안쪽 아래에 1×2 판을, 258단계는 한 팔 끝에 1×2 판과 작은 경사 조각을 더한다. `3710` 두 개와 3023b/54200 형상 후보를 `triceratops-torso-rib-256.ldr`에 실제 배치했다. 긴 판의 스터드 수와 발자국은 확인했지만, 255단계 호출의 둥근 모서리 연결 조각이 어떤 금형인지와 두 팔을 어떻게 잠그는지는 아직 구분하지 못했다. 해당 연결점·삽입만 보류하며, 분리된 판·보강 조각의 로컬 배치는 유지한다. 몸통에 붙는 변환도 후속 접점이 보일 때 적용한다.


## 단계 259 옆볼·테크닉 보강

- 인쇄 140쪽 단계259에서 구멍 벽돌 옆에 들어가는 검은 구형 부품은 수형 축이 있어야 한다. 공식 `2736.dat`는 축 towball이며 로컬 X축의 수형 구간이 17.5 LDU다. `6541.dat` 측면 구멍은 20 LDU 두께의 관통축이다. 축을 `6541`의 +Z 쪽에서 -Z로 향하게 배치하면 횡잔차 0 LDU, 명목 삽입 17.5 LDU, 반대 면까지 2.5 LDU가 남고 구형 머리는 가까운 면에서 12 LDU 바깥에 놓인다. 반면 `32474`는 축이 튀어나오지 않는 막힌 암형 axlehole이라 이 직접 삽입 그림과 맞지 않아 MPD 대안으로 동시에 배치하지 않았다. 실제 부품 번호는 후보다.
- 호출의 검은 1×2 두-구멍 벽돌은 `32000` 형상 후보, 상단 tan 1×1 경사는 `54200` 후보로 로컬 MPD에 추가했다. 상부 스터드 행은 도해에 근거한 잠정값이다. 원형 스페이서 두 개는 `6577` 암형 bush와 `2780` 슬롯형 수형 핀을 중앙 구멍/축 단면으로 구분할 수 없어 인스턴스화하지 않고 조건만 기록했다.

## 단계 260–263 추가 배치와 291–292 힌지 재판독

- 인쇄 141쪽 단계260에서 검은 1×1 단일 구멍 테크닉 브릭 형상은 공식 `6541`과 대응하므로 `triceratops-torso-260.ldr`에 로컬 후보로 넣었다. 그 위의 올리브색 유기형 부품은 동일 이미지에서 구멍/축 단면이나 부품 외곽이 불명확해 형상 번호를 배정하지 않았고 대체품도 넣지 않았다.
- 단계261의 빨간 표시 조립은 기존 단계256–258 늑골 모듈과 같은 긴 L형 조립체다. 같은 부품을 두 번 세지 않도록 복제하지 않았다. 도해는 이를 몸통 아래 옆구리로 옮기는 것을 보여 주지만 실제 스터드/클립 기준점과 월드 변환은 단면에서 확인되지 않아 그 변환만 남겼다.
- 인쇄 142쪽 단계263은 1×4 두 팔, 1×2 두 스터드 판, 두 개의 둥근 1×1 캡, 끝 쐐기의 개수·윤곽을 기준으로 3710×2, 3023b, 6141×2, 54200의 형상 후보 여섯 개를 별도 `triceratops-torso-263.ldr`에 기록했다. 6141 및 접합 위치/층 높이, 쐐기 방향은 형상 후보 수준이며 확정 부품표 수량이 아니다. 호출의 아래 보강판 하나와 중앙 관절 조각 하나는 아래면 결합 형상과 힌지 절반을 분리할 만큼 선명하지 않아 인스턴스화하지 않고 상태에 보류 수량으로 남겼다.
- 단계291–292 확대도에는 중앙 접합부의 힌지 배럴/너클 선과 양 측면 패널의 회전 화살표가 보인다. 따라서 회전축은 중앙 힌지선이라는 질적 근거를 추가했다. `50340`은 아직 금형 후보이며, 정확한 축 중심 좌표, 상대 힌지 금형, 삽입 깊이와 끝 회전각은 도해로 수치화되지 않아 해당 변환만 잠정 상태다. 이 시각 근거는 폐쇄 솔리드·BVH 검증으로 오인하지 않는다.
- 인쇄 143쪽 단계264 호출에서 단계262와 같은 네 실루엣 종류가 다시 각각 한 번 호출된다. 별도 새 부품으로 보고 `44301b`, `3022`, `3040b`, `54200`를 새 ID의 독립 후보 모듈로 기록했다. 앞 단계 후보 ID를 재사용하거나 같은 인스턴스를 복제하지 않았으며, 각 금형·접점·몸통 배치는 잠정이다.
- 인쇄 143쪽 단계265–267 호출을 확대해 독립 로컬 후보로 이어 작성했다. 265는 L형 작은 판을 `2420` 후보로, 작은 쐐기를 `54200` 후보로 놓았다. 266의 세 번 반복되는 한쪽 스터드 곡면 부품은 가장 가까운 공용 형상 `50950` 세 개로 기록했으나 곡률·폭의 금형 대조는 미확정이다. 267의 둥근 스터드 캡과 쐐기는 `6141`과 `54200` 후보로 기록했다. 위치는 호출도 내부 배치뿐이며 본체 변환은 보류했다.
- 인쇄 144–145쪽 단계268–274의 호출을 별도 로컬 후보 모듈로 작성했다. 268·274는 구멍 난 삼각판을 `3176` 후보로, 270은 좌우를 구분한 `24299`/`24307` 후보로 배치했다. 269·271·273의 판/쐐기/둥근 캡과 272의 3개 반복 곡면도 호출 수대로 내부 조립체에 기록했다. 모든 배치는 설명서 외곽에 맞춘 형상 후보이며 연결 깊이·뒤쪽 접촉면·두개골 상대 변환은 미검증이다. 이 후보들은 확정 수량이나 완성된 두개골 부품으로 세지 않는다.
- 인쇄 146쪽 단계275–276의 1×2 판·쐐기·큰 곡면 부품과 지지 조각은 각 호출 수량대로 로컬 후보 조립에 기록했다. 큰 외곽은 공용 `64225`/`61678` 곡면 후보와 대조했지만 후속 시점에서 곡률과 아래 체결점 검증이 필요하다.
- 단계277 호출의 긴 구간은 `14301` flexible hose 형상과 강한 길이/분할 윤곽 대응을 보여 두 개를 뿔 본체 후보로 MPD 내부 로컬 모듈에 추가했다. 공식 형상은 직선 표준 렌더이므로 설명서의 굽힘 포즈를 구현하지 않았으며 이를 연결 확인으로 해석하지 않는다. 필수 `14301k01/k02` 세그먼트를 공용 에셋에 함께 등록했고, 저자 Sylvain Sauvage 및 CC BY 4.0 고지, 원본 아카이브·파일 해시를 `assets/policy.md` 매니페스트에 기록했다. GoBricks 판매 대응은 별도 미확인이다. 호출의 핀·칼라·끝 장식은 단계별 삽입 방향과 수용 구멍 대응을 확인하기 전까지 배치하지 않았다.
- 단계277 호출의 끝 조각은 공식 `13564.dat` Animal Cow Horn 2.25L의 휘어진 뾰족 윤곽과 대조해 두 개를 `14301` 호스 끝 후보로 추가했다. `13564`와 해당 primitive 참조를 공식 아카이브에서 확보해 기존 공용 경로로 변환하고 `assets/policy.md`에 원본·변환 해시, 저자 Philippe Hurbain, CC BY 4.0을 기록했다. 호스 끝점 근처에 등록했지만 실제 소켓의 성별·삽입 깊이·조립 각은 미확정이다.
- 단계277 호출의 나머지 내부 조각은 후보를 하나로 단정하지 않았다. 축/막대는 매끈한 `87994`와 십자축 `4519`, 구형 핀은 수형 액슬 타월볼 `2736`과 볼 조인트 막대 `22484`, 원통 슬리브는 `62462`와 `59443`, 테이퍼 어댑터는 `59900`과 `98100`을 각각 대조 후보로 남겼다. 도해가 각 단면과 수용부 암수 구조를 가려 네 부품군은 인스턴스화하지 않았고, 완료 수량으로도 세지 않는다.
- 단계260의 올리브색 곡선 조각은 전체 부품표의 작은 곡선 조각 3개 수량과 대조했다. 단계277의 두 끝 조각과 같은 형상군으로 보이며 공용 `13564` 형상의 곡선·테이퍼가 부합해 세 번째 `13564` 후보로 배치했다. 설명서 색상 330 Olive Green을 유지하고, 아래 화살표에 따라 6541 상부 스터드 중심에 놓았다. 형상 홈과 실제 몰드가 동일하다는 확정 근거는 아니므로 후보 상태다.
- 단계277 호출의 여섯 범주를 단계 순서와 전체 부품표 수량으로 대조해 두 뿔 각각에 후보를 배치했다: 근위 수형 볼 축 `2736`, 긴 유연 호스 `14301`, 호스 축을 따라 들어가는 매끈한 3L 막대 `87994`, 둥근 슬롯 슬리브 `62462`, 작은 테이퍼 어댑터 `59900`, 말단 곡선 뿔 `13564`. 도해의 짧은 핀·원통·테이퍼 실루엣과 부품표의 두 개씩 수량은 이 구성과 양립한다. 이 좌표는 단계 순서에 근거한 후보 조립이며 소켓 지름/수형축 단면·체결 깊이는 확인 전이다. 대안 `4519`, `22484`, `59443`, `98100`은 동시에 넣지 않고 분별 특징을 상태에 기록했다.
- 253–254단계의 공식 DAT를 다시 좌표화해 수정했다. `3023b`의 두 스터드는 기본 로컬 Z 방향의 `z=±10` 행에 있으므로, 90° 회전 후 위치 `[0,0,10]`에 놓아 전역 `(x=±10,z=10)`에 맞췄다. `4032a` 밑면의 한 소켓 행도 같은 중심이므로 명목 중심 잔차는 0 LDU, 판 바닥과 원형판 밑면의 간격은 0 LDU다. 중심 액슬 구멍은 수직 로컬 Y축으로 열린 채 유지된다. 이는 공식 형상 중심선 기반 잠정 접촉이며, 설명서 금형 번호·실제 공차·하중 검증은 아니다.
- 단계255(인쇄 139쪽) 확대도는 90° L형 스터드판 하나와 둥근 스터드 캡 둘을 부른다. `2420`과 `6141×2` 후보를 새 로컬 조립체에 넣었다. 캡이 smooth tile `25269`인지 studded round `6141`인지는 top-surface detail로 더 확인할 항목이다. 이 조립체를 단계256 팔에 아직 연결하지 않았다. 단계257의 아래 보강판이 같은 중심 접점을 함께 지지하는지 대조한 뒤 한 개 변환만 적용할 예정이다.

## 메인 에이전트의 제품 부품표 대조 — 2026-11-05

공식 77985 설명서 `6649865.pdf`의 161–162쪽 부품표를 기존 공용 사전 `instruction_sets["77985"]`에 등록했다. 281개 요소의 인쇄 수량 합계는 1154개로 제품 안내와 일치한다. 요소·수량·원본 위치와 Rebrickable의 부품/색상 교차표를 구분해 저장했고, 미니피겨·명판을 포함한 제품 전체 목록이므로 모델 범위 수량과 동일시하지 않는다.

메인이 도해를 직접 대조한 결과 기존 기록의 후보 일부에 오류가 있다. 4단계는 스터드 있는 dark tan 18980 판, 5단계는 적갈색 스톱 축24316·회색 십자 구멍32064a·3713 부싱, 6단계 갈색 경사면은28192, 10단계는 흰 꽃4367·초록 막대68211·청색 체리22667 후보로 재검토한다. 247단계는 검은 측면 스터드47905와 원형판6141 두 개, 249단계 검은 캡은25264, 278단계는32056·92907·61332 후보가 공식 제품 목록과 호출도해에 부합한다. 상세 요소 번호·색상·이전 후보와의 차이는 사전의 `reviewed_step_candidates`를 따른다. 이는 새 후보의 근거이며 실제 조립·삽입을 확정한 기록이 아니다.

초기 10–13쪽은 전시 소품의 바위·식물·표지판 기반부이며 화석 두개골 본체가 아니다. 후반 278단계의 큰 tan 화석 두개골과 혼동한 기존 내부 모듈 명칭·연결 가정을 재검토해야 한다. 표지판·미니피겨 제외 지시는 유지한다. 이 검토에서는 MPD 좌표·기존 배치를 수정하지 않았고, 담당 에이전트가 최신 자기 브랜치에서 후보 교체와 접점 계산을 수행한다. 기존 후보로 얻은 잔차0·핀 삽입 결과를 새 부품의 검증으로 승계하지 않는다.


## Current-manual candidate corrections — 2026-11-05

Merged the current `origin/main` inventory review (`a52802c`) and inspected official `6649865.pdf` pages 11–13, 136–137, and 148. The early step 4–6 objects are a display-base/rock formation, not the fossil skull. In `triceratops-v0.mpd`, step 4 now uses the rounded 2×6 plate candidate `18980`; step 6 uses two reddish-brown `28192` cutout slopes around its called small brick. Step 5 axle/bushing candidates were replaced by `24316`, `32064a`, and `3713`; their centers and axes were recalculated from the new DAT files. Step 10 now records the called green stem `68211`, white flower `4367`, and dark-azure cherry `22667`, with local branch fit provisional.

Step 247 now follows the latest crosswalk: one `47905` opposite-side-stud brick and two stacked `6141` plates. Step 249 uses the called `3023b`/`6541` support core plus candidate `6141`/`25264` side caps. Step 278 uses `32056`, `92907` and two `61332`; all former 32140/32184/11214 geometry is withdrawn. Internal link geometry is registered; the step279 external transform remains unresolved.

The same review removed one exact duplicate frame-base placement (`part-0022` 4282) at the root stand plate transform; the frame now reuses the root base plate instead of double-counting it.
