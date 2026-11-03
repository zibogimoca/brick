# 에셋 관리 정책

## 용도

에셋은 브릭을 화면에 그리는 데 사용하는 3D 형상 자료다. 부품 사전은 고브릭스 상품 번호·색상·가격·형상 참조를 관리하고, 에셋은 그 참조가 가리키는 실제 모양을 담는다. 형상이 있다는 사실만으로 고브릭스 실물과의 일치나 조립 가능성이 검증되는 것은 아니다.

## 현재 폴더와 파일

| 위치 | 의미 |
| --- | --- |
| `parts/` | 부품의 형상 정의. `3001.dat`는 2×4 브릭처럼 LDraw 식별 번호로 이름을 붙인다. |
| `parts/subparts/` | 부품 형상의 일부를 분리한 하위 조각. 여러 부품에서 재사용할 수 있다. |
| `primitives/` | 돌기·원통·원호 등 공통 기하 조각. 파일명은 LDraw의 규칙을 따른다. |
| `primitives/high-resolution/` | 곡면을 표현하는 분할 정밀도가 다른 공통 조각. |
| `LDConfig.ldr` | 색상 번호와 화면 표시 색상·재질의 대응표. |
| `policy.md` | 사용자가 알아야 할 에셋 구조·관리 원칙·이용 조건을 모은 유일한 설명 문서. |

`.dat`는 문서가 아니라 좌표, 면, 다른 형상 파일의 배치 정보를 담는 LDraw 형상 형식이다. 현재 선택한 상위 부품은 67종이며, 나머지 형상 파일 상당수는 그 부품들이 참조하는 조각이다. 파일 수가 판매 부품 수를 뜻하지 않는다.

## 왜 나뉘어 있는가

LDraw 형상을 사용하되 폴더 이름과 내부 참조를 읽기 쉬운 이름으로 변경했다. `primitives`는 공통 형상, `subparts`는 부품의 하위 형상, `high-resolution`은 원 둘레를 48분할하는 고정밀 형상을 뜻한다. 예를 들어 `parts/3001.dat`는 `parts/subparts/3001s01.dat`를 참조한다. 하위 파일이 다시 공통 조각을 참조할 수도 있다. 번호와 경로는 사람이 읽기 좋은 이름 대신 참조 식별자로 쓰인다.

부품 한 종류당 독립 파일 하나로 만드는 것도 가능하다. 참조한 조각의 좌표 변환과 색상 적용을 풀어 모든 면을 해당 부품 파일에 넣으면 된다. 이렇게 하면 파일 목록은 단순해지지만 같은 돌기 등의 데이터가 부품마다 반복된다. 반대로 공통 조각을 별도로 유지하면 중복은 줄지만 파일과 참조 관계가 늘어난다. 어느 쪽이 항상 더 빠르거나 관리하기 쉬운 것은 아니다.

폴더를 단순화하려면 형상뿐 아니라 사전의 참조, 뷰어의 로딩 경로, 수집·검증 도구를 함께 수정해야 한다. 불필요한 `ldraw` 상위 폴더를 제거하고 폴더 이름과 형상 내부 참조를 변경했으며 좌표와 개별 부품 번호는 유지했다. 원본 아카이브 경로와 원본 해시는 출처 추적용으로 아래 목록에 보존한다.

## 출처와 라이선스

현재 형상은 [LDraw 공식 라이브러리](https://library.ldraw.org/)의 [전체 아카이브](https://library.ldraw.org/library/updates/complete.zip)에서 필요한 부분만 가져왔다. 직접 제작한 형상으로 표시하지 않는다. 개별 저자는 원본 형상 헤더와 이 문서 하단의 에셋 목록에 기록되어 있다.

현재 형상에는 **CC BY 4.0** 또는 **CC BY 2.0과 CC BY 4.0** 병기 자료가 포함된다. 파일별 고지는 아래 목록에 보존한다. [이용 조건 요약](https://creativecommons.org/licenses/by/4.0/)과 [라이선스 전문](https://creativecommons.org/licenses/by/4.0/legalcode)을 기준으로, 공유할 때 저자·출처와 라이선스 링크를 제공하고 변경했다면 그 사실을 표시한다. 저자가 이 프로젝트를 보증하는 것처럼 표현하지 않는다. 색상 설정 등 다른 자료의 조건을 이 확인 결과로 일괄 단정하지 않고 원본 고지를 따른다.

별도 `CAreadme.txt`와 `CAlicense.txt`는 사용자 요청으로 삭제했다. 원본 형상 안의 저자·라이선스 헤더는 보존되어 있으며, 그 안에 남은 `CAreadme.txt` 표기는 원본의 참조다. 파일 삭제가 원래 이용 조건을 없애지는 않는다. 이용 안내는 이 문서에 통합한다.

공개 저장소나 공개 뷰어에 포함한 자료는 다른 사람이 받을 수 있으므로, 혼자 볼 목적이어도 공개 상태라면 공유 조건을 고려해야 한다. 배포할 때는 이 안내와 개별 저자 정보를 함께 제공하고 접근 가능한지 확인한다.

## 관리 원칙

- 에셋 설명 문서는 이 파일 하나로 유지한다. 새 설명 문서를 추가하지 않고 여기에 갱신한다.
- 새 파일·폴더는 생성 전에 사용자에게 이름·목적·필요성을 보고한다. 형상 구조 변경도 먼저 설명한다.
- 모델에 필요한 형상만 확보한다. 사전 정보와 형상 검증 상태를 구분한다.
- 참조되는 형상을 임의로 삭제하거나 이름을 바꾸지 않는다. 변경 후 누락된 참조와 뷰어 표시를 확인한다.
- 직접 만든 형상과 가져온 형상을 구분하고, 수정한 자료는 변경 사실을 기록한다.

## 에셋 목록

출처·저자·라이선스·파일 검증 정보를 이 문서에 함께 보관한다. 아래 JSON 블록은 뷰어와 검증·수집 도구가 읽고 갱신하므로 형식과 구분자를 유지한다. 별도 목록 파일은 만들지 않는다.

<!-- asset-manifest:start -->
```json
{
  "source": "https://library.ldraw.org/library/updates/complete.zip",
  "archive_sha256": "023083918da2d3697c794fb4267975509584f3611b993095874206a803fa610f",
  "verification": "HTTPS source, ZIP member CRCs and retained per-file SHA-256; archive SHA is an observation, not a separately published signature.",
  "parts": [
    "3001",
    "3003",
    "3005",
    "3020",
    "3024",
    "3700",
    "3705",
    "4274",
    "2429",
    "2430",
    "14417",
    "14418",
    "14419",
    "3004",
    "3010",
    "3622",
    "3023b",
    "3022",
    "3710",
    "3623",
    "3666",
    "3460",
    "3034",
    "3832",
    "3031",
    "3032",
    "3062b",
    "6141",
    "4032",
    "3941",
    "54200",
    "11477",
    "15068",
    "59900",
    "30374",
    "60478",
    "60479",
    "60477",
    "40378",
    "40379",
    "59443",
    "32013",
    "32062",
    "11214",
    "53451",
    "87747",
    "85970",
    "98100",
    "44224",
    "44225",
    "2780",
    "32524",
    "32525",
    "32278",
    "32140",
    "32009",
    "60483",
    "22385",
    "41770",
    "41769",
    "43722",
    "43723",
    "11090",
    "87994",
    "63965",
    "30414",
    "4070"
  ],
  "files": {
    "parts/60479.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/60479.dat",
      "source_sha256": "4cc9f46de13bd157dbbf16757bed1becee52253848fc1827d6c18477b94907b3",
      "sha256": "b7f9aa40e95ee3b7da07b0cd78b9bbe83467bb61dc2db895ebed951bc9556d04",
      "bytes": 1759,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/54200.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/54200.dat",
      "source_sha256": "3f0c25da3dac0600209a032c53c040b8668e617374997546d5449528eb7099c9",
      "sha256": "0cc302d68a07074ca5e26886637280843ad41cde51e4ba7e798857c7cabbb641",
      "bytes": 1209,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/85970.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/85970.dat",
      "source_sha256": "9996c2a08b8e69e48786f2a4ebaa8fef9202e778e3ed12f181cbfac36465ed3b",
      "sha256": "d52d6b7701dea01d5f626a3241c9b4a5fab9f6beeeec17d1fa3529402e78f258",
      "bytes": 14083,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Joerg Sommerer [Brickaneer]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/rect3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/rect3.dat",
      "source_sha256": "07ac46908b6668d993b6de0fb001a34cd996542106b80ebc7de63317d8dde865",
      "sha256": "07ac46908b6668d993b6de0fb001a34cd996542106b80ebc7de63317d8dde865",
      "bytes": 605,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/54200s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/54200s01.dat",
      "source_sha256": "cf96613781f9e09ef1e12bf1be127a99b1a8f18a5e8ee9af434ef4e757696cc7",
      "sha256": "9a9eb964e647817b197ea62deac5d2fb97680d5114cd11c3375eb587d224a8d2",
      "bytes": 3799,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/43722.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/43722.dat",
      "source_sha256": "d39335216438d981aa02687a90f4848fd0495eab386b8ab02ac0cc67edf44dcf",
      "sha256": "b6fe6e28d77d9630aced329f18ff6c1ea2ad4d4362df31d7c63bed6b5687a606",
      "bytes": 315,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3003.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3003.dat",
      "source_sha256": "aed0ccd750126a58d38b012a4e8b16c172896339547c120ef67b69e1386f490d",
      "sha256": "650c0d27aeed01b2c0101ba5b58b724c7984f352f9f8426240c325ee3ae0d80b",
      "bytes": 683,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/11214.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11214.dat",
      "source_sha256": "556deb5046ba561714446377068dbff68eb7db2c313a8a53d8b4bf233db7b959",
      "sha256": "5341cd98f57f8eddec043ab8e48f822b43d6203c4b7994b5e79276d2361a8c2f",
      "bytes": 607,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4274.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4274.dat",
      "source_sha256": "c421cee48c7c0233371144f5a256f7a4503f008318ff523b31e0b5a9d44d9704",
      "sha256": "34c32c4d2ff8bd6ccb94ed85a3d69c1c5dbeb61c3cedfea317f1b4be847332ba",
      "bytes": 837,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/30374.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30374.dat",
      "source_sha256": "db69ea3eecc2a6f2731aaad6ac8fb072c5ecbe136d1ea8a03de593014fe2e9c0",
      "sha256": "42934717f0a6ba9654b884ce735de87eafa69f137a5e230de577b56730ba3d5c",
      "bytes": 1016,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32140.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32140.dat",
      "source_sha256": "5c9def4c5be03a5be161a060cd0a106cbb9bffef7117973181123c33f6200f4d",
      "sha256": "fe0a4b3f1600ff46a32ccffb5ad71e62929a8e14c23f7083be07b39bbd869c8d",
      "bytes": 2885,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/11477.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11477.dat",
      "source_sha256": "fed74af9f56bcb149a7f67af4b427c261b41d24d15ed7a3466e24170377a0ba6",
      "sha256": "d48210fbcaa6d4ff63bd08843e4e05aac6f89cd77215ae06b06db9c2da36e571",
      "bytes": 411,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/60483.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/60483.dat",
      "source_sha256": "e9642b7d24f816f62a37ef798e2a7a21377febec2e857ce0ecc4eceb907ca47c",
      "sha256": "13556cc858e4c8048287c101fce51315316ee426c2c10c4390f742008c11695b",
      "bytes": 557,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/41770.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/41770.dat",
      "source_sha256": "8bd7294d3c547f23ac5233e834fd3a14225b6389c8e5b61e6685ba939f28c0cb",
      "sha256": "81f55bafdbdc380217567562cefee539c65068b4315c4ff8a9f7405957e52dca",
      "bytes": 314,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3004.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3004.dat",
      "source_sha256": "e1caee3b32175393c9d6ea176a47f8869173a01d03a451e1cfe10d09167c0203",
      "sha256": "7d58554752f508189d68319e0674df3e710b9d539084ad6d01ea47fee56c2b0f",
      "bytes": 683,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud3.dat",
      "source_sha256": "d29e9160faeaf85b2b72a098e89a81f41e0082517a82065d7b1f149b5fd2addd",
      "sha256": "e8f6675c19abfe3ec02ac94af909e356aba420f9e1b0a097c5e5cd22b0071f20",
      "bytes": 754,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/rect1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/rect1.dat",
      "source_sha256": "48fdcd3181587b4bdc89d356a5aee21268688f3f2fcdd4d6f5c1a3d49b1a1ceb",
      "sha256": "48fdcd3181587b4bdc89d356a5aee21268688f3f2fcdd4d6f5c1a3d49b1a1ceb",
      "bytes": 556,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3003s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3003s01.dat",
      "source_sha256": "58f0af5b23ccd2bf3b7569a1b6de0b62cb1ae95520994ba7aa0b37c35b2a8744",
      "sha256": "0b8d54258ab9c6bdb41e8b67940bf54a90e07461b8017e91ec3e5158f05a08d3",
      "bytes": 474,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3001.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3001.dat",
      "source_sha256": "70968cb5e4baa92dc6a1939aca7526b8566a17dbea49da9b91182aa864e412c4",
      "sha256": "9ca83b162c399148e81c210e51a149f74a8f04d39952d029d4d40cde24705318",
      "bytes": 676,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/rect.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/rect.dat",
      "source_sha256": "ffeb2dd3d9b83c38841f18f1f74800fbba9e90c5fb6badfff2a795f08a96cb71",
      "sha256": "ffeb2dd3d9b83c38841f18f1f74800fbba9e90c5fb6badfff2a795f08a96cb71",
      "bytes": 654,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3004s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3004s01.dat",
      "source_sha256": "e05db7f7baead09713c4296b4e4e215b3fa5ccbf526e3431cb66a3ce19e321b5",
      "sha256": "bfe452bd416de25d60e462da3c1b5b65ca0b43a4f8a07339285550747afd8cd9",
      "bytes": 905,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/60483s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/60483s01.dat",
      "source_sha256": "19502854a4f0a692bdf46cf90f901fbdf443aa96221fe8436965c6bd97d0b803",
      "sha256": "ed9b52e34dc31fe2c188e52abed7aaa3766a4d3eb1bf3d727cf77f5ee3505c56",
      "bytes": 1054,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Jens Brühl [jb70]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2780.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2780.dat",
      "source_sha256": "2628d30bcfa42b3a616da38b8020cbc2b1edb98b055329cfac56425cdc9a8277",
      "sha256": "37b6506c54382e67f05824a68a887db6dd820b384d6dec7d1376d5dcc40ff4a3",
      "bytes": 473,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3622.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3622.dat",
      "source_sha256": "9317bcec4fbcddbd38ed3972d25ea95d685101904f3ed86c7e769a9f356245d8",
      "sha256": "632f618f151974f69ff1b82527a6a00654e8401a343a9199adeae4236709f55a",
      "bytes": 524,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3032.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3032.dat",
      "source_sha256": "35e8b828a5bf21de83ca898a49b9725e6d08d5752ad6eb57910f27086108ca1f",
      "sha256": "96a528a44b11e86fcb8fc64efd1caa74ed8de63d01e13728d573a03c1c43f441",
      "bytes": 2986,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3023b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3023b.dat",
      "source_sha256": "42f96ca69f8a0b83a877f4e128e4143ce753d038b1074835edc5aca9a9954fc9",
      "sha256": "49a404493d624d3a06cb51d8c5083c639336f9ead1ff062e00dfda0844f3f4bb",
      "bytes": 833,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4070.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4070.dat",
      "source_sha256": "bf1878c02423294b3c0b82db4c416e1d77608bbfb3a2b2b569b42d8a10c75e6c",
      "sha256": "d8e0e34bfa1d0e737bc9fe63a11a740e04f40d0a28dee9b4d29d84e2f72c0447",
      "bytes": 2995,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/22385.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/22385.dat",
      "source_sha256": "0767f2b99fc44acfe409a57aa06f5d25bec8315413335ecd217e77057de6bd0d",
      "sha256": "701fc9453e531e40d2aa22f8df71a3c4f25d328bb087a45b17d233351e53b6e8",
      "bytes": 405,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/rect2p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/rect2p.dat",
      "source_sha256": "faac2b36241a9de0c0108471e59c45734df6c79813332d9cacf97f6391886acc",
      "sha256": "faac2b36241a9de0c0108471e59c45734df6c79813332d9cacf97f6391886acc",
      "bytes": 594,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/11477s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/11477s01.dat",
      "source_sha256": "bc00e46f3d79f0569d3952eb20b91ae2402121d483945fce7e51f3322fdaea21",
      "sha256": "4d596f42b0664d6deb20f0bdc95495a1bb428fe4f8193120c2e3c6acb947d58e",
      "bytes": 3551,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32009.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32009.dat",
      "source_sha256": "aacf33974d07de7cddf19a803972f12c224e1a2a6fd10b59ed1213288ff65f4c",
      "sha256": "8e0c1bd587bfb5e57c32c6cfe7146c3592900e7532aa91e54d5fe5a57f2910d0",
      "bytes": 9304,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3024.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3024.dat",
      "source_sha256": "e053af4f232374b0c8da2dc0f9620bedf0576ca43d7c3ceebc6676050ae61da8",
      "sha256": "d4cc3b719604f0014493d43134752e38dd596c9080fd87cc90c1f27e4363b666",
      "bytes": 681,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32062.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32062.dat",
      "source_sha256": "5d5a970dccccabbd0a0e89e9519c69a51e6a8c75a35af1cfbf61f4fb46231da7",
      "sha256": "8b3a0b3fc364cae90a5e3350ca39c77c6852a7ad3f122a6883228a3e9887ed5e",
      "bytes": 6715,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/14417.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14417.dat",
      "source_sha256": "5da4fc1a13d6110876c944da429ebf2cc29d69b8942fb1dbc05ac8c65480d37c",
      "sha256": "f7bd9c4b6bb871edeca765ad537d441de025f425d2898671071e8b65b3ec3733",
      "bytes": 951,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3022.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3022.dat",
      "source_sha256": "3cd09bfe626e751ad95eab0ea83e5f3adea81f05d34993a1c4bf432ee386fe25",
      "sha256": "3219e4c463fc35c9bebfd6e4e446975cbc7f6fc217f31c71f78d8e87f6166e0d",
      "bytes": 1165,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/connect.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connect.dat",
      "source_sha256": "fa572d5b7bcdb19ea2ba74cd1a98aca913e1e556001232e484611915adf83305",
      "sha256": "efa006e64abd457361f7c0bd84b9c89d6307c5965a0181440a90b061b0971c2d",
      "bytes": 7947,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/41769.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/41769.dat",
      "source_sha256": "013622de3227767ed31ce3c87edbd8cc07c02fa3fb0f00adfc0d2ae242e7ccfa",
      "sha256": "c1710818d4e6828f826eda0a993cccac2a9cf44afc60a0fc7185c7089fc85848",
      "bytes": 315,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axleend20.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axleend20.dat",
      "source_sha256": "ab1e77729fa281549ece68f4ba918b7a673ab4b4678df930969ef1cd016f86c8",
      "sha256": "75f8587dd18545f09809a1ec4b6d281e6a8cd5d2b2dba1a148093b1894c348a7",
      "bytes": 594,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ring2.dat",
      "source_sha256": "dc1748fff34bb0cae3ba1d480921c2f73de4ea1d0532799356b2014a28c8f393",
      "sha256": "dc1748fff34bb0cae3ba1d480921c2f73de4ea1d0532799356b2014a28c8f393",
      "bytes": 977,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4.dat",
      "source_sha256": "871cdcab26e7f5113488a24c453d6fabda75b275b06de592e0bfaad4292c12a3",
      "sha256": "a1340a6652396d41a04ca3c595a663893611dc5db239bf49caa3db1abb466c1b",
      "bytes": 1012,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/22385s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/22385s01.dat",
      "source_sha256": "4d1f8a43e2343f55bbd707197ef57bb8fcfcc48e35ae344cdd65271b4d92fc85",
      "sha256": "75c1c514bd142e23dbe7c59dbbe00d9bb33f3d9fa6cc3601fa3988e33538e6c5",
      "bytes": 4762,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud2a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud2a.dat",
      "source_sha256": "61fbed54b085a30490045309778d1e2a6d95485e6558996b12674f848028d557",
      "sha256": "09de9225684fa0057c54aece78a5a0fd455a1fc026f523ed9b8a6cd29efbb63d",
      "bytes": 921,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/41770a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/41770a.dat",
      "source_sha256": "59648c2ca07a51d82fdc9aabf4edb65f4942760dc9df3b64946d13fd82b0303d",
      "sha256": "9f4850faacdd14b4586db024639a23af74b69bc527382b29c2ad20823dfe4116",
      "bytes": 1079,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Takeshi Takahashi [RainbowDolphin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box2-5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-5.dat",
      "source_sha256": "8f297b754f87da1dbe19eec8704a5ce03a23b794ccd7cd015508e3758a206174",
      "sha256": "8f297b754f87da1dbe19eec8704a5ce03a23b794ccd7cd015508e3758a206174",
      "bytes": 609,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4edge.dat",
      "source_sha256": "54a52196e421fd1717d291ff52ea57553b1fb238907c1678cc1f1a84c698b1da",
      "sha256": "54a52196e421fd1717d291ff52ea57553b1fb238907c1678cc1f1a84c698b1da",
      "bytes": 1084,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-1x4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x4.dat",
      "source_sha256": "e88852b15ca37121e12f7052a234e4a90dc99a8c6d22d45e041f47103c2fb71c",
      "sha256": "13851db043c0c073e299236f8efd1a7715add6477d3e69757db193a273ea0896",
      "bytes": 458,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring8.dat",
      "source_sha256": "4d7ae146c56385df78fb08391c29f72a106355ffe4b7be472461899ebff840ca",
      "sha256": "4d7ae146c56385df78fb08391c29f72a106355ffe4b7be472461899ebff840ca",
      "bytes": 1499,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4edge.dat",
      "source_sha256": "9ce2de7e67bbac575d52cfdc771b9d00856efc9b88002d97db8e665e50f4d467",
      "sha256": "9ce2de7e67bbac575d52cfdc771b9d00856efc9b88002d97db8e665e50f4d467",
      "bytes": 545,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/44225.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/44225.dat",
      "source_sha256": "b0851cbee52ff5fcbb242cf459eb47e9b948b06de47d4eb0748cab8deba942a6",
      "sha256": "897dc03001bb8b189f431327f502ee1d9a4e6965c42c361ea8412c41855c81b2",
      "bytes": 29061,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4.dat",
      "source_sha256": "2cbfcf075ef5c87c6a5f543f837972a78d43274ac7771b92229b5fe5da797c1e",
      "sha256": "2cbfcf075ef5c87c6a5f543f837972a78d43274ac7771b92229b5fe5da797c1e",
      "bytes": 948,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32278.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32278.dat",
      "source_sha256": "c655b689837e76d5bd9dcce36c5b1732384fc76993ad68c8fe7221218397843d",
      "sha256": "f6d3455f14cdfc35b64c9374a99d1ca8f9243167d5c0452cb26cc2822036ca75",
      "bytes": 2548,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Ishino Keiichiro",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug4-1x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4-1x2.dat",
      "source_sha256": "93d8fc1608ff1e899368c604ea42e18e60fb33a68a2e2ae31f2259fbc39deb99",
      "sha256": "b855cdc62ab88786e96da5f598fbef253f7dc7a13b3d9e38a1cb265ab0e1a4cb",
      "bytes": 368,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3001s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3001s01.dat",
      "source_sha256": "bee662925490666aa5956d301b7abc46df88b3cc35737326765441585c720047",
      "sha256": "d3a5fff5fdfc51806583b78997be814ad8357f6978dd6c2739ad24970b44bd4d",
      "bytes": 1599,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8cyli.dat",
      "source_sha256": "46def63dc8293ad9a2dd1d1a5cb720b9ba883850e65d3280d2093c664a6140c4",
      "sha256": "46def63dc8293ad9a2dd1d1a5cb720b9ba883850e65d3280d2093c664a6140c4",
      "bytes": 806,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/npeghol7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/npeghol7.dat",
      "source_sha256": "7892ac0ecc0086f00a15a939292717e5a8f0b9685963de6f95378a6bfa26dd53",
      "sha256": "9ea6d5ca304f90ba591cc4d259cc5e15907658b11c8a2d46bdbef3ae0a92c4ac",
      "bytes": 2731,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Murtazin [SwampKryakwa]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/11090.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11090.dat",
      "source_sha256": "aba9107a06f8d326c3dfe40320d5b661766223425d606b1232b5c85e4a35887d",
      "sha256": "eacba769220f3b71ab2c78435e75a647b0aa9bab85121aeb2850da8a79bb8506",
      "bytes": 1494,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cyli.dat",
      "source_sha256": "4a742c2765b6ebf98245baaf8a160a4ff587fc93d36c8ee2b9074712a2f968c4",
      "sha256": "4a742c2765b6ebf98245baaf8a160a4ff587fc93d36c8ee2b9074712a2f968c4",
      "bytes": 2687,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/confric5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/confric5.dat",
      "source_sha256": "171ab5f7673337292eaf1477798e7fea5163cf409c379dce04f22c755380dafd",
      "sha256": "e79f66c9707da62f6dfcdb14d904a06e38cbcc2e8dd1fcfbaa32dfbe25fc96bc",
      "bytes": 19013,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/41769a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/41769a.dat",
      "source_sha256": "0b069ab042f2cc8297a52e76b49a06e504cd4e9a51f02d6aea8c63f686c28ff8",
      "sha256": "b92da710238134d5363604a47a39092de33f99d7a0b7f1a059803ce9aef1cf05",
      "bytes": 1030,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Takeshi Takahashi [RainbowDolphin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/87994.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/87994.dat",
      "source_sha256": "1a6c0cb9de6da1175fbdf0bd4b7218c1a39e6dc1ff5e53b5d6080267267ee2e8",
      "sha256": "24369ddb93614186642c2a7e89f5c336f15e60149c099ae04e88a0218564b023",
      "bytes": 722,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/60477.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/60477.dat",
      "source_sha256": "838a96304d5ab177a8c7bd2805eacdfdbfeab71fb86802b81b3523484f4df58b",
      "sha256": "423d429378bf26745b7b58fed7fc8325083cf31bd1b15780df9a7e702d10886b",
      "bytes": 358,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2429.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2429.dat",
      "source_sha256": "65cfb3a695f389a76746cda89fdc2b487ff85e090b3cb03483cea463ddf44fbc",
      "sha256": "cea93d87fa4156da1221053d4e311d6b75b59760c081ac31141da1707adf28df",
      "bytes": 2609,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4disc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4disc.dat",
      "source_sha256": "1d4662b73e3196fadeb5ecf2fd27f3dbf7cecce0802cf3d7108ab67bb380eb15",
      "sha256": "1d4662b73e3196fadeb5ecf2fd27f3dbf7cecce0802cf3d7108ab67bb380eb15",
      "bytes": 803,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4cylo.dat",
      "source_sha256": "4fa9f597d775c7f15e3fc66f60e20d914134d13004b485488b7dbff684776232",
      "sha256": "52429e76da96781a14b7b2444263e58e2227042ef083fa84e946f700c62a5110",
      "bytes": 420,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3u6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u6.dat",
      "source_sha256": "362b5deba42781b7ec9b0616c62c242fc46a051edb3ad3e9c7d800d1929bc22c",
      "sha256": "362b5deba42781b7ec9b0616c62c242fc46a051edb3ad3e9c7d800d1929bc22c",
      "bytes": 630,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-16cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16cylo.dat",
      "source_sha256": "6cef884c4f96ec15f5bd1428264af2efba4443cb1e47ead116a8a094febefc67",
      "sha256": "0d370ab7e67f199f33082ef70fd6b45c9e95804ffe2c5577ced59680c9d3fa61",
      "bytes": 427,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/3-8cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/3-8cylo.dat",
      "source_sha256": "3dbb8b5d2f466cd5619485804d9e4218c9dabc051153a9704b698e6536b01506",
      "sha256": "58332ad32d0a8093a26a651a1642343b880ae842d6ac2a869f2494195187a2a6",
      "bytes": 521,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Ulrich Röder [UR]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3460.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3460.dat",
      "source_sha256": "a236ed5a1efb4844f2eebafc6096a90571607af30e287b307400dcdea44f438f",
      "sha256": "09c4faf59667f890c9ce1b154793d3d494880bfe0e302e4dc1e2b2f7bc1fde87",
      "bytes": 635,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box2-11.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-11.dat",
      "source_sha256": "7f29fb8601b419207b5c855af8fad8abb55a967ec73f3d8be841d370c360b97c",
      "sha256": "7f29fb8601b419207b5c855af8fad8abb55a967ec73f3d8be841d370c360b97c",
      "bytes": 489,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32524.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32524.dat",
      "source_sha256": "2c2c55243d404a65b013ea96aeaffc398cb65ae4a0be1fc7246c8a44e0f22947",
      "sha256": "0522909e34974de353bc0ab303b734cb08bb2e87283c6f1d9527aa44e6b56af3",
      "bytes": 1477,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4032.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4032.dat",
      "source_sha256": "5fae837faef6e689f8933cf635de33f2c8d879c8dcd235a4affd518841249426",
      "sha256": "70eb10bd03de47c82257145168d7db19c27a61ba0c6f4ea7c9bd755e576e0dba",
      "bytes": 323,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/43723.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/43723.dat",
      "source_sha256": "6f78cfb24cdaa114c6c753a04f129c2118e6ea551b27a68a0ba791d4841f09df",
      "sha256": "0db0dd4fb98af6fbabc78bcb131e6173749091fa828b3337403d2c5f80c142fa",
      "bytes": 314,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/30414.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30414.dat",
      "source_sha256": "2aedeeaab777539bf76f6a2ad23a9a698c8aa27a3eed82433f0cd3a18d27f90c",
      "sha256": "01fdc52bff7f434cb5cb0517aa778aea16192895f6683746b1b00cad774d83af",
      "bytes": 3974,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "R. M. Rodinsky [dublar]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4cyls2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cyls2.dat",
      "source_sha256": "77a3bf3859fa972a5d047721ef18603694f1a6f83543f955240990be9c9ee9bd",
      "sha256": "77a3bf3859fa972a5d047721ef18603694f1a6f83543f955240990be9c9ee9bd",
      "bytes": 1189,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4disc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4disc.dat",
      "source_sha256": "a00b5547776f61a7389d303616987c76b3c4de86ad8ec32f22857e1bd5e5e40f",
      "sha256": "a00b5547776f61a7389d303616987c76b3c4de86ad8ec32f22857e1bd5e5e40f",
      "bytes": 1137,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-4chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4chrd.dat",
      "source_sha256": "a735a3d5f7652eb4c1ec7fd2fc2d6fcbb0d54cd647cb92c60e64dd3ba000b0a1",
      "sha256": "a735a3d5f7652eb4c1ec7fd2fc2d6fcbb0d54cd647cb92c60e64dd3ba000b0a1",
      "bytes": 910,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/15068.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/15068.dat",
      "source_sha256": "511c620c73d116a9564248a4adb0f564b90f12f1428a4a9276b4bae4f9bd7e4c",
      "sha256": "2651709faadf2ae018d55c3003120f51bc5d354a5c753b37b687e05267dc0fd3",
      "bytes": 420,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3023bs01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3023bs01.dat",
      "source_sha256": "d5d511e8fce3653ea9c0c8662952006394725f4f7a2234842946c417a737ecad",
      "sha256": "638d5f3386760cd8001dbdaebf34617b07bd33ebf9e2696edf8ed90ada5d1ba1",
      "bytes": 801,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ndis.dat",
      "source_sha256": "97e394834789794c8635261fa604ad8e69b4c6872d0cd8d7506408b80023f408",
      "sha256": "97e394834789794c8635261fa604ad8e69b4c6872d0cd8d7506408b80023f408",
      "bytes": 615,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-16edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16edge.dat",
      "source_sha256": "42fc4d69af1281b71cb2eb9546e99e8bca2fc231d05a0379e71d4e1c9a60c95c",
      "sha256": "42fc4d69af1281b71cb2eb9546e99e8bca2fc231d05a0379e71d4e1c9a60c95c",
      "bytes": 506,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Marc Klein [marckl]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/14418.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14418.dat",
      "source_sha256": "50df1a37eb8dd726ea0796c6ca6f88f3ab581f81e2682aa3aad24a3b0e881588",
      "sha256": "d6c941abbd8a4d4aa5bb2188566e33d45fba295cdf5a212ed358c6faec2d50bf",
      "bytes": 515,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-6ring13.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-6ring13.dat",
      "source_sha256": "e3f865101c75343748940b4949617f6d24082161ad4a33edcba47977658d0e26",
      "sha256": "e3f865101c75343748940b4949617f6d24082161ad4a33edcba47977658d0e26",
      "bytes": 986,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/63965.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/63965.dat",
      "source_sha256": "1f9fde9d5987f1bcf2e5e3a8989bb262ca2178b97848b5fae4ab85304194f4ca",
      "sha256": "7830d7b27a93dae84458463bf4d141298874b705277cb0bc8371f8f127cef2be",
      "bytes": 1004,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "El'dar Ismagilov [Eldar]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-12chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-12chrd.dat",
      "source_sha256": "fe2a0252d971dc65126755c4fdb7db900e229dfdce712b42ce9510c7b0390e26",
      "sha256": "fe2a0252d971dc65126755c4fdb7db900e229dfdce712b42ce9510c7b0390e26",
      "bytes": 539,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4edge.dat",
      "source_sha256": "665400f76566b161c28303cdadce40d17d979a8ff9a8a133675af2d17fbe6763",
      "sha256": "665400f76566b161c28303cdadce40d17d979a8ff9a8a133675af2d17fbe6763",
      "bytes": 683,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2430.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2430.dat",
      "source_sha256": "7a41e19061815c561d0930d76bffb0abe38b6323cb72d183b8259042812f7610",
      "sha256": "c37f760a8b47afd6bcf8b87baf3094bb48419037edb0d65591c3e755b1916ba7",
      "bytes": 2187,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3010.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3010.dat",
      "source_sha256": "7d1cb3082199042666045d92388b3b3ab697f969268e87a6c001f80f92a2e0b2",
      "sha256": "8818f8e82090579f5fdafa2a32e24323757da87f7849c34838ad24d97f54fe71",
      "bytes": 801,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3u2p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u2p.dat",
      "source_sha256": "df73118b95f23d693c3b7d25c57c483db3bf61ae017d757848119955d28d59e0",
      "sha256": "df73118b95f23d693c3b7d25c57c483db3bf61ae017d757848119955d28d59e0",
      "bytes": 818,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box2-7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-7.dat",
      "source_sha256": "e0474c5ad7fb9ff77b67883a5b1e327d028e3eb4e59921a626b4215632dd9f00",
      "sha256": "e0474c5ad7fb9ff77b67883a5b1e327d028e3eb4e59921a626b4215632dd9f00",
      "bytes": 577,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4032a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4032a.dat",
      "source_sha256": "ac5774e2a8eeb9811db795707f6c03cc0b834313b9b9ac5ba25dbb576c9851cb",
      "sha256": "7f15a725e6869fe0c7b977f9aabe96f7ee97260842ed8f20f4387996c0fc60e4",
      "bytes": 1681,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/6141.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/6141.dat",
      "source_sha256": "fb2cd4fad207392508bd2ca8b5469b1c351b692e111aa06b55da55d53fd44dd7",
      "sha256": "e478866dd21d44746c7a6e05798bd83ff528dfc8633b5cc94162f4c810b894c9",
      "bytes": 1076,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring3.dat",
      "source_sha256": "1f2835ac308154edc2d6f479d8e742a55be981f6167b20bfa100c195bc0731dd",
      "sha256": "1f2835ac308154edc2d6f479d8e742a55be981f6167b20bfa100c195bc0731dd",
      "bytes": 1628,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4ring12.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4ring12.dat",
      "source_sha256": "1039eb4b2b4fc4fcef26a199f71540c8629d4521720fbadb244f14c4ee06c2b5",
      "sha256": "1039eb4b2b4fc4fcef26a199f71540c8629d4521720fbadb244f14c4ee06c2b5",
      "bytes": 3984,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/60478.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/60478.dat",
      "source_sha256": "39e307038b6a5b2f0124891de47949dc5ffb36233b5f4fa7cdf43f2d159b86bc",
      "sha256": "075bf82b7f1a1bbee7964264526a4e8ac16fb192a153902af7c3f68172b473e9",
      "bytes": 1162,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/14419.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14419.dat",
      "source_sha256": "6bc91fe4e89dd12f56ead36d7af3cf13fcbbd9798bfbe01bfd8a71d9234d1b12",
      "sha256": "ca59c5899c292a86ac0049a3b8de90d81c28463c2fc5704e38b98f707704df61",
      "bytes": 665,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32013.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32013.dat",
      "source_sha256": "0de3200d99cc000fce0d0849f1da2200f1cb2c518a9fdf0e58e9cddca3cbab0c",
      "sha256": "ee271e1378c1776b9014b1bc9586cfa05f24b2f23e47410d3b7f6f2d7a2646d1",
      "bytes": 1775,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Lutz Uhlmann [El-Lutzo]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8ring8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8ring8.dat",
      "source_sha256": "b0402520ad7ae5786bd5a4cb992951d9a476e5802badc2a2a4fe9a43478a8572",
      "sha256": "b0402520ad7ae5786bd5a4cb992951d9a476e5802badc2a2a4fe9a43478a8572",
      "bytes": 801,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4chrd.dat",
      "source_sha256": "ccba3a97b5cc358754e476b78b4ce61cce5f404cd15e37471b73df3e81784aec",
      "sha256": "ccba3a97b5cc358754e476b78b4ce61cce5f404cd15e37471b73df3e81784aec",
      "bytes": 743,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring1.dat",
      "source_sha256": "4ae21061a6d0c9c80c608decb750f16fe1d113d84e08ef2f6082bcbb0f55194c",
      "sha256": "4ae21061a6d0c9c80c608decb750f16fe1d113d84e08ef2f6082bcbb0f55194c",
      "bytes": 1641,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axlehol2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol2.dat",
      "source_sha256": "9d3e161068b049c3a21fbb8c0970d8264215c08bfcefd3508b8bbff47974a319",
      "sha256": "9d3e161068b049c3a21fbb8c0970d8264215c08bfcefd3508b8bbff47974a319",
      "bytes": 762,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl5hol8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl5hol8.dat",
      "source_sha256": "95b2d384c0697cd5dd4ebcc9fd4ab2d005307af5aa611bea20ce832a91f8bc68",
      "sha256": "95b2d384c0697cd5dd4ebcc9fd4ab2d005307af5aa611bea20ce832a91f8bc68",
      "bytes": 2237,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ndis.dat",
      "source_sha256": "21202dc15823f4336bc2544244d0b539b76745c89f7a59ad18cdd03ad45cc543",
      "sha256": "21202dc15823f4336bc2544244d0b539b76745c89f7a59ad18cdd03ad45cc543",
      "bytes": 1219,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-8chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8chrd.dat",
      "source_sha256": "282b0d7dd4e73d273b9cbcce88e30889cce3b44aa8574a25382fe526248d5426",
      "sha256": "282b0d7dd4e73d273b9cbcce88e30889cce3b44aa8574a25382fe526248d5426",
      "bytes": 611,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/connhole.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connhole.dat",
      "source_sha256": "577a734213f632d44646c02d5f9b0f7581df1572aff2f213791bc6172d623af4",
      "sha256": "95efd1d2c34814e06d80f4311df5d915a1e948ffb0f93fff431bd3c4a690f2a8",
      "bytes": 748,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/60477s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/60477s01.dat",
      "source_sha256": "98b912f2b4564702bb52631f13b4b505b66d666ea9ccb8d588bbb79081a8352a",
      "sha256": "b4ba590153e3fa02575f1b681d17c51ead0ca44d34fe0ba7ebeab922408ae8b2",
      "bytes": 2189,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box5.dat",
      "source_sha256": "ccb7b8a1d36692335b10ea6aa196849afcad4b15331683ed8112a10b50977318",
      "sha256": "ccb7b8a1d36692335b10ea6aa196849afcad4b15331683ed8112a10b50977318",
      "bytes": 963,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3705.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3705.dat",
      "source_sha256": "ed90738971675e2dbd05b5a0aecaccf2da32e62b4e9085b886f084de890a853a",
      "sha256": "1a87b2bcb8acaf683f1728a6c0de8ea53c9f8f05dfbf57375da48e6b58450ca6",
      "bytes": 686,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3031.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3031.dat",
      "source_sha256": "e67436538e47cb38b8352e91c2b5b7c7c274e070912603e5e9fc0b4513962338",
      "sha256": "27ed5db0bcda4d06108d90a9eb8c0f06f674d7a8a3946e362a6fa281e9ff4038",
      "bytes": 2235,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4tang.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4tang.dat",
      "source_sha256": "4eb5b51b824675756efd7e74e1141aaeaa9520517754d3bd0cfc1f591a0e04b4",
      "sha256": "4eb5b51b824675756efd7e74e1141aaeaa9520517754d3bd0cfc1f591a0e04b4",
      "bytes": 585,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/40379.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/40379.dat",
      "source_sha256": "5a119a3914cbfc5fc144cb24b8c9ee6767f6b1912b6c521ff6fe1b4d9e80d90c",
      "sha256": "72d5f6e52aaded00572dcf9809920622b1aa0c6f43027f6e09edf4e46ee34f04",
      "bytes": 101094,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Bernd Broich [bbroich]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32525.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32525.dat",
      "source_sha256": "96eba31f9a5e2b7df6305fc73ce60881b7dcee02685ae17264d916725c8039c9",
      "sha256": "112bc92c4559d60b1d3d648f7dc0590d5be879cabb6fda25f3e8f6b84e0c2ef0",
      "bytes": 1978,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cyli.dat",
      "source_sha256": "5a7168952a5a3570327873b9a5802fa7b3be40967ab78c03b6a2bfd4419a1f10",
      "sha256": "5a7168952a5a3570327873b9a5802fa7b3be40967ab78c03b6a2bfd4419a1f10",
      "bytes": 1044,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8edge.dat",
      "source_sha256": "50436a0bce461198c342dccbccb658a1bffae13e44b7c48689b158c946c2c2ab",
      "sha256": "50436a0bce461198c342dccbccb658a1bffae13e44b7c48689b158c946c2c2ab",
      "bytes": 480,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3u8p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u8p.dat",
      "source_sha256": "0f6187106f023d041dcfd2a24e9f5a2a0c37b5c41b0ff171267ae776a8f16760",
      "sha256": "0f6187106f023d041dcfd2a24e9f5a2a0c37b5c41b0ff171267ae776a8f16760",
      "bytes": 737,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/14418s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/14418s01.dat",
      "source_sha256": "43c34331b9b44b63f90a268506c5d7c44368b07d83c64b1a352cc027e831da11",
      "sha256": "f18458d86ab67b7a31b7c8f3b472663e5f48441d747ebae81371f56a7faaa71d",
      "bytes": 1447,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug10-2x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug10-2x2.dat",
      "source_sha256": "860d8586325b33654acf4b20d9275ff078955468eaf86af3c6d7adc624446512",
      "sha256": "3a24b2d890dddbe29192cb8b23e4cf39a9d125ebede52cebbef9be6f7db14abb",
      "bytes": 834,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud.dat",
      "source_sha256": "db037d518d7c08bcdc1f0e7497f4f98e97d99850531dd62d602965520f3bf8f4",
      "sha256": "407a8aad1581c2ef07fc1a1f5aabc4e3b64161f1a2803e154cee75da4561d2dd",
      "bytes": 742,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axlehol4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol4.dat",
      "source_sha256": "256ebbe25364125c893ffd4dbbe5131e46aae4b961611848b3bfde88f855673c",
      "sha256": "83ee43df2599636b3e8d4cd13ec736973caf0fe4c81a272095ab42545b36b87e",
      "bytes": 3466,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring2.dat",
      "source_sha256": "6fb38804b1f5e9bee8c0b80caf1397b09454fc58b048dc19045b6f37c8762ab0",
      "sha256": "6fb38804b1f5e9bee8c0b80caf1397b09454fc58b048dc19045b6f37c8762ab0",
      "bytes": 1628,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3832.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3832.dat",
      "source_sha256": "4928810faf064116f14126735c7a273df15c662fe1d648991c3a3c4cc79b0d49",
      "sha256": "1dd22c2e1af48c4771fc2b09e5722be02983bf236a81c30584d011e9dab5391e",
      "bytes": 2258,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3623.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3623.dat",
      "source_sha256": "08f74845fceb4b39976d8ba56c0d59970483b8956cc59eb08e9f01ca579467e2",
      "sha256": "0a7731850fe984b2220d70064a78d50a71ff4e2e085e40f01aae369bf829befb",
      "bytes": 629,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/joint8ball.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/joint8ball.dat",
      "source_sha256": "db77f15924894538364a9ef227ebeae84a2df1defa1b3bfb474ea29cd0f6f153",
      "sha256": "aef18261cebde99dbd2ecd5dc275ecf3ae6533c5776105ab895c20a2aef68929",
      "bytes": 436,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4cyl1sph2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cyl1sph2.dat",
      "source_sha256": "5899ab994c9e2c2a6ed54f01d195c3ff2990f617b64243c06e6b53abfbb3771a",
      "sha256": "5f33c67bb4170166bb04013c6a4791c868932a3832c0efb59bf5cc7aedf3aea5",
      "bytes": 1565,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug2-1x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug2-1x2.dat",
      "source_sha256": "9cd034fe99c6efd6e158c73a8a95d7b0e6ff4f1671a7ee22e2323c74a43b7f1e",
      "sha256": "454b0cb7790fd7d30248065f4a49557fd688a61fe855e679d4006e6d4b4ace13",
      "bytes": 363,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3710.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3710.dat",
      "source_sha256": "1a2d17e3e35750ccf02a54c7aee0cf7485c1c8596492746fc798d341399a3a6e",
      "sha256": "a2237801ee1d26feef0ec5010b89d42550ae5359e9dc4dc042cafff7e13a19a8",
      "bytes": 635,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3941.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3941.dat",
      "source_sha256": "d0cf49833082c39c358c248fd19c7568030ffc43d7add011feae168d5ad6e693",
      "sha256": "e081b0cf6fe1a947bde2ebe7b3036e9b8d8e6a293deec45747bf8e880b41f26d",
      "bytes": 731,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4cyli.dat",
      "source_sha256": "d486780f0f84893899d9eadcd13150f13a42e15e77a3cda38cdf24ded98862c6",
      "sha256": "d486780f0f84893899d9eadcd13150f13a42e15e77a3cda38cdf24ded98862c6",
      "bytes": 1543,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box4-1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4-1.dat",
      "source_sha256": "2ed58df5da841827dfc5f9ac11c0bd7ffd8a455e46f166638e635f61a014b44d",
      "sha256": "2ed58df5da841827dfc5f9ac11c0bd7ffd8a455e46f166638e635f61a014b44d",
      "bytes": 973,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tore Eriksson [Tore_Eriksson]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3010s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3010s01.dat",
      "source_sha256": "f4616eee36d2474da47fae07a5e1ca59888e580854be17a1a9220d0f88c75333",
      "sha256": "8a71d746554d05a2a9fe1a6281cb8096b0f23de0bc0e058915df4094d6bfb96d",
      "bytes": 958,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ndis.dat",
      "source_sha256": "7557eae598be3f530b840471535198e6b07b03486ffbcc18a00e862c3d25d925",
      "sha256": "7557eae598be3f530b840471535198e6b07b03486ffbcc18a00e862c3d25d925",
      "bytes": 874,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/40378.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/40378.dat",
      "source_sha256": "318bc67762903cb446a618937fdd814926bbb6b307631327f0d017cde0d3e7a3",
      "sha256": "e8f069d53f80dff9ea7ea4ef0066d3b310259457ef0e36fa45529c0559841267",
      "bytes": 103883,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Bernd Broich [bbroich]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3700.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3700.dat",
      "source_sha256": "6cb6522c580754cf970dad0fae688bb78cb3253a7237038dad83965fe47cfec6",
      "sha256": "db2f75922c8017d53518defc9e84bd07b84b9767da1ddf39faeec3b6671718f0",
      "bytes": 2576,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/59900.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/59900.dat",
      "source_sha256": "8416701912ed13937743df8dd877a2a1254925efd4adebb77950f48c3d9d5156",
      "sha256": "b67f0ee45b5e3b5403e6df250b0dedc02564154255b97bae1abac3207b2575e0",
      "bytes": 1927,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/85970s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/85970s01.dat",
      "source_sha256": "670fd38242b77252365c9d4d065558d7478b39a440228e27b64967f05e3d6899",
      "sha256": "e5f57b558983e66c7da3ab19c2c2377267e2c10ecbd559cd4ea4c711c51d92e4",
      "bytes": 30183,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Joerg Sommerer [Brickaneer]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/41770as01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/41770as01.dat",
      "source_sha256": "8d88de31c2ec2050977671b63f6115ae47b72f2c01d9f863bd34ecc00760165d",
      "sha256": "1ba884a47afd380ef1989fb7a3355a638f95d8421b182c090e4d970bf42db683",
      "bytes": 7116,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Takeshi Takahashi [RainbowDolphin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/15068s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/15068s01.dat",
      "source_sha256": "41456734d1b26b9b448eb2fde7f0d4df463c1e2085b79ca9731a0a35554b3c58",
      "sha256": "9ffdbe8d92d8015f84b0e5ebfd2b3443d8f73ca21ca6d3e6e23da2787b4011bd",
      "bytes": 5367,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/npeghole.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/npeghole.dat",
      "source_sha256": "cd0fb8b9943601de2666af54c6fcc9d9903422ee0ab4e4474c8d6c94bfd9287c",
      "sha256": "39c88288bdab42770d9ee95c014ad8d4c51cf3bb9d056ac399b5c2cb6d9ac79e",
      "bytes": 759,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Murtazin [SwampKryakwa]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3460s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3460s01.dat",
      "source_sha256": "0d6285f8a937cef6d6e76bb00f6356f77198a5872df7554a3432120da5eaaa86",
      "sha256": "72ec01cac432cbcd1c44f7afc4c294c370bd6d6642f9ea7a7393eb4a7b276b61",
      "bytes": 662,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3666.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3666.dat",
      "source_sha256": "f4fc83d8c3fc1df32c1a217dc09775a99fad1ced348cffc5167f9c6a69aa9bca",
      "sha256": "41733d38924168ca7565cf80e9d5faa790df940564c50e57ea001c517cd1e9ce",
      "bytes": 635,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3u4p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u4p.dat",
      "source_sha256": "1d63ff287fe62f8636cf59cfdfce5118e1017f66559aeb32abc642bacbacd361",
      "sha256": "1d63ff287fe62f8636cf59cfdfce5118e1017f66559aeb32abc642bacbacd361",
      "bytes": 685,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/87747.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/87747.dat",
      "source_sha256": "3abe84ff43891dd04379aa5cf689305df199a08c2bb295840d00b7622b56d6a4",
      "sha256": "036ae69e008723e62f04c58ea4795178ba3f03ee75bd7a3878b6aba6b2db4794",
      "bytes": 2028,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Joerg Sommerer [Brickaneer]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/43722a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/43722a.dat",
      "source_sha256": "cb9c4cfc5c9254fab8191a085ed77d170e16d6f90647bac2c36ce666c1764f59",
      "sha256": "d6e5d59bedd6d198b8ae379f60ff5dc5d9c25ef2939559c10ac5f01cb445feca",
      "bytes": 893,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-8cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8cyli.dat",
      "source_sha256": "494069ca353e41885bf8f5b6b3ddc9b62aabeca3eedfe6aa5597ac8f12ca12b9",
      "sha256": "494069ca353e41885bf8f5b6b3ddc9b62aabeca3eedfe6aa5597ac8f12ca12b9",
      "bytes": 1361,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8tndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8tndis.dat",
      "source_sha256": "5e3bd48d2e7565fc97a8936255339d9682897b43a38f69da43571f42a4a2248e",
      "sha256": "5e3bd48d2e7565fc97a8936255339d9682897b43a38f69da43571f42a4a2248e",
      "bytes": 346,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-16tang.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16tang.dat",
      "source_sha256": "3bf6430f99195afabdaaab755a660c0978080851fd6f514f50ef0e578e6f82e2",
      "sha256": "3bf6430f99195afabdaaab755a660c0978080851fd6f514f50ef0e578e6f82e2",
      "bytes": 309,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4ring3.dat",
      "source_sha256": "4048b121d53509363cfaa7422648dd29b2eeb93074279feb0bcc7a45bbb7c2e1",
      "sha256": "4048b121d53509363cfaa7422648dd29b2eeb93074279feb0bcc7a45bbb7c2e1",
      "bytes": 1198,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3u5p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u5p.dat",
      "source_sha256": "0f52d5c372a303f508113ace2c7cba6d52b46171052e76a88266679a74f17ea5",
      "sha256": "0f52d5c372a303f508113ace2c7cba6d52b46171052e76a88266679a74f17ea5",
      "bytes": 658,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/98100.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/98100.dat",
      "source_sha256": "1a7bf4c7cc90cb426ac1070d127a6b3d20282e245f8662694825760c733cd25a",
      "sha256": "a81b1b0f04b83f7200f40a8896843cba7b5bb442d48ae753c27f9ff40a8b3d4b",
      "bytes": 717,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3003s02.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3003s02.dat",
      "source_sha256": "ceb77e4263964fc1658630d9533118d8feeddf2aeb7d0a1116c6e5bc2318a92f",
      "sha256": "5b58ce2af983f6330e445645f6142302b4cb6fe2cde7dbd9611b0c2baef952cb",
      "bytes": 756,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-12cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-12cylo.dat",
      "source_sha256": "aba0697449741a95889cb0faf8d6231777086ebed8ee1956ac304bd32b208c6a",
      "sha256": "add89982d8c32c97300476f4ddcd57cb5c7b8619b6f9ca00b04e57fab12e1450",
      "bytes": 488,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/3-8cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/3-8cyli.dat",
      "source_sha256": "71e6dfecfd02d2a202437af82fb89b4b7d4ed3199e7feb38e591f81e6e273f94",
      "sha256": "71e6dfecfd02d2a202437af82fb89b4b7d4ed3199e7feb38e591f81e6e273f94",
      "bytes": 2875,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/4032s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/4032s01.dat",
      "source_sha256": "0b12443c9f5975afabecf7ad9e50384a0237deb74d3fc641705e25cf3a544bb3",
      "sha256": "977a76d8c3f6731d03b4779f90f18cf746f7e641904dea9258a1dab5fa591d4a",
      "bytes": 1681,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud10.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud10.dat",
      "source_sha256": "f7dc3947e0f3b81fadffe6509c52723940dfd4d36e30049874d95784a864315a",
      "sha256": "58d7bf009ca91bc8f0f8ff303f3a57500c2f25230e0f047350793afbb71d4768",
      "bytes": 1831,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-24tndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-24tndis.dat",
      "source_sha256": "d5a37a734ec0b3fd1a81f4ac1858e8bc32639740a5be442a2a41a5173e30c36c",
      "sha256": "d5a37a734ec0b3fd1a81f4ac1858e8bc32639740a5be442a2a41a5173e30c36c",
      "bytes": 470,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4stud4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4stud4.dat",
      "source_sha256": "cc27fe29307676a8f46d25ad35304ce2e576f3c8bee81c20cb461c401512b58e",
      "sha256": "4ef2290e4e871f4b4ab49e661bb04d7934bd06344c29be5b1d0f94c699ec1bba",
      "bytes": 437,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4cylc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cylc.dat",
      "source_sha256": "fdcb54ba2e2731cbb86ea6b2fddb25c7dda060a7780629a72003e0278805dd30",
      "sha256": "99908b5292d91a6f708af8cbe5a24892d1ed125fbb1d690261cc65a56ed46257",
      "bytes": 474,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4ndis.dat",
      "source_sha256": "ff6685838636e7ab6152356d8f09e4f00a38af0d878b0881423f5c45fb868f0c",
      "sha256": "ff6685838636e7ab6152356d8f09e4f00a38af0d878b0881423f5c45fb868f0c",
      "bytes": 692,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/npeghol4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/npeghol4.dat",
      "source_sha256": "ac8a4de8537ea34e4c564cf354c4a8bc9120cc3f4504661038e3f7318812679d",
      "sha256": "ff71b569feabdffbd0739a5ca342434328d1b442e36e4e891bdb38530f76054e",
      "bytes": 1193,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Murtazin [SwampKryakwa]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4edge.dat",
      "source_sha256": "d7f5aff979bc227b601abbb8e0226d6055d08eafb5faaf507b3055f712cd4c04",
      "sha256": "d7f5aff979bc227b601abbb8e0226d6055d08eafb5faaf507b3055f712cd4c04",
      "bytes": 831,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3020.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3020.dat",
      "source_sha256": "551e433cc4bcfdeeb6e390e509d52ee2e62c90d3eae625ee36928ef32291bb79",
      "sha256": "5455ab5298a3844f8831512fb1acf440a0bf279aed51e8e86fb6874bd64e8942",
      "bytes": 1484,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/53451.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/53451.dat",
      "source_sha256": "84c97139fbc684919588a7c160858f55fe7fa9517527ce3481ec30419c1bed55",
      "sha256": "a348c550de42f76b6d4bde092ed36f03f6f6e7cd380531f338e1d14c61d44718",
      "bytes": 34821,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Andreas Weissenburg [grubaluk]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/3-8cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/3-8cylo.dat",
      "source_sha256": "357980a30dd89cdd6f6e0d46e78a1984a900cd22a0d7b1b75662fdd40b53c880",
      "sha256": "2a7ddc1aac53d59dba649ae23ed3e2976b5240d0c92567e428a260114f5ba7d9",
      "bytes": 435,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/87747s00.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/87747s00.dat",
      "source_sha256": "1426efaf77cb35070deb746169b5c008d457b2ba0212c579531f61ba9be2436b",
      "sha256": "1426efaf77cb35070deb746169b5c008d457b2ba0212c579531f61ba9be2436b",
      "bytes": 70341,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Joerg Sommerer [Brickaneer]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con15.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con15.dat",
      "source_sha256": "5d77b989bff18aabcdd79cc106c040d23e2fc5743ff5d4996d6d78def91e464c",
      "sha256": "5d77b989bff18aabcdd79cc106c040d23e2fc5743ff5d4996d6d78def91e464c",
      "bytes": 2499,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4cylse.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cylse.dat",
      "source_sha256": "3c2c53a4ffd03dba04d3410b11763a020c603eefaf5ab425c282fb18744692c8",
      "sha256": "c78fd77b08ad0ec528faa926114ae4907c2e7b33c38218e4f6c584a88e202567",
      "bytes": 660,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/3-8chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/3-8chrd.dat",
      "source_sha256": "38da11ee98a5af1aa8519ef2695f07f9182b1e3d555d02724c0f0f3eaf5d2631",
      "sha256": "38da11ee98a5af1aa8519ef2695f07f9182b1e3d555d02724c0f0f3eaf5d2631",
      "bytes": 351,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-2x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-2x2.dat",
      "source_sha256": "16114159ea25719341a852d5403dc9982a6211f2fcb23f5c4c3eac05a2ad43f7",
      "sha256": "603779c0fa898af5eb0df8e10b0fb2d7497d979f51d3429ce366ee0c9f7a4559",
      "bytes": 809,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8cylo.dat",
      "source_sha256": "870bbbf6052e075598de7dce7efe7a139ea5189820e7a296442fe2b3318c18bf",
      "sha256": "1082de713b8b09b9eb95ef5f256387fd00ef00ec464996c487e4f539d0a5977d",
      "bytes": 414,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-16chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16chrd.dat",
      "source_sha256": "e429dd760eb6f0cf460a74e6ebf52c023bedbdea82de7801efa1694b5a1a82e8",
      "sha256": "15aaab08a97f05f9d4d2c63c7d11ece9e2dc472930fe6d8d8577e67c52d6287d",
      "bytes": 712,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3062b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3062b.dat",
      "source_sha256": "cea4d47bad2ba17130e8fdd298f4f0b0dd4efdaf6edadd3bdd5e089e1cb60bac",
      "sha256": "f6da186437af015e1ddec4eb19ace02e1b88f52a73a03de16aca979cfee023f9",
      "bytes": 944,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/confric3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/confric3.dat",
      "source_sha256": "a94c90c0506925a3f018449053ab790a98ecdbdba6d793aafe26d6a75e0ee8d1",
      "sha256": "46cc3d8bc70d39265640ea0d2dec6a2585999294f9cb346305cf3dfa21473670",
      "bytes": 2454,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring3.dat",
      "source_sha256": "641f3ae7395e7d38e57ab918928ac19209ed72e8474fd1646e2d70f223c4a0ce",
      "sha256": "641f3ae7395e7d38e57ab918928ac19209ed72e8474fd1646e2d70f223c4a0ce",
      "bytes": 610,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-16tndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16tndis.dat",
      "source_sha256": "98bf2c3ef480d10f1fb8aac9af0240a0a0704b395b9fb61373c719648ae782d2",
      "sha256": "98bf2c3ef480d10f1fb8aac9af0240a0a0704b395b9fb61373c719648ae782d2",
      "bytes": 304,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/59443.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/59443.dat",
      "source_sha256": "4c451f31b44a80755de7ed364ddf606a472bdbdf4b36a410646b09b3623911f5",
      "sha256": "965f42396f3cb5686a5d5cdfbced874152d677270009612a94bad6a8c2df899f",
      "bytes": 5429,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/44224.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/44224.dat",
      "source_sha256": "c9783a9c8aebeeb04f226a9d50d12ae676d2ca53762236a86950eb6bdbcfb18b",
      "sha256": "98f807a035cf5fc5082e811a2c35a07eeed9f58decfb786a450a05cbe75f7573",
      "bytes": 8977,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axlehol8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol8.dat",
      "source_sha256": "e3cf8856c972ecaf486a344c171cb4ab601efcb08956bd7b6cfafa39b0439493",
      "sha256": "9abe1cbf32250bcee6f70d1b9bffc271344c5f790ea23cf8606429d09e28e2c8",
      "bytes": 1750,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/connect2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connect2.dat",
      "source_sha256": "34ff327f32629d65ae37d8ed1f24d9be5951876ca418cfa219c98aca63dc0506",
      "sha256": "7c7119cc86c95b5391ec493141a036175c8646c26bdf20135fce68d1dd46b554",
      "bytes": 6991,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4stud4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4stud4.dat",
      "source_sha256": "7afa4b4fd96a1fab9ecf90c1828968b5997d311ec6eb32021d1ac30334d36c7e",
      "sha256": "c4e7fb72d062d739ce5a99ba06a4a2dc8427d6d9ac69c9a7d6b14012028607cb",
      "bytes": 783,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4cylo.dat",
      "source_sha256": "ce018b080f8d657ed514164b995e119e9ea104a03cd84e6a6f736b40f58252a6",
      "sha256": "390ecc955e3e3f4cd5ce157ec05683fec5e1943746710cd3deb344f8ffd6b84b",
      "bytes": 477,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4cylc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cylc.dat",
      "source_sha256": "0183cffc7f56a2f3e5e3511f0d07ac484d3039c2d41bee802a94344ec95ec8bd",
      "sha256": "4d0ad04115975ec97ff67d1241d97d1c7553df9099bca7a86ce1ce6ceb52de65",
      "bytes": 520,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl3hol9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3hol9.dat",
      "source_sha256": "a99c7a963b46b735e36743f216efdd4916f982b4b984469de5b7e6bddb18e8c7",
      "sha256": "a99c7a963b46b735e36743f216efdd4916f982b4b984469de5b7e6bddb18e8c7",
      "bytes": 617,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8stud4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8stud4.dat",
      "source_sha256": "9395515b1e38008dab61d9a971d9564e36ea6fbe4a32a244c789e8e5a2a58f6d",
      "sha256": "bf561e85b319a2d9ba4219758fc485455079734da21873e07c5ce91b5299f288",
      "bytes": 438,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3005.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3005.dat",
      "source_sha256": "f86e5f3aed432cab8f5dffcf2e41a9f2ee8c3bd4dcad1732da9630837849a4f8",
      "sha256": "daa9cc12d8dcafc6c2a6c3b1225d650b9e812d600a8093ceb93fdeb397f23d3a",
      "bytes": 683,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/43723a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/43723a.dat",
      "source_sha256": "27225adfc6ffa1e36ae9a1a9448fada822a6f3e43c996c5512f5b2d6be24f181",
      "sha256": "e0088a61b37def6ee6c5466c1eefb2243a15b08b28510157665807683f248f92",
      "bytes": 896,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3034.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3034.dat",
      "source_sha256": "035f4ac31ecad8943fd0ac6baa155c6ff38c75a4d8ef1083fb2afa48b166a845",
      "sha256": "309ca4390852fb66806f17006390ff80d7f650995838fe4d1a87e7e59e6bc3f2",
      "bytes": 1979,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4disc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4disc.dat",
      "source_sha256": "3b8faa77185c576085c38f37b13c6a04e2e889eea6a7dc8c4db2d1699a33bcda",
      "sha256": "3b8faa77185c576085c38f37b13c6a04e2e889eea6a7dc8c4db2d1699a33bcda",
      "bytes": 584,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-48cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-48cylo.dat",
      "source_sha256": "0d3b2c6f9dddb5cf047c9b96573049da0c73caf2c81b0656796e62053853a150",
      "sha256": "8f598232a8c25549e4181cd0920f992d3ed98553404fbdf19449496d36bfab9d",
      "bytes": 489,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/beamhole.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/beamhole.dat",
      "source_sha256": "8622d704b75a6f81cdccf99e44f8e88a6b1df024d90e160ff18afb07c482f77b",
      "sha256": "88a8c113a85e1ceb166a6f34db335cada04d38162ce91b8646045b1a913baccb",
      "bytes": 1004,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cylo.dat",
      "source_sha256": "792a01362608c3f385dd7f01a1bd7d19cf9ed8a40f793266345cc86d1d98f3af",
      "sha256": "47ce5c0c2fa14c458445dd10b9d3b99136e9cd0b55fe970d17573e439f53b947",
      "bytes": 421,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/npeghol4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/npeghol4a.dat",
      "source_sha256": "1217309bd824bba07477b53f3e4120aaddf2d8690f0188e8ed2ab6106f6cff56",
      "sha256": "8d44fd7737670362d1f189dc47f86804905618a7db0af39b7f4ea88a865e6c23",
      "bytes": 1444,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Murtazin [SwampKryakwa]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3622s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3622s01.dat",
      "source_sha256": "bb4e34ea6d2c7b7f7591b6051d69fd09f18a52486c2495b27c5baed67ea616f7",
      "sha256": "9a89e4dc2f9d22d1152811306ededd919e1cd22a3e95dfdf2c722596de51475d",
      "bytes": 1028,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Takeshi Takahashi [RainbowDolphin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-4ring13.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4ring13.dat",
      "source_sha256": "d7dfc4b8b151df84300b3419d0f7f024e0caf43d97668d60d786726d4a29fed8",
      "sha256": "d7dfc4b8b151df84300b3419d0f7f024e0caf43d97668d60d786726d4a29fed8",
      "bytes": 1178,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-12edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-12edge.dat",
      "source_sha256": "c1320fa098058f1bb4bb73a4bd02a9533bdcc4f22ac4a0f0a1dcd5cdf85deaed",
      "sha256": "c1320fa098058f1bb4bb73a4bd02a9533bdcc4f22ac4a0f0a1dcd5cdf85deaed",
      "bytes": 584,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/boxjcyl4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/boxjcyl4.dat",
      "source_sha256": "ceb4a5fd46fbff7d2e396afbc308379b914b99556b30a136cfb578a3dc360877",
      "sha256": "8a922e6344c786397bc9276270bdce185685cf32f21eb416d94b01b784b31948",
      "bytes": 1280,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4edge.dat",
      "source_sha256": "db8fd751c8c6b1f72211903adbff3aa90be6808cc4fcff391f1c320adced5da7",
      "sha256": "9935e24ca354e2bd6ec742e4104ca612eec3e4a3c89f55b3c7e571252dddfe70",
      "bytes": 808,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4a.dat",
      "source_sha256": "29e414ab757f2a79073aa0d5d10c4c925da1fc239d20019d7615c06db612e2f6",
      "sha256": "ea160347af7bda0a3df8570013dc58811d5e09f819ecf17f025e2c4a18c2148d",
      "bytes": 926,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-1x8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x8.dat",
      "source_sha256": "e592fd59bdd7333f0430cdd7bebb0d25bfdb3f244af03a17b0be2861c62205b7",
      "sha256": "2bc88f37853d6879c59128334d47178663df7bdfeb4a669279ffd7257d8f216e",
      "bytes": 664,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3941s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3941s01.dat",
      "source_sha256": "0285481f2422f6e098a36f26cb5337338a26048c348a266a2220e154e6f3a7a2",
      "sha256": "caee615c48b322c9ad4fe2492d2a97015bcea8a9a6f41d2eadc6bb1515eb2dd7",
      "bytes": 5275,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-8sphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-8sphe.dat",
      "source_sha256": "37fa33d0b13605e0e1a84b8e0917953d42beebee08dc444e1bd44015acd64d9e",
      "sha256": "f2134d0793f73c443f620e4d700a5c3272222a4a99f42af66cc2e6340dce2425",
      "bytes": 667,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8tang.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8tang.dat",
      "source_sha256": "4f412bd10e7dd081272e6fcbf7480674b639d48e35437c6d006f5bad099e4af6",
      "sha256": "4f412bd10e7dd081272e6fcbf7480674b639d48e35437c6d006f5bad099e4af6",
      "bytes": 419,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/3-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/3-8edge.dat",
      "source_sha256": "2f597879c4dddfff751af3253f7bb2e4ec1c493ee962fc14ff709a3db95aa5f6",
      "sha256": "2f597879c4dddfff751af3253f7bb2e4ec1c493ee962fc14ff709a3db95aa5f6",
      "bytes": 1085,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-1x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x2.dat",
      "source_sha256": "5842fa1baf6ea7f18fe4e355238cd733ff9bdbdc3d722be5cf8988f1c5fce414",
      "sha256": "1865152383a42b7b072a2a80fa7fcedb9efb947fae8b84c86ca88e1ef02a3ff3",
      "bytes": 355,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/peghole.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/peghole.dat",
      "source_sha256": "90c6dba9e5bcdd63955b9a5208f377761850863be9ed26cac7cd2be61ab85c92",
      "sha256": "43475558e4b686792d9a28bfb5c608db8edc0e5f4d527547b0716eefa5ce3c4d",
      "bytes": 869,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box2-9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-9.dat",
      "source_sha256": "4ebaa1a0a59a2e219b61d376e86cad06dbd36845a3c15bcde3e3d44cd3be473d",
      "sha256": "4ebaa1a0a59a2e219b61d376e86cad06dbd36845a3c15bcde3e3d44cd3be473d",
      "bytes": 398,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4ring8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ring8.dat",
      "source_sha256": "e8f7ef17c0d9a9aa11b3ee09f46113f0e0c6d529fd6c24df2b2c74e8eaad6a9c",
      "sha256": "e8f7ef17c0d9a9aa11b3ee09f46113f0e0c6d529fd6c24df2b2c74e8eaad6a9c",
      "bytes": 925,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/cylj4x8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/cylj4x8.dat",
      "source_sha256": "9cbf5025a81af8a9cb07f56b43ec46a587256995c14aadd934b6f70262f523aa",
      "sha256": "9cbf5025a81af8a9cb07f56b43ec46a587256995c14aadd934b6f70262f523aa",
      "bytes": 4035,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/npeghol7a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/npeghol7a.dat",
      "source_sha256": "9e0c2321dee34bb45e80deb19db2d46376e398353e57abbc89f3161af0065967",
      "sha256": "893bd3a40b54abdde3e1df85fae27947f1b3571331f73f7868823bbe35e50dc9",
      "bytes": 1021,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Murtazin [SwampKryakwa]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8-8sphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8-8sphe.dat",
      "source_sha256": "27a7d82cce6d579b6a83ddcccee1c38ec1e37781831dae65b2cdf704d84d64b1",
      "sha256": "7b930d39d2901538e80f4422b00d4c0d7d4e1f20625ceab1c51ea81d64ec9d93",
      "bytes": 969,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3666s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3666s01.dat",
      "source_sha256": "71aefa629ca2df065d9cde349bb46a51a8e59265ad4d74e55da24611095d5538",
      "sha256": "f3bad52945a480ab877fa9427d94e2dab6512b1e4c157a6550212ba3447c630a",
      "bytes": 662,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/43722as01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/43722as01.dat",
      "source_sha256": "e2dddcddb4bf0c30f9ba2f5880d9bca822bde31d07a3bfb094b8b2c4b8711d68",
      "sha256": "f204f0f81ac18ea4393dec39333a78d8392bd1e3196656608ebab336fd494e33",
      "bytes": 4107,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8edge.dat",
      "source_sha256": "eec30153f06bac336ca71ae16b31c5d0c7ae432acb5e91befe37fdb7b6bb1c8e",
      "sha256": "eec30153f06bac336ca71ae16b31c5d0c7ae432acb5e91befe37fdb7b6bb1c8e",
      "bytes": 711,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/confricrib2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/confricrib2.dat",
      "source_sha256": "029431b8493179b67ac662e609f61cac5b75bda8974360886214c1d6fbce9603",
      "sha256": "029431b8493179b67ac662e609f61cac5b75bda8974360886214c1d6fbce9603",
      "bytes": 4462,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4ring1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4ring1.dat",
      "source_sha256": "e40c29daf302d57b488bb8168aab6755d80adb4e30bc8df24ed34cd42b34dd5c",
      "sha256": "e40c29daf302d57b488bb8168aab6755d80adb4e30bc8df24ed34cd42b34dd5c",
      "bytes": 1196,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/phandle1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/phandle1.dat",
      "source_sha256": "3cd5c4eca20ef297d265e4ba7228b04a5fb7f332b89f923ead8366987021d6e2",
      "sha256": "f4beac38563a355074aed380aedfb51a2693278dcd3e3ab14a4818700368d80a",
      "bytes": 1330,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-16cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16cyli.dat",
      "source_sha256": "b60f031d9dfd0995c1741992a5695ee3789419886e8189dead961d05f75f7bfc",
      "sha256": "b60f031d9dfd0995c1741992a5695ee3789419886e8189dead961d05f75f7bfc",
      "bytes": 693,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Marc Klein [marckl]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl3hol3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3hol3.dat",
      "source_sha256": "05fd46a65cb2342d3e88e3789a610b4f17f9fc8fd614f90bf8c2b3f44e13a171",
      "sha256": "05fd46a65cb2342d3e88e3789a610b4f17f9fc8fd614f90bf8c2b3f44e13a171",
      "bytes": 743,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cylo.dat",
      "source_sha256": "d6ca97ee2e75918b3309a5c88aafcd2455b3a316f7cef8963517c19f1d86b38f",
      "sha256": "8f6e757b6d93b445406cd05d7d9bfc9ea3ef174801e5e15cc2def81420f71857",
      "bytes": 416,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-12cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-12cyli.dat",
      "source_sha256": "a645a42a5ed912a059a9336ab1449d02efd067008f034549cc8c5ae488159fd3",
      "sha256": "a645a42a5ed912a059a9336ab1449d02efd067008f034549cc8c5ae488159fd3",
      "bytes": 1027,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/confricrib3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/confricrib3.dat",
      "source_sha256": "4c1187b3607031a39b1ced6415c90b7ac0bdc11e622312ecb4206f2cec05f64e",
      "sha256": "4c1187b3607031a39b1ced6415c90b7ac0bdc11e622312ecb4206f2cec05f64e",
      "bytes": 2664,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-8ring14.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8ring14.dat",
      "source_sha256": "01aec18d1add23c5e73cce9060d38c0e85db21726b5780c17a0276e6f4c1512b",
      "sha256": "01aec18d1add23c5e73cce9060d38c0e85db21726b5780c17a0276e6f4c1512b",
      "bytes": 797,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box4t.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4t.dat",
      "source_sha256": "9e85c281fff9c33ce26931d772310c8faeeaba4dca1036acf1e6ac578dc50c00",
      "sha256": "9e85c281fff9c33ce26931d772310c8faeeaba4dca1036acf1e6ac578dc50c00",
      "bytes": 963,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tore Eriksson [Tore_Eriksson]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8edge.dat",
      "source_sha256": "a590f230678d592d514a9c5e307c6a30945e50e4c529fc06accf37530d0e0ed5",
      "sha256": "a590f230678d592d514a9c5e307c6a30945e50e4c529fc06accf37530d0e0ed5",
      "bytes": 615,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8ring12.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8ring12.dat",
      "source_sha256": "3480b87412d6592fcbcfbbea7e1c1120c63b13b96a88bf64a0cbc689ce2aec00",
      "sha256": "3480b87412d6592fcbcfbbea7e1c1120c63b13b96a88bf64a0cbc689ce2aec00",
      "bytes": 986,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16edge.dat",
      "source_sha256": "c08dd83bb7fe90b61f7cd0b10ebef0d9a9ba33b497676dedd2e2e968cb8248f9",
      "sha256": "c08dd83bb7fe90b61f7cd0b10ebef0d9a9ba33b497676dedd2e2e968cb8248f9",
      "bytes": 586,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl5hol9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl5hol9.dat",
      "source_sha256": "d46a457be819e6b46b7fc85f8610b8850e0d0a40556c65b74dbda04179b68a20",
      "sha256": "d46a457be819e6b46b7fc85f8610b8850e0d0a40556c65b74dbda04179b68a20",
      "bytes": 677,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axleend2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axleend2.dat",
      "source_sha256": "cedcec0918b69285f612c94d1f6532f7352a08f18b2749dde6f6a5235c1a0c73",
      "sha256": "cedcec0918b69285f612c94d1f6532f7352a08f18b2749dde6f6a5235c1a0c73",
      "bytes": 8085,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3u4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u4a.dat",
      "source_sha256": "15463f41f9947dd75486dc7af3231b1037704f1b654c2555e3ba705817a2db75",
      "sha256": "15463f41f9947dd75486dc7af3231b1037704f1b654c2555e3ba705817a2db75",
      "bytes": 545,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring4.dat",
      "source_sha256": "e046737f05ca843c7fc32bbfe9f5b26f3409c5b42b786d8809aa789faf761154",
      "sha256": "e046737f05ca843c7fc32bbfe9f5b26f3409c5b42b786d8809aa789faf761154",
      "bytes": 1640,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16stud4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16stud4.dat",
      "source_sha256": "6dd3e7068ef5fe4ab07ae85e51eabfacef0886cdf0f38941618e5c36fa03e198",
      "sha256": "31ebcd189335063b78850135a3a3954910d2d3407e9c9c22754d381e816f31e3",
      "bytes": 553,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ring3.dat",
      "source_sha256": "045613f5bb90e0c283211b1fa261cc66f8ee8ab968dc9763222e7e592cbf83fc",
      "sha256": "045613f5bb90e0c283211b1fa261cc66f8ee8ab968dc9763222e7e592cbf83fc",
      "bytes": 1159,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8cyli.dat",
      "source_sha256": "9224d4e5edc6f5b0f75f6fa358fd1368a4fd65f676b74fe1bb6e3bbb05046206",
      "sha256": "9224d4e5edc6f5b0f75f6fa358fd1368a4fd65f676b74fe1bb6e3bbb05046206",
      "bytes": 1303,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axlehol3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol3.dat",
      "source_sha256": "81caa1e48cb356fd74575f2a37a4422d75cafb930fae19182783f48381e48d2f",
      "sha256": "ee58f1125ebcb6d67881f994e1a037f539a9abd4997ca777347d816ad7061da4",
      "bytes": 1161,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl5ho10.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl5ho10.dat",
      "source_sha256": "5658b3df4183184a5d5104624ff85b3048a658972991b1dfc489dc05728278ba",
      "sha256": "b4e39ce17dd6138dd45d1773f391ccc5d6ec9d8dc52b736bd99d6a587f72a150",
      "bytes": 1217,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8ring2.dat",
      "source_sha256": "c65d4b41084dd68c63f74ca1f92d7ae9e7a79e5b1632823f24739f3ff8196691",
      "sha256": "c65d4b41084dd68c63f74ca1f92d7ae9e7a79e5b1632823f24739f3ff8196691",
      "bytes": 934,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-6ring14.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-6ring14.dat",
      "source_sha256": "b2b50e2b8f23f853136f642bdc949a58106cbc88f7cc58dd0127df07c2e55614",
      "sha256": "b2b50e2b8f23f853136f642bdc949a58106cbc88f7cc58dd0127df07c2e55614",
      "bytes": 975,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16ndis.dat",
      "source_sha256": "abb7da370e72fe9e75faf5d10c637b476202dbd8ced9cb5b0f96433e1f72f529",
      "sha256": "abb7da370e72fe9e75faf5d10c637b476202dbd8ced9cb5b0f96433e1f72f529",
      "bytes": 557,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/joint8socket1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/joint8socket1.dat",
      "source_sha256": "e86c9edd5355ee2c95b50a29c9e62f5a308279c1dcbe3d10202b9ef509d3d745",
      "sha256": "ca2c0cc5c71e1e60feafee5e02991267ba5cd6996e58675e89175573f891d0e5",
      "bytes": 5744,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/clip5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/clip5.dat",
      "source_sha256": "6e332cc47c0ba00dccf63f2afd42c6a27ca2ac11e81f432981ded3689f646145",
      "sha256": "15e1058afb4566d927d5310f4058242097d3c7e97cdcd5ed8eacd71f8f6b91ac",
      "bytes": 2483,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8chrd.dat",
      "source_sha256": "7694157b725563188a6efd69b3f558b00533b375b8a4e82f469497a03e471e74",
      "sha256": "7694157b725563188a6efd69b3f558b00533b375b8a4e82f469497a03e471e74",
      "bytes": 561,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3062bs01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3062bs01.dat",
      "source_sha256": "b1c8fbaebfab27230569a83c3e47853b7b7b98f9229c2d9540f4f86e9aff0325",
      "sha256": "0cfaf1d6185dd539267d922213a628e77a3d4bcde1c624081868d522179b4787",
      "bytes": 978,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Takeshi Takahashi [RainbowDolphin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-16cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-16cyli.dat",
      "source_sha256": "b6fb5e76f958a18c4cc88866d5e6a0502b62d3abda1a72450663b82502645330",
      "sha256": "b6fb5e76f958a18c4cc88866d5e6a0502b62d3abda1a72450663b82502645330",
      "bytes": 908,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3710s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3710s01.dat",
      "source_sha256": "57df307f7e3843f4c702311b82e93988bab6d688cbb8ab82bb4338184696780e",
      "sha256": "3f56dbe7c31f935388ce4d428e2b48867f3d94e9f1bf35600606f3fee9a2f463",
      "bytes": 662,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4ring9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4ring9.dat",
      "source_sha256": "d8de1753705319aa11a189b579323b778c9b6cf4869360e698c64a8a0cdbf3d2",
      "sha256": "0d5224ea899eb7f19431f1a1334e359569a83782aac026457eaed9bbc21cb7d2",
      "bytes": 785,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-48edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-48edge.dat",
      "source_sha256": "89dbd38b8578e8fa60ce2f80e8d7aa9b20d53c31cf40d2d322519287e6eeff19",
      "sha256": "89dbd38b8578e8fa60ce2f80e8d7aa9b20d53c31cf40d2d322519287e6eeff19",
      "bytes": 317,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16tang.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16tang.dat",
      "source_sha256": "885c0d73076a80315960cce8e87214bbee637fc547d1c6fc19b5c807e693f29b",
      "sha256": "885c0d73076a80315960cce8e87214bbee637fc547d1c6fc19b5c807e693f29b",
      "bytes": 412,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16cylo.dat",
      "source_sha256": "a5c8370842299035a9cc14308301614c6fb169fb873a7950c888928cd8d9181c",
      "sha256": "74836865b8e474c4085736e605450e55afdb1668802d3f2e63eac226449af317",
      "bytes": 419,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/npeghol2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/npeghol2.dat",
      "source_sha256": "7bbaec49211f6f511bf04c9c53af78c1478d10f22797e9d26da5e2ba719d5d64",
      "sha256": "4caa2c7e0424025987c21479cc6b240b999aa6044fc53873aa3ce0e285ed8eff",
      "bytes": 1013,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16chrd.dat",
      "source_sha256": "2bb493e8b5b56a5d63bfa7356a0ed5d6403a68e5e9a983e13a57541783ad19c1",
      "sha256": "2bb493e8b5b56a5d63bfa7356a0ed5d6403a68e5e9a983e13a57541783ad19c1",
      "bytes": 317,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/recte4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/recte4.dat",
      "source_sha256": "183b28b7586ffce3049e9248301668b4e16a84671b0f423efd792fb84a969dfe",
      "sha256": "183b28b7586ffce3049e9248301668b4e16a84671b0f423efd792fb84a969dfe",
      "bytes": 340,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-8ring13.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8ring13.dat",
      "source_sha256": "2a3bc0b9c962e7b315988553b8c1deab7769b980b1e82fffdf40ee43eb9eb3c3",
      "sha256": "2a3bc0b9c962e7b315988553b8c1deab7769b980b1e82fffdf40ee43eb9eb3c3",
      "bytes": 712,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4con8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4con8.dat",
      "source_sha256": "ca58d0e2a1aaaec9033f745f638c557dbe6a721957b7ce4cfbae60a88d64368b",
      "sha256": "ca58d0e2a1aaaec9033f745f638c557dbe6a721957b7ce4cfbae60a88d64368b",
      "bytes": 6861,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring12.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring12.dat",
      "source_sha256": "3308fbae0dbb0ac056ed5322a416e37ef39ae9200201cc71cbe6e81ec504a1b4",
      "sha256": "3308fbae0dbb0ac056ed5322a416e37ef39ae9200201cc71cbe6e81ec504a1b4",
      "bytes": 1629,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-48cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-48cyli.dat",
      "source_sha256": "e3c990b627eee00c08d92bcdb482761c2783205584b2cde454cc07cac827bacc",
      "sha256": "e3c990b627eee00c08d92bcdb482761c2783205584b2cde454cc07cac827bacc",
      "bytes": 628,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4chrd.dat",
      "source_sha256": "3b0dfcf2cb881fae0acfe1e53b703104768878636477e540d0c893fc3fd87f8f",
      "sha256": "3b0dfcf2cb881fae0acfe1e53b703104768878636477e540d0c893fc3fd87f8f",
      "bytes": 490,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/recte3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/recte3.dat",
      "source_sha256": "e7f5ccbb040191aaa4cd469a25b086299cba4a3eaa8d3b0fbf71240e3de0359a",
      "sha256": "e7f5ccbb040191aaa4cd469a25b086299cba4a3eaa8d3b0fbf71240e3de0359a",
      "bytes": 319,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4ring8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4ring8.dat",
      "source_sha256": "161616084a55a91c2e068afc2c51cc60fc08872e4ea4b55fa40f8e3155c24099",
      "sha256": "161616084a55a91c2e068afc2c51cc60fc08872e4ea4b55fa40f8e3155c24099",
      "bytes": 3654,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-4ring14.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4ring14.dat",
      "source_sha256": "9e9fbbdf29f83f5591a006cc06bd2b145c7f5733999f95ff3496df210959bb22",
      "sha256": "9e9fbbdf29f83f5591a006cc06bd2b145c7f5733999f95ff3496df210959bb22",
      "bytes": 1430,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/7-16ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/7-16ring3.dat",
      "source_sha256": "586ca9d96aafb0d4224fe43eb866cc0bff6d19ff1bc13092dd6869eee73f7089",
      "sha256": "586ca9d96aafb0d4224fe43eb866cc0bff6d19ff1bc13092dd6869eee73f7089",
      "bytes": 809,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3024s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3024s01.dat",
      "source_sha256": "a706692e2c838f20f3b3e4bd5ff03c4ab6c5c0d5816b0944ac39d6100fd85275",
      "sha256": "3ecfd5e48ec10129300d4bbaa86b7a2ddfbc1cf2c11040266dace172d73110a4",
      "bytes": 605,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tore Eriksson [Tore_Eriksson]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4edge.dat",
      "source_sha256": "e4ebabd21711f16411b3c8b8b278995a56c5f25919cd424976357da5b19943c6",
      "sha256": "e4ebabd21711f16411b3c8b8b278995a56c5f25919cd424976357da5b19943c6",
      "bytes": 1196,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud3a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud3a.dat",
      "source_sha256": "91b1f54ed55b2f57dd73225da3198b5198e31f7587a5e8b7d3351b1478c8881c",
      "sha256": "85fe4dac071ab43e2d7056d7234d7d2f15fe05ebf03e38e62a612e30bc688846",
      "bytes": 636,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axlehol9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol9.dat",
      "source_sha256": "ac0d0c6e94427fc30f64e90f1efcbf6b46b36762510245dda7450b0c3ca8ebd1",
      "sha256": "ac0d0c6e94427fc30f64e90f1efcbf6b46b36762510245dda7450b0c3ca8ebd1",
      "bytes": 960,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-6edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-6edge.dat",
      "source_sha256": "91d8e78d97ae0ae1e0a21d7b1c7d2e50ee931d9eee798b3f9d0cff5034369ab9",
      "sha256": "91d8e78d97ae0ae1e0a21d7b1c7d2e50ee931d9eee798b3f9d0cff5034369ab9",
      "bytes": 809,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4ring4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ring4.dat",
      "source_sha256": "55bd36c735c720ee8160709a3b6a3a02d828ec12ef56bcbbaf2eafa066de99b6",
      "sha256": "55bd36c735c720ee8160709a3b6a3a02d828ec12ef56bcbbaf2eafa066de99b6",
      "bytes": 1090,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-24cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-24cylo.dat",
      "source_sha256": "efeb548c4941d52d9642c0343fa790fcf4778cf4bf1b869de91502933f07671f",
      "sha256": "e302b25551145c96dcebccd166cbee124d2f7ce860ed274cafadb1d807fddcbb",
      "bytes": 488,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cyls.dat",
      "source_sha256": "aaee6ffe6e4a191d6cad4496677132eb0349303d6e48c13c7a2240dcea1db621",
      "sha256": "aaee6ffe6e4a191d6cad4496677132eb0349303d6e48c13c7a2240dcea1db621",
      "bytes": 1107,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16ring2.dat",
      "source_sha256": "39481beacecc688590dff4d877e177657d133fbaee449ad60f346c18ccce3d3d",
      "sha256": "39481beacecc688590dff4d877e177657d133fbaee449ad60f346c18ccce3d3d",
      "bytes": 580,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/5-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/5-8edge.dat",
      "source_sha256": "ecac980b3e5486dda1363611cd2cbba5e3309b2fccc255363b6d9858f00ce583",
      "sha256": "ecac980b3e5486dda1363611cd2cbba5e3309b2fccc255363b6d9858f00ce583",
      "bytes": 881,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8cylo.dat",
      "source_sha256": "f5e90ea29201b4cea569e2effe32eee5fe95146e3eadcddc054a881ef4f839bd",
      "sha256": "a834878b0fedbdf976bed7c75c82dfe8e043067ea88e8d181a189e5c8c5f16e6",
      "bytes": 414,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cyls.dat",
      "source_sha256": "eb26a554261899f82fda150ee70827a010b7d29206b5b577b2ee5831851d8f29",
      "sha256": "eb26a554261899f82fda150ee70827a010b7d29206b5b577b2ee5831851d8f29",
      "bytes": 2643,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4cylo.dat",
      "source_sha256": "b7ff6f92e06cea3815be42f757f17cd28350f2a4ff18dd1a11de0db3626ec44b",
      "sha256": "ea5b3ab978f97a39ba738f76c3fee934f52d25cb943d4a8a335076c330270750",
      "bytes": 417,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/npeghol3a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/npeghol3a.dat",
      "source_sha256": "f00979f44ded211b0e9df3a9f5f88dadd505676ad2ec98c7f9ecccabd0b063f0",
      "sha256": "806a5f234be70d4abff443bc812ae27b18dd61ef4a6c57fbfd31f1c1fb16f599",
      "bytes": 6066,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Murtazin [SwampKryakwa]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box4-4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4-4a.dat",
      "source_sha256": "58c69e00462c0a74c1bd6d75d757d826ae13e98bd3928b0e685209003bfbee54",
      "sha256": "58c69e00462c0a74c1bd6d75d757d826ae13e98bd3928b0e685209003bfbee54",
      "bytes": 1067,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl3hol2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3hol2.dat",
      "source_sha256": "5d35ee8c2a5ecf50222d9e7a5a489730f4296b47e781157a7f01263b162c6901",
      "sha256": "5d35ee8c2a5ecf50222d9e7a5a489730f4296b47e781157a7f01263b162c6901",
      "bytes": 656,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con29.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con29.dat",
      "source_sha256": "3f1e7839c6b53247a2ab5f4ca6bb0e028e4b2e9839d8cbfaf0b0ef3ef3c8b4be",
      "sha256": "3f1e7839c6b53247a2ab5f4ca6bb0e028e4b2e9839d8cbfaf0b0ef3ef3c8b4be",
      "bytes": 2491,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/empty.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/empty.dat",
      "source_sha256": "192c9b9ee2e425cfbc9e9b12ff61ee0f05ae1cb0c12dc37d5590adb6abb65128",
      "sha256": "192c9b9ee2e425cfbc9e9b12ff61ee0f05ae1cb0c12dc37d5590adb6abb65128",
      "bytes": 825,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4cyli.dat",
      "source_sha256": "4a54732476cf4eaad2c9f7b40a3cef24db025132004328e4e84c0666cd217533",
      "sha256": "4a54732476cf4eaad2c9f7b40a3cef24db025132004328e4e84c0666cd217533",
      "bytes": 2031,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4cylc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4cylc.dat",
      "source_sha256": "a5b68e5d662209f4139803034f45330ba677b1aff449fb609d95a6f27ddc5469",
      "sha256": "150f71f94afc9c8158a730da6b7a0fc06a96b0eb5c5f7413928e48db5f9f9673",
      "bytes": 472,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box4-2p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4-2p.dat",
      "source_sha256": "a4cb5395b3ec8bba18d81e36c32f43cb9349a55fe97729c367afaa5e1e8b7f0f",
      "sha256": "a4cb5395b3ec8bba18d81e36c32f43cb9349a55fe97729c367afaa5e1e8b7f0f",
      "bytes": 756,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3623s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3623s01.dat",
      "source_sha256": "87c2404623acb5ab59cdebe1d0c4a16b471855380a1715ab831b8f1bb2e769f8",
      "sha256": "ea8c2a417e6cacbca8404843a67d2d403e9f28e0cd5688379428f773a5442230",
      "bytes": 714,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16tndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16tndis.dat",
      "source_sha256": "013e74f7eb727ad92396676544e09a80994a05200ba3a2c3ec1e6597b90bf892",
      "sha256": "013e74f7eb727ad92396676544e09a80994a05200ba3a2c3ec1e6597b90bf892",
      "bytes": 392,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16cyli.dat",
      "source_sha256": "f50d12a37a22ae4a5f37a017b8e39d1e729577b0a4aa376ca685b210806b49c8",
      "sha256": "f50d12a37a22ae4a5f37a017b8e39d1e729577b0a4aa376ca685b210806b49c8",
      "bytes": 942,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl3hole.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3hole.dat",
      "source_sha256": "eb2369c61af0f2e3c2bf85f0f23ca92d5d313719941f0f8ff4eabde4b131ba7e",
      "sha256": "eb2369c61af0f2e3c2bf85f0f23ca92d5d313719941f0f8ff4eabde4b131ba7e",
      "bytes": 4789,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-24cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-24cyli.dat",
      "source_sha256": "5e767152f719b094442a5e68060781c9f2b7304595c6956bf98183bda00a9a36",
      "sha256": "5e767152f719b094442a5e68060781c9f2b7304595c6956bf98183bda00a9a36",
      "bytes": 537,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8ring3.dat",
      "source_sha256": "c44e0a5db0b1fc228aa513880a7717cab472194b576a75a89fd71e4059d6d8a2",
      "sha256": "c44e0a5db0b1fc228aa513880a7717cab472194b576a75a89fd71e4059d6d8a2",
      "bytes": 804,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud2.dat",
      "source_sha256": "5ed3702c7d7000bfac2906f12b74ae312c59194a8e3b504952820c826b51c810",
      "sha256": "456404d0c981e5d3ef48c168a1b5cc9baeb9ccfca889b687fa89f4726fad03b1",
      "bytes": 1007,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/32013s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/32013s01.dat",
      "source_sha256": "5e22d4835fdd05e3c5813beb1cb676b31011879daaaa18a65fabc29339486728",
      "sha256": "479d688dc4bc9e461cb283da41bf917d2c94ade05621d1e15064e7f555a36ae0",
      "bytes": 6877,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-16edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-16edge.dat",
      "source_sha256": "9b3b4df68d3c0d68fd3e5c52346871867043f67522e53aaa21991562c89bdc10",
      "sha256": "9b3b4df68d3c0d68fd3e5c52346871867043f67522e53aaa21991562c89bdc10",
      "bytes": 550,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl3ho10.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3ho10.dat",
      "source_sha256": "7799ee39b85781d7283d952136cba415605b819a87b9ec92cbfe3f348c8c1f5e",
      "sha256": "7799ee39b85781d7283d952136cba415605b819a87b9ec92cbfe3f348c8c1f5e",
      "bytes": 743,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug3-1x3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3-1x3.dat",
      "source_sha256": "80f86a2ea87dfabc79c3daf963a14c7757caceea6b402ac4f2178a6088de08ac",
      "sha256": "3809308f62201547100313e2f87c4053474f55d9dc6c9f1a684499c6dca51a56",
      "bytes": 420,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud4od.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4od.dat",
      "source_sha256": "6f6ba215655349845b069f9647fffa22fbc43cf083dff46900353c3dc579ec72",
      "sha256": "fde578ca8eb4647ae576915c45f597fbac4009746e75118c78279028cacd0212",
      "bytes": 581,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-1x3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x3.dat",
      "source_sha256": "f24de368545aa96580b811daa6c25e18f5bfdbaca1d4b11addcfa7cbb625f4c9",
      "sha256": "1c61730ba196264300a3cc50ca7d466b68f80f75301e0c215b0b26fb643feea2",
      "bytes": 405,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4ring1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ring1.dat",
      "source_sha256": "a04bfc7ffeeb56f92a83aaa60429939e896facb5a407f93a50f24fd1b2b1706d",
      "sha256": "a04bfc7ffeeb56f92a83aaa60429939e896facb5a407f93a50f24fd1b2b1706d",
      "bytes": 1009,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/rect2a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/rect2a.dat",
      "source_sha256": "6d75ffb88e705a35f34e095ec0848a7bb70b577a376fdae05804da214b0d6369",
      "sha256": "6d75ffb88e705a35f34e095ec0848a7bb70b577a376fdae05804da214b0d6369",
      "bytes": 586,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-16cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-16cylo.dat",
      "source_sha256": "94929f851cefec060fcf3222213a1f9743f9b6549a9e7bbcf471482dc546a827",
      "sha256": "ed0a50d7c4cbe0dac5919b341d5e5cf65a55eb8c5aa50f697c1c69682fa5e657",
      "bytes": 488,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug3-1x5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3-1x5.dat",
      "source_sha256": "85d37bfc3cbb90f12a55dfe2543f507c1763f0336962c712cbec327d688b5624",
      "sha256": "5491084b54192db394e8418e338deb2c5c099bcc5a7c18f4276301644a73a41d",
      "bytes": 525,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/confricrib4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/confricrib4.dat",
      "source_sha256": "8377c04d9e319692ea66b73be18ac5d01e6ac6683c4e99c3ed6b1f19b2f22d57",
      "sha256": "5b0d61cf390a4532d7c3d73c137c1749fe149763ec69b4f547947ef16070e78d",
      "bytes": 3675,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/connectslit2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connectslit2.dat",
      "source_sha256": "f57c2e74ed9a190f1abbff9a7dc073034d2e2dc654d3c9a13587cd8a859b9697",
      "sha256": "ed73281ac48030dcaaf13bb04019bcb70d89b627ede2d2800cd141a5704e767e",
      "bytes": 1117,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug3-1x7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3-1x7.dat",
      "source_sha256": "381169c4592a6ed096c0011e06e6000c65200492fe6126b3aa9e6a51ae2ba244",
      "sha256": "b50565911bb5642246b38407ff4df81ac4840292994a202e7779c62391b26b6c",
      "bytes": 630,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl2hol9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl2hol9.dat",
      "source_sha256": "5864b8cde1b8987a041e762f9186ca45b1e3687e34c3a201cf8b70092256c89c",
      "sha256": "5864b8cde1b8987a041e762f9186ca45b1e3687e34c3a201cf8b70092256c89c",
      "bytes": 881,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-1x6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x6.dat",
      "source_sha256": "907b74bad03688f6d2f22220db6ec4a6c922203a3e3001aa24f214c6ed48a226",
      "sha256": "734e1eff0a56364ce10c6436b2b71f551de8358e97a5af96149755cd5dbfe6a1",
      "bytes": 561,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con4.dat",
      "source_sha256": "7c49737dec9819a49e43d7af5926c05d8a1a1226bc0f2cb15cbe7cddb035f00b",
      "sha256": "7c49737dec9819a49e43d7af5926c05d8a1a1226bc0f2cb15cbe7cddb035f00b",
      "bytes": 2722,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/44224s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/44224s01.dat",
      "source_sha256": "50dd74a6f6c721fd30736489dfa06eb4b91d0c8bab6482ea3d7b975a24334a74",
      "sha256": "810d86a5c8ae7364642f75e4c7dcfa94ea207c4066019269150bd4079da04d0a",
      "bytes": 9987,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4disc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4disc.dat",
      "source_sha256": "86c45014c54ad4c82fcf8a96553942c756e39e6b2b109aeccb9f47873f5f3f52",
      "sha256": "86c45014c54ad4c82fcf8a96553942c756e39e6b2b109aeccb9f47873f5f3f52",
      "bytes": 916,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/confricrib1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/confricrib1.dat",
      "source_sha256": "3d4f3394b9aaa9007498a35a33e2c63113c6b6113027c205531bc91bb6335067",
      "sha256": "3d4f3394b9aaa9007498a35a33e2c63113c6b6113027c205531bc91bb6335067",
      "bytes": 1795,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/3-8cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/3-8cyli.dat",
      "source_sha256": "a48d8a1256f826b5e4e3644aa83f8233d1d295ec90509283a798fd24f86eba4c",
      "sha256": "a48d8a1256f826b5e4e3644aa83f8233d1d295ec90509283a798fd24f86eba4c",
      "bytes": 683,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug3-1x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3-1x2.dat",
      "source_sha256": "e78926d1494fa67b984f390aa1c05d01c35eff99030209e9bbee4e15bfcc0ecb",
      "sha256": "1a388399b805addc3e4d78099032a54a24d60302355b9955fe76093f98826919",
      "bytes": 369,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-16ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16ndis.dat",
      "source_sha256": "80fe13f5d5458143a68a5fa9e4cf4eba0d22b3df7cf3c255630276d1687c53a5",
      "sha256": "80fe13f5d5458143a68a5fa9e4cf4eba0d22b3df7cf3c255630276d1687c53a5",
      "bytes": 297,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con13.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con13.dat",
      "source_sha256": "340b30ba8205ef76e4457aaba4620b9a1a2ad13e14bbcacac63dae1dd224812d",
      "sha256": "340b30ba8205ef76e4457aaba4620b9a1a2ad13e14bbcacac63dae1dd224812d",
      "bytes": 2435,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4ring10.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4ring10.dat",
      "source_sha256": "180b6a4e892347f36562b20f70e96d6d57737c9911651f3be7c7623998ce407b",
      "sha256": "180b6a4e892347f36562b20f70e96d6d57737c9911651f3be7c7623998ce407b",
      "bytes": 3575,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl3hol8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3hol8.dat",
      "source_sha256": "2349b82c7dd4559a45913986e07e185035fdb48928ac13e5fd774f4c30a65e96",
      "sha256": "2349b82c7dd4559a45913986e07e185035fdb48928ac13e5fd774f4c30a65e96",
      "bytes": 2605,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-16chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-16chrd.dat",
      "source_sha256": "612846540dad896fa0610b5f7eb9ec1f7a39c0bbbd68dd7e3a9114da1737173d",
      "sha256": "612846540dad896fa0610b5f7eb9ec1f7a39c0bbbd68dd7e3a9114da1737173d",
      "bytes": 419,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16ring3.dat",
      "source_sha256": "3e0d8f9325ef96db0fa0a471240f810181a235736554c040a303f20d03294136",
      "sha256": "3e0d8f9325ef96db0fa0a471240f810181a235736554c040a303f20d03294136",
      "bytes": 580,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16cys2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16cys2.dat",
      "source_sha256": "705ec7384e735a8e7a864403831e55cb1e62f88ec09126a8b379b7e27288607a",
      "sha256": "705ec7384e735a8e7a864403831e55cb1e62f88ec09126a8b379b7e27288607a",
      "bytes": 702,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con7.dat",
      "source_sha256": "a1041c95280f6b9551e6171d8090cb4e0f0dbec7a9a85fa5bb71d0a613827696",
      "sha256": "a1041c95280f6b9551e6171d8090cb4e0f0dbec7a9a85fa5bb71d0a613827696",
      "bytes": 2426,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4ndis.dat",
      "source_sha256": "7536759336f15eee2ad9a2c73f96fc6bd07222918811bb2321e6c51a9210e6d1",
      "sha256": "7536759336f15eee2ad9a2c73f96fc6bd07222918811bb2321e6c51a9210e6d1",
      "bytes": 2615,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Franklin W. Cain [fwcain]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/3-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/3-8edge.dat",
      "source_sha256": "f28310dd1755cabdd2451f190f85ed2cbd0f3419d11f560bcbfd5971b27529e5",
      "sha256": "f28310dd1755cabdd2451f190f85ed2cbd0f3419d11f560bcbfd5971b27529e5",
      "bytes": 390,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/98100s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/98100s01.dat",
      "source_sha256": "ec5906bdde13641db85789111e07a7761e8fb0bc64a169a070af161ddf2d29b1",
      "sha256": "08cb0cc63945a361debc842a71df69cd4c14ddebaa39ef2afe34758c4a4427ef",
      "bytes": 22226,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/connectcollar4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connectcollar4.dat",
      "source_sha256": "1e0b2f3bc1872c405e6ed0bc7b6fee8416a4756f7d6ff78b4a028acbeff69722",
      "sha256": "6f44af2852c4b57f397dd814298b1db5c950e2a95108a52e449e9a683b1372f9",
      "bytes": 3707,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8ering.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ering.dat",
      "source_sha256": "5bb705192bc6c39dada3895e6c6efe15a6c98a84e9747aff0e98104e750c4e4b",
      "sha256": "4203edd35539f38f34595671b8f00ecc400df4a360e4d5d8562e0f66ef8ae735",
      "bytes": 726,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box2-9p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-9p.dat",
      "source_sha256": "6c68301a34e42d105e716e5ae5edf02e3d58978db24619f0364887c339edd331",
      "sha256": "6c68301a34e42d105e716e5ae5edf02e3d58978db24619f0364887c339edd331",
      "bytes": 539,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/5-8cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/5-8cyli.dat",
      "source_sha256": "91679da1ed677f4273989f784e212d4a3f332cb4bee317617682b216f6aaf284",
      "sha256": "91679da1ed677f4273989f784e212d4a3f332cb4bee317617682b216f6aaf284",
      "bytes": 1742,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4cyli.dat",
      "source_sha256": "6c466cd94f69ecdb3a5a83faee52ad2e5ecd9d1560975feaf854c3433de6e6a2",
      "sha256": "dc8f952f88f6a11c226b8e9d094a12cc7b5f614a7144464b39b5e93f75fc0f73",
      "bytes": 779,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3005s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3005s01.dat",
      "source_sha256": "ed6218c566690622fed39b8fb3dac9ae9a36df66cac106e2e1d4b5862567841a",
      "sha256": "0fe23ab896c48bf2e31016e8c0f67a876d3e6f148a20c81b338e2d0417c5f10a",
      "bytes": 936,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axlehole.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehole.dat",
      "source_sha256": "8dfcdd5058a66fba2ea4f59ddc7fd4510118baca9f745e5dfe341ccf0e24b49e",
      "sha256": "29894fd670c4b481a1c20502ec5b193825fc8fb60034ede916b9f740477a841f",
      "bytes": 2205,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl2hol2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl2hol2.dat",
      "source_sha256": "588bf34d84213c071fcd6fd31dbd2a19db8797cfefeabdaf566b56a467260c57",
      "sha256": "588bf34d84213c071fcd6fd31dbd2a19db8797cfefeabdaf566b56a467260c57",
      "bytes": 894,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-4ring9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4ring9.dat",
      "source_sha256": "08cf8697a97526c9636b00578b792ef8452d3f74d7615e3a1d5644417908b42a",
      "sha256": "08cf8697a97526c9636b00578b792ef8452d3f74d7615e3a1d5644417908b42a",
      "bytes": 1374,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8sphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8sphe.dat",
      "source_sha256": "c38f9b8df6f260a26e920d8bbfb2d6b11667026e0675733d7fc2d3653ef92c53",
      "sha256": "c38f9b8df6f260a26e920d8bbfb2d6b11667026e0675733d7fc2d3653ef92c53",
      "bytes": 4040,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box4o8a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4o8a.dat",
      "source_sha256": "2144edea417bbc55c261e3731ea86d52ac50c7cb651b4879f55ec39966fd0f5b",
      "sha256": "2144edea417bbc55c261e3731ea86d52ac50c7cb651b4879f55ec39966fd0f5b",
      "bytes": 749,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/1-4cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/1-4cyls.dat",
      "source_sha256": "c4cb59937f09c2c106bafd2c971302d8319247180e1dd0e9a010e1b34cfc4ada",
      "sha256": "c4cb59937f09c2c106bafd2c971302d8319247180e1dd0e9a010e1b34cfc4ada",
      "bytes": 469,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/joint8socket3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/joint8socket3.dat",
      "source_sha256": "1ca3edcebff34b3cd646933c4c92830c3e31528dc8cb71c189c366a6fa7bff0a",
      "sha256": "52382d53701c4bb794f20b6873fa1c10eb608f4555fc87185169c5c465e91323",
      "bytes": 31435,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16cyls.dat",
      "source_sha256": "166309d0dba474780d13a812b58b952b790512f6036dbfb93cf43ab53401be0a",
      "sha256": "166309d0dba474780d13a812b58b952b790512f6036dbfb93cf43ab53401be0a",
      "bytes": 638,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/1-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/1-4edge.dat",
      "source_sha256": "841b1c8c1e48553b010ba25fde8e9ef1ea959c1ac83c7c7b6dae7277fbee4a35",
      "sha256": "841b1c8c1e48553b010ba25fde8e9ef1ea959c1ac83c7c7b6dae7277fbee4a35",
      "bytes": 348,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4ring12.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4ring12.dat",
      "source_sha256": "0ff1a27681d9f28da3cc1e382f94597090389646a92b7d044b8c4999c024a1e4",
      "sha256": "0ff1a27681d9f28da3cc1e382f94597090389646a92b7d044b8c4999c024a1e4",
      "bytes": 1012,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Franklin W. Cain [fwcain]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring9.dat",
      "source_sha256": "f1b98f891616369b58e4ff5d25ba9598ff7ef71b63e72cf3c500e72540390efb",
      "sha256": "f1b98f891616369b58e4ff5d25ba9598ff7ef71b63e72cf3c500e72540390efb",
      "bytes": 1533,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4cyli.dat",
      "source_sha256": "e2ed297feaf608b7319c2e54cd81dcb653fbb3d87b5a8e48ab2f54b32953fc6b",
      "sha256": "e2ed297feaf608b7319c2e54cd81dcb653fbb3d87b5a8e48ab2f54b32953fc6b",
      "bytes": 2413,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-24edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-24edge.dat",
      "source_sha256": "0946112b54d72f44d95d9f48b652bec53468f05eaacb2503ca09f58bee518e04",
      "sha256": "0946112b54d72f44d95d9f48b652bec53468f05eaacb2503ca09f58bee518e04",
      "bytes": 630,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/1-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/1-4ndis.dat",
      "source_sha256": "c47a4b0165bfffb084112a6703f4dc1641fdea7c3c68337a4b745223cf400ce2",
      "sha256": "c47a4b0165bfffb084112a6703f4dc1641fdea7c3c68337a4b745223cf400ce2",
      "bytes": 375,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/1-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/1-4cylo.dat",
      "source_sha256": "d0b0c3568d1ec7160378aec8e90a9ac101c6bd4398ea9d70c15feeb6f2574211",
      "sha256": "c6c345e1f64bf750233a9d048e19fd13f3c9310bcfe6705c2d03e8efd213fa41",
      "bytes": 435,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl2hol3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl2hol3.dat",
      "source_sha256": "6312105b4ba20ad750f6e75a4d0b8bbc4f8ae69139115ec6404e2a9bc9b6b20c",
      "sha256": "6312105b4ba20ad750f6e75a4d0b8bbc4f8ae69139115ec6404e2a9bc9b6b20c",
      "bytes": 991,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con8.dat",
      "source_sha256": "9c5ccecc4d79097dc58c4c67d095bcddd0c307a40239dac29e8bf780f46709df",
      "sha256": "9c5ccecc4d79097dc58c4c67d095bcddd0c307a40239dac29e8bf780f46709df",
      "bytes": 2626,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl2ho10.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl2ho10.dat",
      "source_sha256": "5890f737d6d8507967dbbd552d8a5122f669b47cde1fd712f3f9bef098419361",
      "sha256": "5890f737d6d8507967dbbd552d8a5122f669b47cde1fd712f3f9bef098419361",
      "bytes": 1013,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con18.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con18.dat",
      "source_sha256": "408db04ac5da531068855defa5bd797adee5442091c8124c6cb9a513b0539173",
      "sha256": "408db04ac5da531068855defa5bd797adee5442091c8124c6cb9a513b0539173",
      "bytes": 2452,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl2hol8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl2hol8.dat",
      "source_sha256": "aec8db1ea95afe49ff1e3a6ac36a7df8735fe03300d58aa0b9da28bec25be5ea",
      "sha256": "aec8db1ea95afe49ff1e3a6ac36a7df8735fe03300d58aa0b9da28bec25be5ea",
      "bytes": 3386,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axl5end.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl5end.dat",
      "source_sha256": "bcfcb15a7ed768ff4c6746f5ed319c8a6d92d0e720b51e9fd973391987403af2",
      "sha256": "bcfcb15a7ed768ff4c6746f5ed319c8a6d92d0e720b51e9fd973391987403af2",
      "bytes": 818,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8sphc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8sphc.dat",
      "source_sha256": "7de34335dafbbb745901dcfced234f81b4ffaa629c6796837c99dbd375f768c2",
      "sha256": "7de34335dafbbb745901dcfced234f81b4ffaa629c6796837c99dbd375f768c2",
      "bytes": 2451,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Franklin W. Cain [fwcain]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/1-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/1-4cyli.dat",
      "source_sha256": "a9e8266ebf4bdb75f8ac643596e29e3069cc88697a379e4b116fa59b1c138bbf",
      "sha256": "a9e8266ebf4bdb75f8ac643596e29e3069cc88697a379e4b116fa59b1c138bbf",
      "bytes": 550,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "LDConfig.ldr": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/LDConfig.ldr",
      "sha256": "d3490047460ad7a511b150006b009830fc52ecc1899b514c7380e9de644b3cfb",
      "bytes": 67580
    }
  }
}
```
<!-- asset-manifest:end -->
