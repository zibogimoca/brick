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

`.dat`는 문서가 아니라 좌표, 면, 다른 형상 파일의 배치 정보를 담는 LDraw 형상 형식이다. 현재 목록의 상위 부품은 290종이며, 나머지 형상 파일 상당수는 그 부품들이 참조하는 조각이다. 파일 수가 판매 부품 수를 뜻하지 않는다.

## 왜 나뉘어 있는가

LDraw 형상을 사용하되 폴더 이름과 내부 참조를 읽기 쉬운 이름으로 변경했다. `primitives`는 공통 형상, `subparts`는 부품의 하위 형상, `high-resolution`은 원 둘레를 48분할하는 고정밀 형상을 뜻한다. 예를 들어 `parts/3001.dat`는 `parts/subparts/3001s01.dat`를 참조한다. 하위 파일이 다시 공통 조각을 참조할 수도 있다. 번호와 경로는 사람이 읽기 좋은 이름 대신 참조 식별자로 쓰인다.

부품 한 종류당 독립 파일 하나로 만드는 것도 가능하다. 참조한 조각의 좌표 변환과 색상 적용을 풀어 모든 면을 해당 부품 파일에 넣으면 된다. 이렇게 하면 파일 목록은 단순해지지만 같은 돌기 등의 데이터가 부품마다 반복된다. 반대로 공통 조각을 별도로 유지하면 중복은 줄지만 파일과 참조 관계가 늘어난다. 어느 쪽이 항상 더 빠르거나 관리하기 쉬운 것은 아니다.

폴더를 단순화하려면 형상뿐 아니라 사전의 참조, 뷰어의 로딩 경로, 수집·검증 도구를 함께 수정해야 한다. 불필요한 `ldraw` 상위 폴더를 제거하고 폴더 이름과 형상 내부 참조를 변경했으며 좌표와 개별 부품 번호는 유지했다. 원본 아카이브 경로와 원본 해시는 출처 추적용으로 아래 목록에 보존한다.

## 출처와 라이선스

기본 형상은 [LDraw 공식 라이브러리](https://library.ldraw.org/)의 [전체 아카이브](https://library.ldraw.org/library/updates/complete.zip)에서 필요한 부분만 가져왔다. 출처별 저자와 조건을 보존한다. 목록에 `original_project_geometry`로 표시한 누락 부품은 프로젝트에서 만든 시각 참고 형상이며 제조사 CAD와 동일하거나 실물 결합이 검증된 것으로 표시하지 않는다.

현재 형상에는 **CC BY 4.0** 또는 **CC BY 2.0과 CC BY 4.0** 병기 자료가 포함된다. 파일별 고지는 아래 목록에 보존한다. [이용 조건 요약](https://creativecommons.org/licenses/by/4.0/)과 [라이선스 전문](https://creativecommons.org/licenses/by/4.0/legalcode)을 기준으로, 공유할 때 저자·출처와 라이선스 링크를 제공하고 변경했다면 그 사실을 표시한다. 저자가 이 프로젝트를 보증하는 것처럼 표현하지 않는다. 색상 설정 등 다른 자료의 조건을 이 확인 결과로 일괄 단정하지 않고 원본 고지를 따른다.

별도 `CAreadme.txt`와 `CAlicense.txt`는 사용자 요청으로 삭제했다. 원본 형상 안의 저자·라이선스 헤더는 보존되어 있으며, 그 안에 남은 `CAreadme.txt` 표기는 원본의 참조다. 파일 삭제가 원래 이용 조건을 없애지는 않는다. 이용 안내는 이 문서에 통합한다.

공개 저장소나 공개 뷰어에 포함한 자료는 다른 사람이 받을 수 있으므로, 혼자 볼 목적이어도 공개 상태라면 공유 조건을 고려해야 한다. 배포할 때는 이 안내와 개별 저자 정보를 함께 제공하고 접근 가능한지 확인한다.

69787–69790은 공식 전체 아카이브에 없어 [LegoMaster 공개 저장소](https://github.com/iefierros/LegoMaster/tree/0b2eb83be4c34193521a962b3136c553d14322c3/ldraw/UnOfficial/parts)에서 확보했다. 저장소 라이선스는 MIT(Copyright 2024 Lego Master)지만 개별 원본 메시의 저자·라이선스 표기는 없다. 공식 LDraw CC 조건을 이 네 파일에 적용한 것으로 표시하지 않는다. 삼각형 좌표는 유지하고 비표준 UV 꼬리만 제거했다.

## 관리 원칙

- 에셋 설명 문서는 이 파일 하나로 유지한다. 새 설명 문서를 추가하지 않고 여기에 갱신한다.
- 담당 모델에 필요한 공용 부품과 필수 의존 형상 파일은 개별 에이전트도 별도 생성 승인 없이 확보·제작·등록할 수 있다. 기존 형상과 원격 변경에서 중복을 확인하고 공용 경로를 사용한다. 필요한 사전과 이 문서의 에셋 목록을 함께 갱신하며, 출처·이용 조건·직접 제작 여부·검증 한계를 보존한다. 그 밖의 새 파일·폴더는 생성 전에 사용자에게 이름·목적·필요성을 보고한다. 형상 구조 변경도 먼저 설명한다.
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
    "10247",
    "11090",
    "11153",
    "11211",
    "11212",
    "11213",
    "11214",
    "11215",
    "11291",
    "11458",
    "11477",
    "13547",
    "13548",
    "13731",
    "14417",
    "14418",
    "14419",
    "14704",
    "14769",
    "15068",
    "15397",
    "15535",
    "15571",
    "15573",
    "15672",
    "15712",
    "17114",
    "1748",
    "1751",
    "1762",
    "18651",
    "18654",
    "18674",
    "18980",
    "22385",
    "22885",
    "2310",
    "23443",
    "2357",
    "23969",
    "2419",
    "2420",
    "24201",
    "2429",
    "24299",
    "2430",
    "24307",
    "2431",
    "24316",
    "2445",
    "2450",
    "2456",
    "2462",
    "24866",
    "25269",
    "26047",
    "2639",
    "2654",
    "26601",
    "26603",
    "26604",
    "27263",
    "2736",
    "2752",
    "2780",
    "28192",
    "28802",
    "29119",
    "29120",
    "30000",
    "3001",
    "3002",
    "3003",
    "3004",
    "3005",
    "3006",
    "3010",
    "30136",
    "3020",
    "3021",
    "3022",
    "3023",
    "3023b",
    "3024",
    "3028",
    "3031",
    "3032",
    "3033",
    "3034",
    "3035",
    "30357",
    "3036",
    "30363",
    "30374",
    "3039",
    "3040b",
    "30414",
    "3046",
    "30503",
    "3062b",
    "3068b",
    "3069b",
    "3070b",
    "3172",
    "3176",
    "32000",
    "32002",
    "32009",
    "32013",
    "32014",
    "32016",
    "32018",
    "32059",
    "32062",
    "32064a",
    "32073",
    "32140",
    "32184",
    "32192",
    "32278",
    "32291",
    "32324",
    "32524",
    "32525",
    "32607",
    "32802",
    "32803",
    "32952",
    "3298",
    "33320",
    "33909",
    "34103",
    "3460",
    "3484",
    "35044",
    "35480",
    "3622",
    "3623",
    "3659",
    "3660",
    "3665",
    "3666",
    "3673",
    "36840",
    "36841",
    "3700",
    "3701",
    "3702",
    "3703",
    "3705",
    "3707",
    "3709",
    "3710",
    "37352",
    "3738",
    "3766",
    "37762",
    "3795",
    "3829c01",
    "3832",
    "3837",
    "3941",
    "39789",
    "4032",
    "4032a",
    "40378",
    "40379",
    "4070",
    "4073",
    "41539",
    "4162",
    "41682",
    "41740",
    "41747",
    "41769",
    "41770",
    "4274",
    "4282",
    "42862",
    "4287c",
    "42924",
    "4304",
    "43093",
    "43708",
    "43710",
    "43711",
    "43722",
    "43723",
    "44224",
    "44225",
    "44301b",
    "44728",
    "4477",
    "44861",
    "4519",
    "47457",
    "48165",
    "48336",
    "49656",
    "50340",
    "5066",
    "5090",
    "50923",
    "50950",
    "51274",
    "51739",
    "52501",
    "53451",
    "54200",
    "54383",
    "54384",
    "55013",
    "55236",
    "5649",
    "5907",
    "59443",
    "59900",
    "60470b",
    "60474",
    "60477",
    "60478",
    "60479",
    "60483",
    "61332",
    "61406",
    "6141",
    "61485",
    "62462",
    "63864",
    "63868",
    "63965",
    "64225",
    "64799",
    "6541",
    "65426",
    "65429",
    "65509",
    "6589",
    "6632",
    "6636",
    "66956",
    "67329",
    "67695",
    "67696",
    "68297",
    "68568",
    "69729",
    "69787",
    "69788",
    "69789",
    "69790",
    "70681",
    "72132",
    "73109",
    "73230",
    "73562",
    "73825",
    "73831",
    "76959",
    "77765",
    "77844",
    "77850",
    "78257",
    "78258",
    "78329",
    "78443",
    "78444",
    "78666",
    "79180",
    "79389",
    "79846",
    "80177",
    "80178",
    "85861",
    "85943",
    "85970",
    "85984",
    "86996",
    "87079",
    "87087",
    "87544",
    "87552",
    "87580",
    "87620",
    "87747",
    "87994",
    "88292",
    "89678",
    "90194",
    "91988",
    "92438",
    "93273",
    "93274",
    "96874",
    "98100",
    "98138",
    "98989",
    "99207",
    "99563",
    "99780",
    "99781"
  ],
  "files": {
    "parts/2357.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2357.dat",
      "source_sha256": "9a398ede6ad8392cd9d07302e6d8e7d19894c4c67ca9f943c1920be0b61d2bae",
      "sha256": "710c53bce34c53855d4304145054c896e6fcd7027f827089614ebe29d4a5dfd1",
      "bytes": 1983,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/26601.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/26601.dat",
      "source_sha256": "76154f150a645a5e78f1ddf838cef722e8355f2bdfd67885660e31d5ae7399eb",
      "sha256": "773c9c5ddd27868876419e98fa94f1bc30099d4f36a1ab83a4ffbae879c91bda",
      "bytes": 1949,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3040b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3040b.dat",
      "source_sha256": "47a73c42c206e34c11f6d54a48ee186e53a5a941d56923b5221bd244f7926fed",
      "sha256": "e040e1470352d5cde5efe7bce1c82b8311db7d921db4fd234a7e5b27df86c344",
      "bytes": 649,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/30000.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30000.dat",
      "source_sha256": "f9bbd07d99d49105dd98179029c6d1b34a26838972d673b5a3f5e7fb21457e4e",
      "sha256": "d01f39ae1c5fb5e28608eff93b9f5c1e2bf9a4ebc28f328aeee0032fc9cc5b94",
      "bytes": 1950,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3702.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3702.dat",
      "source_sha256": "178d615c51c97ad00bdb25b8ed56bb7dc9ecff79cec77a102df053ca57cbb03d",
      "sha256": "d7e3d68a0d6524842a5ff1c2f353ded803f386ffa6d8b4c3585d77da7fe2a338",
      "bytes": 8603,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/13548.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/13548.dat",
      "source_sha256": "da7dad5bfda052390db82b36039502fb24b789dc07f869e3b15f86b10080a45b",
      "sha256": "a4afd4f0c8d2306d941786d2957950ae579daf8607a60fb8b6ed85cd0aa43443",
      "bytes": 580,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2420.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2420.dat",
      "source_sha256": "ded452d47f31f69b4c3128674ee851f7ae05205230c4e414ce2823b3b014d384",
      "sha256": "f2bdbd7e07f2a2705159f0bd35c6aef5dbf2bac8c7bad967c9b2ef9cc0335cf6",
      "bytes": 1450,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/33909.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/33909.dat",
      "source_sha256": "8da6789db82746f179997ed4b917d00d34d03a6486d6aa27c76d17c9b21d8609",
      "sha256": "029c21681dc269ca7e55ebf0ad98d4bf587ecea4154e498ecccd42380338cacb",
      "bytes": 782,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/39789.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/39789.dat",
      "source_sha256": "34a385fdb4d332220edd5021f99c8a136c090db2a07e8c99d4d0708d7121f7be",
      "sha256": "d0789a7966081c3a43d81773a5c46d36e6afb70f322d51d5625590e155532dc2",
      "bytes": 3486,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
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
    "parts/3659.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3659.dat",
      "source_sha256": "7544bbc1fae27eb339ee29a72900d411ade577a78a1686227af32ac0efce150c",
      "sha256": "1baeea008b087a6cef500c8fd64d57b55a5fcc039e684a8de5b5db547aa48fdd",
      "bytes": 3818,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/54384.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/54384.dat",
      "source_sha256": "f1721be6c504efac27bb135fe79d888d3e0c578591f1cbd0327d716c2d3aee4f",
      "sha256": "e7444cff68d4559788f715e9cf74a0933e4e957b2c9aa47c37ca472add1d5f0b",
      "bytes": 593,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32059.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32059.dat",
      "source_sha256": "2a4ce2b1a4fd9c713410b0a1592f600cecfb51ca18727d7f88f2c2964339d95f",
      "sha256": "a4f24bf7417780d880141cbb2a01616ab760b0b19bf6b871834784eb303709c8",
      "bytes": 7266,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
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
    "parts/87620.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/87620.dat",
      "source_sha256": "b905013f247004edf60f07d05a5ace90dcec9afb64e3e37f8de2ebc9dc1decd9",
      "sha256": "e9e505fcd0d811d4ee2c82a6c8d68df16c4cdc3c528a38b6c609e588956d4f94",
      "bytes": 2828,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Ronald Vallenduuk [Duq]",
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
    "parts/5090.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/5090.dat",
      "source_sha256": "ee6f107f66b1a49d261f485c2d60c1b6e4c1d3c52927e782e13883eb5a46c190",
      "sha256": "5ff14be7eca8db163d738348ddd7f06d7f4277177321472cd4d7cc82a5866dbb",
      "bytes": 3028,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/73562.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/73562.dat",
      "source_sha256": "492671ff00f6266b748a826b0da312fc82a9d51f1a9730956e892876f2aa050c",
      "sha256": "13dd05d7edcbf4e2674454f423aa113bc4335ca0695ac2e9b90ebd13ea9c3faa",
      "bytes": 2459,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
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
    "parts/10247.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/10247.dat",
      "source_sha256": "2fcb10fd982acad58cc424bfff9690f8a4787c94bff75cb58081f4f440c0d3eb",
      "sha256": "6696c9400a1645fe6c3d18092cc2459cce6cf3aff62f6299616121e41b5f6935",
      "bytes": 2650,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
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
    "parts/99780.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/99780.dat",
      "source_sha256": "68108030d27c159a11ae1a53728b67e1091ac9406c8bb770ae38a6f1c29c031e",
      "sha256": "d9c101a341863068330bb7354fdca9785905eb98fdef7808ceaac7c5bd07de51",
      "bytes": 2012,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/37762.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/37762.dat",
      "source_sha256": "daf7f2a72ce22b311a2abff4097a09c5184565c5ad3581c199665e539bcfa1dc",
      "sha256": "39a65504a1d71ec4af19b5d7ebdf94ad854007c787a0f4c751a7260ecda67a3d",
      "bytes": 1809,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niklas Buchmann [NiklasB]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/72132.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/72132.dat",
      "source_sha256": "fdfbfff2fe699f89f1b4665724c71ba18e3a2a8911104f13c3e6a2c116e0a6e5",
      "sha256": "fbb4491454cc1ebe0077efa1019f998158bb03e5516b32744938e0417f300789",
      "bytes": 603,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/28192.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/28192.dat",
      "source_sha256": "775a140d76a7f0253e29ff1b87c97b1caf65dd78df87634564f15c9cb3b197d2",
      "sha256": "1028f18cdf55ba63cdddbe340eb7cb882157d84aeadf0f460173dcbf6c496098",
      "bytes": 558,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
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
    "parts/3837.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3837.dat",
      "source_sha256": "635c9c4dc7c1b9820a50849e5a64359f18d87f4a10424385b515cb10c79b3e2c",
      "sha256": "d50dafaa03a2a8bd086c95f1d13adf4fb406123c89fa7195e4b084b2e8b21217",
      "bytes": 7206,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/54383.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/54383.dat",
      "source_sha256": "5c8d2a4649d0229388af615afc9e954d27844009156404fd546a97efe7655bfc",
      "sha256": "5584040238200f82edfcf74a4749d249541a79d53c8a8f994ba9e0be9569bb94",
      "bytes": 592,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/61485.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/61485.dat",
      "source_sha256": "0440241d70259aa894077e1212a4f72d6373a99b6192972b0b69f4d2ebabb968",
      "sha256": "20d74cc5c8c321c93c1b69af8fefa1f72d1694960739ab7a94b9ddf69fc0ad5c",
      "bytes": 8258,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/30363.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30363.dat",
      "source_sha256": "31810a0ecd76411adb047643d7832dac8e5ab10183382fa68dfb7da531944046",
      "sha256": "7987d153c3c47b2573b73aef64c4683b889e93bd86ae3fb3b14af6e1b926744d",
      "bytes": 619,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "John Van Zwieten [jvan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/3021.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3021.dat",
      "source_sha256": "ad56a79b7c774b99d30a54bd1e198ab95918ba3d1bcfc6a788ca15cf05d757e8",
      "sha256": "4417aac018236736fd7d41a87241ec550737c114cdcddd0bcb4dc373398ffb3d",
      "bytes": 1323,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3829c01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3829c01.dat",
      "source_sha256": "c4efe9f2b3ed960b822aaee6bea9dec4db3c7315afa3ca0d5b1496eed35433fa",
      "sha256": "53678ba4195b1172a4af97913d6f507905b46db2d985dd03b8a6fa0ce69e867e",
      "bytes": 618,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/11458.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11458.dat",
      "source_sha256": "a63db48f5a845a453050271a0ea0dbc8da6f47c57d1ee42d91f1cac139932424",
      "sha256": "8befb1ba0c8134049dab2f3488d315f5fdf2001b3cfda6db082aab685acc23b5",
      "bytes": 1908,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/32073.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32073.dat",
      "source_sha256": "2d4c66bf2cbfcb3aca89ddb2fd8ecc50631093f6e3d693ffd6d9ccbd63beadbf",
      "sha256": "c4786c187f4bf7330c0ff5cb2b0809f501fe5bfe8e22a51915553c88c990b557",
      "bytes": 601,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/77844.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/77844.dat",
      "source_sha256": "3a1abf0ad321a6ac2b57c242c23d076f9e1abcfb976931a29fbef8192917dea0",
      "sha256": "d40355f09ab7f1ec5079cd31e38672bd032752d2c08c91810d3adb8919728861",
      "bytes": 1566,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/15712.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/15712.dat",
      "source_sha256": "d038b496c5c172e56967e26266d82734447417b21c951ce116f20c77b3640007",
      "sha256": "eff4da1993c0e25140c5e76cbf51e69a75300d00bd38014b81e0d51256bf9e65",
      "bytes": 2237,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/5-8cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/5-8cylo.dat",
      "source_sha256": "1b6b84c6316986d887e62da30a38d63d7e789dbf0e77e5ee53655dd78c218a12",
      "sha256": "ea133c575fcea237a53e2f88ad8df9e6e6ad17994b82df2bfe7ce3cf3b94a26f",
      "bytes": 414,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3033.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3033.dat",
      "source_sha256": "fccb28156f2a418eb0e9dc4f73cf51da4f13c5f5dadaa76e5bb643273e8c2067",
      "sha256": "deb5c376be8532e5599b3dbe93947d8c23231979d5c110cb931e63516a50d95a",
      "bytes": 6401,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/32018.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32018.dat",
      "source_sha256": "52544f2b606467ec6f4097afc6b3d3a85cc4827031f16f166c8ec817140265e1",
      "sha256": "8fa3226991b5f6e74270344a8e90f125caa0915f46b74258ef74f708813d78d7",
      "bytes": 14867,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Remco Braak [remco1974]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/77765.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/77765.dat",
      "source_sha256": "2fb7777a7bb22a293b40704bbcaaaf2f113a336bc3ed193edb7ceacfd5f1be8e",
      "sha256": "399918dac7e1b3da3b9251fd64db211c03965d9cb2687163602c4e283bcf7958",
      "bytes": 1482,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/subparts/3040s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3040s01.dat",
      "source_sha256": "e350abf28f7b7e91b9dfbc7f6780974f0841960a0c8d50b7abf5a9e8c9550bf5",
      "sha256": "671a99488dbbaa809c9e04556d2265cff29f022e4d1f8a909ca8d057fce2d7fc",
      "bytes": 2498,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
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
    "parts/47457.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/47457.dat",
      "source_sha256": "3f25d139cb8c6347a9bfdba72859abb013906329c91e70cf7a41c140d6f246c3",
      "sha256": "83cd4da953b83584b9f821fcc607b396f8bb0e611e01fb3d296a241e98068834",
      "bytes": 12195,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Edwin Pilobello [g_fly]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/35480.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/35480.dat",
      "source_sha256": "61d6d988e6549678ec0b6343bf7554ff14781006321da10da9adbbf4e68f2613",
      "sha256": "b18736591153dd2fc2ed6dd1a0af45f87eb9852d65450147fb7a04ece7227957",
      "bytes": 2650,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/24307.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/24307.dat",
      "source_sha256": "959e20f1f282dbdff12aaadcd6b06903ac7272592c8dec38fcb6055e4d5156d5",
      "sha256": "043ebafb0c3434ef820373451dbe3f1668422fe2842239bcb7abe66049666b79",
      "bytes": 551,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3707.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3707.dat",
      "source_sha256": "e7843fe0f96ce7c6c99cd79bff5ee5d5493e438bfb822f00a739f900bf3374ae",
      "sha256": "293a92b433cf6d6a4ebe1bc2a578d90c19f6c6c67797e6fcdbdab58fe0e5cf71",
      "bytes": 687,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3709.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3709.dat",
      "source_sha256": "042ab3796a3dd594bc111071977f6eef0bcf48a51de7079cbb18a32a0b532bcd",
      "sha256": "c4bad2cfb1a84db92c21b9161576e3cc1f556af8de802df61fb6e75f41674652",
      "bytes": 409,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
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
    "parts/73109.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/73109.dat",
      "source_sha256": "88ca9c0322d529f8d6215be9df06cdae2a8dea4140ba22a01f5cb7d3a27b86e0",
      "sha256": "ac1560560214661e4df3e2a80280e48bdcc91056c39f836baebce97b796b9435",
      "bytes": 8099,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/93273.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/93273.dat",
      "source_sha256": "14bec7745fd39abc663d276997724137dbe2c927d4658ea36730213b3df81eef",
      "sha256": "ddc0c5b0334adab7607eec56ef7dbd5126236f0ffbfaa82ebc245622b7a93b08",
      "bytes": 420,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/76959.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/76959.dat",
      "source_sha256": "2ba4ae357cceeaad40a65385bcd4ceac25ef05681d012afb02699dee615c0c5c",
      "sha256": "bfcf0870f371d4bfdf8d66cbb12aae2946d4c2cb5b20e05cefff078f612564e2",
      "bytes": 535,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Florent Faramond [Makou]",
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
    "parts/11212.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11212.dat",
      "source_sha256": "c527adbbc5db2983cdc9d0b28481d57a248fd0125d8aa00c13aebd7c32b6633f",
      "sha256": "1acdc31ef3c210fa24f543bc985049cfa42a2bec6e5a2c2c8149ed190489ad07",
      "bytes": 686,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Rolf Osterthun [Rolf]",
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
    "parts/3660.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3660.dat",
      "source_sha256": "79f4b7c72cbc672054e6972f6faec91fa90571030ce91b1c0c12095dde184ca5",
      "sha256": "ac9e31a766801399a2839a5a308a4ab59179705dd7728cb5d257ce0f1b9ab13d",
      "bytes": 314,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
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
    "parts/1748.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/1748.dat",
      "source_sha256": "d194c62844fbaed08be5faada35cb4ed45a6150ea7d06bb57b0874413cd90e7d",
      "sha256": "8e646254e2b4e3e06af65cc21a2b260c1521642f625575b0a245bdb1574c9de1",
      "bytes": 370,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/23969.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/23969.dat",
      "source_sha256": "dfd50e323a6f7b1c2c138acacbea866edf106274bea29e0562f2740d6db61387",
      "sha256": "f6d19eb632f7aa52725f96d7696ffc0d9c1087cb40b2541c1281b8ea41c126da",
      "bytes": 494,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
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
    "parts/62462.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/62462.dat",
      "source_sha256": "3d30f5717e76fbe3b368eacf72d24f0449f0a7ad4e1603f83a283fb5f38fb284",
      "sha256": "f93fe7f79aeed18b78ab4ffb9be78851726e8ff4d5009a76498f0ae792516e6d",
      "bytes": 2474,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/79389.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/79389.dat",
      "source_sha256": "d319c8dddea6be8b4dbec94b2ca76b844b36bdf4610846b60e4c60c8891de067",
      "sha256": "ad17486271fdca1c5856a7dff345b408520c8a1de5c8c4d48badcb5633b503e0",
      "bytes": 1715,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-8sphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-8sphe.dat",
      "source_sha256": "63a1d64d6c27e64ace1fe6e5233aef04f7af15e39c6e1d36717dfe5c6d226c3a",
      "sha256": "2b1a3d07f1dc6e4f8066fd92ba922a492c74eff376b4cd1b35966dcabe1368f9",
      "bytes": 559,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/11291.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11291.dat",
      "source_sha256": "fdb9c57a17dab2d373671524d5158333dece4ee8b1d15a1caf1012bb7d19d017",
      "sha256": "59c8fcd4408e940786362e2eb6d404247941a8cb934c30fe99b16ff377712efa",
      "bytes": 1022,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/44728.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/44728.dat",
      "source_sha256": "725b98aa6be8e10bff785d6d29308401d05bee8dbd48d54eda11ece2d79a2dda",
      "sha256": "f1e43f40d9e14f75b1bb5a6bb7932f76e37bf4041dd935a3bbb9200e1882c1fc",
      "bytes": 2677,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Brent Jackson [bjackson]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "primitives/4-4ring7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring7.dat",
      "source_sha256": "67b27c082eec7286888ac427f11db06c5eca6c9bcec76c7e2b2014841afa83f3",
      "sha256": "67b27c082eec7286888ac427f11db06c5eca6c9bcec76c7e2b2014841afa83f3",
      "bytes": 1628,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/99563.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/99563.dat",
      "source_sha256": "c2706e2934e9fd6f4ba07a7155f83952ad5937c3b4f187ea903a3148b045307e",
      "sha256": "69638f7b0990593781b673c4488fd9ca14b360bcfa19a201482b83d1709af2d3",
      "bytes": 317,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
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
    "parts/subparts/30363s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/30363s01.dat",
      "source_sha256": "3efe07314a5b42d008e3bba022dc3c7921b16953596cde390ba4a658eaaf8212",
      "sha256": "83d22d10b9c1d80f5b19adebe6d2b697452a5c68a677ef82bdde6c82efffd69f",
      "bytes": 2909,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "John Riley [jriley]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/13547.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/13547.dat",
      "source_sha256": "2950c95268fca53b9724a387115a1f554f75c1694c88e49f93cc7c2bd2bc52b0",
      "sha256": "f0ad7b07fe669b16e8bd55ddbc226523308bbd27c1abd9154862413bd72a8614",
      "bytes": 5763,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/69729.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/69729.dat",
      "source_sha256": "2145aca5aa453d2a7ba512fb6be58ce7a77e9136fbbc137536aa759ef377ec61",
      "sha256": "456dbb1964bf0fd36ca2bdcf9f1ac8addadd10ddc55679a1fb9abe0beed878a2",
      "bytes": 347,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
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
    "parts/14769.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14769.dat",
      "source_sha256": "9f16f101db994b3c5a738c32740f7f17982378a74a0db4e2235efa296217ca08",
      "sha256": "dd9a5bc1a42bec562b7bd3a2d53e56279678bd4462f2de31494b39ebea7b1787",
      "bytes": 394,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/14769s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/14769s01.dat",
      "source_sha256": "95b7a9a3bbc2d5b160022325b86fa022bd8299cd04cb2aade260bcdf70417471",
      "sha256": "522395d41c11cd28b4b9ab5efd4382790bc1d7a05e230876b79c416c99d60a4e",
      "bytes": 651,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
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
    "parts/32192.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32192.dat",
      "source_sha256": "27377dfda4b2bc830b54f749b63dd8221239e37d2007ade633c61472d2840160",
      "sha256": "e9e894f3774dc1079d037602a03edd7ca6dd6cf7262b14e2485698a9c2d4b66a",
      "bytes": 4758,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Lutz Uhlmann [El-Lutzo]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/6541.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/6541.dat",
      "source_sha256": "4e8fd6dea6a8dd300119ad80ca42a9e55b8fb904db98238d93667ebfdd004826",
      "sha256": "d6f9dcc36629b04c2d5451b1517fd94afbfdd1262cfcd9a502f042a8876e5efc",
      "bytes": 1866,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/73825.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/73825.dat",
      "source_sha256": "0b54a78bc58b9adc3ade5bb9255082c1e30153f22a6dce379e9aa6ea87c89586",
      "sha256": "68a0e6833deef7ff8e4c9807b1b8c9ef56c7809495d6d3d8641a7bb37fc11b7d",
      "bytes": 1778,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3701.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3701.dat",
      "source_sha256": "8b720a50ed946757a9e7c33f2bf9f67c956ec24da48416c87610ff0048575bcf",
      "sha256": "269d270e585210f001097471e7599a2650e4b8a98d0dbc1fd62d897a684ee7c0",
      "bytes": 4681,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2654.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2654.dat",
      "source_sha256": "65e6a2e1fe8dbd94fe4252a1c14344dcdbdbb7925a4daeb52938ec4992d238d5",
      "sha256": "a399887fa22098b0fc786388e3dd36d8f1769035e2ef638f29c8a7e7841a59a8",
      "bytes": 304,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/70681.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/70681.dat",
      "source_sha256": "4c0ac823d19d84d00f411caa0690d9f67a6a8ba242ee1f1c652f81e10901c638",
      "sha256": "9b9648095c6392e8b6d99a734a9fd85777a243f8c8c847c76b53db235729d303",
      "bytes": 4141,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/66956.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/66956.dat",
      "source_sha256": "525b8190fd685d98dc32c4e87b9260b14315a2353beb51be1d5b8ca20a3ddecb",
      "sha256": "8cdce3fa8a860b13d475beadc5cdf2fa828f2dddd0fde863b7bb8ad5e17b3968",
      "bytes": 1042,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/33320.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/33320.dat",
      "source_sha256": "5fb4f2eac8858264fcd3a7bfe018e206d3452d51e3b9e9334ecbcbfe3b240d31",
      "sha256": "60c9956b63a6f9bf40ae2d493bf4d4ec058e225411027635869398856ec87c07",
      "bytes": 7711,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/50950.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/50950.dat",
      "source_sha256": "95ce8c0315699aa02e600e36a9fed48f991e95974c536ede259caa5c12c7dd9d",
      "sha256": "df17fc454561d057b42cad26770e4da776c63532799f681cc8bc53868735a7dd",
      "bytes": 691,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/28802.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/28802.dat",
      "source_sha256": "aaa44c27ae9885a6b463aa477fcd1b2b153fa540aba626823bc3bb0844b0780c",
      "sha256": "740b09114f9d93277ed74e0898f9a05f2d8bb40ed5c30194076ba5bf0d64941b",
      "bytes": 1799,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/27263.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/27263.dat",
      "source_sha256": "075cf9a0339fc6546066690b062639de13d2ee13463b55e4f45834813c4c96f7",
      "sha256": "7d0a51f05a690d926f5fe9f305868bf19f9fd3068ce037ef0b82fba308dbc65a",
      "bytes": 3452,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/77850.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/77850.dat",
      "source_sha256": "2deff749e2e2987803a229e56775525f283b129b463ecc336e1a2e953405a660",
      "sha256": "8126fad6c802aee29efd57a3c858f29ae73a4ab024b433a523bde5b020fcfa7f",
      "bytes": 1974,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/14704.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14704.dat",
      "source_sha256": "c71ef813d0e8a77913c364903e1d38a4382ed34a8e9100768e571fd583f2aaa1",
      "sha256": "ccbbcee76f4f5a8248865c3d1e3f1763b0ba1bdc653a6f63e093691bda08f292",
      "bytes": 2012,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
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
    "parts/4162.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4162.dat",
      "source_sha256": "558dae4d9439dfcf4290601873fb2e3ca7387dbe6c29a9478a12003ea604f8e9",
      "sha256": "d747fc447615b6b3b0b176c0705b6cc5a721938e2d0e4f16a31d9218b2a4b22d",
      "bytes": 731,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-6x1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-6x1.dat",
      "source_sha256": "dd1e100388d799a6a4dcecbb1e8fa53aaa2e542470d5dd8acb6446a0324e6fb4",
      "sha256": "1cb161db71ea4b359d056f967ae9a2cd319ef1d39f623ad83bb1b55350e40be9",
      "bytes": 569,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/15573.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/15573.dat",
      "source_sha256": "c6946965875a8275996c4559cd355ea13a20197e96f33585cd750bb1da89b56d",
      "sha256": "53985b42a65537853c8d8a5f9a655e73be1d1c35026ec8e94ac4501764cc0c80",
      "bytes": 2514,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/32016.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32016.dat",
      "source_sha256": "87ea744dda1529115463ae3541f70a4bf30e6de2d479fc61b914d5c0c568eb09",
      "sha256": "8b18819b23ff240ebb0be506e64bfd7b5220fe355e82c4412067cfae509e82d9",
      "bytes": 8911,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Lutz Uhlmann [El-Lutzo]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/33320s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/33320s01.dat",
      "source_sha256": "6c8795d991bc7aa93fc9ce95adb471aa7dc6ca74d66d26236f0038ec95749ede",
      "sha256": "042cd77b495b7a8985eac35f2ab8978926b4a3068fe84de641881334de19a312",
      "bytes": 169045,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/85861.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/85861.dat",
      "source_sha256": "784d1058a83110e5c883ca5f289ceda9fb6b707ed9da86a53c29a89c30197857",
      "sha256": "7c020688e21dd596d3ce8e739d0d74363851ec36247e297a5e6c090003a0b09f",
      "bytes": 1045,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/4-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cylo.dat",
      "source_sha256": "d6ca97ee2e75918b3309a5c88aafcd2455b3a316f7cef8963517c19f1d86b38f",
      "sha256": "7ccfd523adf8b887a1eb8d1b84e30832d48a0f09cfd4810467f72ed936d92d1d",
      "bytes": 413,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
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
    "parts/subparts/76959s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/76959s01.dat",
      "source_sha256": "b51259907d45b9b110c8fdd1ecd26883b6509ac2cd4cce5843d4333ad5819db7",
      "sha256": "cc6c9757763138de0c1a9d2727ec504d5e7664a7f57af7a4e559ece5c63a0ead",
      "bytes": 2213,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Florent Faramond [Makou]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/17114.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/17114.dat",
      "source_sha256": "7b988dc02b913bda1c58ef0d6877a92c3724c852f835631a081202e3e759b6d7",
      "sha256": "53536343b05e650364848dacca37d3928265371b548ea2947e4d52bf8f14c96a",
      "bytes": 2011,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Rolf Osterthun [Rolf]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/44861.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/44861.dat",
      "source_sha256": "d35c30e37e676d32f90a9ef9a0d2b4d9ed881f958c0f348fefbd1bd5bba7262c",
      "sha256": "6db0a80c956ea929477311dcf31ffcc659c5aee26f34a17c015abd2651d38815",
      "bytes": 1704,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32952.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32952.dat",
      "source_sha256": "75845fb18bc640a880033b8933f94da7a71c426cce7011a47ed80cd43663cde5",
      "sha256": "3a3dbfbf825a4ec9ac921b94b5e8d66e27f028889f168796cf4b66ceac94f2c4",
      "bytes": 689,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3006.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3006.dat",
      "source_sha256": "fe6499b0e1b98113d736330debd5809665737c9c7b0c9345af8a673a793be905",
      "sha256": "95d2d5fc0ca5320ea3ec138777c92d21ce1a3ddeb18f14c300756bdc215ada59",
      "bytes": 2482,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/4282.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4282.dat",
      "source_sha256": "8ac1c865bfccefeda7bc7ed5b1105a5389c3b303e5937f3f1ad6bf1736d384a0",
      "sha256": "1cb44ca2e0c14cdf3e8344435eea00a0e440eb48c4c97c287a37f5a7014b0787",
      "bytes": 3242,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/79846.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/79846.dat",
      "source_sha256": "0f53d9a9666aa6b97aae20f266660532d61952682db9620680f115b3db0fb6e7",
      "sha256": "a9e0798c2e961f4904c962baddf0242f751e739e01086a9a8028d7943466ab5c",
      "bytes": 2799,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/29119.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/29119.dat",
      "source_sha256": "54dcca07fc5f5842b88a70eb027a5afe0e9fcf2cf4ffb2fa929020554b6a87f4",
      "sha256": "9716bc945d83bac1bb1554a746e0fadf33abab70f0affb75a0cd75c1c2f491f7",
      "bytes": 325,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4304.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4304.dat",
      "source_sha256": "5ed8033f1effdaf08901ac8ac034fec3a4bf135c6470ca86e413c60b0a7f011d",
      "sha256": "4176c01b4eedf2b6babf6250bbfa7aea678b2a18bc2dee345dc2fd5252d48bb2",
      "bytes": 1306,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/85943.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/85943.dat",
      "source_sha256": "b193ed59c9f1e499542bfeeb3526d649b9de41b92bf4a4c5dafc296bd628a2f2",
      "sha256": "91fd5cefedb98e734b6c329ebaff483e6c9961244b04c34384e504e54b915710",
      "bytes": 5966,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/24201.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/24201.dat",
      "source_sha256": "53fe42324d928c32876373ca38c8ba1bc85c5d3d97261f7f18f513e4105fb118",
      "sha256": "fe1fe010e2e3a8df830a1070c4fabc4f96d1c7b641ed807a1d356df06cb0ae2b",
      "bytes": 2590,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2445.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2445.dat",
      "source_sha256": "1a5bb74442dd985894e46af12d0e313856ba08d9d7c6f7ae4fc3b262e6df0942",
      "sha256": "ab692477d18b68bd6535247b7fe888cc9771891bf8a52b5b88c75cefb02d3fbd",
      "bytes": 2589,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/6589.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/6589.dat",
      "source_sha256": "8064a6eff49d283d98f2a6d8a0f6bdf9873e5a8c5059d9511eeaa8e2a4d4d3e5",
      "sha256": "d56270c0016701deb219ef6e5d9351bbf7da59bc14c318a8a505d6a9c0714240",
      "bytes": 28505,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Jeroen Ottens [JeroenOttens]",
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
    "primitives/clip13.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/clip13.dat",
      "source_sha256": "fbcf72ae53da25e41e2dfbb0159ada51b9e41af1390156086654476cf90a888f",
      "sha256": "25c28a4d90639e3029f93ccdb9fc0ce1fb8cb0532768177efcf5ec709077b4d6",
      "bytes": 1930,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/26047.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/26047.dat",
      "source_sha256": "2df22b606bf562fb460f67944dcb19ab583d1a09362256f75d329727b8dda6cd",
      "sha256": "a8a160c2433e9ffd0defd79f8544722fd0c13c1fe43c056b620500fd588b6309",
      "bytes": 1531,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32324.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32324.dat",
      "source_sha256": "747d12fad747caf3ddf6ad2d2172841d13b308024031659330d84d7b33b15c9d",
      "sha256": "c44c95a54fbfec515c3e21ec053575bcde07b01330ce298aaa15293113751cdc",
      "bytes": 1192,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Marc Klein [marckl]",
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
    "primitives/2-4ring6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ring6.dat",
      "source_sha256": "e51be9ca0a1c92c838f4b188a2fffad612e1309ac3a3234afaaeb640a45fd226",
      "sha256": "e51be9ca0a1c92c838f4b188a2fffad612e1309ac3a3234afaaeb640a45fd226",
      "bytes": 983,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/24299s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/24299s01.dat",
      "source_sha256": "2f7a25e1a7af7d49e2256639971955cccb2f4e364211d182c849f10725a70139",
      "sha256": "525302bc64aa0f6fb179c7bb562ecc35c459716156622a49fc7a4c5997313d22",
      "bytes": 851,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug2-4x1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug2-4x1.dat",
      "source_sha256": "179d252971d76f12196c7c2c3b6f89bb6c7eab21d9df9625f44a8064e49e4996",
      "sha256": "a5fb8107cf947ccad47a75aab62d50d44a05e8dae9401eb2c3eaab9240a3a24a",
      "bytes": 468,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/11211.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11211.dat",
      "source_sha256": "a88c76a8936395abe5554aa2273c92271cc3c595e800a6ecfb479d2a9670f532",
      "sha256": "4c0c3d3305e97580a59247937171f95e5757a5fadfc6f22f11657bac2bcf12ec",
      "bytes": 2619,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/15672.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/15672.dat",
      "source_sha256": "da8b39dc3f5095d6b3caad28a6924a0585e9e8886aa25ef8691912a657421c8e",
      "sha256": "c7e345fb52fb5d86f16aa2cd1bd9bbcc5d70ed8359806a654452c72b5d3ee049",
      "bytes": 2950,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Remco Canten [rempie]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/1748s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/1748s01.dat",
      "source_sha256": "29e1d493ac9b7a479a3add8f460fb416e6e7a903b1fd3c6734b0b249d8bdbd6a",
      "sha256": "5fd5b0b9047101b29a41d336254c0e478985f20b2a78da49df46c5c200d71fb9",
      "bytes": 8614,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2462.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2462.dat",
      "source_sha256": "304f4ca0c40902312d5a4c68b0bdbbb5d75be3df03d64a7f362dbf60022fbf69",
      "sha256": "e00816c4e99d9b34dd0be74f7abbe91991a77d37f5f621bcebe5d52d5646ae2a",
      "bytes": 4765,
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
    "parts/3738.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3738.dat",
      "source_sha256": "934fc8ddec16a9d1dba3bb987ef8dbc30b48d319e9a9d141c051ef437d858159",
      "sha256": "fb1b1e4ce7a87bf557d09cfacbaffa1885bb2f4e281decfbaa3be1c54783068e",
      "bytes": 4762,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "primitives/box5-1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box5-1.dat",
      "source_sha256": "c23e2cb13761c0af92c930af610075d82370a7f2ea89194fa808f0c4cf877bf2",
      "sha256": "c23e2cb13761c0af92c930af610075d82370a7f2ea89194fa808f0c4cf877bf2",
      "bytes": 655,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug2-2x1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug2-2x1.dat",
      "source_sha256": "bebdd1550d6572a47f57ebcff7369be1fd5aaad3db7cceb38548dbf9b63ef270",
      "sha256": "3551d80ae436ef92cb5a22d1fa22ff29a579a4f5d3ff6de7086055fb2b11f4d3",
      "bytes": 363,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/73230.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/73230.dat",
      "source_sha256": "ec023f3811316edc70dd0422b1c87ed2630cc299b63382168076947414a3deaf",
      "sha256": "fecabe6d9d7ae2355af2495d2ac68cfde7b8f5952ac01a0476200096377aff90",
      "bytes": 2542,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/44301b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/44301b.dat",
      "source_sha256": "81afd34966087c870b52f3a0958cb05250476912cd97f8ee8b4c9941952cb603",
      "sha256": "034a6b068b18a64dce32d1aab88772490189146faad6faefea8d25c0c0abe068",
      "bytes": 629,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
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
    "parts/3660a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3660a.dat",
      "source_sha256": "5af0358d61d83b6767358a71055e8950e015f9f6fc9d49687f29ce8835541058",
      "sha256": "f022b089ee1e20462305091e2bdec7a73a54d298b10ae5f2fea17baa84789c1d",
      "bytes": 947,
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
    "parts/2419.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2419.dat",
      "source_sha256": "f4f52aa5aec500d2dcce29f0760da7aa78457ee17e44a5f9573de1bba12f5cc7",
      "sha256": "449887f82c00f25ae2d424f3a82ce0040a4e759c55ae2319d1214f9d02594d26",
      "bytes": 3328,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/65426.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/65426.dat",
      "source_sha256": "4d191f96fb7771c8f5f5523846dc1261d70959ed18771c8ad611e6601519e42f",
      "sha256": "2c8dc7a034f0c96a0d35283243aa5fa6cca87e05ab855fa5b7151f967015dc88",
      "bytes": 390,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "primitives/box.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box.dat",
      "source_sha256": "a1dd11c88627c1a6bfe28119c235dcdad25471c5f8aa948ead850397b939a7c3",
      "sha256": "a1dd11c88627c1a6bfe28119c235dcdad25471c5f8aa948ead850397b939a7c3",
      "bytes": 891,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3703.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3703.dat",
      "source_sha256": "e153e72f7df4bcdb79fa713b7b5d3b711dac9373fc9fbdc45493b8e1cbfd3577",
      "sha256": "ec8fdfd0e3ce8f0ee604bbc71e0ca60d2d2aad45081f5796e90bf858ceda15ec",
      "bytes": 16850,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3795.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3795.dat",
      "source_sha256": "3a18cdb8f18fe9dba6fae79b525aee17be8bee71ea75fce3a794724d2a9b672f",
      "sha256": "2cd41b03b3606b1259a33847127e79f5c4714a0e66b328516e8c4bf5eab48c86",
      "bytes": 1711,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/30357.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30357.dat",
      "source_sha256": "a4d5a169af2b78840aae6122b49981ce7db81ef40713ff994615764b5760edcf",
      "sha256": "00d0dcdbfaa5868947c1d64e97fb27e295ef4258576a64f0992dc40c3c159d35",
      "bytes": 1444,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
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
    "parts/2450.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2450.dat",
      "source_sha256": "5bdb50ad11b750ca1621a7c1717f1dee4af58ae8816af3c77f4af75f7e72f408",
      "sha256": "7e1020bcb9a077b0e6ba643f8acd196b1d4ef728d9616fcdaf0f602a9a4ed2cc",
      "bytes": 2533,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4477.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4477.dat",
      "source_sha256": "4530db7fa36dc6039661336b73d0bf3ea80d8a6d24a8638e57f16d8fe20c501f",
      "sha256": "040a283bc532f0870cba8613452b40158ff4d7834005723ed791ce2f61eb46ce",
      "bytes": 1704,
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
    "parts/32064a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32064a.dat",
      "source_sha256": "b35a848b805493527b83b3a087d0a7f139084834c1f3325045905aa09ded26d2",
      "sha256": "b4948bb85b7dccfd50379b3044b1344635400323a9fd18d8bde95928810ec7a8",
      "bytes": 6322,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Lutz Uhlmann [El-Lutzo]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/32000.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32000.dat",
      "source_sha256": "d5c344e273a7df7bbbd49e5696c973d9f31359e2b658acf620d5c23302c06811",
      "sha256": "9359e90ce29b9d290ecf2e8e3f86e70e4c1368064cb84196d995eecf4cc713bc",
      "bytes": 4439,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3298.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3298.dat",
      "source_sha256": "d362317a6a7aa9dcb4d84e014acc5d64fecd4ef19a54f5f22ebe3f13a01e1216",
      "sha256": "468b453d09a7408b211d7a2a4add2a1f44d17d2ee2d723cfa04aed56964bba15",
      "bytes": 610,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3070b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3070b.dat",
      "source_sha256": "c7608c7e9f40c61747fb46c7107ef141b0a441e381768d2cdac0129f8ad03752",
      "sha256": "c1c118e795562ef6388e5d50773469feb92ef7448404524b8cece05466d8969e",
      "bytes": 490,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
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
    "parts/3829a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3829a.dat",
      "source_sha256": "d55b794eaef00822478da85273c406406704767f0adc77bbd69be92f785c8e9b",
      "sha256": "e37bbb63f34d2749f4fd0723165ae7f4f83b2a359982ed350da0b3bc6de35371",
      "bytes": 2450,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/79180.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/79180.dat",
      "source_sha256": "1fe7323749e3a27583e652f361f119e26593d8024ef4eb0b35cac21e428ff7eb",
      "sha256": "f3882d117aefa91c1af23f3597fbcd5d9ac001e717da0d5c11633f19e429b82a",
      "bytes": 4581,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3070bs01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3070bs01.dat",
      "source_sha256": "34d2f42bf42b1c22a184fbbfea6f51412a0f49def10157b2d472f3f6faf1a304",
      "sha256": "771e4a706bdee9b635bcc9e7cd569f7442c61e0ad64a71a40e2011d8c539e4b7",
      "bytes": 742,
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
    "parts/65429.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/65429.dat",
      "source_sha256": "a3c43bb6e54b88d098a52a95986a55fa4f06aeda14c82d96e5796f74ff0a2171",
      "sha256": "b70b846cc9310abc0fc082f1aaa868c78ae393c7577fd33dcb8bce7f49a0bb38",
      "bytes": 389,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/78329.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/78329.dat",
      "source_sha256": "79ec75c5092750b0f2022dab9c7561376d8b2b33fc3dea7059081ef273d4f7fc",
      "sha256": "c4edf1c4c6dacbaf3627e09828d2d4b45db6ceadb3c7bcf680d37a8c5564af0c",
      "bytes": 643,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/15535.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/15535.dat",
      "source_sha256": "b4866080c6c7e9b2e525c4b8ae17a589a98f6c320afa64f605974ef914cd091d",
      "sha256": "99f3c04c1ceda3c4982d7bb93e9d1e17e35b014c773ef6bc5605d2af222d3882",
      "bytes": 527,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-2x1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-2x1.dat",
      "source_sha256": "03d08cea230e892e1b6cbfe523c19b568a834c5888aac5c789d1fb8d6ee93d96",
      "sha256": "5851ada6bfc176aed63a50773525fd75705ec2ef91caa74bd9db3c6f5ba79af6",
      "bytes": 363,
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
    "parts/50340.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/50340.dat",
      "source_sha256": "a1878f425f5c2edc4530de1663ad23df534b31a71851a4821b008a1ebfbb8269",
      "sha256": "ee0bd4edadc7b1eac57716e1993110042ded60dd6166678c9ec4c78247de4f9c",
      "bytes": 1880,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "primitives/stud4f2s.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4f2s.dat",
      "source_sha256": "aa5be47ef8f9378136f772d0b9dc8bc0d19c64a75f9b3fe02f823930e9477264",
      "sha256": "98afb2aa01e0e61991ad4fdbc72c9adce17be889d0eb414ec02b189f19fc5a0c",
      "bytes": 1021,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/26604.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/26604.dat",
      "source_sha256": "a62afda5f29f4940e628316700c140f8f820ce89cdb1283a56b6acd7bc2a70d6",
      "sha256": "4043691db2b603602fd817a3424d59db7a16079e02c80e0acb63112b2abaf88d",
      "bytes": 2240,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niklas Buchmann [NiklasB]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/80177.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/80177.dat",
      "source_sha256": "402887456cbb029fbaed97a9fcaea3fb96d8991cb362de60eb3664920d459ff6",
      "sha256": "1961355b4505a2f6e52807ba477bbe7591f4fe2d53907449846aab151609d026",
      "bytes": 2117,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2431.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2431.dat",
      "source_sha256": "8e5999a1352d8204101b2311ca435f88c7d7af20fb8214fa588e9bacd3942315",
      "sha256": "b135f79e25abc5b79953babcef79e17e54603a72cbf0106e1a375cf40e69a91f",
      "bytes": 360,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-16ring19.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16ring19.dat",
      "source_sha256": "85335184888f902f5b4ebe51289ccb3305f08cae028d684d20aea5ff19d7031f",
      "sha256": "85335184888f902f5b4ebe51289ccb3305f08cae028d684d20aea5ff19d7031f",
      "bytes": 424,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
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
    "parts/25269.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/25269.dat",
      "source_sha256": "27d965f14caa2c9ebb13c07190f5683da8aca2471671e469e923b623e7978e6c",
      "sha256": "6a436925ba9d3c3fd9a8aa950de44272dee62a1ee670f0c4c76948a3ca3a987c",
      "bytes": 376,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3660as01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3660as01.dat",
      "source_sha256": "a1ff7bd6e237a2f5c7c7f57e7c09ec029402f37e935506287a4d3829137a024d",
      "sha256": "02c6fa8aed9af1536f9315001d769e25ff913fc7e5002786d0ce51c41a498d77",
      "bytes": 2335,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/64225.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/64225.dat",
      "source_sha256": "e9bccbfbea18f42cde0b3697d6c63623d34b2bdedd5f9841aa0fbd41daef24ef",
      "sha256": "68afdbbe58cbe31291c64cca2af805143e00156709eb3cc56cba2017371ac57a",
      "bytes": 51052,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/26603.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/26603.dat",
      "source_sha256": "74bc4947791435f65463427b1a0c187ed5861256256698b45696d2148daa67eb",
      "sha256": "c5463cfacaf63e5c7d653b486ab0d92aee6c0c5d5894c98b6a0eba514e86da72",
      "bytes": 345,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/96910.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/96910.dat",
      "source_sha256": "7d778edf30ddded0d5d2d160a5d4cab472cc8780df8a7571e3c961f80109d554",
      "sha256": "501963ba34dc6706b99e0a360e10f2dd64c9db5a8efffac7c0a66fe79707e55a",
      "bytes": 6248,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "parts/68568.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/68568.dat",
      "source_sha256": "2ac4248a6c0baa21848a7a3817f633c279b2dc142874196029e8c4f509c4d117",
      "sha256": "c9a26d43f4e6afb3ffa1fdc685983a9a7780737efbd131f9a0dc4a2f28700ed5",
      "bytes": 6363,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug2-3x1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug2-3x1.dat",
      "source_sha256": "f34397b5f31ebc52e944090d1ef996fd70ce1ea75568294fc0bd56fb53992faa",
      "sha256": "46c3b7add37604e12a70d8dd481bebaf9e424ea4f4bfc5a929b838666528c522",
      "bytes": 414,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug2.dat",
      "source_sha256": "e1dfe5f5e0c433cd406467d366d278518cde9d7e83cc5d4229c451adf52fcc71",
      "sha256": "8666093cb79e3b874592aac984240a35f3c4176b4c1d7a1440159f5e63b475c5",
      "bytes": 318,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/78666.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/78666.dat",
      "source_sha256": "735bbc8ca8dbe47ad223fcba8bdcd75eac5b1181a8bc6c5ab93fa03b74b20857",
      "sha256": "8addf778d580444be2d8a4ce3b99d6b0dffc365d61b5850af37894c12458628a",
      "bytes": 3353,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/85984.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/85984.dat",
      "source_sha256": "4ec471415207722114f48abb384626d3dbda59796803cafc7feaf824ed88d426",
      "sha256": "024c151d7d4625b7c1a407e8433c2fa6da8a01943b263dc86ba7efd611335e67",
      "bytes": 903,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/42924.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/42924.dat",
      "source_sha256": "fc4235b6958bc6bc23e6e4b93031c4618a4b4edd5827f625da794843ce32cb58",
      "sha256": "d0f3e48fa4ee99c2a51dc20d3b26634c0c3f57f7cf56d19a6437163ecefa28c6",
      "bytes": 3870,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axlehol5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol5.dat",
      "source_sha256": "5977860888c76d8170d9ec33c93f6c431133bfdc79435e7eac9c32bb15c0a83d",
      "sha256": "b165ec3b82bdf9c8a222214d8b71d5d04a1d5b5c772aa563d1b76ee79f85bd5a",
      "bytes": 3301,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3039.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3039.dat",
      "source_sha256": "301b762e26166a9629c143c83611619e1a12f5530f912cb3759973ab4f6c983d",
      "sha256": "75207045bac5e8dfb53d3ce837be6edb34ffb00a786f8c1f9becdc5bc269c3f3",
      "bytes": 559,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/13731.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/13731.dat",
      "source_sha256": "2d9d219ee18fa682f39b423b4e15d8eea2171c320df273fd7cfdaa7765111aab",
      "sha256": "114653d3efad577100ea61810047baedee0abeb8338f0db5939146334e6ad2e3",
      "bytes": 480,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
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
    "parts/subparts/26603s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/26603s01.dat",
      "source_sha256": "0be779a6b9a8be93836a339dfd0a07ea40ad79cb2a5d64ce7774397f71aff2a2",
      "sha256": "599405cc4790674a65a7ff68d7fc12829b049907cbd000e4b8220f20fdb6ba6a",
      "bytes": 834,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/55013.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/55013.dat",
      "source_sha256": "33df6317275cd8d01e333ff9d727f8741d7f59fe877d0098b8f688edda8d8ee6",
      "sha256": "c3604449333e1a7698e21da7e7363705518704164f36a48d26e60c728a7ac64a",
      "bytes": 699,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/78258.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/78258.dat",
      "source_sha256": "62182806d9caf851c3841f50cd99156b0f94db6f714ef9fccfdfbe1a711b7194",
      "sha256": "bcce92850b2b089103b953bfde21841f7392c39413f2f0903405a5597aacc2ac",
      "bytes": 749,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/96874.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/96874.dat",
      "source_sha256": "4d317f22f17cb79465e5c438c927178e448e807192b6ffa4773817ff7a2ff8ef",
      "sha256": "3b6244faf6a23120a545c3456842cccf3c698404bf6357ee4e384baadc13fe05",
      "bytes": 16259,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/48165.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/48165.dat",
      "source_sha256": "cfb440a11c09f931687dcf4b1eb2d93cffd0790f81644103957d1d952414387c",
      "sha256": "5de5b44d2f3ecb8d662b0c795f967e9f8b51ad32c8971c1e1514301e4b1ce214",
      "bytes": 420,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/43093.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/43093.dat",
      "source_sha256": "6ff7c720e1492cf27e8a10a79ffb2eda93608ffea43dc3f40670f399141311b2",
      "sha256": "21f19e937c113b4caf061ede57606ab748af916c8de6c71a6e2e1e803ac5734d",
      "bytes": 702,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/67695.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/67695.dat",
      "source_sha256": "c6bc04850ff571fccc70c74887eea633d2de0e46aa148724c6f4b1050b304757",
      "sha256": "1bbde45d44c71b9633f958e1cdac9237fe301db39472b7bc50451b1aca131550",
      "bytes": 6566,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/68297.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/68297.dat",
      "source_sha256": "4da3513e30c985a48ac825cc300fcf008bee24fd594eff4262e24d9b423c2073",
      "sha256": "fe92b411dfbf36b541733bef0f04385e06fd524fec970e6bf34312437d2a3cf6",
      "bytes": 3613,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/32324s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/32324s01.dat",
      "source_sha256": "050ef46187bc7fdbf44dffd683ca6a14ee6ac66f1f41163d26197aa2d4065ba3",
      "sha256": "af1110ff2a1e571635cf4ea7bfde4aa5f0a6e04ec85142eb4d695935ad3baf7a",
      "bytes": 9000,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
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
    "parts/32184.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32184.dat",
      "source_sha256": "b8b99136eec5188641ad689bed183ad787f5b3325329f7e22c61cf8271f947a4",
      "sha256": "62ad3ddf7f01ae294d628ff37d3a0f24ec1a88c19700146afd617c46238f6232",
      "bytes": 6777,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Jeff Boen [onyx]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/23443.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/23443.dat",
      "source_sha256": "5bd2a9ce300b07802e4f5b63efbe51a5b0f84e4f2195ff37ef8309fce9e332c2",
      "sha256": "4689a53078383d134272a020caf4ce5a9fb8254125c6a2b4a7dfe128c2213369",
      "bytes": 7448,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/48336.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/48336.dat",
      "source_sha256": "489efe3590aa45106913d2e2fa1fd89cf6dd4a55c4f89c20e07f9a5dc729a24a",
      "sha256": "9a8ac0161b4a7e79af670794a82acb2dc0b1cf41508860211acac2e69c443328",
      "bytes": 1184,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/43710.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/43710.dat",
      "source_sha256": "e8560ef89f17bd769bd24a02c9d55d6c973c2e92478ef106d0e4bdfbacf9286c",
      "sha256": "963fdf0a9aa18bf445f85bdb7f40e0518a938d9ff95564e7399be48b42cf634e",
      "bytes": 524,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/91988.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/91988.dat",
      "source_sha256": "873411a516fab0f053bbbf77cfd8d9babc64647d6432400a42a0026635debb42",
      "sha256": "5fb25f4d2e9b4a3ce5a868ed6cf5992da0e4765d43d3a008a15743c53ec92b68",
      "bytes": 958,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
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
    "parts/50923.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/50923.dat",
      "source_sha256": "92623c8cd14469fdea824ad5d4d17e9cbaff6336ec6bc23e4c026a1fbec5f11c",
      "sha256": "326de605014ff96f01f8bec032b570afc79b1b4777f13601dd7e4d9949fb5ee7",
      "bytes": 5288,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
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
    "parts/subparts/2431s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/2431s01.dat",
      "source_sha256": "8fe749b2dc7e732a9cf954472d48be1b095f2b0faef1244035ff4513905e8c17",
      "sha256": "fa97829023b24e3eb8f3b7325723c97c0bc032dc51d541003894685e7b042903",
      "bytes": 931,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3u7a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u7a.dat",
      "source_sha256": "3a5af83a6ab07628ca04494fee90617f459c9b88add044b1bbb96b7f386aeb0c",
      "sha256": "3a5af83a6ab07628ca04494fee90617f459c9b88add044b1bbb96b7f386aeb0c",
      "bytes": 482,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4287c.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4287c.dat",
      "source_sha256": "d4256d2b9e198b7b22124bdb6832c35bd45471b1490817b1a7fdb42bd1ac8a20",
      "sha256": "cfa3387f6f362bfaceec06361573254cffd976cbae4289dca74c6676ca7403ce",
      "bytes": 4764,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4ring4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4ring4.dat",
      "source_sha256": "6fed0ef17eaca407c7b17efc82bb7dc8860324b79817da345ebf32f7911dbbba",
      "sha256": "6fed0ef17eaca407c7b17efc82bb7dc8860324b79817da345ebf32f7911dbbba",
      "bytes": 966,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "parts/4519.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4519.dat",
      "source_sha256": "ecec609013e9d7af63c352cb61d990077c005c4c5453e121b3d192914ab55ff0",
      "sha256": "4dada10c8420fda49f2e24c331eb7e6828e3a0d7cb7428ddab8896460b74ffb6",
      "bytes": 686,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/18654.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/18654.dat",
      "source_sha256": "80a0c04eb2ac78eed9f0fa740cb332ce8d08f2c89c9839cbd9492e8b54d4474a",
      "sha256": "5422d0fd1adf1ec045a02a594baf6873954d35e840e08c1aa15b36565718b6e0",
      "bytes": 357,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
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
    "primitives/box5-4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box5-4a.dat",
      "source_sha256": "70d5f7f2d0720b84a06100b12b449b8ad37d66a02fc4650b31d556d7b1d0fe41",
      "sha256": "70d5f7f2d0720b84a06100b12b449b8ad37d66a02fc4650b31d556d7b1d0fe41",
      "bytes": 752,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "parts/80178.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/80178.dat",
      "source_sha256": "b0b4a6233bd77a27468cd4862de78784f2ea9dad00ba062de6365b3669f504db",
      "sha256": "36efffc719e15502705d4811c9b0bf2f058977e8fd8dc40ee1c8a294e43dd5cc",
      "bytes": 462,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/5066.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/5066.dat",
      "source_sha256": "4ef4b4617922100c316e2cc35c80dfe7185e71951fd71e648444e2138071f30f",
      "sha256": "bdb11284c64aa05747541a30768ca59c0554b76395901dc4428ef20039b023da",
      "bytes": 2711,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "primitives/box3u10p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u10p.dat",
      "source_sha256": "a9a9edde9b651aaae34a33728d30ad606e295e0257bca896a07c1b65864370b4",
      "sha256": "a9a9edde9b651aaae34a33728d30ad606e295e0257bca896a07c1b65864370b4",
      "bytes": 424,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4con0.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4con0.dat",
      "source_sha256": "a74d82aec7f856cc294d7707dd69ebd68f1d1947fc9b0f9801003a70a7e57c82",
      "sha256": "a74d82aec7f856cc294d7707dd69ebd68f1d1947fc9b0f9801003a70a7e57c82",
      "bytes": 1109,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/axlehol6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol6.dat",
      "source_sha256": "e7d0115c0eaab5acfb54d9b4d034bbf938d8d44d3be830aae73b091e1d1ce774",
      "sha256": "6f59a185715bb8852610a557b9b71a61611f39ba81a58d47ba2e15c71e540ded",
      "bytes": 1798,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
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
    "primitives/high-resolution/4-4ring22.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4ring22.dat",
      "source_sha256": "c099a3e13cebf0e96275b33c8320e368f435b5793de7f3bc18f6db9d6b0dfa30",
      "sha256": "c099a3e13cebf0e96275b33c8320e368f435b5793de7f3bc18f6db9d6b0dfa30",
      "bytes": 3883,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-3x3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-3x3.dat",
      "source_sha256": "ec81497656a4a77a32cc09b131026c9882ab2da35944f701aa7575d43667d7f0",
      "sha256": "14b3c35f33fb2f42d6eed98a68abcc48ff80235468d88552ff4ac6d92ac70507",
      "bytes": 968,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
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
    "parts/32802.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32802.dat",
      "source_sha256": "18436c5640920b9a82fb805b01212cf2f40b3a85831acfc6515af7b89b8ea5e0",
      "sha256": "a6f59d6d9b2017f7ec579cf76d85ad5c0e4c62ca01fe8013f11d44380176f024",
      "bytes": 3626,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/78444.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/78444.dat",
      "source_sha256": "60b25df87df3193baa9f66945a3836f7268b9896c3220ddd8deaaced5779cb9d",
      "sha256": "c4d1f543af9b85d0657acb38ac0dce383555ba9501b33f690f54b9c986bb1005",
      "bytes": 422,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/subparts/50950s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/50950s01.dat",
      "source_sha256": "60849823f4bdc411b403c5e28c515e7e114bfd3bd5c456bf50892255d99efad4",
      "sha256": "0deef8ef5531711582c4a8b1e7f1c2aca68294aa740d1467626b3cc1dcdb6c99",
      "bytes": 3983,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Rene Rechthaler [Blechtaler]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-1x7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x7.dat",
      "source_sha256": "56d3a20fd99045f45521dcf3f30914b174d81f7db148187f6701a0a3199b50e5",
      "sha256": "8ce5f123b6fd5b8b47602006d28738d3b5ade6f46d004b2f2c4ecca27102e527",
      "bytes": 611,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "primitives/stug4-1x5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4-1x5.dat",
      "source_sha256": "7afbba4b66e5993938f452531c213e9bfd06744f7967460992cb31b4c5ac4191",
      "sha256": "442a4d124c214307c872e096366c1635886278a73229617876f52592143e898a",
      "bytes": 524,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "parts/30503.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30503.dat",
      "source_sha256": "132b14ffca8e2f2b6296a0a1bcff77187d064c00340ac36fa0cb4784cbc8b56c",
      "sha256": "5dac9c3ec92f0ab9d287d60dd1957fa2fa43808c991779f4af3fa800a194bbc9",
      "bytes": 2545,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Ronald Scott Moody [rmoody]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/tri3a4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/tri3a4.dat",
      "source_sha256": "8c1cf47d85e2d2b429c0ac404108a9e91048fe7c9501b527dda55e75ad11bc4e",
      "sha256": "8c1cf47d85e2d2b429c0ac404108a9e91048fe7c9501b527dda55e75ad11bc4e",
      "bytes": 468,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/24316.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/24316.dat",
      "source_sha256": "9dc8ccbeff15c6a7ef20e9109d8d5eac17a4ef9e9a7ff229cec58a56880062f0",
      "sha256": "7816cfe02e0c09050115124e242c05f68a5a29092d9757ce1b6535120bb6cad0",
      "bytes": 697,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
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
    "parts/61332.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/61332.dat",
      "source_sha256": "aad5098dbfdd4399e30568fba684a7d851b07676e9a709e4f33f483ebab34d67",
      "sha256": "2932cf802890c955a34f8291492c47d333fd984d15226fc9ea0d60b953f036fb",
      "bytes": 2663,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/18674.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/18674.dat",
      "source_sha256": "1a6a54b886d17bf5b5556c1e5db9ee3c6a30cfe5228cc53eabfced3d37bb499e",
      "sha256": "27a5033d5f84585affddf6c614af7891568caf432429fde4c0718663d82715ac",
      "bytes": 1051,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/87544.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/87544.dat",
      "source_sha256": "70dad5448009af938468c1253f98be5a108c67fd8e24779feeab47a5747f3962",
      "sha256": "8c6f258868dfb33ef086f278ac28e0e637aee0a3bc471afe0c7a0ec2493c5d0f",
      "bytes": 667,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Rene Rechthaler [Blechtaler]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/87544s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/87544s01.dat",
      "source_sha256": "1300990698e3c5e42964a13b3704fd6eaaf7d4ca7c0b9f63133c47ba10bd47b5",
      "sha256": "4a6de899925e656db82483dea1b7ef9364a8d98f1d4683d74ae295d3628fe61e",
      "bytes": 3084,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Rene Rechthaler [Blechtaler]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/87552.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/87552.dat",
      "source_sha256": "0e5f75467121336c5b7874381e1eda4d411af863fb9260fc43533649b754396b",
      "sha256": "8a9bf9f6014cffa4d06aaf8a9e9750f2d6f8dd8763bca90aca6f5960a9ccc32a",
      "bytes": 647,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4ring3.dat",
      "source_sha256": "b8b40d441cc3adcc6e30a6869b107f0456ead529510b43b3d8d37896f362e352",
      "sha256": "b8b40d441cc3adcc6e30a6869b107f0456ead529510b43b3d8d37896f362e352",
      "bytes": 3773,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
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
    "parts/1762.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/1762.dat",
      "source_sha256": "e17b6f17c6cda8bede4fd3ef6584956d67721d23d10be7604a1a9706e604f3db",
      "sha256": "38e884f036106e6b4bab2e5f7bd4db50cc2dcc8c1259db81babdcd8129896a72",
      "bytes": 1104,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32002.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32002.dat",
      "source_sha256": "f6b7a001276f00fa004a2c710b9e57271f7261563dc73d5c2feca0f694be6110",
      "sha256": "103c2f3f84150b6d621f17e62c00dbed8b39cda74978648116ef47d21b27b7cf",
      "bytes": 549,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box4o4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4o4a.dat",
      "source_sha256": "a66f3fc32d0209b5b2432c82414997dc0910c48a074be1d96ef5ec088a2594dd",
      "sha256": "a66f3fc32d0209b5b2432c82414997dc0910c48a074be1d96ef5ec088a2594dd",
      "bytes": 827,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
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
    "primitives/4-4con1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con1.dat",
      "source_sha256": "b7e91225acedda94bfcf36dee83212c6b7ab845e435a375b595dc754e3fda6a7",
      "sha256": "b7e91225acedda94bfcf36dee83212c6b7ab845e435a375b595dc754e3fda6a7",
      "bytes": 2770,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
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
    "parts/3176.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3176.dat",
      "source_sha256": "d8a54fbc0da898e0a168f0de89082af2e60719411a0c0010f14faccf0ad4a8d1",
      "sha256": "176ca7bcbab8a3f7d2298682e4fdd464c95ab841bc72b8550d42513532acf5e0",
      "bytes": 1019,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/3023.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3023.dat",
      "source_sha256": "fa3eeab92b077488bae3dbc0fe974ef3327a77f130776d2965f13d3ebc22ab57",
      "sha256": "9c7fc502f7490e49a304f8ad47fb49da0b104a8d7ac0e47f78a93a663953381b",
      "bytes": 397,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/41740.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/41740.dat",
      "source_sha256": "c58230d99e4d72a0948d37fd0e0019d97d12ed05813031bf6aa50fb585614795",
      "sha256": "bce5d31af23f753c95ced3afed09525729e2ecfe6ac914f7f0951640d7867c98",
      "bytes": 1825,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "primitives/stug2-1x3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug2-1x3.dat",
      "source_sha256": "e3944f4657c3e4620509cca9b6923ddb2d88fc9e4ca52d102579f90f6680d6ad",
      "sha256": "0a7fd9c27ecb4e8127833e5afc591282a927d522929b011088cfca2c4dbc32a0",
      "bytes": 414,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/99781.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/99781.dat",
      "source_sha256": "0fc22c8ef47c4e3c7d19a8d34921acea5559d7ffd2cf508fca2a212bbd0e27c6",
      "sha256": "3f3be72785bdd52e62bc30bd4781ebc3d42f140b9a3db7a82173df9b937fbbc2",
      "bytes": 2063,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/15397.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/15397.dat",
      "source_sha256": "2c30210a2c74c9ac221b7eb73bd837f0099f7e449ea6b2c564f39be3fe66fd2a",
      "sha256": "a3f33ee850b25f731b2e269497961c9364bf758babe9c6718d2e24af15185963",
      "bytes": 2670,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
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
    "parts/6636.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/6636.dat",
      "source_sha256": "e4bd77135a542e0953fd9d6e08e050911ce920582f0e1020f02bedcd9cbee84d",
      "sha256": "1294402ab4eb6fa924f3262a8ea20f955339298be539d216b64a32e1ffea4d43",
      "bytes": 742,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3828.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3828.dat",
      "source_sha256": "4414834f8bf573d4369325448a65c38332aac392bb4ab868b48f8cf74dee0e7e",
      "sha256": "a96f0683d7026fc5d67cae7fb502a9e0a277f47022163b085eb935f8199c71ca",
      "bytes": 4389,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/54383s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/54383s01.dat",
      "source_sha256": "0b98f176b3df329edc0721e916c80f9c9007290da9e75c236e3cd6baa120ecaa",
      "sha256": "3586102d5432cc8e724f28e9f719db7faa774951b8032f7afba6600777bf9e97",
      "bytes": 7851,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/90194.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/90194.dat",
      "source_sha256": "e409fe832e570e09d6a74157afbc42e94e474a3527a47ebfb10ac9277a736807",
      "sha256": "673de0bf9df07ccf6bd09b5fc506988fe159f48f44d0e84ca83b0f4f14ea28f1",
      "bytes": 7009,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2736.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2736.dat",
      "source_sha256": "d898ac47d1108483d5e36c1c3fb656003e4716646f6fd5c0850db8e12790d42d",
      "sha256": "e353f9c74bac64fc971ae0191830f4d6b5d1dbac172fed710ce28170533f3d07",
      "bytes": 1365,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/24299.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/24299.dat",
      "source_sha256": "9abd757286fd53c498ac45e6b1d1e610710ad796fe9134529a5ad0e444c44ce8",
      "sha256": "8a6adef8fb0c8bfef84357a32a97b4117d2055f0c1ba3fab11403c26cecfa72a",
      "bytes": 550,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug2-2x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug2-2x2.dat",
      "source_sha256": "7598876867b19a9dd40e058188967a0ea0250e1ec07cdb4aae338ad782ae8097",
      "sha256": "e69a74dd3e9753a681d606aa1b77dec06645440c5bec21aec6ed3c53506dd8ba",
      "bytes": 687,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "primitives/confric4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/confric4.dat",
      "source_sha256": "038addd6f853b704739ee4c9d9432a9557b02e2e6ab8ba874abb35bd9c90a56a",
      "sha256": "89881b4aabf54a5071e24f1ef12d8838b8d40ec08c8eed94d064c58d42e9bf2e",
      "bytes": 1006,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
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
    "parts/34103.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/34103.dat",
      "source_sha256": "81e985e6dce3d56bec5fe2226b16139e38474f2fd1ff63ab4fa6fbdaf8b7b2f4",
      "sha256": "99d0056be1058000ab7b14f23cffd9f1cb88a26608999282fe5e5512022496ba",
      "bytes": 535,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
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
    "parts/43708.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/43708.dat",
      "source_sha256": "ca2d9120adcacc7d0604ee7de598b9e5c5562e4b7820a45f0cd4567206021aef",
      "sha256": "58977c2d111691c27900ea463dbae2f4bdd526f58de1d8555682bc5e78a7a915",
      "bytes": 52004,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/86996.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/86996.dat",
      "source_sha256": "85f41e33d184010baece50154c3337fdf233561e115d827b6d40bf10de5c68b7",
      "sha256": "07472e8a0aaa2a83560f4058ac7d6dc485d255ecfabfe0f541a22a80d9fc7869",
      "bytes": 1175,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/87609.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/87609.dat",
      "source_sha256": "33489f89ea264b31a89d9d92b5da815e22949339a65b08ee95d81dce02bfa781",
      "sha256": "32a33047cf08956e0ad65651a765f56b2ac5324a8760db59c7bb3d1683e23ac7",
      "bytes": 5873,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/3766.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3766.dat",
      "source_sha256": "c3c3d2cf3c3fd3e03773dde2a84a29fbaae660a3bdeeb61c13427a19ef3e25aa",
      "sha256": "2145c6e602bb309460b41658b5cfca57f250f0a3642ff92cd7e417724d74c71c",
      "bytes": 2740,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/ridges.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/ridges.dat",
      "source_sha256": "d9e1a7e71997c20d0467d0a1f9ec00049d204c133b3d25eebf6fdc7260493cb9",
      "sha256": "d9e1a7e71997c20d0467d0a1f9ec00049d204c133b3d25eebf6fdc7260493cb9",
      "bytes": 553,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2310.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2310.dat",
      "source_sha256": "7b99197eb639aa9c527ff3f1283cac652230323847febd0174bd19630b8df0e9",
      "sha256": "277afe7b54ff6852b1100c04b4dac0132b7e2bbe4333f3170afb5803fdbd67ac",
      "bytes": 1765,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/11213.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11213.dat",
      "source_sha256": "6babeb4b350da4203d6d834b8fa21269be2b2c621fca56f5842947a64ab016e8",
      "sha256": "0ca0fd2dbe420e94400be6cf332b98c6171c2247cbe49a5694f02dd4953d40a5",
      "bytes": 4615,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-4x1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-4x1.dat",
      "source_sha256": "2425d69fe600eb8367ffbef363e237bf1c2a7b725a96616b6597705080f4b497",
      "sha256": "659b6bcbb60866be5a47d29958a7200598b83b9297a6a33bdadb40b3bbd54d37",
      "bytes": 466,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/43711.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/43711.dat",
      "source_sha256": "884b7c24be7ca5cb0bdfd2ae6671a8dd47e271e10c3973d6fb27a85784a65208",
      "sha256": "a3d220e6e07ef673cbadf7c10049e9fd5ab245c2344f2b19d8d2348ddfcb157c",
      "bytes": 526,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/connectcollar5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connectcollar5.dat",
      "source_sha256": "07ba9d384db439d768430ab502e1408d9e34d7519757a7544c752d42628183cd",
      "sha256": "395d0861879b290048c37e6c4b0c968f97def6be29b15e2c9c87d8bccafb6cbf",
      "bytes": 3613,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32014.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32014.dat",
      "source_sha256": "47dffbabb4ffdf077951512bfe018a780b55a21e2279f035fd36343073581933",
      "sha256": "14572ba96c0b9a31d6941d039b906c1df32c729cbac224e9cf6e12d2242dd2cd",
      "bytes": 8214,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Lutz Uhlmann [El-Lutzo]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/ribt45.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/ribt45.dat",
      "source_sha256": "5b6445c727883aa656fd52dfcfb3925ec8c95f6ecb4c7b5f95ff67f13c0acb47",
      "sha256": "f5141c060b9b1f1820db92011e8784fa3ae5c441371fc09c53007d0936c04499",
      "bytes": 839,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/13548s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/13548s01.dat",
      "source_sha256": "a75cb067718a8e5bb4e3b0c2f803499d83c9c0a8e60fc38d42e3e36c41e85f9d",
      "sha256": "f3a4118a198f0c72fdee42141d890851a59c4670c0a3ecb41884fa45ab343f67",
      "bytes": 4835,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
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
    "primitives/stud2s2e.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud2s2e.dat",
      "source_sha256": "081b02709254de058a1877984c7f888741ba319be79db085297291a88c5b5188",
      "sha256": "2793b824d5222ef0aa9dc4f07d645c40374972b59fabe4f7f4f089ea7f3f959d",
      "bytes": 587,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/7904s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/7904s01.dat",
      "source_sha256": "5c90b49a6e2c569168f4035322f71247aca6f782f8bac1895bea1d81ecd9b55b",
      "sha256": "3c04a89d92136ee8ba880d87a177d0955c2da10960bb629d540bb464df9f95f5",
      "bytes": 2601,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/78443.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/78443.dat",
      "source_sha256": "01e0f82140065329409e7b6d4f8e58202c6825a71c9a98ac617e5dc79788739c",
      "sha256": "19fe5b3968c3dc49d6861d8c7a25ca5922164912873183c74856ab3af08abd20",
      "bytes": 422,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4con1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4con1.dat",
      "source_sha256": "da6bd834f802df4f9d87cf03ad7b425dcdfa257555beca40c9ae62f9352ecaa0",
      "sha256": "da6bd834f802df4f9d87cf03ad7b425dcdfa257555beca40c9ae62f9352ecaa0",
      "bytes": 1400,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2456.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2456.dat",
      "source_sha256": "59137cf0481aef7fffd3635459813bae50f67869612f64c88e7fcf6f3fd8d384",
      "sha256": "46053f5597165dad370c0de13bc5c5e216b3f4e1e7e5c9749644bbd5e2fdc01c",
      "bytes": 1647,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/subparts/23969s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/23969s01.dat",
      "source_sha256": "fa665618590c48a39b71253ef05e88655a9852fd12b5a3736df7b5fa80572147",
      "sha256": "dd74d453ba148ce855412c5c153f6e88eca3fbc8e5b0c725e867bb8f9d46a6e2",
      "bytes": 1945,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/51739s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/51739s01.dat",
      "source_sha256": "2fa153c39f869c9c9fd4b4289022395d8bf8e748cffbdc2ef98e6d24858b2da1",
      "sha256": "61d73b47842a2d2cd28ef32d5783dca18b0904c5fc6152c87601318430eaf81f",
      "bytes": 2381,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/15571.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/15571.dat",
      "source_sha256": "3a2512db2af032b44a1dd5aba467b98a55c649cf307914f14c997c5700d6a176",
      "sha256": "9cddfd4625859e0959a9dcb172a38cb098947ff7ac981f336708b66d22eef433",
      "bytes": 3951,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/18651.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/18651.dat",
      "source_sha256": "5f9479e8458667cad41fc87c8d5d0bbc4a548bc8e10e3b736c5cf0476dfa58d4",
      "sha256": "04a20df9847b46e53af39f67845b9c2a36af1a1b569c449994a753633dfe854a",
      "bytes": 779,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/22885.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/22885.dat",
      "source_sha256": "4de53d9eda9ba6c71310fa64726e03365dcdb1ea4d727b4f56aa91f4f7856e4d",
      "sha256": "1532a216887f6487a1c4f53155001e70824990e85f64db089e8f6c164f28acb6",
      "bytes": 2352,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/87087.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/87087.dat",
      "source_sha256": "0d170f4222bc555c4c0f85de872f3481715d4e2557a0359448d95352df1b2ac9",
      "sha256": "3468d0dfcf43a37cc1fd58da7af2fbfdfe6be8295f77fbc4f2c08431fd388572",
      "bytes": 1445,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32291.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32291.dat",
      "source_sha256": "ea01f7274042e2a6d14d72ae4b6a22caeac28994621ec89b6a8db6b5369fa6b9",
      "sha256": "59be0450e266a9aaba74a1e77751ba26d01ae50efbf9953bf8567054bb857cc6",
      "bytes": 5640,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/35044.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/35044.dat",
      "source_sha256": "246bcf37907edf37f3b30c15f26c6bad435487e3a5cf53b26e2238f139ab1915",
      "sha256": "f8431f84433d78acfd5d764a153aaeaf4e62397152a7b5528ac546918f6a1fc9",
      "bytes": 9119,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud2s2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud2s2.dat",
      "source_sha256": "47e7d97470e80b5f97ef78623db8fb8b03643fd2e1115c5d0b6c8b8f30ede983",
      "sha256": "94c4dfb119ba93df019ba97765d1cee0bfd1ab51a247dd07c8f1a01f44d72467",
      "bytes": 637,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
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
    "parts/6141.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/6141.dat",
      "source_sha256": "fb2cd4fad207392508bd2ca8b5469b1c351b692e111aa06b55da55d53fd44dd7",
      "sha256": "0364e421813b92ffebd100b815a9a40d630759eebc11aee37ac637eeb9e2ee19",
      "bytes": 1069,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/52501.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/52501.dat",
      "source_sha256": "3ba239c855e9335b4e61916ebb548d23214fcdcd15ed7ac46c87c8c770af50f9",
      "sha256": "6deb2e095fa2f5430591cd0b7cfbf830e0144d593e19f24907e771919a768b87",
      "bytes": 4537,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
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
    "primitives/1-4ring1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4ring1.dat",
      "source_sha256": "5d34b5bae7e8a8f7c7100d61e8cf2e4c2d7a4758edeee66911d968114bed9cad",
      "sha256": "5d34b5bae7e8a8f7c7100d61e8cf2e4c2d7a4758edeee66911d968114bed9cad",
      "bytes": 834,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/51739.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/51739.dat",
      "source_sha256": "7b07281c2fa86a18bf5f9461cf6dfc2893cee1186fdfc7f27e1ec453ecc6c53d",
      "sha256": "ad8b3758945b9f8a3bdf50e8b7643acff1218ae4dae2a1b58a8f5fd7ab148fa4",
      "bytes": 1316,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/87079.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/87079.dat",
      "source_sha256": "bb9846478e000ce54f7ffad0ea82cb9e4a3e98e1a1b8d04799d4b26a2ac52eeb",
      "sha256": "f823920553bba943f6d700c67fa0040034c767386ec94ba81e1e8a49b96a6f3c",
      "bytes": 583,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t01i2000.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/t01i2000.dat",
      "source_sha256": "877574c6be908beb7a51832d7cf7d3abee5cc13c404377c56632b7611b7c54e7",
      "sha256": "877574c6be908beb7a51832d7cf7d3abee5cc13c404377c56632b7611b7c54e7",
      "bytes": 17555,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/connect8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connect8.dat",
      "source_sha256": "0bc309d24dbf2b1bda1a0dde6a065d230e81c7d1f012c622ac0fafecf7f98529",
      "sha256": "33bae4bee8c29a1b1a667135186dc1ca7d80609df7564a257460c876cebdc467",
      "bytes": 6884,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
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
    "parts/18980.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/18980.dat",
      "source_sha256": "1b147eec799e747db9179695803bdf6987d6f82c0bd38f8c0bad7c9ebc25cc5f",
      "sha256": "3e379ce57bb3e0ef0eafb381bf58c4fa551263ff695db7c9da0b7306bbb592be",
      "bytes": 1489,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4ndis.dat",
      "source_sha256": "4359a309a22272c7b82b284b28c99bcc0a120c34e5ea6351e59da356890b84bf",
      "sha256": "4359a309a22272c7b82b284b28c99bcc0a120c34e5ea6351e59da356890b84bf",
      "bytes": 1135,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Franklin W. Cain [fwcain]",
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
    "parts/41682.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/41682.dat",
      "source_sha256": "5cfa8cee2d25fca26c2283a12b43978f4861359bc69affc26c337c3bdfcfb8f2",
      "sha256": "3fefb5cfece82e2ca266914940f54a32e41c9d5018059a56dfb3fbc9db2d2f32",
      "bytes": 2206,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/65429s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/65429s01.dat",
      "source_sha256": "7dfae9d3473c7739b87d00198fed428b18ed1f717b1a062a7c573df29d799c75",
      "sha256": "c5c8d22f79c1a8abcf39ab1afb66188d5cf88053cbf0168dd08c5471facfba24",
      "bytes": 5717,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/15535s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/15535s01.dat",
      "source_sha256": "645c58e841efaec59ef35f9eb5ef9b5aeec4b6e2a10c539e0502577b004f5889",
      "sha256": "fdba99f1a41c487edac9a2ac29cf1dcbf6114aa3023aeddafc7c1e7c5c94bc56",
      "bytes": 582,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/5649.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/5649.dat",
      "source_sha256": "18a50c75d7ec8886d7d1a18ede714d9828bea17da2a409dae7355eae5f16bca0",
      "sha256": "e99f16e27c40320063881104cbe12d4c75db9b4b6825dac1861011d2f03953ac",
      "bytes": 1210,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/32803.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32803.dat",
      "source_sha256": "0814f31a00ee30b41631f8451d4d84a3bec81517636ea3b1c324a99ffaa39d89",
      "sha256": "19b064d76b2c934b64271dc99af214c44c39fd1a7bdbaa948fb830984b92e36d",
      "bytes": 2995,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/peghole3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/peghole3.dat",
      "source_sha256": "21348115453a7745bd59c1d9903bb8daad0bc89ef5f4c3e5c74ce432b54959de",
      "sha256": "83b960f5fef18ac1d0ab4d3c9260f3487a395ba5826788e4098a9b5c20242bf4",
      "bytes": 1201,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4ring2.dat",
      "source_sha256": "bd89c3e763a34c598455330647ae0c5c16ad4a031e1c72408be7f6eebb4133a9",
      "sha256": "bd89c3e763a34c598455330647ae0c5c16ad4a031e1c72408be7f6eebb4133a9",
      "bytes": 3757,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/87580.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/87580.dat",
      "source_sha256": "9f1fee81902d00778bb6e91d6239d83ac6e3fca788954f30bbaab149abff6d54",
      "sha256": "1bdbd3dedf5781ad35795770fc1eae003799d61f1c6744c98c7468ff154d5f21",
      "bytes": 682,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Joerg Sommerer [Brickaneer]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3035.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3035.dat",
      "source_sha256": "325a0682753f92e97145d8e750cd86ac31af565a852554725f9bff27a1fd8cb8",
      "sha256": "1a18d0c8247f3d8efac6e28637ccfc6ea9ccdc149e05ff9c0bbbbdded48454f3",
      "bytes": 3716,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3484.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3484.dat",
      "source_sha256": "9f3aa420e80253f13ac9e423ec5a9d724d95f83cd36f22ea31c619e4f9434ca8",
      "sha256": "f2f36e3a672ee6b26dac12eb3554586eef1b7aeaaa5f6b501415b9c488bf4203",
      "bytes": 732,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/11153.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11153.dat",
      "source_sha256": "7a9cd5156ca6cdc39f0626f73297248bfd4acd261684594c7f7c4f90c2c23170",
      "sha256": "e05574b804a85459c2469fa9ff3d9a4bdb6dacda4da3da6d132bc07c020f0b32",
      "bytes": 332,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Rolf Osterthun [Rolf]",
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
    "parts/63864.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/63864.dat",
      "source_sha256": "040f04315bec9f44a0250220303aa74c9661e6a8f26c2539a80effee0a27887d",
      "sha256": "53296079ff6a68fdcb8b94bfa930c027d4f49ac227cc14446067c4b82c6621ba",
      "bytes": 446,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring15.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring15.dat",
      "source_sha256": "d0eafd1cabc3eaf0d254f590d1ab5dfa9eaafed9719f6257d1ab3fb181f2bd8f",
      "sha256": "d0eafd1cabc3eaf0d254f590d1ab5dfa9eaafed9719f6257d1ab3fb181f2bd8f",
      "bytes": 1696,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
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
    "primitives/stud4h.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4h.dat",
      "source_sha256": "ad758cd52c58cadc5ed16cc8d2248e22ef159d3529f25ca8312ce0ba8d131a92",
      "sha256": "64888f70937b95b934f6acc09e35d25636fc6341f6493e04706656712c7a2333",
      "bytes": 724,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-8cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8cylo.dat",
      "source_sha256": "bc5df94184d568c4b032959d7ec8fb138adc17acf14d8f9b4d41b69e96bc9f5f",
      "sha256": "7ce86496e88d239d642172b1390855272d9aa3b7d9368bdb1f6f53d031067deb",
      "bytes": 483,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
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
    "parts/2639.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2639.dat",
      "source_sha256": "5fd91ee37f9bc3739c07adbe48875673df07fe067405151b7217d5ff594b6012",
      "sha256": "b7686116a5e755866ef2ef6c125eb8ea301011c93078572ce37833f55cc499a8",
      "bytes": 3494,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/subparts/80177s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/80177s01.dat",
      "source_sha256": "da19b24ea9032be29fc66011e9cdc34f3a90f1d524e0816ca1969ae8956a5bc7",
      "sha256": "b514b4e74d88d3a97e0eaa0f2d83c87877f6e865559e6b4525c581c3ef40fb74",
      "bytes": 13283,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/64799.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/64799.dat",
      "source_sha256": "3421b418451513b3346db7d0886268aaf7eb62cf41268c456b5c017d7571e320",
      "sha256": "ae04477d0ffca7f8ed7cc07657cad746f201a41ea1b32cbc987f95cf7ff81766",
      "bytes": 3138,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/34103s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/34103s01.dat",
      "source_sha256": "6356fdae493a0e9bed79cef55e145f62a83826998279befb311fd8467a102233",
      "sha256": "e6f946899715d5410f7f039e014463f5593539d64d6735392a421d458333f133",
      "bytes": 2385,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
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
    "parts/55236.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/55236.dat",
      "source_sha256": "ba0dd0de116b2cec72ccce2853b8b7482111f044a6934cfe6719ce22ea5e3263",
      "sha256": "0e9003e4ea3a3a0cda473454bfeea85e5ba6cdc55b7115d4627f182a873217fa",
      "bytes": 79426,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
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
    "parts/subparts/1762s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/1762s01.dat",
      "source_sha256": "ada490c046d9a9bdced6aa16da4904321a740c3bee897e24b2965f6bf181bea1",
      "sha256": "adf3ff76c25fa58de14ad34316527bec30a2987cde38572526de0355f87e8720",
      "bytes": 6320,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/99207.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/99207.dat",
      "source_sha256": "fa15d4d820a874ab370cde738955e56094d3aec22b9d23d3987209edc3dc8432",
      "sha256": "84d0a4a88a0bc2598539e50d2437877d2fc0ff4c26e36ec619f293a07cc7f88c",
      "bytes": 2074,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/3172.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3172.dat",
      "source_sha256": "f20337f7944f6fc8080c2165b491fc9fed215e863cc59214f37456bdbebe61e6",
      "sha256": "1550ef90ab6a2624534c4db4a24250b4ec79872a6006dfe2f98d0c180363f0f7",
      "bytes": 2663,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/6632.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/6632.dat",
      "source_sha256": "a79de214f796e2cfcae6e2327e69ae0674f3a9727b64ab3d644203d18fde394a",
      "sha256": "7ba3cf7a957938af5220cdcf8aea9a826ece39daae4feaf5aa70dc2b7b445aeb",
      "bytes": 1468,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/65509.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/65509.dat",
      "source_sha256": "9ae28cbb0d73d5448fde83c9c296c5bc8747d95243f467080a786985ad922c1e",
      "sha256": "77a14340a2fc1b94b34852c2747612c6abe21c2941277c0959347de9757c092a",
      "bytes": 467,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/88292.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/88292.dat",
      "source_sha256": "180f44618797ce84c1e4ac3cd8c40c24126018b1fcaab9e970f520834e361bc4",
      "sha256": "a5232c964289c9be2629e4b1a8b974bb28067a9a4d5e1e7a9ea716947d03f8e2",
      "bytes": 3896,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/subparts/85984s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/85984s01.dat",
      "source_sha256": "be8c8a230e87f02663d9a985895d1342fe5246523609296e3d64862895bb8721",
      "sha256": "9c18ef813035cbcb094f9a9d6cb42675c092a11e4d1eb37d0b4c257dd4f4a33e",
      "bytes": 5250,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/73831.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/73831.dat",
      "source_sha256": "4d0378d08a37a67bff9a262bbe5ca6eb78b72ac76b51c391716b29d55be1a028",
      "sha256": "6cb05b665dd9bb359d3433e721cfcb24a6acb6df62cad61faee369d985a41ca6",
      "bytes": 1992,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "primitives/stud4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4.dat",
      "source_sha256": "871cdcab26e7f5113488a24c453d6fabda75b275b06de592e0bfaad4292c12a3",
      "sha256": "b4c45522882db818641f56b4abd95c5ba3b76da74c567ba0d9dc3da89c10fcf0",
      "bytes": 1005,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/67329.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/67329.dat",
      "source_sha256": "90b7dd721a756d84c0248598a506e7d287d217893bc4b95d483092489d06ba1c",
      "sha256": "709b9105536306ce618cb3b554d8d50a9374244faa82eea0ba897cf8f9ff7f1e",
      "bytes": 439,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Rolf Osterthun [Rolf]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/42862.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/42862.dat",
      "source_sha256": "88df9aac666e1ec45e341aaf04c4b4a3a1430d0c88f5300d3c1b887577b88709",
      "sha256": "1c83b4eaab507604ce5cdf6a1b29594be84f9304d2034261d5c0c784b604821c",
      "bytes": 417,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/60470b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/60470b.dat",
      "source_sha256": "04cb0b662f4d4f9fbe0a5d50a4c285ee318944ff95d9cf02d017fba5360fe31b",
      "sha256": "87d10e8770aa2e46b1cf2aaa296f3b3073fc458f15f9c43568775dd12b06eca8",
      "bytes": 1265,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4ring18.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ring18.dat",
      "source_sha256": "b253419394f98c8f3be0b8d07ed3b4f4c6272f9e535050bdac90abcda0ce6740",
      "sha256": "b253419394f98c8f3be0b8d07ed3b4f4c6272f9e535050bdac90abcda0ce6740",
      "bytes": 967,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
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
    "primitives/tri3a1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/tri3a1.dat",
      "source_sha256": "f4c045989b96a7ba22ba7f7f9414f2bdfad8d89aa280778f49f1d789ef6acbe4",
      "sha256": "f4c045989b96a7ba22ba7f7f9414f2bdfad8d89aa280778f49f1d789ef6acbe4",
      "bytes": 520,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
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
    "parts/3068b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3068b.dat",
      "source_sha256": "57179cd9dc0ee31742b9947157636b1b5eafc8d98a283fbd99e9abf8fda977ec",
      "sha256": "bcaf3d8d9a0d7c5e66e97d4ccff2d849290595d4a9a2488b8ccf52d93819e74e",
      "bytes": 817,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Takeshi Takahashi [RainbowDolphin]",
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
    "parts/30136.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30136.dat",
      "source_sha256": "6962505eaa5bdba252dc42d6c5990a9f8e6a653b2b6650469bcff488f304a242",
      "sha256": "9003d275b0b117f0108051cda77d4004b681ebd171fbb7aa4bee4473cbbb6e36",
      "bytes": 2766,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/37352.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/37352.dat",
      "source_sha256": "ac079482cadd761e9bfd83b19495be202d7579260a393d33a84ce83b1db11cae",
      "sha256": "3108c1ff3a4ebf963cc9e3719251701712e69fa6020124fe803dcf7b9edfa69e",
      "bytes": 543,
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
    "parts/11215.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11215.dat",
      "source_sha256": "a92ad6242848d4d86b9b40fac2e317ac5e9af15730d94e67d373cd455076a0cb",
      "sha256": "b30769cea1450d95f66bbc21721caa4c7d6c18a3e3e5b9f2a48311e27f901d1a",
      "bytes": 5072,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/98989.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/98989.dat",
      "source_sha256": "da6edcd1d76da069e8b1d9ff4e91ad9a6faddcec710b8362464d3b5e63730ab3",
      "sha256": "2b1cd595385024b627f39c81602f50ba7adfa647ee67cf8f6a42f00bf4b9786e",
      "bytes": 9577,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "primitives/stug4-3x3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4-3x3.dat",
      "source_sha256": "7028ea702a2cdc2be01565ac1672c9a891bc01788a52b54e98ec05c68e370f00",
      "sha256": "c336bacf08008b721dd6d53646826fe37ad3bfbd697a723006b11e2192fa55af",
      "bytes": 740,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/36841.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/36841.dat",
      "source_sha256": "4cb6480708e17c8ccc9dd80047f4c72ff46c1d187e8a5995ddec0b08ec714c58",
      "sha256": "b94c98ca60c02eb6fac3a30188229cee036c25e64ce869326d720cd4d81f9fe3",
      "bytes": 1637,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/48995.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/48995.dat",
      "source_sha256": "868e2ed1a5145c3a6b5bb1bfaae2abbff20babbb1ed230d960ea27f7c0224570",
      "sha256": "eef805d0c5fadc2b7d365344398b9e7d5af4c1a92e672117783398e95793f873",
      "bytes": 656,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2654a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2654a.dat",
      "source_sha256": "bfc1e914300019b7bf1d8721c82d37315725e0edded205717dc797bae6d859d8",
      "sha256": "6abb286a16a7a78d80e417cda8705f60bd62b8bde15e00d4f3c6c63a9ea103ad",
      "bytes": 4188,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Evert-Jan Boer [ejboer]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/67696.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/67696.dat",
      "source_sha256": "0da738301f08f550e60471d674ca01a9ca3d76e91c24d781f8032cc9741938f8",
      "sha256": "1ccc7071cfeab35b65069f9ab187a951b27d7a8e674a548883d81b7f99faa55b",
      "bytes": 1125,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/78257.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/78257.dat",
      "source_sha256": "4ab9e502e6045f1039cf1a81fcbc73d7aac6b732e920661ef1a113a0348827a1",
      "sha256": "b2bdf9e351cab11ce70c62f5251e0a2f14c2fc76007b60621832303e3865fdc1",
      "bytes": 1261,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/63868.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/63868.dat",
      "source_sha256": "12d633c88546c6fca9417bc0c0a00aeb855d3a1e6da20f98d8d5a47fed697d79",
      "sha256": "83746563f0aa398e6ddb429b60caff666954904f73af4681d274430acd65d96c",
      "bytes": 1177,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
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
    "primitives/stug4-1x7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4-1x7.dat",
      "source_sha256": "faea6b3da53b4b9c4313577eaca0b03f7d7062d8ee6a44aca9c03abab8d8fc9e",
      "sha256": "5e5619ab03a50b70cb9c30da5b7c57bdc1151eeb68a0c9c7eb289dcaa138aee3",
      "bytes": 629,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "parts/3002.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3002.dat",
      "source_sha256": "02065cff45c9f5cbc52259757813d3ac66e013777b759bf35a6bb94c9cbf1681",
      "sha256": "4ca6fbb87b7c388ebf7b783029ede7ba96ea99a37b32475ef87c88eb30fc2ed7",
      "bytes": 694,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3665.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3665.dat",
      "source_sha256": "f2aab885f641bf17707c020d5962660977d3c6a838d372bdb71ff0aefc640a4d",
      "sha256": "8c5c24f5c78f82b89408e278299763fdc659468776bba9404c9b8348084e0d72",
      "bytes": 314,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
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
    "parts/subparts/44301s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/44301s01.dat",
      "source_sha256": "a15b16bdf7142e7f951dc1d8fdba85876d40ca61dfabb0729b9b38e80a8dfd0f",
      "sha256": "45dd2aecdb41ecd4dfd86552c939563b02ddaff72828efafb86aa061ab3927b3",
      "bytes": 964,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/28192s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/28192s01.dat",
      "source_sha256": "d5d7b1f1c50074096102594094a80fc9d782b2293e126697ba60a3081d0d4c9a",
      "sha256": "e145a3d43b84f19eefa5c6369faa616be557ff5c44af74fe315a9fb024db27cf",
      "bytes": 1627,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/89678.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/89678.dat",
      "source_sha256": "7b56ae687b68e042660d175f55cb3241329b9cbde63b2a3402eb47f1b1cf6093",
      "sha256": "5006dd3bde51d280d694a237ea6438aba716f39fda588c0869c3672ebd4cf8fa",
      "bytes": 944,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-4aring.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4aring.dat",
      "source_sha256": "8d67989822c019531862f5c2d5cc724145f5e81e00121433065d3fce3b52dac2",
      "sha256": "8d67989822c019531862f5c2d5cc724145f5e81e00121433065d3fce3b52dac2",
      "bytes": 673,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
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
    "parts/subparts/11291s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/11291s01.dat",
      "source_sha256": "d99eed2e5e23e3b418b387bfe808e05a14e867cc3969ea8e733b471eb654bc22",
      "sha256": "36deeb8e6211c52b53f11041502853c5a6d229ab13ce4368cd9643eda76af8b9",
      "bytes": 11520,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4ring6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4ring6.dat",
      "source_sha256": "58a64c659a70b3c371b5b8e8b3716fdf954139e97ce2fa09518b950e59559e34",
      "sha256": "58a64c659a70b3c371b5b8e8b3716fdf954139e97ce2fa09518b950e59559e34",
      "bytes": 3654,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "parts/subparts/18671s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/18671s01.dat",
      "source_sha256": "96389cd775faf8e7690928e7dc3d82af65fc80b9fd8d51db02e0084d34aafca0",
      "sha256": "5ba610e493faf07dc165bd273b44e50f821d660b49e7ae6fc25ea0014547d254",
      "bytes": 2381,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
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
    "parts/93274.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/93274.dat",
      "source_sha256": "a79e081e0e2bad746ee66458e4f5c342bf1ce5b7a2161e0fde9732bf26bc1e8f",
      "sha256": "be9d0eb229acc932b15bdd6043fa06e85d96dd4e272093446d10e50704849725",
      "bytes": 2348,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8cyls.dat",
      "source_sha256": "ef52179e3e48dbdb94b5b99a69839a2d0c4d9cbe110dbbad234da311060dc51d",
      "sha256": "ef52179e3e48dbdb94b5b99a69839a2d0c4d9cbe110dbbad234da311060dc51d",
      "bytes": 1326,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/subparts/3766s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3766s01.dat",
      "source_sha256": "46a3fb5ccb32e32e71d9538541520a9c7930f4c21444a8afdfa8fd0e887ab432",
      "sha256": "b3d7f2614d7c84a2201ad7e0855cd3cf16af580f74751bc34e64b4869e05f90f",
      "bytes": 2280,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/12787s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/12787s01.dat",
      "source_sha256": "bd20243da016fb8a85df2b5c94bdddb104e8fcfa4a6d5c3ec8b62d0c748a55e7",
      "sha256": "d38514a061a7fd6c5005182a397fb4104ec3749dc05d6bb6f002265162276eac",
      "bytes": 769,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
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
    "parts/36840.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/36840.dat",
      "source_sha256": "292173cc2f450be1dd7a155140545a023e48fdb9b6594e8ed0d7fed8cbad681c",
      "sha256": "ba61be093edfdc729c0b34f798a5e26d04cb8f520f7736fb2cb217b67ca8c51e",
      "bytes": 1723,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/connectcollar3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connectcollar3.dat",
      "source_sha256": "3819ba78c3042db1aa6d2c96591538e964bbddb1f6cef97c01d63c64b06a538f",
      "sha256": "7e6d5745d32499ed0c95871209c7fcc117584a9dca30999da2fb078c8a91e366",
      "bytes": 3685,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/clh6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/clh6.dat",
      "source_sha256": "d4b66d6adfec456775ca0c193d7a57f65a25a9c9a7342de0f819451ff2ee779e",
      "sha256": "991f305a9e98f7a1bafec2dd10235ae5950d4c3bd3ca3b04d2dd773192316d15",
      "bytes": 1910,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
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
    "primitives/stud.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud.dat",
      "source_sha256": "db037d518d7c08bcdc1f0e7497f4f98e97d99850531dd62d602965520f3bf8f4",
      "sha256": "20de312b34b2769113d15581ed298971d246f7585f23cffe1e334747a6d3ced2",
      "bytes": 738,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3-3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3-3.dat",
      "source_sha256": "41b7873e9102a898c6d89c22fc2b7e733ca1afb6bd0a4b5b5a9497b13a5a86e1",
      "sha256": "41b7873e9102a898c6d89c22fc2b7e733ca1afb6bd0a4b5b5a9497b13a5a86e1",
      "bytes": 709,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/29120.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/29120.dat",
      "source_sha256": "ba0fccf62cf9d143a4945cc183b8233e57da640754c17bbb3d35645378d6d173",
      "sha256": "9326a32a626105248145cdc8643cf513942d37a03c64f5231d2b177f4cd8c99d",
      "bytes": 5304,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3673.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3673.dat",
      "source_sha256": "d846c8c80ecd254b61378e7a40b5b75b243be75de63b2458ac834de988c05b7b",
      "sha256": "6543932900701de8f9082d34cd3b35c60542fabac2b5a450d521d66f6951d429",
      "bytes": 515,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/3709b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3709b.dat",
      "source_sha256": "9235cd86abe488a4a644efdf43a1bf927c9f49b39b0e248b91f3608ab13447a5",
      "sha256": "0ca26216652f3e3a22d286d3a4b16b6a65afa8dc52acf6c10f33d3a8e664b422",
      "bytes": 2740,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/clip6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/clip6.dat",
      "source_sha256": "814e294097fc0ba433756469579d1267ccd88ff43ef1e5edd0f77e24037f628b",
      "sha256": "3eb148e2385afb6d200a554fe6e9fa3e6c60f464171dc3c6c882e9e493507794",
      "bytes": 2933,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/stug4-2x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4-2x2.dat",
      "source_sha256": "cf6e68b84d37562ed1a035015c23f804157ce6a80a7632a179e4def8ddcacfcb",
      "sha256": "bb92ecce31e81395ae67a4abad112022d7e3c085a465c9a8d4f05f054d3d9255",
      "bytes": 479,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "primitives/high-resolution/1-24chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-24chrd.dat",
      "source_sha256": "9c1442d69aa0acfe4de87e4b9cdce8b164c88289640c9aa980afafb7b4aabd74",
      "sha256": "9c1442d69aa0acfe4de87e4b9cdce8b164c88289640c9aa980afafb7b4aabd74",
      "bytes": 311,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/25269s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/25269s01.dat",
      "source_sha256": "104059a3b2702cce52f7626190f0876ae91972c9d9751c0bed4a0f686d6378fe",
      "sha256": "ec870614f0efa5e1536eb85270ab2ad2fb9fef7fe6bfeeb6d76982bd70a1d5fd",
      "bytes": 3834,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/subparts/3039s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3039s01.dat",
      "source_sha256": "febe4e468e966574084aac811cbf5321670d940736fe3ab748276fa585ac9962",
      "sha256": "7997b87578cc4b2b9ff56958c954cc23eab1114fce629442bbcc58d37e261c31",
      "bytes": 3082,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/77850s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/77850s01.dat",
      "source_sha256": "dcb501a23e7a5108bc3085e43e142281805b8a6bfb3be783b102343da8980a65",
      "sha256": "a6106a690b5ca173a7947c8f33731c4186379181f84c88508c33b0564aaa2496",
      "bytes": 1145,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/4162s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/4162s01.dat",
      "source_sha256": "77bdbb1641274befff6beb95ff94f32b1625ccdc0c9f0556c7e4a79aaeee2b3b",
      "sha256": "b7cee84e9e2cc644a48b1e3c4ff5f79e710e02f4df55a1a60f362a4f8a16640a",
      "bytes": 813,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-3x1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-3x1.dat",
      "source_sha256": "9ae441c03c2e73972a26d74f7ead4de280947397dc09e2fd9857ca73ec87181a",
      "sha256": "d49998cbf8f769966a611430844a7c57e25d5c95ed3cbc2e6814801d97e8df04",
      "bytes": 413,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/subparts/48995s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/48995s01.dat",
      "source_sha256": "0e0c9c69eb811b6e189d484659d1796bd8d312dc39c689d2b202d4f6004f4a08",
      "sha256": "379d44b4fb9b68ac003dcbbd3f25279beee987fec10a4ee3cdb8240982d011e3",
      "bytes": 3455,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/4-4con5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4con5.dat",
      "source_sha256": "86c49af64c12622bd3ebd7d741a23eb66394f277ecda99b4c164eb110fc5e8cc",
      "sha256": "86c49af64c12622bd3ebd7d741a23eb66394f277ecda99b4c164eb110fc5e8cc",
      "bytes": 6709,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "primitives/1-8cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8cyls.dat",
      "source_sha256": "95945719c0c6075f3f1222f77ba390d7e5c59f99933ffafda039808a6fcd4522",
      "sha256": "95945719c0c6075f3f1222f77ba390d7e5c59f99933ffafda039808a6fcd4522",
      "bytes": 1040,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3298s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3298s01.dat",
      "source_sha256": "6f034691077dfe42a89713261283b27066560bac70001532442172c26cc622db",
      "sha256": "cdc6b9a9280ebe838d68ba0a6c880f099f2f5953fdc389354035f232ba0127c1",
      "bytes": 2668,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
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
    "primitives/7-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/7-8edge.dat",
      "source_sha256": "1224e5c6c52b35f8423de197b7c87e6ab1dba52ab85fc6ecebb031c4a90912c1",
      "sha256": "1224e5c6c52b35f8423de197b7c87e6ab1dba52ab85fc6ecebb031c4a90912c1",
      "bytes": 741,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/63864s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/63864s01.dat",
      "source_sha256": "f490f09b4057820d9efe750ca502ece3bd8c9efb149fda9ae46b83397274b9f7",
      "sha256": "3c3be8a831958272e3784e9b8abe87d87ad2aa64ae31a137fb4ddfbb48aa0f40",
      "bytes": 858,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Ulrich Röder [UR]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/5-16edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/5-16edge.dat",
      "source_sha256": "17a9ae47e68e98286d27fc7be4a48e1110d1cae0d3abff658f3378a552857fc3",
      "sha256": "17a9ae47e68e98286d27fc7be4a48e1110d1cae0d3abff658f3378a552857fc3",
      "bytes": 437,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/7-16cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/7-16cylo.dat",
      "source_sha256": "347b7feca8d94f501ce40045c987575fd830ca0a5aae7cfdea49daf61e540bb9",
      "sha256": "81a7382b2849aab2d21eb850e3b54b0b45ae820843e3a2af0a887b8691a2c241",
      "bytes": 427,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16cyls2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16cyls2.dat",
      "source_sha256": "cac33c64acb85e031b5caebb09380388a29273cb2068ca90e092250cf0cf2ffd",
      "sha256": "cac33c64acb85e031b5caebb09380388a29273cb2068ca90e092250cf0cf2ffd",
      "bytes": 668,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/3-16ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/3-16ndis.dat",
      "source_sha256": "3b600e0ba29080acb9dba24341521507fdbbdac822a836b0c4875ad816c50d5d",
      "sha256": "3b600e0ba29080acb9dba24341521507fdbbdac822a836b0c4875ad816c50d5d",
      "bytes": 1058,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/69729s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/69729s01.dat",
      "source_sha256": "54b5a49c4e6f91eb599696cec9decc6d3f3d1c41f4cdd9edb08349004dfab768",
      "sha256": "34a016a51f4439e1b250cbebdad6338d53b7dfefb5bbab4cbb48867f9b08fd20",
      "bytes": 836,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Vincent Messenet [Cheenzo]",
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
    "parts/subparts/99206s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/99206s01.dat",
      "source_sha256": "7965cbc54454d09c7ae25b63cd45ec1cc843b578c5e5fc0426bab9555d502e09",
      "sha256": "20f800c9827694ed9775cf43b31c6c776d446441294441ee168e7b6552b26192",
      "bytes": 2131,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-16ring12.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16ring12.dat",
      "source_sha256": "1365475b6b63cdfe3ef4e244143b3d80f4e6030f2a483a11681123c937b84673",
      "sha256": "1365475b6b63cdfe3ef4e244143b3d80f4e6030f2a483a11681123c937b84673",
      "bytes": 570,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
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
    "parts/subparts/42862s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/42862s01.dat",
      "source_sha256": "c74f81e652ac58f0e55eb8cfe449fa5cd4eb4bda2447ed4c85a1e9eb7a28805a",
      "sha256": "db0cf419f62fe0d829949effb37350aca16fd9a65cb52d60c8f00de57c2de316",
      "bytes": 18003,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/bush0.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/bush0.dat",
      "source_sha256": "e624dab4cba4934f674647672537c284597a2467bac06ae3e9dbab8e3857782b",
      "sha256": "260fc73f95d3f7e0a145c6d50576e9596730527562b071692b92161e95dd89f0",
      "bytes": 833,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud18a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud18a.dat",
      "source_sha256": "5c02e7ce688de49bc4db00751988cf9044ba9c8b2b0b45ba836154be3637b2e2",
      "sha256": "f153d96029c4352d0369f2296763ca3ac92505bc94498cd9d858f7f79c938123",
      "bytes": 32087,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/ridge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/ridge.dat",
      "source_sha256": "76fb031a2c509f0e267d133594b1a814490eb7b4db5321479ab98a88619e2eaa",
      "sha256": "fe6cccdb7d17c52ca8038fb3f34ba2070c21ca2bc5dfcf091b7544c7bac83a03",
      "bytes": 440,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud2s.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud2s.dat",
      "source_sha256": "d58ac90a6b6e5cfa137c3236c73d49bef1957929edb96f229341bab84ec6fef7",
      "sha256": "9d652955c733a250f10c543b8e1bb7d01a42505553b308af50c8d7a08351d324",
      "bytes": 793,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "primitives/stud23.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud23.dat",
      "source_sha256": "10b4d24d10a6c81cd1fd5df67b613a083edef0fc5b4b28848b4262b4240a9554",
      "sha256": "29a7774070dbc10a38e6d363f03383e91afd0b2bd0c24452454a13ecf0142aaa",
      "bytes": 328,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "primitives/1-8ring4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring4.dat",
      "source_sha256": "08954a02988b658890a539ae61db3e6225a587bd52b2e160c4f292d37629cc3d",
      "sha256": "08954a02988b658890a539ae61db3e6225a587bd52b2e160c4f292d37629cc3d",
      "bytes": 688,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
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
    "primitives/stug3-1x4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3-1x4.dat",
      "source_sha256": "cae88c418acb36719fb6bc1d56916ab7e0734ffaf9204d7e3077a3c45ae7c79a",
      "sha256": "b5735e66378595f482309cf29f7e32f152dead62a1726851a924153da70fd106",
      "bytes": 474,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/connhol3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connhol3.dat",
      "source_sha256": "8601ce04ac639c448ede7910756e033f55fef3cbb19319e7efe1d8512957a8f8",
      "sha256": "df12b726262b070dd5c6d9137f21d2a8c4a0317691a1ab387acde8aeb486072d",
      "bytes": 639,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/connectslit1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connectslit1.dat",
      "source_sha256": "d5652a51cc1459e770d15816afc00b7c09235c85a032ec3c3e8d16c2c6bb0b6a",
      "sha256": "f848ec57d86bb8647787c308680a65e03045770aa042b171bf90ba39a4de0906",
      "bytes": 1104,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/93273s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/93273s01.dat",
      "source_sha256": "95d97ee75937fa8baa4b0fca339143ed3a5d1b812e4b2e76ef20d2a4c4622489",
      "sha256": "e24376233beb9b3fcde893b1d909289ab410d42c4ff196bd7c6aad3c6d7f2823",
      "bytes": 6123,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/66956s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/66956s01.dat",
      "source_sha256": "9e706d79dff04726511fb256b2515f26d46ca978da570d2acf9fffb7bafe216e",
      "sha256": "073d59fd0119586acedf97f943a7fef27420876da171993b1715165ca3a43683",
      "bytes": 9102,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
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
    "primitives/stug-4x4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-4x4.dat",
      "source_sha256": "d167d3367e9d6346e217331f3d35c7b2700d1c87f35e87b40cb3a702afa90e54",
      "sha256": "ced80ae47629388ed75a2f91b1024a11055a578cd47b5f259870e9be7a73a535",
      "bytes": 785,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tore Eriksson [Tore_Eriksson]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud4s.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4s.dat",
      "source_sha256": "4cdb054167ab5b860990b20c84f7245b60b64b809a002fe909cc8e946a6708dc",
      "sha256": "7250cf44d054cf2d9e12617f30b92db22b43877024b1485a560d6967a0b1d1a3",
      "bytes": 1119,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "parts/subparts/15535s02.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/15535s02.dat",
      "source_sha256": "4df4b43c8a74657711da3890d0a242eca23298bd153312b2de8793f3203d33d0",
      "sha256": "ef1534b02aba6371d7fe50c385f73d4868e9556ee59dc6b43ce9199929812dc4",
      "bytes": 4824,
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
    "primitives/bump5000.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/bump5000.dat",
      "source_sha256": "e5421cb73e8e81827e5600317c1b08d8ec53cfc90912799e4f99cf2289e51d93",
      "sha256": "b91a3c9375d47a8d43e7294d0bb6fc28b078485530f7c2405da7ead4f7cbc816",
      "bytes": 3409,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/subparts/3068bs01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3068bs01.dat",
      "source_sha256": "b49ecb2e8e57d8ae4a64aa5e71713d769c2a5dc91f4611fbd3157fbc30a4c6c3",
      "sha256": "5ed2affcfd8d9d28e91cc052ada92f4b4f9f5b45953ef4428e59e59476088eeb",
      "bytes": 1436,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
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
    "parts/subparts/43710s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/43710s01.dat",
      "source_sha256": "2e42b7016c75e97602900e6f7fef9d45bfcefb87466f0e0cc13e9a712140517a",
      "sha256": "243c3143cca766db559ce75842f7a96a0efe8e4101607ab1a69e9b03a64b75d6",
      "bytes": 25031,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
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
    "primitives/box0.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box0.dat",
      "source_sha256": "c2a26e0f7caf639bcdd55dd56325f8756ef39a1f86ed16bacd2c9fb625af2847",
      "sha256": "c2a26e0f7caf639bcdd55dd56325f8756ef39a1f86ed16bacd2c9fb625af2847",
      "bytes": 524,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
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
    "primitives/3-8chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8chrd.dat",
      "source_sha256": "dd829916e86c0c8e9a1d9d87d04d93d013d074402a43de210d399f9f4b9c58ce",
      "sha256": "dd829916e86c0c8e9a1d9d87d04d93d013d074402a43de210d399f9f4b9c58ce",
      "bytes": 768,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/11213s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/11213s01.dat",
      "source_sha256": "2fd235d9b2d546785ca5eeee6e4c29246c70332cf2d38d865af6be24497f6676",
      "sha256": "f4766bfc05c1882b4c62e8bad2782ffa4a30a46c562dad3f378c562d23b1755d",
      "bytes": 3680,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/axlesphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlesphe.dat",
      "source_sha256": "fb0f74281570ea0435692783f0d7da62c84b0e84576e2f7eab1403dbc5904a13",
      "sha256": "fb0f74281570ea0435692783f0d7da62c84b0e84576e2f7eab1403dbc5904a13",
      "bytes": 4721,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
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
    "primitives/peghole2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/peghole2.dat",
      "source_sha256": "eae97c935449554e3251ef2b7aaa55a6cd4d406a3acadb52ca190921cd240d35",
      "sha256": "0dfa6f92be89a084ed12155c3476c0ff59e2f1cbbcaf7535273cb2349b23a506",
      "bytes": 1194,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/5-16cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/5-16cyli.dat",
      "source_sha256": "3a46e175cd13f2343645b5ba1be54f1f2fdf446cf28392383d511d85eaa7665a",
      "sha256": "3a46e175cd13f2343645b5ba1be54f1f2fdf446cf28392383d511d85eaa7665a",
      "bytes": 946,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box4-7a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4-7a.dat",
      "source_sha256": "93ac5f1805fc4e785c9532c0b40851a9d03da37241f85d5513b059c4358839f4",
      "sha256": "93ac5f1805fc4e785c9532c0b40851a9d03da37241f85d5513b059c4358839f4",
      "bytes": 1008,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "parts/subparts/12787s02.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/12787s02.dat",
      "source_sha256": "1a248b1739c9b9ae89e7f885803785942875c2f42403d8634008f254aa7c225f",
      "sha256": "a1731122824f02fa0b360a271fb49e853e24e549826878365210851bc78960e5",
      "bytes": 91085,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/9-16edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/9-16edge.dat",
      "source_sha256": "5d9e98308232980f596c14e0a6e1d9d4e97fc472a6ada152ae5f4ee6eb504868",
      "sha256": "5d9e98308232980f596c14e0a6e1d9d4e97fc472a6ada152ae5f4ee6eb504868",
      "bytes": 531,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/79846s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/79846s01.dat",
      "source_sha256": "c6a5fef106d925e8741a4b1c14383b089c64beecb7617d3f3cefc0e8a49df9f3",
      "sha256": "8582693a70cfdf76af20bafc8a594763763a391caeb707c8abcc12c43be61923",
      "bytes": 7472,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3-7a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3-7a.dat",
      "source_sha256": "4fd59e0bd2a5c2b076568627eaf4ad6696deb1f245422bf124bf4dda160a5c43",
      "sha256": "4fd59e0bd2a5c2b076568627eaf4ad6696deb1f245422bf124bf4dda160a5c43",
      "bytes": 632,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/79180s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/79180s01.dat",
      "source_sha256": "ed874582d49edf67fc7f16398351b3ce2f45318ffabc30707de3cd54e0d6625d",
      "sha256": "a6da73573e64d1ac3240c169f91942d5fab89f5b813382f17d2254e9cf7a1ed2",
      "bytes": 2231,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/5649s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/5649s01.dat",
      "source_sha256": "5b9ef34fb0b96f1c0f8edbc912c07f0c76c5d5047087dfa96ca7dec13854efe7",
      "sha256": "5eb99a630f77be2495b829efd3e742e193222fbf7e8638cfa6e67a5a091b1c81",
      "bytes": 23959,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/subparts/2654as01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/2654as01.dat",
      "source_sha256": "c53f59c9d4cd99dea87b5e11f096ed195045cf38492499cb8dabcbe7afbcd0c3",
      "sha256": "accebfd9436a376dc6ffe38b21300960dabc3ef0c3a1238b673dedd66acb4301",
      "bytes": 5936,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Evert-Jan Boer [ejboer]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/37352s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/37352s01.dat",
      "source_sha256": "f6d9cf5b10f788d3ee8667e7a66015392cc00e4977755bbf989ce1a492f97a89",
      "sha256": "a33ff208040f185342bbe0c883d32569c335b2e97d4a8eac4dae2b0bf5438410",
      "bytes": 3587,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4ndis.dat",
      "source_sha256": "c343cdb5d839040d346818adc6aa39586338c5b0a6a9d2ab7162c60e4caba5f0",
      "sha256": "c343cdb5d839040d346818adc6aa39586338c5b0a6a9d2ab7162c60e4caba5f0",
      "bytes": 1053,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/61678.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/61678.dat",
      "source_sha256": "e06daaca0499570e65d18b3e969be2e7be66896e0735b829c579bfcb6caa1eb8",
      "sha256": "e07daf8944acead09a7af864bf44e07031a8be90cb2fdf205c8db931604b3c64",
      "bytes": 598,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-1x5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x5.dat",
      "source_sha256": "9d7c7dc1ea19c9370dd1dc439aee1a69fb6deb190a09f7b1561a1a34ae7103b4",
      "sha256": "6a07ee5f3aafe9c0cd768d60e39a5ef6174c95fcaed91866cb6b32d44958041e",
      "bytes": 508,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "primitives/box4-5a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4-5a.dat",
      "source_sha256": "a6e309efe429eb61ab822935ae437d322deb6fb1c80f292472d9de9f38992324",
      "sha256": "a6e309efe429eb61ab822935ae437d322deb6fb1c80f292472d9de9f38992324",
      "bytes": 538,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/box3-5a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3-5a.dat",
      "source_sha256": "7c6ca41f483553472e0fc63bb494ba1494918b28e511e2f179fbb5618f7240a3",
      "sha256": "7c6ca41f483553472e0fc63bb494ba1494918b28e511e2f179fbb5618f7240a3",
      "bytes": 535,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/subparts/3002s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3002s01.dat",
      "source_sha256": "b97861207148255ab4423744b0507bd5e46bae843d52e6904df0700260f198fa",
      "sha256": "719adfb6f583e0323c06eccc0206d4161e27666b4bc8863e5f6f2d886887b9d2",
      "bytes": 1656,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-8con3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8con3.dat",
      "source_sha256": "c379b2f199de186f42333fa5d9868becea35576fb9aa05fa11bf99c669986854",
      "sha256": "c379b2f199de186f42333fa5d9868becea35576fb9aa05fa11bf99c669986854",
      "bytes": 1145,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/3-16cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/3-16cylo.dat",
      "source_sha256": "76b0bf74b19495e59a445c0968739af5186827f331f03736b77c2c2bda71b866",
      "sha256": "38c6ef0f36823127d72e71f67c09b5f7f087cda98c25773e42345a192324a9f2",
      "bytes": 488,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
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
    "primitives/9-16cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/9-16cyli.dat",
      "source_sha256": "283c32f8d76c127b24aae66f1b94bc90565ad06f5751d182cff821a3e2625479",
      "sha256": "283c32f8d76c127b24aae66f1b94bc90565ad06f5751d182cff821a3e2625479",
      "bytes": 1476,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/87552s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/87552s01.dat",
      "source_sha256": "856d6f152d18beb432958c209879b222fe05f2a32f5d623329e644364f0d9249",
      "sha256": "58d268bd7490fdc9a6f6761ba50690809b62f027962f0872165499ef359c4c7d",
      "bytes": 2900,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/connect3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connect3.dat",
      "source_sha256": "d74e0e1388df7764b5dd4073d4264db3cfe6b04166cc2adaa3301768adf412ff",
      "sha256": "8efde50ce3e4ef022b89a53ba8863c57145d0f03813af0638d00ed0d3efa384b",
      "bytes": 7080,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "primitives/stug4-1x6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4-1x6.dat",
      "source_sha256": "edd68f6fb00f00ae9becee2942097280e5d5744481c2b8ae624942b8ba817ce6",
      "sha256": "df4c06135adaa1397051e73c2fc44195108442e528c1002b5c24a7ee997ebf98",
      "bytes": 578,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/st4jfil3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/st4jfil3.dat",
      "source_sha256": "54d3c4d736e20df6048b2b4b8cacb4625dde7f9e14eb5e79d9cec44f195d18f4",
      "sha256": "e8aaeefc289fb362ba63e438def1aaadcd501e015454600d96ae666df0fb9733",
      "bytes": 1548,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con3.dat",
      "source_sha256": "1aed96f9d90a36758bb299c01db21f8fd795a4734bcd605171c76ea61116697e",
      "sha256": "1aed96f9d90a36758bb299c01db21f8fd795a4734bcd605171c76ea61116697e",
      "bytes": 2426,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/67695s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/67695s01.dat",
      "source_sha256": "d49d1c36118199090f1089969aa459e0243e8c9c0e104cb5473ca7c59dcacd21",
      "sha256": "25254b5b2c3555632d8fb8c9ca1b0d7c9bd30b0b2a2286c28adf6669c8295c60",
      "bytes": 14743,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/subparts/87079s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/87079s01.dat",
      "source_sha256": "8d73b808e1e1dd46bbca13104de8779c6da6270131e65c7028a84ac41f198506",
      "sha256": "466633b8c315a3b9755f21b12eac379aab68ddc630ca9c4d43b7f71cca344082",
      "bytes": 1123,
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
    "primitives/2-4cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4cyls.dat",
      "source_sha256": "0b0d6602c4a5d86542312f2428a6c384483eb435b9a0057ddde80de33ec7b441",
      "sha256": "0b0d6602c4a5d86542312f2428a6c384483eb435b9a0057ddde80de33ec7b441",
      "bytes": 1660,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/subparts/32064s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/32064s01.dat",
      "source_sha256": "e89d5e33547325f5a84aa9b0c374f3cd997eae841057dc2697e76f5dc1cfd502",
      "sha256": "d35bc2a2252bfd314b3a789cf64c83c6061b15e7ddea6f673638810ac1a7573c",
      "bytes": 1587,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/clh10.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/clh10.dat",
      "source_sha256": "9cd5530d987ac13befc3767dfee6469b741cd054851df24f8b0d81afccd3fce9",
      "sha256": "3544e3d5a560409e3ef043d7ebbde5bd317834a44eb4a68c624d4dcdad181237",
      "bytes": 2847,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
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
    "primitives/1-4ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4ring2.dat",
      "source_sha256": "98a52c605fc13721f1e86030f67c4233587c8c80243ce8c0889cdc8147894207",
      "sha256": "98a52c605fc13721f1e86030f67c4233587c8c80243ce8c0889cdc8147894207",
      "bytes": 882,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Franklin W. Cain [fwcain]",
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
    "primitives/4-4con12.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con12.dat",
      "source_sha256": "d3f7bf504ebed748c6c161bb2f7b128a5a95c33dec54ed7c506ee02ea0097b05",
      "sha256": "d3f7bf504ebed748c6c161bb2f7b128a5a95c33dec54ed7c506ee02ea0097b05",
      "bytes": 2941,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/triangle.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/triangle.dat",
      "source_sha256": "67e7a72ed488412a974d622570704c4a734d9ba9fe671b03261fcec8520e01f2",
      "sha256": "67e7a72ed488412a974d622570704c4a734d9ba9fe671b03261fcec8520e01f2",
      "bytes": 320,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "primitives/7-16edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/7-16edge.dat",
      "source_sha256": "c98b01990a94c2c5a786f06cdfbc199a2bb4685e2d605b7ed2c6efb98e710842",
      "sha256": "c98b01990a94c2c5a786f06cdfbc199a2bb4685e2d605b7ed2c6efb98e710842",
      "bytes": 568,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/clh-base.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/clh-base.dat",
      "source_sha256": "58c3f98f8a13a46370197fa2ccc5364fe75747ff3f36ab8f2552e6bcd5759a4d",
      "sha256": "07f47a05d791ccb2699f7d8384acf7c900bffebab478d4411994b7d4bdb3849b",
      "bytes": 2439,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/5-16ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/5-16ring3.dat",
      "source_sha256": "6b4ec6cf8d22d201644c72a6569f8b1b830135554eebd9087ed4bab82eb90586",
      "sha256": "6b4ec6cf8d22d201644c72a6569f8b1b830135554eebd9087ed4bab82eb90586",
      "bytes": 727,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/fric.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/fric.dat",
      "source_sha256": "7d8e50de2144286e6028ea5c97d03b9c5ef50f8c3353527fc2f5d8d36ba4b85b",
      "sha256": "018989fbcb8793469c73503654974201aa0fb1dd04d271cd3eb7a5556d186e64",
      "bytes": 861,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
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
    "parts/subparts/78444s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/78444s01.dat",
      "source_sha256": "5d861aaed677d8746658a6fd786031c84a6ec89c76d567624e4bc7a43a6110eb",
      "sha256": "1eb4cb012f19c462d01b507fe9d8eaee7de0ee8dba30aa4cc6564d8dd92b0327",
      "bytes": 8844,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-48chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-48chrd.dat",
      "source_sha256": "849fff998e086998d6361b6df1656aa8bb8551adeef975e2ceebfb45b850f0e5",
      "sha256": "3c291783922a79228c37f4a7229d30d278ce7db59ee0e3a0b06984d01da9013d",
      "bytes": 664,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "N. W. Perry [Plastikean]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8ring8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring8.dat",
      "source_sha256": "6166b3c447f674cfb20d21eb4fcaa5e3c0ab20d9aee25a1c6d981f38ec09e496",
      "sha256": "6166b3c447f674cfb20d21eb4fcaa5e3c0ab20d9aee25a1c6d981f38ec09e496",
      "bytes": 610,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4con4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4con4.dat",
      "source_sha256": "cb5c0bcd7006e448a2a5681bc6fbfc71e1f424b9f8de8d47b7731b32ce5090a6",
      "sha256": "cb5c0bcd7006e448a2a5681bc6fbfc71e1f424b9f8de8d47b7731b32ce5090a6",
      "bytes": 1447,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4stud4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4stud4a.dat",
      "source_sha256": "d5dd7aa154ce15038615040980263970044e9ae9c266c9abbdaee7ea1b0853f2",
      "sha256": "e5051a2eccd8f0527a76bfccc28498f4f15d4ac1baf5b32f6b355d89d00066db",
      "bytes": 573,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/ridgea.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/ridgea.dat",
      "source_sha256": "7f8b2df1724dff7edf8619fb4a77fb38ac298475e0136b15d9e254f1a9de74ca",
      "sha256": "f81f04f886721a9e0b9732540bb11556bc3423af8728b9c42dc68f170e616d76",
      "bytes": 461,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/6636s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/6636s01.dat",
      "source_sha256": "ab03bda811375ed2edb0c165d7c0bb0936c7febdbd10428a707f9cc413cbb1c2",
      "sha256": "72094fc6f2bcdcc1999e0594c79014ca960453754e19efc222103cfbb8273604",
      "bytes": 976,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Takeshi Takahashi [RainbowDolphin]",
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
    "primitives/1-8ring19.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring19.dat",
      "source_sha256": "3e960324d4741e841725a81b8be1efa24b72460f12d50c0ecaa9578a11c05641",
      "sha256": "3e960324d4741e841725a81b8be1efa24b72460f12d50c0ecaa9578a11c05641",
      "bytes": 706,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "primitives/bush0a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/bush0a.dat",
      "source_sha256": "30213424b26a50531b8656dd973beaf6fa6f7ab4cc4419522d710851c2edbf02",
      "sha256": "01960162f4c2f60864afceb583bce32ac8be4d7bf1142c239ab407b6d16f44ab",
      "bytes": 4944,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug4-1x3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4-1x3.dat",
      "source_sha256": "29afffc8e5e9f4cd96a8e4d3031b9bea98416c344214e2969b22a0edc01f7980",
      "sha256": "3c2afc4c7881e1fc19020ab4f1a0efce012065ab98287072a976a2ef25b5c1b9",
      "bytes": 419,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "primitives/1-8ring6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring6.dat",
      "source_sha256": "bfec71b5d0b0ba1549923f349ec1d07cc8694a4827f88d9ef955457cecdd90a5",
      "sha256": "bfec71b5d0b0ba1549923f349ec1d07cc8694a4827f88d9ef955457cecdd90a5",
      "bytes": 477,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring2.dat",
      "source_sha256": "e455551969062c34d061d1b74df9b18f63deffb3efdbeb175a4a80a674f5ff68",
      "sha256": "e455551969062c34d061d1b74df9b18f63deffb3efdbeb175a4a80a674f5ff68",
      "bytes": 791,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/67696s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/67696s01.dat",
      "source_sha256": "8e0a459a27c2ba8a808c62c02a806b82e353c3e020eba49afd6f3cf4dcda3ec1",
      "sha256": "dbbcbd364e5afede20dff03e8bea0d1e032dac7fdf6c7c21ae7985190ee2b1c6",
      "bytes": 31099,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/subparts/3484s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3484s01.dat",
      "source_sha256": "541c53acb785c4b7ecdca6989169f27dcf7a538da757d64fd01446610e02ce91",
      "sha256": "fe1738df5350bd6027e376fca1904df99b1dcc1b36374be91719476e92ce1637",
      "bytes": 4183,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "primitives/4-4con0.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con0.dat",
      "source_sha256": "b9e568215ff9786203c7d8e7ee4b7f99b72222a097c7663c732c4ecae77eaf9c",
      "sha256": "b9e568215ff9786203c7d8e7ee4b7f99b72222a097c7663c732c4ecae77eaf9c",
      "bytes": 1814,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "primitives/1-8ring18.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring18.dat",
      "source_sha256": "bb03cb6a1df637953544d4721509130eefdbd76b49eae2673031fc7ca5e970fa",
      "sha256": "bb03cb6a1df637953544d4721509130eefdbd76b49eae2673031fc7ca5e970fa",
      "bytes": 712,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "primitives/1-8ring1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring1.dat",
      "source_sha256": "5bdd939ba22dc7d9237657fb345a358a8993ed4f61531433371e0241371b9ced",
      "sha256": "5bdd939ba22dc7d9237657fb345a358a8993ed4f61531433371e0241371b9ced",
      "bytes": 746,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4stud4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4stud4.dat",
      "source_sha256": "07a1e91dc4b6624fa88f269a74c42e4265784702bf4871412439ea98fc2adb48",
      "sha256": "61e358c0f01e2a9d3ff39d03fa9ab14350f7fb92f9e75edfc2282c044d2903c8",
      "bytes": 437,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
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
    "primitives/high-resolution/3-16cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/3-16cyli.dat",
      "source_sha256": "70d8abd40f9811f79e109a8508112001d4249fb9b2ca204cec54d883d5bfa7bb",
      "sha256": "70d8abd40f9811f79e109a8508112001d4249fb9b2ca204cec54d883d5bfa7bb",
      "bytes": 1747,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
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
    "primitives/clh6c.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/clh6c.dat",
      "source_sha256": "3cb91ca4b98cf1d0d639617e0eff946ee518835b98424c61ecdb1ac042be10a0",
      "sha256": "60172bfff2084a8913fa186af4e6eb56f35ce9a820976857f172221e1aad19b8",
      "bytes": 6025,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/1-4chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/1-4chrd.dat",
      "source_sha256": "dc080d295da1d9732d9346882608078f6b32c4cf75d2a6174ecc16fdcf1e20c9",
      "sha256": "dc080d295da1d9732d9346882608078f6b32c4cf75d2a6174ecc16fdcf1e20c9",
      "bytes": 333,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/62712s02.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/62712s02.dat",
      "source_sha256": "5525c4b9c9fa179e802aece12a7187b97349ad4713908b28974420cdbdbc5f0c",
      "sha256": "61f1ba7a359bc6fb8191aa9d7952cc553243e66fcfd94584ca1828fae3e9716f",
      "bytes": 3439,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/2-4chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/2-4chrd.dat",
      "source_sha256": "2caebc5de687f190e7ef2f25724665284bf0139e4db42844d0e2691128b9c0ea",
      "sha256": "2caebc5de687f190e7ef2f25724665284bf0139e4db42844d0e2691128b9c0ea",
      "bytes": 343,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3665a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3665a.dat",
      "source_sha256": "5e0b6473a41e98abfa96f4842fe43c28d6e2702a9040f1bdb775de9c49f6e413",
      "sha256": "2910d1f15d330d1178f82bf83180c11edf8082be3567d4a68c62b45b81e44517",
      "bytes": 893,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "primitives/clh-finger.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/clh-finger.dat",
      "source_sha256": "51f78bcccfe4d25dd6680aa47856ebc9ffa7240004bc7c045a450185a185fc32",
      "sha256": "51f78bcccfe4d25dd6680aa47856ebc9ffa7240004bc7c045a450185a185fc32",
      "bytes": 2545,
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
    "primitives/high-resolution/1-8ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8ring2.dat",
      "source_sha256": "b74996bc03e4bec0bd50439ed4b609ce8f22178f9446a4fd22af277a6920ef1a",
      "sha256": "b74996bc03e4bec0bd50439ed4b609ce8f22178f9446a4fd22af277a6920ef1a",
      "bytes": 668,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/1-8ring13.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring13.dat",
      "source_sha256": "7aee0e8ac0a5d9ed69c5f5728b345f4456e90a91a4294149a750648fd22fca34",
      "sha256": "7aee0e8ac0a5d9ed69c5f5728b345f4456e90a91a4294149a750648fd22fca34",
      "bytes": 419,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Evert-Jan Boer [ejboer]",
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
    "primitives/stud6a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud6a.dat",
      "source_sha256": "efd3e269d1ec7b1496734d616922101e1da56198d3bb44454c6413176ef6bd2a",
      "sha256": "4e5053ceb7f7d9fb3f15c8f36007bb96dfe5aef9869354dd89c4c07593647952",
      "bytes": 2373,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
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
    "primitives/1-8ring27.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring27.dat",
      "source_sha256": "e9f77a928fcca927105cd1588232c74cd52b53019953bb52a60689317036df94",
      "sha256": "e9f77a928fcca927105cd1588232c74cd52b53019953bb52a60689317036df94",
      "bytes": 429,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/2-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/2-4ndis.dat",
      "source_sha256": "4f646d4ca8dd67205faf9b0e233c4921b85d3b30a9283090b0482397aad1a487",
      "sha256": "4f646d4ca8dd67205faf9b0e233c4921b85d3b30a9283090b0482397aad1a487",
      "bytes": 447,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/61678s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/61678s01.dat",
      "source_sha256": "2445d156ebfd9aa072bbb84ef79421d6f9638fca4dc431e8fce0fb3fa059a6c5",
      "sha256": "4c104f46ef5d47aaac9067d57e74fe516f432a932db8ea9eea5f7d64fe414df7",
      "bytes": 5728,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t16o1429.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/t16o1429.dat",
      "source_sha256": "feacc63d988960380c67d79f303dcfe0a62f93816d7282088796af745ddc1249",
      "sha256": "feacc63d988960380c67d79f303dcfe0a62f93816d7282088796af745ddc1249",
      "bytes": 1892,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/7-16cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/7-16cyli.dat",
      "source_sha256": "e829752713ec727431bf5053bd3ad60a113236ad10a885aa87c0e5fd856598ae",
      "sha256": "e829752713ec727431bf5053bd3ad60a113236ad10a885aa87c0e5fd856598ae",
      "bytes": 1385,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/box3u6a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u6a.dat",
      "source_sha256": "11f6175e76c3bd1e857a216f80b7e7d81288ec130a33d9b242d1fa3d448cb873",
      "sha256": "11f6175e76c3bd1e857a216f80b7e7d81288ec130a33d9b242d1fa3d448cb873",
      "bytes": 514,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/2-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/2-4cylo.dat",
      "source_sha256": "cf7a9969c8d7396d17966b65c8ea48ea36445e98580dc76d18e5aa1fc5afd54f",
      "sha256": "b723a9c589e51924717309ba96160669ed73c344b4c59f94a2e079990d619fed",
      "bytes": 427,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4ring7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4ring7.dat",
      "source_sha256": "c58f1ebaec67452bbdf41be056b371a61c79c2a0fa5327c37e3e88d453b8bc5d",
      "sha256": "c58f1ebaec67452bbdf41be056b371a61c79c2a0fa5327c37e3e88d453b8bc5d",
      "bytes": 850,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Franklin W. Cain [fwcain]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/5-16ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/5-16ndis.dat",
      "source_sha256": "e804ca14b6bdfb07ce83094b72434614ac485682e753708e7b71537c87730c88",
      "sha256": "e804ca14b6bdfb07ce83094b72434614ac485682e753708e7b71537c87730c88",
      "bytes": 494,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8con3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8con3.dat",
      "source_sha256": "986781a1289b9f2b3fdd91ca6f0f8d7056955dd88a4a4e7e70803e2946815de1",
      "sha256": "986781a1289b9f2b3fdd91ca6f0f8d7056955dd88a4a4e7e70803e2946815de1",
      "bytes": 1095,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Ulrich Röder [UR]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4ring3.dat",
      "source_sha256": "540acda3cc2567820cbba2ea67320bab8c80a99cc94d974cf70b58c1c32573cd",
      "sha256": "540acda3cc2567820cbba2ea67320bab8c80a99cc94d974cf70b58c1c32573cd",
      "bytes": 1482,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/3-16edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/3-16edge.dat",
      "source_sha256": "9db5a2634d599770c8bd3f3f7dc790e0198b938054878d2149b25303896b4ab4",
      "sha256": "9db5a2634d599770c8bd3f3f7dc790e0198b938054878d2149b25303896b4ab4",
      "bytes": 1012,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-8ring35.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ring35.dat",
      "source_sha256": "7c2beb4a5a8c5c80c0248470f3d9892369cabb0742c293ac83487b12a90caffe",
      "sha256": "7c2beb4a5a8c5c80c0248470f3d9892369cabb0742c293ac83487b12a90caffe",
      "bytes": 427,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Evert-Jan Boer [ejboer]",
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
    "primitives/5-16cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/5-16cylo.dat",
      "source_sha256": "3468b4f9bf29026d7266da964f4298eea5d4bfa30f09d80e11abfb39cc9df797",
      "sha256": "aec771bc7b006a8c942bdcb3de4f18c5644f873dbbed5fe76f7f3d7eb2949b5b",
      "bytes": 427,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3665as01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3665as01.dat",
      "source_sha256": "4d6a5b3124fa3e0b2edbf8fe262ad420b6bfc816704d7028d433f23accf6a709",
      "sha256": "b2878b4660e741db9ec4b9a3b0c5201010554daf53b7222fd33f2804bc9b1908",
      "bytes": 1951,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4ring2.dat",
      "source_sha256": "9ef881ae14ff1d311865994ede3409ef9ce162890981bfbdd860384661c37f1a",
      "sha256": "9ef881ae14ff1d311865994ede3409ef9ce162890981bfbdd860384661c37f1a",
      "bytes": 1119,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/1-8sphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/1-8sphe.dat",
      "source_sha256": "e3227b1d5255603bae9963eb4f5c464063743d62f78acccb712008358b47f6f7",
      "sha256": "e3227b1d5255603bae9963eb4f5c464063743d62f78acccb712008358b47f6f7",
      "bytes": 929,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/2-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/2-4cyli.dat",
      "source_sha256": "9e5869a3bf444fcda1cc9908ef96ce782b53fc68f94eaf6903a0dbca6c582215",
      "sha256": "9e5869a3bf444fcda1cc9908ef96ce782b53fc68f94eaf6903a0dbca6c582215",
      "bytes": 763,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/8/2-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8/2-4edge.dat",
      "source_sha256": "3154ed3f142d644552b2533457c13c56ef326b0f7d31ea425585d6cdde2a3129",
      "sha256": "3154ed3f142d644552b2533457c13c56ef326b0f7d31ea425585d6cdde2a3129",
      "bytes": 406,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "LDConfig.ldr": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/LDConfig.ldr",
      "sha256": "d3490047460ad7a511b150006b009830fc52ecc1899b514c7380e9de644b3cfb",
      "bytes": 67580
    },
    "parts/69787.dat": {
      "source_url": "https://raw.githubusercontent.com/iefierros/LegoMaster/0b2eb83be4c34193521a962b3136c553d14322c3/ldraw/UnOfficial/parts/69787.dat",
      "sha256": "e6b135eacd325a067f824cec993b773aed79040f131bba2fb8365c3f34f19fbd",
      "bytes": 251862,
      "author": null,
      "license": "Repository MIT (Copyright 2024 Lego Master); original individual mesh license not stated",
      "modification": "Removed nonstandard trailing UV coordinates from triangle records; positions unchanged. Added provenance header."
    },
    "parts/69788.dat": {
      "source_url": "https://raw.githubusercontent.com/iefierros/LegoMaster/0b2eb83be4c34193521a962b3136c553d14322c3/ldraw/UnOfficial/parts/69788.dat",
      "sha256": "fd22bc910928cfdf885e8779f1a286c77e9657c75eb2398bfcb6b9df00e22f7b",
      "bytes": 396542,
      "author": null,
      "license": "Repository MIT (Copyright 2024 Lego Master); original individual mesh license not stated",
      "modification": "Removed nonstandard trailing UV coordinates from triangle records; positions unchanged. Added provenance header."
    },
    "parts/69789.dat": {
      "source_url": "https://raw.githubusercontent.com/iefierros/LegoMaster/0b2eb83be4c34193521a962b3136c553d14322c3/ldraw/UnOfficial/parts/69789.dat",
      "sha256": "f9a8b7e724610b9dc73b3fe82a07f54a0602c08888601eb9a5b3cd0a5df925ee",
      "bytes": 219583,
      "author": null,
      "license": "Repository MIT (Copyright 2024 Lego Master); original individual mesh license not stated",
      "modification": "Removed nonstandard trailing UV coordinates from triangle records; positions unchanged. Added provenance header."
    },
    "parts/69790.dat": {
      "source_url": "https://raw.githubusercontent.com/iefierros/LegoMaster/0b2eb83be4c34193521a962b3136c553d14322c3/ldraw/UnOfficial/parts/69790.dat",
      "sha256": "886282dd92a99623c76a85692c7d48f9c5488443b6c6cd593cc3a2717ef6f968",
      "bytes": 302410,
      "author": null,
      "license": "Repository MIT (Copyright 2024 Lego Master); original individual mesh license not stated",
      "modification": "Removed nonstandard trailing UV coordinates from triangle records; positions unchanged. Added provenance header."
    },
    "parts/2752.dat": {
      "source_url": "https://raw.githubusercontent.com/iefierros/LegoMaster/0b2eb83be4c34193521a962b3136c553d14322c3/ldraw/UnOfficial/parts/2752.dat",
      "sha256": "c8493b833fa6aed2de09d4124ae5b47240173eba109139ccc2555c96e6aeec8b",
      "bytes": 139891,
      "author": null,
      "license": "Repository MIT (Copyright 2024 Lego Master); original individual mesh license not stated",
      "modification": "Removed nonstandard trailing UV coordinates from triangle records; positions unchanged. Added provenance header."
    },
    "parts/61406.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/61406p09.dat",
      "sha256": "477f9bcbf6fded984c3dc36039bd16c5537a40c72c0d6aa2caaea8e6b62c6256",
      "bytes": 23989,
      "author": "Vincent Messenet [Cheenzo]; inlined shapes: Joerg Sommerer [Brickaneer]",
      "license": "CC BY 4.0; inlined shapes CC BY 2.0 and CC BY 4.0",
      "modification": "Inlined two identity-transformed subparts 61406s01 and 61406s02; rubber color 10019 retained; primitive paths normalized."
    },
    "parts/3069b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3069b.dat",
      "sha256": "ddfd95b62a2234ffc483c78f6ee52c6e6eb570285634b49e25aa648f4893a523",
      "bytes": 964,
      "author": "Santeri Piippo",
      "license": "CC BY 4.0",
      "modification": "Inlined identity-transformed 3069bs01 subpart; primitive paths normalized."
    },
    "parts/51274.dat": {
      "source": "Derived from official40378.dat; https://brickset.com/parts/design-51274; https://brickset.com/parts/design-40378",
      "sha256": "4c05e7799fbb72a4811791031bdbf4d02f058651989b5301fefa3c3288d75cec",
      "bytes": 143709,
      "author": "BRICK reconstruction derived from Bernd Broich and LDraw contributors; full attribution in asset header",
      "license": "CC BY 4.0",
      "modification": "Outer curve and connector positions retained from40378; base pin inner bore changed to nominal8LDU square. Internal dimensions inferred, not manufacturer measurements. Flattened geometry.",
      "verification": "derived_reference_mesh; catalog identifies same nominal7.84/6.47mm dimensions and square-vs-round base pin bore; physical fit untested"
    },
    "parts/subparts/24866s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/24866s01.dat",
      "sha256": "d6bcd3355e0533f1b976dd029377d7f3b5876f6c0985a1216a7957cf21fa44ea",
      "bytes": 15965,
      "modification": "Normalized dependency paths; original geometry/author/license headers retained."
    },
    "parts/24866.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/24866.dat",
      "sha256": "6bbb06c4363ab2e0adf461323d06fb04640e487ed2d0d106065b6441a1f99434",
      "bytes": 6876,
      "modification": "Normalized dependency paths; original geometry/author/license headers retained."
    },
    "parts/3046.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3046.dat",
      "sha256": "d94872b6df0c29fe91de1fdee0de129514860cc920ad27227e6f1fcdfd105f64",
      "bytes": 4474,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/32607.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32607.dat",
      "sha256": "72347b010649c819022097f0767e99730288db479a1a802c8d6d74d43c26b30f",
      "bytes": 50479,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/subparts/49656s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/49656s01.dat",
      "sha256": "fd5b83a4ad33d7e48de7292c0676d6fd2bf8a4d31c2f841c3d532572a79ce0f0",
      "bytes": 49301,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/subparts/49656s02.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/49656s02.dat",
      "sha256": "2e83f71ab66fb53b6ba919348b8ca5dca6f164b8d44a1d816ec7e53eeb851795",
      "bytes": 31473,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/49656.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/49656.dat",
      "sha256": "e540586acb23835a2b52abfde56aa1da074d70d6030aeae858cf634c1faa6983",
      "bytes": 490,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/subparts/41748s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/41748s01.dat",
      "sha256": "aa7b5113de1547670964a9abf8d617fa1c4b77ee742f6a9929c3df7b0f7ad1e6",
      "bytes": 36887,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/41747.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/41747.dat",
      "sha256": "add5449e46294fab7d9b381bba418a766d7ae8b4a94c7a96169d4824f4559a9b",
      "bytes": 1725,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/subparts/1751s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/1751s01.dat",
      "sha256": "86c6f741ca2e9775f6a6bcd650befb77208197f1375cdc954897455dba674234",
      "bytes": 812,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/1751.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/1751.dat",
      "sha256": "6965a5a063fdde924c346c503a6f7840ca58c39ed5fedaa168b5884327998f77",
      "bytes": 331,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/60474.dat": {
      "source": "original_project_geometry",
      "sha256": "9d0d80416163041535a7c5ac5b4540cd9cfa48a136522f75a27d77f3a0ce87c8",
      "bytes": 17222,
      "modification": "Created as an approximate 4x4 round plate with central vertical pinhole from instruction illustration; not copied from manufacturer CAD or LDraw mesh.",
      "author": "BRICK project",
      "license": "Original project reference geometry; no third-party mesh license asserted."
    },
    "parts/92438.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/92438.dat",
      "source_sha256": "d180860e2598fa2576ef9d7af7084179c04bf5f5092662c491ee1b90576657e4",
      "sha256": "dda9fa8edb3f9bc77c4267f451389f8ba8884e227853fd355452b85662a2ecc2",
      "bytes": 842,
      "modification": "Dependency paths renamed to the project asset folders; geometry coordinates unchanged.",
      "author": "Rolf Osterthun [Rolf]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug-8x8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-8x8.dat",
      "source_sha256": "e9c033a1b9bd6f9d1f3c5d095e66824c9bc2f3e1034e805908c1b8c033e9b232",
      "sha256": "f88eb1218f6bb3413af3bac428c151709921d268f8c6316cc3515d9a9751f3ca",
      "bytes": 737,
      "modification": "Dependency paths renamed to the project asset folders; geometry coordinates unchanged.",
      "author": "Tore Eriksson [Tore_Eriksson]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug4-7x7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4-7x7.dat",
      "source_sha256": "0d0c714589226c4a5eafe92706ace22d6a5c317f681d4ecf1eece02cf6ab4740",
      "sha256": "6791ea30205d5591a344861d010dbae0d231c3c8bb6ef8516601639a23aa3bbe",
      "bytes": 439,
      "modification": "Dependency paths renamed to the project asset folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug4-6x6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4-6x6.dat",
      "source_sha256": "6e127410d945a8e2d85eb8df4815f60a9c90c4f2fd38296f4af6fe16817e1c5f",
      "sha256": "d2be076f28e6bc511fd61b744be8fd0003ca8f5950b270213555c8badc137507",
      "bytes": 495,
      "modification": "Dependency paths renamed to the project asset folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3028.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3028.dat",
      "source_sha256": "52dfb92f2351b6a6ba5cc00039be58bc024ca50697d6d7aeae5d02a308b6fd33",
      "sha256": "b4b88a2455081ab0f8fb514c6081785b40cd9afa4634960ccd8d04affbc663f7",
      "bytes": 7635,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3036.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3036.dat",
      "source_sha256": "3074a0b2952f5d9903ac2fe2196a8110e1553fd245a1d8bc7ccb43f99c654d38",
      "sha256": "7c108504e6823f46eecab58f22931e13acd9cf6a355e849f11556bba88a6e71c",
      "bytes": 5246,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/41539.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/41539.dat",
      "source_sha256": "8b07f1bb13a223f20d2587560540a584d99fdab788c234168e57c18ad796d084",
      "sha256": "2f01cbe3e4239b745973cfc7f580f43afe0846e429de03c5943cbcdb05e8e9c8",
      "bytes": 6741,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Martin G Cormier",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4073.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4073.dat",
      "source_sha256": "18f33637a25a55fc066769ec283719fc096e90eb7007136531bfffdc00126e0a",
      "sha256": "f26e90154a9aecabc6a3e6ba06905883b731f4154b1865601b48f78460e7c5ba",
      "bytes": 400,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/5907.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/5907.dat",
      "source_sha256": "f9e2cbc5b4055e24ad726bd4091192247ada114b528f4d621611a339a7c6ed5f",
      "sha256": "583bf05b0ab25e079430d5c655105c29dc7bc7b544d7eeac7eff2e41fe2f5632",
      "bytes": 3423,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/1-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4cylo.dat",
      "source_sha256": "93f7305e7575678ae00336972ca5078611c37a02d9755865d38cea4ff122c345",
      "sha256": "3e0881ead66c56f9ec778d04e25eb1a67fdd860b3f18c22bdbca62997b453f53",
      "bytes": 482,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/98138.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/98138.dat",
      "source_sha256": "1d506f39ea2bf69757206009498025381bbf28d9fa0b79385a30f4c5fa37f111",
      "sha256": "cef11392cb9b30616b48def70d9b7b14340a75918347862fe995c089b823321c",
      "bytes": 377,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/98138s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/98138s01.dat",
      "source_sha256": "dff4bf55eb5b4d6a8f3889fc208b5946a8f7b139e297a1edb67e2f976fc165b9",
      "sha256": "8884354bcab3c95b408a465ed0cc288cdd163075a9c666c72bf5969641af92f4",
      "bytes": 710,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/98138s02.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/98138s02.dat",
      "source_sha256": "5bda194e7fcb4eaac3211f712ec73a18988f4312fc94aade40722b1e9da00548",
      "sha256": "812989e6f5b93eee1caa6a1642611ff7c7282ba7670d2cc75a8b502387d0fa2a",
      "bytes": 572,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stud4o.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4o.dat",
      "source_sha256": "827edfc93ece0c6898443bf247207e0a5182fcdaf30e1efb85285c9ab586e884",
      "sha256": "0a0cd8e3c7065c7325747f644a0222202f640d663f55d34b705a5efdd948af2d",
      "bytes": 565,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    }
  }
}
```
<!-- asset-manifest:end -->
