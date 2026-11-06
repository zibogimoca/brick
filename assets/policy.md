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

`.dat`는 문서가 아니라 좌표, 면, 다른 형상 파일의 배치 정보를 담는 LDraw 형상 형식이다. 현재 목록의 상위 부품은 640종이며, 나머지 형상 파일 상당수는 그 부품들이 참조하는 조각이다. 파일 수가 판매 부품 수를 뜻하지 않는다.

## 왜 나뉘어 있는가

LDraw 형상을 사용하되 폴더 이름과 내부 참조를 읽기 쉬운 이름으로 변경했다. `primitives`는 공통 형상, `subparts`는 부품의 하위 형상, `high-resolution`은 원 둘레를 48분할하는 고정밀 형상을 뜻한다. 예를 들어 `parts/3001.dat`는 `parts/subparts/3001s01.dat`를 참조한다. 하위 파일이 다시 공통 조각을 참조할 수도 있다. 번호와 경로는 사람이 읽기 좋은 이름 대신 참조 식별자로 쓰인다.

부품 한 종류당 독립 파일 하나로 만드는 것도 가능하다. 참조한 조각의 좌표 변환과 색상 적용을 풀어 모든 면을 해당 부품 파일에 넣으면 된다. 이렇게 하면 파일 목록은 단순해지지만 같은 돌기 등의 데이터가 부품마다 반복된다. 반대로 공통 조각을 별도로 유지하면 중복은 줄지만 파일과 참조 관계가 늘어난다. 어느 쪽이 항상 더 빠르거나 관리하기 쉬운 것은 아니다.

폴더를 단순화하려면 형상뿐 아니라 사전의 참조, 뷰어의 로딩 경로, 수집·검증 도구를 함께 수정해야 한다. 불필요한 `ldraw` 상위 폴더를 제거하고 폴더 이름과 형상 내부 참조를 변경했으며 좌표와 개별 부품 번호는 유지했다. 원본 아카이브 경로와 원본 해시는 출처 추적용으로 아래 목록에 보존한다.

## 출처와 라이선스

기본 형상은 [LDraw 공식 라이브러리](https://library.ldraw.org/)의 [전체 아카이브](https://library.ldraw.org/library/updates/complete.zip)에서 필요한 부분만 가져왔다. 출처별 저자와 조건을 보존한다. 목록에 `original_project_geometry`로 표시한 누락 부품은 프로젝트에서 만든 시각 참고 형상이며 제조사 CAD와 동일하거나 실물 결합이 검증된 것으로 표시하지 않는다.

현재 형상에는 **CC BY 2.0**, **CC BY 4.0**, 또는 두 조건이 함께 표시된 자료가 포함된다. 파일별 원본 고지·저자·해시를 아래 목록에 보존한다. [CC BY 2.0 이용 조건](https://creativecommons.org/licenses/by/2.0/)과 [CC BY 4.0 이용 조건](https://creativecommons.org/licenses/by/4.0/) 및 각 전문을 따른다. CCAL version 2.0으로 표시된 LDraw 말·미니피겨 형상은 해당 LDraw Contributor Agreement의 CC Attribution 2.0 조건을 따른다. 이 프로젝트는 원본 `CAreadme.txt`·`CAlicense.txt`를 별도 보관하지 않으므로, 고정한 LDraw 라이브러리 원본 저장소의 파일 헤더와 라이선스 고지를 확인한다. 공유할 때 저자·출처와 이용 조건 링크를 제공하고 변경 사실을 표시한다. 저자가 이 프로젝트를 보증하는 것처럼 표현하지 않는다. 색상 설정 등 다른 자료의 조건을 이 확인 결과로 일괄 단정하지 않고 원본 고지를 따른다.

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
    "10172",
    "10247",
    "10288",
    "10928",
    "11090",
    "11153",
    "11203",
    "11211",
    "11212",
    "11213",
    "11214",
    "11215",
    "11291",
    "11458",
    "11476",
    "11477",
    "11609",
    "11833",
    "13547",
    "13548",
    "13564",
    "13731",
    "13965",
    "14301",
    "14417",
    "14418",
    "14419",
    "14704",
    "14716",
    "14718",
    "14719",
    "14769",
    "14769p0f-b2b8c170a3",
    "15068",
    "15070",
    "15100",
    "15207",
    "15208",
    "15254",
    "15332",
    "15397",
    "15462",
    "15470",
    "15533",
    "15535",
    "15571",
    "15573",
    "15672",
    "15706",
    "15712",
    "16577",
    "17114",
    "1745",
    "1748",
    "17485",
    "1751",
    "1762",
    "18646",
    "18649",
    "18651",
    "18653",
    "18654",
    "18674",
    "18759",
    "18838",
    "18920",
    "18980",
    "19119",
    "19121",
    "1927",
    "20310-eacab9d213",
    "20482",
    "21301-68d242599e",
    "22385",
    "22388",
    "22667",
    "22885",
    "22888",
    "22961",
    "2310",
    "2339",
    "2343",
    "23443",
    "2357",
    "23949",
    "23950",
    "23969",
    "23986-c2299585eb",
    "24093",
    "2412b",
    "2419",
    "2420",
    "24201",
    "2423",
    "24246",
    "2429",
    "24299",
    "2430",
    "24307",
    "2431",
    "24316",
    "24324",
    "2445",
    "24482",
    "2450",
    "2453a",
    "2453b",
    "2454",
    "2454b",
    "2454b-d0adf8a59d",
    "2456",
    "2458",
    "24593",
    "2460",
    "2462",
    "2465",
    "2476a",
    "24855",
    "24866",
    "2489",
    "25264",
    "25269",
    "2540",
    "2566",
    "26047",
    "2637",
    "2639",
    "2654",
    "2654a",
    "26601",
    "26603",
    "26604",
    "27263",
    "2730",
    "2736",
    "27448",
    "27507",
    "2752",
    "2780",
    "27925",
    "2815",
    "28192",
    "28621-b886189b34",
    "2877",
    "28802",
    "29111",
    "29119",
    "29120",
    "2926",
    "30000",
    "3001",
    "3002",
    "30029",
    "3003",
    "3004",
    "30044",
    "30046",
    "3005",
    "3006",
    "3007",
    "3008",
    "3009",
    "3010",
    "30136",
    "30151b",
    "30153",
    "30165",
    "3020",
    "3021",
    "3022",
    "3023",
    "3023b",
    "3024",
    "3028",
    "3029",
    "30292a",
    "3030",
    "3031",
    "3032",
    "3033",
    "3034",
    "3035",
    "30350b",
    "30355",
    "30356",
    "30357",
    "3036",
    "30363",
    "30365",
    "30367c",
    "3037",
    "30374",
    "3038",
    "30385",
    "30386",
    "30389b",
    "3039",
    "3040b",
    "30414",
    "3043",
    "3044c",
    "3045",
    "3046",
    "30503",
    "30504",
    "30505",
    "30553",
    "30562",
    "30565",
    "30586",
    "3062b",
    "3065",
    "3068b",
    "3069b",
    "3069bph2",
    "3070b",
    "3172",
    "3176",
    "32000",
    "32001",
    "32002",
    "32009",
    "32013",
    "32014",
    "32016",
    "32018",
    "32028",
    "32034",
    "32056",
    "32059",
    "32062",
    "32064a",
    "32073",
    "32123b",
    "32124",
    "32140",
    "32184",
    "32192",
    "32270",
    "32278",
    "32291",
    "32316",
    "32324",
    "3245c",
    "32474",
    "32498",
    "32524",
    "32525",
    "32530",
    "32531",
    "32602-f847c42f9e",
    "32607",
    "32802",
    "32803",
    "32828",
    "32952",
    "3298",
    "33057",
    "3307",
    "33183",
    "33291",
    "33299a-5a3cb0bc24",
    "33320",
    "33909",
    "34103",
    "3456",
    "3460",
    "3464",
    "3484",
    "35044",
    "35394p00",
    "35442",
    "35443",
    "35459",
    "35464",
    "35480",
    "35485",
    "35563",
    "35787",
    "3622",
    "3623",
    "3626c",
    "3633",
    "3659",
    "3660",
    "3665",
    "3665a",
    "3666",
    "3673",
    "3678b",
    "3679",
    "3680",
    "36840",
    "36841",
    "3684c",
    "3685",
    "3688",
    "3700",
    "3701",
    "3702",
    "3703",
    "3705",
    "3706",
    "3707",
    "3708",
    "3709",
    "3709b",
    "3710",
    "3713",
    "37352",
    "3738",
    "3747b",
    "3766",
    "37695",
    "37695-847931e4a8",
    "37762",
    "37775",
    "3794b",
    "3795",
    "3815c01",
    "3829c01",
    "3830",
    "3831",
    "38317",
    "3832",
    "38320",
    "3835",
    "3836",
    "3837",
    "3844",
    "3849",
    "38583",
    "38585",
    "3894",
    "3899",
    "3937",
    "3938",
    "3940",
    "3941",
    "3942c",
    "3957b",
    "3958",
    "39789",
    "40232",
    "40243",
    "40244",
    "4032",
    "4032a",
    "40378",
    "40379",
    "4070",
    "4073",
    "4079",
    "41239",
    "41539",
    "4162",
    "41682",
    "41740",
    "41747",
    "4176",
    "41769",
    "41770",
    "42205-97cfe4dbdc",
    "42446",
    "4274",
    "4275b",
    "4276b",
    "4282",
    "4286",
    "42862",
    "4287c",
    "42924",
    "4304",
    "43093",
    "4332",
    "4341",
    "4345b",
    "4346",
    "4367",
    "43708",
    "43710",
    "43711",
    "43719",
    "43722",
    "43723",
    "43888",
    "43892",
    "43898",
    "44224",
    "44225",
    "44294",
    "44301",
    "44301b",
    "44302",
    "44375b",
    "44375bp04",
    "44375bp04-ccb1d3a60b",
    "4449-f1",
    "44567b",
    "4460a",
    "4460b",
    "44728",
    "4477",
    "44861",
    "4490",
    "4493c01",
    "4510",
    "4519",
    "4522",
    "45677",
    "4594",
    "4599b",
    "46212",
    "4697b",
    "4723",
    "4733",
    "4738a",
    "4739",
    "47397",
    "47398",
    "4740",
    "47457",
    "47905",
    "48092",
    "48165",
    "48310",
    "48336",
    "4865b",
    "48723",
    "48729b",
    "49307",
    "49656",
    "49668",
    "50340",
    "50450",
    "5066",
    "50746",
    "5090",
    "5091",
    "5092",
    "50923",
    "50950",
    "51239-702e8473f9",
    "51266",
    "51270",
    "51274",
    "51739",
    "52107",
    "52501",
    "53119",
    "53451",
    "54200",
    "54383",
    "54384",
    "55013",
    "55236",
    "5649",
    "57895",
    "59",
    "5907",
    "59230",
    "59349",
    "59426",
    "59443",
    "59900",
    "6003",
    "6005",
    "604552",
    "604615",
    "60470b",
    "60474",
    "60475b",
    "60477",
    "60478",
    "60479",
    "60481",
    "60483",
    "60581",
    "60583b",
    "60592",
    "60593",
    "60594",
    "60596",
    "60601",
    "60616b",
    "6063",
    "6081",
    "60897",
    "6091",
    "6106",
    "6111",
    "6112",
    "61184",
    "6124",
    "61252",
    "6126b",
    "61332",
    "6134",
    "61406",
    "6141",
    "6143",
    "61482",
    "61485",
    "61678",
    "6179",
    "6182",
    "6192",
    "6231",
    "6232",
    "6233",
    "62361",
    "62462",
    "6254",
    "6259",
    "6266",
    "62701",
    "63864",
    "63868",
    "63965",
    "64179",
    "64225",
    "64390",
    "64390-03ad90cc81",
    "64644",
    "64647",
    "64799",
    "6536",
    "6541",
    "65426",
    "65429",
    "65509",
    "6558",
    "6577",
    "6585",
    "6587",
    "6589",
    "6632",
    "6636",
    "66906",
    "66956",
    "67142",
    "67329",
    "67695",
    "67696",
    "68196",
    "68211",
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
    "7324",
    "73562",
    "73825",
    "73831",
    "75902p04",
    "75937",
    "76764",
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
    "79757",
    "79846",
    "80177",
    "80178",
    "80796",
    "85080",
    "85861",
    "85863",
    "85943",
    "85970",
    "85975",
    "85984",
    "86210",
    "86876",
    "86996",
    "87079",
    "87081",
    "87087",
    "87421",
    "87544",
    "87552",
    "87580",
    "87601",
    "87609",
    "87618",
    "87620",
    "87693",
    "87747",
    "87926",
    "87994",
    "88072",
    "88292",
    "88646",
    "89522",
    "89523",
    "89678",
    "90194",
    "90195",
    "90398",
    "90540",
    "91405",
    "91988",
    "92262",
    "92263",
    "92280",
    "92409",
    "92438",
    "92593",
    "92907",
    "92947",
    "92950",
    "93095",
    "93273",
    "93274",
    "93550",
    "93594",
    "93609",
    "94161",
    "95228",
    "95344",
    "95820",
    "96874",
    "973",
    "98100",
    "98138",
    "98138p85",
    "98138p8b",
    "98281",
    "98283",
    "98313-027c3f0ff6",
    "98374",
    "98989",
    "99206",
    "99207",
    "99563",
    "99780",
    "99781"
  ],
  "files": {
    "LDConfig.ldr": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/LDConfig.ldr",
      "sha256": "d3490047460ad7a511b150006b009830fc52ecc1899b514c7380e9de644b3cfb",
      "bytes": 67580
    },
    "parts/10172.dat": {
      "sha256": "efa060bc3d8a23cf57d85600395d9527aab4915d20b076271ba7b5bf14426895",
      "bytes": 2111
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
    "parts/10288.dat": {
      "sha256": "55e9c5928c156ebe901f9a34b184767a0af890d3e4f4a63057778c252c34f7a3",
      "bytes": 813
    },
    "parts/10928.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/10928.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "4e9abab2fd12627380774c03974e59b5a3387922",
      "source_sha256": "9c2af4f7128bbf5012f458a6cc63626ba65df2549c17f1445c66c17eeb2bc697",
      "sha256": "816201ab16b3715ab45b3d5e923bc98d8b4879de78c3494976cff00d06390528",
      "bytes": 1479,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Daniele Benedettelli [benedettelli]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/11203.dat": {
      "sha256": "5f1e06ad29b475263a6b459cf813552d6ede7739250b0add83784f187db8d2dd",
      "bytes": 593
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
    "parts/11476.dat": {
      "sha256": "8d41bc075c09abc6150ad157057484cd5869351fea4909acd3a93cdf2748e5cd",
      "bytes": 1042
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
    "parts/11609.dat": {
      "sha256": "5c7b7e5e53f4495da101ce56efd45fe85851dfe2a7ade3563676de89edc62c22",
      "bytes": 3288
    },
    "parts/11833.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/11833.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "6d4744e3fa36c38f38c63a88a6e90a21ea17fd7d",
      "source_sha256": "a4e609dc79399b0c2aa0fdc83002630d99b5be00212a4953ba1d14fadf747387",
      "sha256": "777cb171b2c1e3a5d94891fbb9aefbfb3eaf0f33834ddcdfa6bba589e080c1ae",
      "bytes": 1169,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/13564.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/13564.dat",
      "source_sha256": "290146789259ca9044e55921d8f53620769b47416581474988164e67037aa6ba",
      "sha256": "b2098a8691b29ff95e6c6dc79bf0e0fbfac37818ed8ae78b763355d116bcd435",
      "bytes": 35209,
      "modification": "Official geometry retained; primitive references converted to shared asset paths; coordinates and surfaces unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/13965.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/13965.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "c8d81c082dd24e2175f914e15a3cd6e4db08a1e4",
      "source_sha256": "96ed3d9ea70f313718b421a9484bba7d35a72bf46bd805bb7f00314e0983ef94",
      "sha256": "6b8a6918818145f66b8868179923583b047187158c3ac1c8c993186cee9df2ac",
      "bytes": 3463,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/14301.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14301.dat",
      "source_sha256": "d0008172df5fcaabd22416934902aa5ef344d314a8b78b9f3e08c5845f6b6705",
      "sha256": "0503638c3d15cae928c5701313a468b6d3a03707987fb74ddd2d07d161fca625",
      "bytes": 2521,
      "modification": "Official geometry retained; internal part/primitive references converted to shared asset paths; coordinates and surfaces unchanged.",
      "author": "Sylvain Sauvage [SLS]",
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
    "parts/14716.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/14716.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "577a07d48bf170d93b9ed5cd47eed2380876b431",
      "source_sha256": "6a65d7df417ff6a3eb91334cc6db5a6e51dc5a916281d9d732b253eb334fa668",
      "sha256": "b9e4d5386aa68ab35ddb19478160a4b58c1b62c8b23a3be9e25e5cdce4128a27",
      "bytes": 575,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/14718.dat": {
      "sha256": "48c8d8b8c6c032d36545f2a64ea8a2653fef0cb6869b3584f9dc623b5eacf3e6",
      "bytes": 479
    },
    "parts/14719.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/14719.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "76d492d4115696503c40b626ee1db08095f63011",
      "source_sha256": "83318a6398f6c313a39fe6c18e3c9341c1f6ee948572f5626bbd11a4a83c250e",
      "sha256": "8e2c0571d6411aa18db650e4c1fa8c51cd5a72d558f0d51dda606065855d2f28",
      "bytes": 383,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
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
    "parts/14769p0f-b2b8c170a3.dat": {
      "sha256": "f16f0c36616ed707432dbd05dc3c52fc5e319174209fb55351b0be5f70d99bab",
      "bytes": 5326
    },
    "parts/14769p0f.dat": {
      "sha256": "f9fcb9dfca12ebeb905148c6719ad91e8a7814b540e49f71e6c08952432bf4a2",
      "bytes": 836
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
    "parts/15070.dat": {
      "sha256": "1e0b27f376e8d861dcc339e9d4c2aab8d9d058956c1c05c98da4f6864750b021",
      "bytes": 12402
    },
    "parts/15100.dat": {
      "sha256": "ce37e61249ed9be62e0155095d29a64f5b6d4d70fd6c0b6dd0b32865768a44aa",
      "bytes": 767
    },
    "parts/15207.dat": {
      "sha256": "97bb501b4f643d7a7ac5081b62cf4a2b7862ececfe666f5566478dfc8611e7ff",
      "bytes": 1857
    },
    "parts/15208.dat": {
      "sha256": "a1484e6ace06c280ca3a38d17149042359e1feaf1715646914a285e281689dc3",
      "bytes": 1090
    },
    "parts/15254.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/15254.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "b96091884fc358affd3c45cf8fee59215e3f84b0",
      "source_sha256": "d0a46511d5348dcab1d16852e930fb2f7ea96ed461aed46cf0343b0a2feae883",
      "sha256": "58a1e092b34e0eb49bdee238b718ccffb1d82dbb79b5bb45808b360242926dd6",
      "bytes": 2045,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/15332.dat": {
      "sha256": "121d83163ad1d2e4a1b05702813e83e1f3f4259dbb855febea8652e6d46013e4",
      "bytes": 4310
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
    "parts/15462.dat": {
      "sha256": "80ca646d8687776725bb216206bc0910c0fe3831e0df09822b1ee1b0733f05f1",
      "bytes": 727
    },
    "parts/15470.dat": {
      "sha256": "2369cfd9dca768b9685657d2a5dd9f9acf4e82039e6a4c2eff3a1cceefb4660a",
      "bytes": 2058
    },
    "parts/15533.dat": {
      "sha256": "fa0103ac1bec907f58b00298776ec847b80df79d0fc8aaeef223cc4ede365bc5",
      "bytes": 5918
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
    "parts/15706.dat": {
      "sha256": "51287ae4bc71bb099d3105af4e70d72ae33c2b0c0e1dc8343b422e13e1b1e3b1",
      "bytes": 1344
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
    "parts/16577.dat": {
      "sha256": "454b9c1a22b1183e4e67bd54d8b8852752b774bebb1cf92a4e1cb3938caac16a",
      "bytes": 4062
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
    "parts/1745.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/1745.dat",
      "source_sha256": "b017d0da54803c72a658e813dc8808a9ec92f79a5cdbd3b14a2c86ebc8cca427",
      "sha256": "31de551befe53592561d3ef4dbf4826ed355757cfc3e471ddfa802e137d4e338",
      "bytes": 577,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/17485.dat": {
      "sha256": "2e4d18f10294167736950ee36a83f215d5e90ac4d1b80e05359c8ee49349b0fa",
      "bytes": 1556
    },
    "parts/1751.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/1751.dat",
      "sha256": "6965a5a063fdde924c346c503a6f7840ca58c39ed5fedaa168b5884327998f77",
      "bytes": 331,
      "modification": "Normalized references, original author/license headers retained."
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
    "parts/18646.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/18646.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "99fafa0e6a0f3db75d6cb4ab8eeb83b43d5742a1",
      "source_sha256": "11ba2c647c1a70a40a2f5541a5dda5e675edb9a589ec79f35c80a3641fc6b811",
      "sha256": "3908b6260186deea959f1eda8572120a4cad1b7a86a902695e51486cfa74db3d",
      "bytes": 13753,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/18649.dat": {
      "sha256": "16326a00096e38e1a36eb7c6a99f9f3d5b97cfd2f5de779c3d016bf10c45cb4f",
      "bytes": 1397
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
    "parts/18653.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/18653.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "db46f3625e719a0aefdfdb7b76cdd7d96d2037f7",
      "source_sha256": "add1d1d5238ff649f202d0b989736b4fd34d53401ec0103e3b9cb0092a5c6084",
      "sha256": "c251d6504acd70a97179e89c9aba73814c02ae160ae375a63312cff27da7c8e1",
      "bytes": 4293,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Rolf Osterthun [Rolf]",
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
    "parts/18759.dat": {
      "sha256": "87e60c06ba221d391faf22aa4fcaea718e4efbf289b78ada015fb898a46584fb",
      "bytes": 2126
    },
    "parts/18838.dat": {
      "sha256": "d5ab53471c4b6572136a1c052acf82acd8b6884009b304598c15fa9c33262056",
      "bytes": 10252
    },
    "parts/18920.dat": {
      "sha256": "91973773b379247f38c249db99d0d46a12ecbfd847a8940533cdf5b902c57ec9",
      "bytes": 839
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
    "parts/19119.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/19119.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "a7c83efb90bdbda4f16b02b105aa0dd34b4e9100",
      "source_sha256": "0489fd68cb86898ef60e234de7425346d1324036ed88b5536655bc31f9e09d5f",
      "sha256": "f209caa61a1d095056734f501a3528c0dfac1311bdb94e2e0838b3d9b513f08c",
      "bytes": 11610,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/19121.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/19121.dat",
      "source_sha256": "62860464fc99573e72dfb482f836fef56421ad2e3325c299f4f182605fd5b2cc",
      "sha256": "fe05498881d86b1be3c99a72865a1c1453f5a445781982dd85df87a74e55ba81",
      "bytes": 51244,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Heiko Jelnikar [KlotzKiste]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/1927.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/1927.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "4b6ecc7322f199d1a309ef707e764dd26ff36b42",
      "source_sha256": "7c155ae3f4ddbce3c837f29cd43e9320010373b0569147f68285c0a5c209cb79",
      "sha256": "03a74818047667aef35742982043fa2c01ab77013e3debaa19b582c1a4e35832",
      "bytes": 320,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/20310-eacab9d213.dat": {
      "sha256": "34ae734e195e5a5ad774898ed54e545ff3af1681f205bb7fbaf7efafda59a24f",
      "bytes": 4495
    },
    "parts/20310.dat": {
      "sha256": "4a32c128bde5395a2646215b516386016b14a1784e0b5d43383cc52485ce43a2",
      "bytes": 4539
    },
    "parts/20482.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/20482.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "570b4f3c6892f8380779d27aa66287d768da918d",
      "source_sha256": "3d995abf641bda00a9a95faaff2bcea2af9c760b6b675b131e0b7105bdf4dd11",
      "sha256": "7070648a61e1a3ba7a0ab28bb33e93b38b4489167b99093a4eb3ba3bf3d8d0e8",
      "bytes": 948,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/21301-68d242599e.dat": {
      "sha256": "c6ac001fd82ee4dfe0cc9d9a5dc79c1fb34a3954de7bf937fe5a2b4a49cb0271",
      "bytes": 14522
    },
    "parts/21301.dat": {
      "sha256": "f919d815638f5accaf32d031263d712470a1b6bfff758bdeb75972ab54248d69",
      "bytes": 13622
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
    "parts/22388.dat": {
      "sha256": "5e139bf625340d56242273ed010c83e49953335763a098de9096f9c6d8ea8970",
      "bytes": 1286
    },
    "parts/22667.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/22667.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "308d744c37b1a27e8300f0f4393dd1b15e22e7ba",
      "source_sha256": "fffeea9aeea24487e26b3a8fb6dfe91df67753cba92163a9b591b2c38558963b",
      "sha256": "ff45101c9c6bba6bb0c95a9cc115f5d62ee5d779f60c471bcd5b3bf88296e7f8",
      "bytes": 4893,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/22888.dat": {
      "sha256": "496f847d4079e3bca2647a9e8e99273e3b6fca10b50880ba841612a568dbd963",
      "bytes": 4601
    },
    "parts/22961.dat": {
      "sha256": "04a35ec516e3a899517e7fbcd36196bd5be18c9d74e4eb7114ec05a6e58cf18a",
      "bytes": 1130
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
    "parts/2339.dat": {
      "sha256": "722ae6d8eabea3bafbd49f175ddf7f73a9687246f2e9cebf06b13c4ab9928c03",
      "bytes": 6990
    },
    "parts/2343.dat": {
      "sha256": "48460c891e0c50478eb066e8d76f64dd1e2593240704eb5fc2b4a9610ae9728e",
      "bytes": 2625
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
    "parts/23949.dat": {
      "sha256": "2bd64a89d4fcbc15ece7cc9d59fb54442b3716fabacaf27d702375307d99304a",
      "bytes": 1894
    },
    "parts/23950.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/23950.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "c66295e70c99bace59b253372757e3a4480ff312",
      "source_sha256": "ed990fe3bb91fd3a86f0a7165a7ca7881a3bdb68363792378091c2f6dbdb8726",
      "sha256": "d4bca51efd7854f3d4f0365fa9e7fe5fe4fe737ee5e230510f05e24bda579e29",
      "bytes": 1604,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Rolf Osterthun [Rolf]",
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
    "parts/23986-c2299585eb.dat": {
      "sha256": "e9ec98f65a0e42df3bd33db8d36fd8bab6d0eb45786348baade7f4cbdae1faa1",
      "bytes": 2789
    },
    "parts/23986.dat": {
      "sha256": "3eaeef45de4428ae8a1ded997a310fe69028e40e78f1b544d7612febf3044773",
      "bytes": 2758
    },
    "parts/24093.dat": {
      "sha256": "9aae81434826d40c4c24ca589fc40f34559fb7393a746a2bb53ece2c42550220",
      "bytes": 410
    },
    "parts/2412b.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/2412b.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "3641160328746a7af920228de125ee5721037e5f",
      "source_sha256": "a7e7b03fc76cad9d94eb7199721b929f95227b1f8a35add5b7c66ee1ba6dca57",
      "sha256": "aec55f6031126851b8ed1ad6434b0b9f004be4b2928061254b7e0e385897658e",
      "bytes": 2906,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/2423.dat": {
      "sha256": "78d035432ec1924d7d7cae0bf22a6f3b2b347ce50eda0527cb0838c30b92bd39",
      "bytes": 11028
    },
    "parts/24246.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/24246.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "b35e0fecbff0ed3fe4b61f68e15bc29e2090bfa0",
      "source_sha256": "2ca90b1f66e26e82debfac6ff1cbce2b8696902cce622d13b4a65941e9cafcd7",
      "sha256": "5cf3d6e509c52a8492273ad359214c261e157f048a672cf56087eab1971d2cfd",
      "bytes": 403,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
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
    "parts/24324.dat": {
      "sha256": "b0087cf855c43cea0287442f92d580b8e64f7aa22a0db01005b5adf3508cf05f",
      "bytes": 3789
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
    "parts/24482.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/24482.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "c08d36e79905d57fb70e27ad6cd1cea323216c68",
      "source_sha256": "039e6499791be066eba835bec3a2617a79238c1b7f6801b87015e7f3b5785d1e",
      "sha256": "e080453ddbda9cf55fd3784f8ff84e859fee8854b6ca59dc7cd39200518759f2",
      "bytes": 971,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/2453a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2453a.dat",
      "source_sha256": "457ff62a325babfceea10b02c7933d09ca422a0479fa51e9b1623b56f543a0c3",
      "sha256": "866961860f0def02ca41053c5575e4bbe4450c552c150d33efcccc99d8ea1610",
      "bytes": 1605,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2453b.dat": {
      "sha256": "aaf9d1e985bd9cef68b8d0faf7fff03144ceb387460a3799a53f66ecfc3f28d1",
      "bytes": 815
    },
    "parts/2454.dat": {
      "sha256": "e71a5f4c29462fa11a9ecfebc49b3aae385f901030f08e0828bbf8b0d16dd6fe",
      "bytes": 732
    },
    "parts/2454b-d0adf8a59d.dat": {
      "sha256": "117d02974d2fff3b15d0d039ccfda76859696b3d35b687128b448947d38165ee",
      "bytes": 369
    },
    "parts/2454b.dat": {
      "sha256": "f2aa3fd453db345a798cc55a1993201ab5f0b6a763936185fc30bd5aeb6ebab0",
      "bytes": 495
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
    "parts/2458.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/2458.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "fd3b4daf225348926cb5e45064e854040a2783cb",
      "source_sha256": "7c8e68deb0f2c31f2cb06e17fc469a6d2c67358cc530fe01c1feea1e50bb0ba1",
      "sha256": "533a5b21bfc5af41f67b6bb1ffb3d89443e9e405b3ce4ef708eecff9924f605b",
      "bytes": 794,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/24593.dat": {
      "sha256": "cc638ea845a9cabf325550f7473c2f65c4c566a36bb7f17f18270ceec5fe82b4",
      "bytes": 641
    },
    "parts/2460.dat": {
      "sha256": "754cd3a83798f4073353193a1a8ca595aeca8a94ac8afaed4cef2ec5fcf7e1b0",
      "bytes": 724
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
    "parts/2465.dat": {
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905",
      "archive_member": "ldraw/parts/2465.dat",
      "source_sha256": "3237acda8a54e8835b93abd983b847ff1921d05d8ff52a8e1f3c47f88d98ec64",
      "sha256": "2e5000c3c99a13a96832c71fc00bf7adfd539c6b1e58a479e85aa44740a4b8ff",
      "bytes": 546,
      "modification": "Renamed recursive reference s\\2465s01.dat to subparts/2465s01.dat for shared asset paths; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2476a.dat": {
      "sha256": "a54542c6904ba434bfc7db9f73f46b8ba4db09eb5b46c391acc757d06fab8511",
      "bytes": 1804
    },
    "parts/24855.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/24855.dat",
      "source_sha256": "a5dabe75e9eb7e9380db7d2873fda078d8af1d722bd1d1dfe8d559ab2f50834c",
      "sha256": "856a9d5ce22e799d7bd0ad4cb504ba4406f157d716cd6d7e7bd0fad26b429ca0",
      "bytes": 11968,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/24866.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/24866.dat",
      "sha256": "6bbb06c4363ab2e0adf461323d06fb04640e487ed2d0d106065b6441a1f99434",
      "bytes": 6876,
      "modification": "Normalized dependency paths; original geometry/author/license headers retained."
    },
    "parts/2489.dat": {
      "sha256": "5bca3f589d5cf3b0a1c583957e5bb8c8e58d1c691db72484e745ece29e0bca7c",
      "bytes": 9757
    },
    "parts/25264.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/25264.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "6b8c771fe737beba6ec3b66f3ce6d25d90c1d6af",
      "source_sha256": "aa3d8c602cd18b4a0c5fa8b39bd0b4fff6b358032be5140b4ca3562af4636310",
      "sha256": "2a9be832f3dbcd5b7f63c256ff29f34fcee8bd0c355e510d8a1738c97bdddc28",
      "bytes": 612,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/2540.dat": {
      "sha256": "bdb7c1cfab1695e175099e23c2cbdd36960b812994dc69fc5fcec7ac899c8163",
      "bytes": 1859
    },
    "parts/2566.dat": {
      "sha256": "693428069bff976e9a9d768045cb37be2167582c5895748dc4f8743df08ad5e4",
      "bytes": 1759
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
    "parts/2637.dat": {
      "sha256": "35e0728d3192fbb0a0f6b45e41f869ee2b66058d5b29cffbb6c7f4d3f6bcf959",
      "bytes": 2428
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
    "parts/2730.dat": {
      "sha256": "31fec841037cee632c41a599bd5b1e642a066e250be7afcf24506dae04a3fde4",
      "bytes": 10415
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
    "parts/27448.dat": {
      "sha256": "8460f50b2d98e99e40e7044ae2637306f354a46323acadc4eb02fc9e2da5f940",
      "bytes": 5066
    },
    "parts/27507.dat": {
      "sha256": "4c3741ac4382ca5804c98f90f7d1ef3a218f3797b7b8049ddc34a9f1dbeb5e48",
      "bytes": 469
    },
    "parts/2752.dat": {
      "source_url": "https://raw.githubusercontent.com/iefierros/LegoMaster/0b2eb83be4c34193521a962b3136c553d14322c3/ldraw/UnOfficial/parts/2752.dat",
      "sha256": "c8493b833fa6aed2de09d4124ae5b47240173eba109139ccc2555c96e6aeec8b",
      "bytes": 139891,
      "author": null,
      "license": "Repository MIT (Copyright 2024 Lego Master); original individual mesh license not stated",
      "modification": "Removed nonstandard trailing UV coordinates from triangle records; positions unchanged. Added provenance header."
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
    "parts/27925.dat": {
      "sha256": "725e6244de2112f081ef4fdc290a8d4897f8c50d100062c1436c0b20ba53ae9b",
      "bytes": 563
    },
    "parts/2815.dat": {
      "sha256": "1008437d0d152cf5d13658c8147022d3225a64b8aec0400d9c9b5c768309cf52",
      "bytes": 2355
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
    "parts/28621-b886189b34.dat": {
      "sha256": "7b558d0c5473d3e42bc41435e4a1a073e64509bdd9d400143d43d34de3178b2b",
      "bytes": 761
    },
    "parts/28621.dat": {
      "sha256": "6e4618e3a692ca6efc5008fac3dac4098e39da77d716b0d41120a9955d736647",
      "bytes": 957
    },
    "parts/2877.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/2877.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "e7ed306f681c9c7ab5f278c0e47fe5ee0c887499",
      "source_sha256": "46c3a0dc6329d3f0be9b3b4485b5e2e41295bad750a0f4c4b6a2e6631c0c0029",
      "sha256": "8b001bb936d35de0d9a0f853173ce25fede3702c1e4c0cac38657a423b8c1e75",
      "bytes": 5417,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/29111.dat": {
      "sha256": "5b1c95674db00145d8057e7670f39bbf041974f58b812a60468b6354135ba554",
      "bytes": 3049
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
    "parts/2926.dat": {
      "sha256": "8dd5271d005d0dbd534b84b061dc2c8bd2a46b7736802f864c09a5f2023482bd",
      "bytes": 1578
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
    "parts/30029.dat": {
      "sha256": "0a4104aaca5ad05d3db31a385407dcef030622b0a82359ed0f619b4586157e50",
      "bytes": 8293
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
    "parts/30044.dat": {
      "sha256": "07bb9a1138de5d67bcb1765d29737196885e3401c7cd78c44f18f0e3ab183d69",
      "bytes": 5050
    },
    "parts/30046.dat": {
      "sha256": "da07e5ce7ac6b8dcde58c464d515506f6d013ae0e181b0464bbbfaa465c55d3a",
      "bytes": 12285
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
    "parts/3007.dat": {
      "sha256": "aa70ccfd441f9dbeb8c4358a5efde7c48b91c86929a1db272dd40b0d813d48eb",
      "bytes": 663
    },
    "parts/3008.dat": {
      "sha256": "b79ba5ddcd7ccd3d3612907467161f0e087dbf3918fb340b48dad93186e6b443",
      "bytes": 666
    },
    "parts/3009.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3009.dat",
      "source_sha256": "950a186800b17a778e6c4b91420b1846df98c2bdbac8a551cfe7f74ddc831a3e",
      "sha256": "ca401017967bedb8ba6b638a51bf24d904015556cc48cd85783580fbd3cdde8d",
      "bytes": 676,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
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
    "parts/30151b.dat": {
      "sha256": "efc559f2995a1475620887b84569edf0adb8abd97209db7b29f70207e88dfcda",
      "bytes": 663
    },
    "parts/30153.dat": {
      "sha256": "b3271ce915c7c64b49a76bdc24995e1383ae078a7ed8faff667b14c2dd11f899",
      "bytes": 5986
    },
    "parts/30165.dat": {
      "sha256": "b321da1a9ed18a4ea25cff25baf749730362692c504cf0497563ed2bfa4b7377",
      "bytes": 3164
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
    "parts/3029.dat": {
      "sha256": "a722f16468aca5e7d7682d81892f50b61da499ee83aaf6b046bce683df844092",
      "bytes": 5169
    },
    "parts/30292a.dat": {
      "sha256": "db3f7ecd21ac6dcefda0a68de75b900050c8dcb358b7414be2d268a76f84d9ad",
      "bytes": 3955
    },
    "parts/3030.dat": {
      "sha256": "5a990584eb7db0f05de8fa9804c886a20c6f70a7f3f50f1f8a018fc80fe66530",
      "bytes": 4404
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
    "parts/30350b.dat": {
      "sha256": "f64eac28c8ad6c5408da412a408959bb0d5dea71a555c73f7d58b76de57813ea",
      "bytes": 397
    },
    "parts/30355.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30355.dat",
      "source_sha256": "362db433aede9c8c0089da37f1890c9b7b9dad35ba4ee43deddaee4656342c2c",
      "sha256": "786a1b645bcc0c0956defcbe647cc9462a3cbf839b8d7ed6c9749ea27e221cfa",
      "bytes": 1017,
      "modification": "Official part references converted to shared assets/parts/subparts paths; geometry coordinates unchanged.",
      "author": "John Van Zwieten [jvan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/30356.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30356.dat",
      "source_sha256": "df9929620c63ab49cb3ac4eb77b541cc14d7a5a1821801801f221d1691b2eab3",
      "sha256": "c1fd4875afe55e3212743e4b374535dabc4a8dc9685c51ebbf5a4b1c1a9470c7",
      "bytes": 937,
      "modification": "Official part reference converted to shared assets/parts/subparts layout; geometry coordinates unchanged.",
      "author": "John Van Zwieten [jvan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/30365.dat": {
      "sha256": "e7263206220023e6f17a03d67aab0f8bb32a724017a9705b2a301bd77f122470",
      "bytes": 1106
    },
    "parts/30367c.dat": {
      "sha256": "47fe7bd308a2fc66cbce992bfe15fe289b8ff7ba5ba617c0f15f92725aa97234",
      "bytes": 759
    },
    "parts/3037.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/3037.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "a78828df0e1c350f71e5505b261cf284de28f825",
      "source_sha256": "879b9e1226d6cccfde2779877489c184db02d2f926ddf069f674bf6057230909",
      "sha256": "fdb99eea2d03cb469ecf011fce5311943dcc155fd47570f15458be5313060e01",
      "bytes": 616,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
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
    "parts/3038.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/3038.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "ea06f9b908b260074f1ce6e0d0343eda81c811fe",
      "source_sha256": "d12164e5bfcff0bf2b15b78ef915af8b42e212c010090e2650bf782a86aa13dc",
      "sha256": "631c37000c83355255613a7d47b44fa01d5c317b6f2aeebef843f975c2ae8b60",
      "bytes": 639,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/30385.dat": {
      "sha256": "ea87197aac6e420d7663172bb890839f31bed4e57f1f9f596cee330ffed3e69a",
      "bytes": 12922
    },
    "parts/30386.dat": {
      "sha256": "8b8c7d1194c298c80a54a10fbda411a315b717fed78ec517e2fe92139ffdf22e",
      "bytes": 1209
    },
    "parts/30389b.dat": {
      "sha256": "67f972f32f05c9d834573544c1591b317ab6f168d8d2db69c6862ecf2b164a3e",
      "bytes": 2130
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
    "parts/3043.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/3043.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "4eda91bbdae73ba695019b6db23785349858196a",
      "source_sha256": "a898dae958e21f8a5fdda63fec772358e7d75c4e8c2d7f227ffd26783601505d",
      "sha256": "0f357ae350349140dd58311426245c3a2feb62174a3d7efe1cfecba592946f26",
      "bytes": 1918,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3044c.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/3044c.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "5f2b00df89882861ebae8eb9a528968cf6bbe275",
      "source_sha256": "d92b5d2113670dddbe6f19413e5b821d17021e2d6037ef07252f7fa4c7d73834",
      "sha256": "75c1f4d5aedfe2d805df7d8dcfc2d347305c05e97d20294ae14a2b688aa86d89",
      "bytes": 2947,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3045.dat": {
      "sha256": "0c372e2cbb49a618a2664dd313100b9e07dc84959cdfe839ce05c88aa242ef99",
      "bytes": 3509
    },
    "parts/3046.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3046.dat",
      "sha256": "d94872b6df0c29fe91de1fdee0de129514860cc920ad27227e6f1fcdfd105f64",
      "bytes": 4474,
      "modification": "Normalized references, original author/license headers retained."
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
    "parts/30504.dat": {
      "sha256": "225f2876ebf4ba975c1ff164f7f760478a8d29927ee741ac802bb666283d2b14",
      "bytes": 7028
    },
    "parts/30505.dat": {
      "sha256": "28fad3271e0f5fac6b2685a8260304f7ff314e562c0d9f03c0aa9f61d751945e",
      "bytes": 3063
    },
    "parts/30553.dat": {
      "sha256": "c4c393567c6c1fa7ede28bb86587978e48c8ce33def9156b27bd09261a9a9dfa",
      "bytes": 1295
    },
    "parts/30562.dat": {
      "sha256": "1f9446eaea241b0a5ed88a8144e441cad7606d5af41331e6fe796e837e5b30ed",
      "bytes": 871
    },
    "parts/30565.dat": {
      "sha256": "6ba2c119b1b6e3964686c17bd3df9fb503e7073244ab258e5487bb980db63ded",
      "bytes": 2195
    },
    "parts/30586.dat": {
      "sha256": "215fec57b25f7170895d00010c4348d762a0e1074c44c06cb17619ed060976f6",
      "bytes": 2840
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
    "parts/3065.dat": {
      "sha256": "66cc024802e14ecf22b62a256e7b62953b7a6fb411234eeab62dfa4f89b758d6",
      "bytes": 637
    },
    "parts/3068a.dat": {
      "sha256": "b845ce0db5dc0582792d243c1924c0ddab9542b316cc93af28b50915403f6b52",
      "bytes": 608
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
    "parts/3069b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3069b.dat",
      "sha256": "ddfd95b62a2234ffc483c78f6ee52c6e6eb570285634b49e25aa648f4893a523",
      "bytes": 964,
      "author": "Santeri Piippo",
      "license": "CC BY 4.0",
      "modification": "Inlined identity-transformed 3069bs01 subpart; primitive paths normalized."
    },
    "parts/3069bph2.dat": {
      "sha256": "d20c6fdcb366fc08dee2d4c10d69f853a4adf5a7ee5a827452a4c5f2bee26eca",
      "bytes": 32629
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
    "parts/32001.dat": {
      "sha256": "2f41a5a5f5a8c91488f21f9bfe2b01f01c0681420f8354d0080d414abaf2d55f",
      "bytes": 3622
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
    "parts/32028.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/32028.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "384d612483b98e3916e2c79f51e2a8da4c4388ba",
      "source_sha256": "041e22ba92d36c0dd7affcd1bb161821f2aba185f77b74fa302f9d5c56abaa95",
      "sha256": "f5627755b1a2c0a071c5a98b2986ec6e1e38236bc25ccb7fc00884a3ef4c5f21",
      "bytes": 1718,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Remco Braak [remco1974]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32034.dat": {
      "sha256": "a43ad28a4226d126f4d50728a44581006f3f3f3a9ef89ec8ddae9b1d670e020c",
      "bytes": 5416
    },
    "parts/32056.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/32056.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "9a6c112cd51ea4a540f5d6ec57fc011aa7de84ac",
      "source_sha256": "a787df6e3bcb1238b7e6c8693eb20d994f20511728b101575d26a2ced7ab7ead",
      "sha256": "b9b6255d3fe2019a54c523ace61ef12aa2e1618793d56c481b35f9b22df3065f",
      "bytes": 3217,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Lutz Uhlmann [El-Lutzo]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/32123b.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/32123b.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "85ab0fe14ac6a809e9390be4718a6dcdd4ed4017",
      "source_sha256": "d94f7a46be0ca7dc45e586fc904024ac4ee89011b923ccdcc65a2ea4a3d1a9af",
      "sha256": "f39f5c1303b105eb49ae4805511a4b4633e254fbd32761f01bb33b196e1c949e",
      "bytes": 1413,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32124.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/32124.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "5696028835475920d32c1c15af10d28558ae6273",
      "source_sha256": "d0216a76dbcc6009e50a5bf58513124d7e02d3dda39119570cc288b815e36e2e",
      "sha256": "8916d65007622bd0ba361192851f3598f3b5aaac346dc1a41ba56dcdfc36f957",
      "bytes": 2371,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Rene Rechthaler [Blechtaler]",
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
    "parts/32270.dat": {
      "sha256": "99299c0e487ee7b33c59199d8fca420e7d150124e3acd0512610c81c9f3dbb46",
      "bytes": 3742
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
    "parts/32316.dat": {
      "source": "https://github.com/ldraw-linux/ldraw-library/blob/master/ldraw/parts/32316.dat",
      "source_sha256": "a56dd40ce6d005a85fdd88848edd704108ead94afe667d8da7e3de206664e41b",
      "sha256": "540fcf5812b423f9f6306b6141c417b7a1aeb8bb46cdd0dab657c3b1e5ffc29f",
      "bytes": 1275,
      "modification": "Dependency paths normalized to the repository primitive layout; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
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
    "parts/3245c.dat": {
      "sha256": "25dcabea62f17134b7128b367df47fe015354688be508dac81aa6c72b7034e80",
      "bytes": 483
    },
    "parts/32474.dat": {
      "sha256": "2921c3869a978714db158c5845f8d350da9fbf47e54c68c3bf14e94dd12703bb",
      "bytes": 1551
    },
    "parts/32498.dat": {
      "sha256": "9a845934a39d733e733c94c8dcef7a5ef3c795230ca76cbdb2472655dfbed832",
      "bytes": 2243
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
    "parts/32530.dat": {
      "sha256": "958cda93bfe86f876b75c3ef14be9dd3b169cd932c2fc70219cfbd33151c8010",
      "bytes": 2246
    },
    "parts/32531.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/32531.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "6ea2ad263985d2b8e19aa73272457a46b1503abb",
      "source_sha256": "f12d4a846b2d83a0da93e5d516a4c225eaff4931c91df46a8c75921d656b6ba1",
      "sha256": "5729f89ad50f8368ea2ac5bfb4535010d163b83b66c5398a44bce93811869504",
      "bytes": 360,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32531a.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/32531a.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "abddefadfba9e20fd01ee9a0834f1d206068743c",
      "source_sha256": "c993db1bfab853c5009c2b6a76ab3e972ddbf2b7dea7eabaa8d9f89d88efafa6",
      "sha256": "3fceb7289300a3f90981bdf39e67ec5d217aadd55064ead398925b53a70e0680",
      "bytes": 2666,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Marc Klein [marckl]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/32602-f847c42f9e.dat": {
      "sha256": "13b688a105aebbee9a2f159ea8fa57a408628f7a5de2ba735b62172132f8870c",
      "bytes": 175633
    },
    "parts/32602.dat": {
      "sha256": "a7614573757e75018f2a6a951fffe86eaab5a0c5586dbfbffd8a4bab0edad362",
      "bytes": 176126
    },
    "parts/32607.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/32607.dat",
      "sha256": "72347b010649c819022097f0767e99730288db479a1a802c8d6d74d43c26b30f",
      "bytes": 50479,
      "modification": "Normalized references, original author/license headers retained."
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
    "parts/32828.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/32828.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "0f0a2e26b1c526089cf175e4a5fd5da2f4869253",
      "source_sha256": "e99657afb143d632ad94088246cca208c6d16bf9b7439a8a1d5c4f0f310b03ce",
      "sha256": "fa1e4fabe5a2b864b20def326208bc459466f8dd171665af7569a13dd4acc153",
      "bytes": 7755,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/33057.dat": {
      "sha256": "07d6a37a46c5143f18c4ef4b19c18afa17799db82615bcd6f3121a26015f02c5",
      "bytes": 757
    },
    "parts/33183.dat": {
      "sha256": "13a8e2cbc03d23204e8b71e3fea0542bb6b044f304fee113bb8759fc6cfb1d73",
      "bytes": 52236
    },
    "parts/33291.dat": {
      "sha256": "c1f2f4f121bed5fc2f641ec762fe8d148727c3df1bf9541d6f43e34e42fc01f0",
      "bytes": 4610
    },
    "parts/33299a-5a3cb0bc24.dat": {
      "sha256": "cab1e2cf1dbec9487a03384b132567aa02a791efc5cb7b67bd34df22260d31e4",
      "bytes": 1018
    },
    "parts/33299a.dat": {
      "sha256": "183e8f4a97415095977b6f23c2efe8a2971318b7c99c3be62245b170b1ba4074",
      "bytes": 1152
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
    "parts/3456.dat": {
      "sha256": "a7fc19949c042960cfd44727a2c16bad3d666c838134d53341e3757b349289f6",
      "bytes": 8600
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
    "parts/3464.dat": {
      "sha256": "c673d08a188f0908d94619409784e36e84afb289e5115afedbaa055eb3247263",
      "bytes": 375
    },
    "parts/3464b.dat": {
      "sha256": "4180233e73aa52d69ab29f20a5278e4b9cec88dfcd80ecbcb9394af8c9638906",
      "bytes": 2427
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
    "parts/35394p00.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/35394p00.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "2904d88652b52849f79a62f1f324ea6065c96175",
      "source_sha256": "4ebd6e547a0e8f779714e4db8817ece20319ae635d5c33068146fc44c76061ee",
      "sha256": "ed1d21891208de7b1478b59bf04abe599944c3ef218f230cf393728e3aff0ade",
      "bytes": 891,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Marc Giraudet [Mad_Marc]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/35442.dat": {
      "sha256": "27f4a18dd8411e338fd07d27b61c5794bc2544b6fab1981124a44540347003a9",
      "bytes": 5037
    },
    "parts/35443.dat": {
      "sha256": "89c294bc9ee4f2a174038049cf0dc248f7199c82f8dc93d21609881fbe34287e",
      "bytes": 15240
    },
    "parts/35459.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/35459.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "32026f3663c5fd2fc27128b8efcd7562dc276c5a",
      "source_sha256": "03fef6b689761168b8226bfd2079493c6c6580a77cce9360c3738fa478913593",
      "sha256": "e3bd176d720eb0b165ad47f113b175c2a0c936508ccdfc7980cfb0679146c750",
      "bytes": 2652,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/35464.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/35464.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "da1feb7fe0f07841cdded20a3aff9773fc995600",
      "source_sha256": "0c4a292f9040030ca40a705c617f22a12357975f47dc18d3aaa1b353aa05966b",
      "sha256": "f90f177599e7f01805cb324c64f0e8ecf28e7bb4e3c146d102ed4db63dc69288",
      "bytes": 999,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/35485.dat": {
      "sha256": "e2da488842b4f17f395b2c02d397c15bf4c8aa31e0e76af0381b8fcaf082d844",
      "bytes": 698
    },
    "parts/35563.dat": {
      "sha256": "edfe2f113c299fbd1b6fb02d98558c81a0fe64435ea286b3d19192740cc4621b",
      "bytes": 1744
    },
    "parts/35787.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/35787.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "9add246cebd582963457b7432283b247302b757f",
      "source_sha256": "15504e50d1cf297ead59fb2120663613049fddf604181c1af99479cf9a9a3602",
      "sha256": "31c537fb41a6b53f385e068db237e4524dfab4460600b0a08f8a317c7b1a239b",
      "bytes": 380,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/3626c.dat": {
      "sha256": "db46101a5fed2e10ca27471de9da14a9d08de684c9c38f8cc5ce1b023bb80f64",
      "bytes": 725
    },
    "parts/3633.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/3633.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "74ff52c7e4a7cc374dcdca9a991f5021f5f03083",
      "source_sha256": "abd5af65920a4677364834e7258b2a347ff2240d6c3bb4667a8bb75ec16147d6",
      "sha256": "b1a0556d4a7d76d22dee7fb04455ee6d9dc3ac8d5793af71a87e4488c96fa3b4",
      "bytes": 4489,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/3678b.dat": {
      "sha256": "bb6e788d7f80435682f9de6ff0765bab014ce0cf55b9f9ecf949ee596860627c",
      "bytes": 452
    },
    "parts/3679.dat": {
      "sha256": "bfa01d7657ed0bf46f36b69b8d66cbc268c10836a2064a57cc3f983510a18a53",
      "bytes": 7918
    },
    "parts/3680.dat": {
      "sha256": "64eb3e9f54a07e30911587a4fba92e4b50ed18a1611fdef93b4f0b4dfa9139f4",
      "bytes": 1250
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
    "parts/3684c.dat": {
      "sha256": "a15af6e0d99f60a3cd8036abe88a90fa2f634d0facf492d25fb74e0be7f929c0",
      "bytes": 509
    },
    "parts/3685.dat": {
      "sha256": "8bfa3fc3a3b9eece66c2dafe6f0a37c637eac0b02b83d8c8e6e4711e67144cca",
      "bytes": 3804
    },
    "parts/3688.dat": {
      "sha256": "d7b0542db09a899325b4a345533d6f05886ae9166aaa70658fba7cea9eb0cca7",
      "bytes": 4277
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
    "parts/3706.dat": {
      "sha256": "61d1fe2ca1dc6ba33337e09ed0b08749ed31296db2faafb3395bf942b1cecf43",
      "bytes": 671
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
    "parts/3708.dat": {
      "sha256": "62111e272a27ac9bd13b95e2d49ee9e0a1e93ac31cff4ffcf53a6c61e310e98d",
      "bytes": 674
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
    "parts/3713.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/3713.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "222a0c2f118ad1f739d09939ad9faa77807f336b",
      "source_sha256": "2b813f30e7a6843cbd330035763f6ef904eafc8e7b5395c98332d07e8dfa1c43",
      "sha256": "b3dd14db80ea1f3c589c06572745c04f0b438b2c4ed4de47fa447c7039ac5555",
      "bytes": 1024,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/3747b.dat": {
      "sha256": "2c49473cfc088e2890a7fa4dd12cd66bcf61abb678f3acca1851f7ea12223577",
      "bytes": 14181
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
    "parts/37695-847931e4a8.dat": {
      "sha256": "2764118488129fc779a24625174be1d216eb11a38834b6c0fc1e9b43cfde2bd4",
      "bytes": 7328
    },
    "parts/37695.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/37695.dat",
      "source_sha256": "90685bd63dd8693508ba3fc25d4151e9ac53272645ebe6616d54089ad8633775",
      "sha256": "2158b5caed610aa868714a131b659361afe7c77177c04bfcd7dedb4e6bd6d050",
      "bytes": 7158,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/37695s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/37695s01.dat",
      "sha256": "93faae8f7cff333fa15f0486b4cdf9d574ddf97548e75a689166d0cd0557b905",
      "bytes": 52052
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
    "parts/37775.dat": {
      "sha256": "10e53f4a51e86a32b927c7b2c835bc4ebbd3f3e6f8d12957af3e8f5245f2dd92",
      "bytes": 18623
    },
    "parts/3794b.dat": {
      "sha256": "4b495ae1d384b9213dfdb4e308a3145f637e048ea044716ea569f032ad7d31b8",
      "bytes": 885
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
    "parts/3830.dat": {
      "sha256": "2e3a5b0cd5eb9b438871d06cb609a0e5929ce41c3f7b96c5fafed39e02ec6e22",
      "bytes": 2501
    },
    "parts/3831.dat": {
      "sha256": "86cbd97be89360658412eb7b0e93bbc774571c75bd0091bbdb02c829c771af31",
      "bytes": 3032
    },
    "parts/38317.dat": {
      "sha256": "2cd13fa6c8e3116c6c9d494e39e5b212f0fc0f66049a67168a9561c70a4ff2e3",
      "bytes": 11106
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
    "parts/38320.dat": {
      "sha256": "4fe2cebd7c7d721d5c40d2be7ec8f4c7a1959b004386af1c1c2eed9f9bcc9f87",
      "bytes": 8272
    },
    "parts/3835.dat": {
      "sha256": "b67ae2bc9ffbbcd1a1c1a86ea6b46802bb508bbd284eef56eeccc7ca2f76e6a8",
      "bytes": 6069
    },
    "parts/3836.dat": {
      "sha256": "5d3e174a1208c464c5a09ea69dd52fbb7d90104f7395c5b8d91d43a455c30d63",
      "bytes": 3586
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
    "parts/38583.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/38583.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "861a3316ebb07e89450a4b7a12a43213ddf2fe2d",
      "source_sha256": "95c6f095c33fba68b8c34f5e77fa1abd6752ac213e1cfff4a9e8478352506a18",
      "sha256": "e7f3d40f96ea691dd5cabe643d6a04af483558910857c81511b71b44192fca09",
      "bytes": 1061,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/38585.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/38585.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "859f3727c39e31919ab3c8f38e277ad2f18eb89a",
      "source_sha256": "eda3965088eeae7cbca7ece2fac458d2bbb9be07b53ec2707da51cfc23e090ce",
      "sha256": "6e1a0b29151fee7bb78ad4501cef161f089061fda614bcd605ff46f5b610ebec",
      "bytes": 1467,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3894.dat": {
      "sha256": "8f6476d7d3974eb8a0742880030a1064d8fa8391d4c603f65f00bc3f1a90d9fe",
      "bytes": 6458
    },
    "parts/3899.dat": {
      "sha256": "f280663cfeee746ed0414ab20b941aaf3203ce4a8f09f4b6fb114d730c30b53a",
      "bytes": 1235
    },
    "parts/3937.dat": {
      "sha256": "8d94f866c19f30e8e3728d78fc6fc6f4f6d5b26b82e1d9251268a4db5162ca8c",
      "bytes": 6193
    },
    "parts/3938.dat": {
      "sha256": "fe356c939ea583c297f058dbbfe79ef276ea9a4e31e3f5b150fc0a99c9e00ce7",
      "bytes": 1394
    },
    "parts/3940.dat": {
      "sha256": "cd24f278ff081accec7019665a7a1c3bcef3aa70b3188286638d1b935faeeb4a",
      "bytes": 309
    },
    "parts/3940b.dat": {
      "sha256": "1a3911af374d59068e68da1717cc4d6e89aa1efbb26141678a6f883439d992de",
      "bytes": 2064
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
    "parts/3942c.dat": {
      "sha256": "dd4ec034870cbcbe593c7382255b245b808c58047d0087a06727062bfbc4682f",
      "bytes": 11888
    },
    "parts/3957b.dat": {
      "sha256": "6acbc2e308cc43d71cef857ba26166212366b1a2c40fc01049e6c6b2e0c31326",
      "bytes": 1368
    },
    "parts/3958.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/3958.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "55a2b6efa9af43d9aa803736341bfbddd18d60c8",
      "source_sha256": "9f64b46369f84ca4b172fd1a9e239cfd9bc17801d0999c38ef8847bf683e1dac",
      "sha256": "ec985842747799503581c097ff9b67c3a3d681f262391e6b11c034f762bc0524",
      "bytes": 917,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/40232.dat": {
      "sha256": "0f9e04b82711a1dcd68cf0e605d40c9a10bafbc78d601c5fcd9bbaae71073d83",
      "bytes": 828
    },
    "parts/40243.dat": {
      "sha256": "56a7d6ff30e314ee75e071f5625fae7254b72e000593a59c784caff9de7a2d44",
      "bytes": 17826
    },
    "parts/40244.dat": {
      "sha256": "c8fd2b3f753624bd8bfd5e19f8998320a0079cdcc3bfdbaacc4f40ae82cd1973",
      "bytes": 7912
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
    "parts/4079.dat": {
      "sha256": "f2125a10775c5f8a9abf237517d9bf967e5bb991edb9878b0025ebdca590d40f",
      "bytes": 5097
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
    "parts/41747.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/41747.dat",
      "sha256": "add5449e46294fab7d9b381bba418a766d7ae8b4a94c7a96169d4824f4559a9b",
      "bytes": 1725,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/4176.dat": {
      "sha256": "f57671f66f2eb8fd78150ad5201fc97e69960d1b285d21ec1700a99d40a6eaaf",
      "bytes": 6550
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
    "parts/42205-97cfe4dbdc.dat": {
      "sha256": "1b8b6aef92f9f2c9445874a638873e1cc522fe5afa2472e7e0f60e163e980be2",
      "bytes": 2899
    },
    "parts/42205.dat": {
      "sha256": "768403dbd7895d2a631cd3246a768d624ccabf55aced2e11546867b987bd067d",
      "bytes": 3106
    },
    "parts/42446.dat": {
      "sha256": "a1f14ee7797bd8130ea3e67999ec81129ae784f04756ea3d9e65d913aad4d6c2",
      "bytes": 3486
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
    "parts/4286.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/4286.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "bcda7058eb030375db9cc36b64f8d6633e5841d8",
      "source_sha256": "ce0b8fe0d83dd527625b773a26725ec927d462bc4216a8f3912fc72862016539",
      "sha256": "255f6df9f085795b7e920e25148078d7eb86087c571c5d2f63caa511414dddc6",
      "bytes": 928,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/4332.dat": {
      "sha256": "6bdaf43b93d656300ef5c3717611ec901b9e7af187cfa58ca4ed74cfc4aef3eb",
      "bytes": 158806
    },
    "parts/4341.dat": {
      "sha256": "002717ccd72d8b9ab31e13760366b70163f2868c3993b8bdbc52430a4d0fb09c",
      "bytes": 13698
    },
    "parts/4345b.dat": {
      "sha256": "277c41356a6b9fb4aeae36c641746e831c934a06e8c3efba1efaa31bd3a66b0b",
      "bytes": 1088
    },
    "parts/4346.dat": {
      "sha256": "7bf68d657b0d7bdfde87b75b5ff5230cdf88c555e80ccf34b874cb2bcee88a5e",
      "bytes": 877
    },
    "parts/4367.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/4367.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "c5f6383253ef2a47e63449289454415e923e2de0",
      "source_sha256": "8c558c9f19b2bd87c88d7e8de0a07a492f20741ec85ae5437f3e7726a4bf0246",
      "sha256": "22e46efbf090408ae2bc534f6861961007690ea962de1d10408196244e3022e2",
      "bytes": 101559,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/43719.dat": {
      "sha256": "4764737770b7acff170c8423021a163abf904aca42f774b3898d41618748895f",
      "bytes": 8650
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
    "parts/43888.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/43888.dat",
      "source_sha256": "f4687f2989f6ceeadfc45add9061d37440646cf0bd353aa8fecd481e7a505c6b",
      "sha256": "f38ac30af46dce870eaab62d710a9f8a18a46c314bd1877155647d02bfea0fc1",
      "bytes": 1517,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Stig-Erik Blomqvist [stigge72]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/43892.dat": {
      "sha256": "e267111f35ea96836ef3f934c854db1fd76b07a1c13e63bef6b7ab210eda9eae",
      "bytes": 622
    },
    "parts/43898.dat": {
      "sha256": "83a9a6359d08d1f43a76715f8343840bf2e39c51e9b202317cc4370a2a0a9fff",
      "bytes": 12379
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
    "parts/44294.dat": {
      "sha256": "8864ea2acb3d8175d1669fad74c018aaee494da0ac1de7c6a842ff676719da4f",
      "bytes": 714
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
    "parts/44375b.dat": {
      "sha256": "b8c94d834d042292a6b1b69d9a44278abf3b066478bd1ded63210290c942d78c",
      "bytes": 9438
    },
    "parts/44375bp04-ccb1d3a60b.dat": {
      "sha256": "4aa3d6a9b08841b1f75d2c68fe0aa6fc254fde175856ba50b49407af59d42be3",
      "bytes": 78752
    },
    "parts/44375bp04.dat": {
      "sha256": "38e268825583815db02e4c34c2aa96257684f5686bd2c355deda3be7341b62df",
      "bytes": 78552
    },
    "parts/4449-f1.dat": {
      "sha256": "b57dc0fa270155d2343b7fb6a7dad894fbaa1206cb6508e4d6d3cb3c4f0e1aba",
      "bytes": 845
    },
    "parts/4449k01.dat": {
      "sha256": "0c5e306a7e88d6f56120bdf02213a5c21d030f4e44bd9e4faad39c6b2e610faa",
      "bytes": 1066
    },
    "parts/4449k02.dat": {
      "sha256": "aa450002111420b03815f6104fe68810c79fdb2e3c7da984fb8e3325eda87328",
      "bytes": 7335
    },
    "parts/4449k03.dat": {
      "sha256": "efe0fb03a76468632007ea3286bac26ace3bdf619690de724436b8411c10f9ed",
      "bytes": 4778
    },
    "parts/44567b.dat": {
      "sha256": "736fba80e5facc0dd29dd8ef3207c97af31dd010ea7421174048eeaa1e2a7076",
      "bytes": 969
    },
    "parts/4460a.dat": {
      "sha256": "408fb85edaa7b37aef42e3c16cb02b9030b7fb523bde7295fd45cfc5abb07376",
      "bytes": 1398
    },
    "parts/4460b.dat": {
      "sha256": "5874528a9f658c48352db35f01c3dc35c75fbb97e94500d45d7dac33b2a20657",
      "bytes": 451
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
    "parts/4490.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/4490.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "3a716c8152d9e21f86f697cb2e1bf5faa20bede1",
      "source_sha256": "b0fba2a016312270e488c390f02ac6612b877576b05b2cbdc8c8a934dff11ec1",
      "sha256": "1f25a2cc4d0f59c30b4544b89d8ba91404384050adbe01fe7c0aac48511b34af",
      "bytes": 1131,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4510.dat": {
      "sha256": "017c99024a4f4d6c46557a9f49d1a25cf15482d2f28ec28c0860abf2d0028b64",
      "bytes": 1961
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
    "parts/4522.dat": {
      "sha256": "b7ec943354460d705542e0c3e66d95b2ace60dcc77ab407581171f3c83fd4b7b",
      "bytes": 3412
    },
    "parts/45677.dat": {
      "sha256": "9beffcc01cde768dd7b95f0839a16a42d6d3c26fa372e62c9c3288f129054e6c",
      "bytes": 30484
    },
    "parts/4594.dat": {
      "sha256": "eb564be1dc43c8a4756ceb6d5e0a971ad4a63ad2c65ae6bd5c9b2134525cf906",
      "bytes": 8735
    },
    "parts/4599b.dat": {
      "sha256": "41c89b5dec12b40d2c50e510f0e8e2b5f65a638e10eb26380c9d0e713358ea88",
      "bytes": 2023
    },
    "parts/46212.dat": {
      "sha256": "ec8c3b25ccf7683acdc819cdc065aa29a50da9324bcacee719ea4bbb49f2f4f4",
      "bytes": 2102
    },
    "parts/4697b.dat": {
      "sha256": "9f8967e0b1edb68500dc0e485be6ff5b976f68b50dcde75e8734ee5db051a1c4",
      "bytes": 13796
    },
    "parts/4723.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/4723.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "33938dad381181d86b067629ad127a70bcc0c5df",
      "source_sha256": "3f4c9bfbf8445c88d61ef771493e7135004fc5eaf9987a117f1c091a91b5d608",
      "sha256": "87acaed4558b6dbf417633517f2c127b5327d36f65af13a14d6569d2a92f66e1",
      "bytes": 368,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4733.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4733.dat",
      "source_sha256": "1a78f23c832965da11a06c18090e0f8ac101f89c4a6d85d039d5548916ec68d6",
      "sha256": "a4f331b68c01eea27d536678ed91a419930f2d919340de2e691388a18bd7959b",
      "bytes": 4320,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4738a.dat": {
      "sha256": "1f9462199d9a0ff8b9b3a83baea1ca930f15bd5d17d155ac288c9b369ffa05a7",
      "bytes": 12563
    },
    "parts/4739.dat": {
      "sha256": "30800273d1aaeea1abaf44e98516efe2a947ce9893a9d9f8b8ba48b098035c1f",
      "bytes": 312
    },
    "parts/47397.dat": {
      "sha256": "d7a2eb619feb5ea34ddc0dac1ce027946f325cffaba8ce4fef4be2df9529e978",
      "bytes": 1593
    },
    "parts/47398.dat": {
      "sha256": "611323266bbe29dfa8df5344dba694dbec6f54992d75141135b06f4c5218ea3a",
      "bytes": 1582
    },
    "parts/4739a.dat": {
      "sha256": "21b79cffc39454fb14e08a0557522c05e34c364d1ac5c482fe359c30afb3bd7b",
      "bytes": 2130
    },
    "parts/4740.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/4740.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "0d06accfba7f369f2c4c06899f0419a84529da49",
      "source_sha256": "ae5f6d05a1aab00f3e9e66e29f95af272821ed94eecda1ad719462115b7aa144",
      "sha256": "bd8e01edad59617cf2cd5723cfcf1cf6f2f39dc43addaf3856b2fd2ff8019f4d",
      "bytes": 3366,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "parts/47905.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/47905.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "c2845e9119b0fe510632d8ff3ad481bcde03339e",
      "source_sha256": "26179f7718ef7f77eb128d2473589ac4536540bb262fe5540b10fe7d9870f425",
      "sha256": "807622758e4297de36659905a0b0e27eaa0deeb12ebc8ea8fc6f0044a248ee14",
      "bytes": 2404,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Sven Moritz Hein [smhltec]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
    },
    "parts/48092.dat": {
      "sha256": "b6ef068f8c6b7d94a12c9fe5fba188ce784a72e28a21445d52460194d0164e08",
      "bytes": 19938
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
    "parts/48310.dat": {
      "sha256": "784491ba581b8a9b7d4c74f3a8cd52af3c9d5bcdc266dd331bb68243472ed4af",
      "bytes": 478
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
    "parts/4865b.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/4865b.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "25adf7512f93c70a8b9de1ff79fb6bad170fb934",
      "source_sha256": "5a0c449bed1b4c712b090cca8949eb93dcebfc101687d7a76d63b9295763ebdb",
      "sha256": "fd7af062b47ca43479dffc871bf2dfed05d93f31992c50fbb1bca99c97d8dbbb",
      "bytes": 660,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Rolf Osterthun [Rolf]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/48723.dat": {
      "sha256": "e65bfd0be7dc3096f9ee3409fe5ce9db1338a7ac3dc6b235eebb9fe3a282ad0b",
      "bytes": 25867
    },
    "parts/48729b.dat": {
      "sha256": "5c8d0292e2f81fdcbefc59698857ad7d40de9a12595183dd7b036c278fcccbf7",
      "bytes": 17433
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
    "parts/49307.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/49307.dat",
      "source_sha256": "5ab186e08cf7dfd9ff7ce2e1afcd69d08479fd44972340d53d78f67ffdceb135",
      "sha256": "e74806b6aad033c09cf9bed3d89d1c89fbc4447fbd168c6b0d7cbc95f2e85325",
      "bytes": 1133,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/49656.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/49656.dat",
      "sha256": "e540586acb23835a2b52abfde56aa1da074d70d6030aeae858cf634c1faa6983",
      "bytes": 490,
      "modification": "Normalized references, original author/license headers retained."
    },
    "parts/49668.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/49668.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "0a40cc1672bd87a503d2ba841cf7a1d2a6fe35a3",
      "source_sha256": "49d912d06cd0952073243191d85f9957ee7b04f05cde40de7c69ed92297ae639",
      "sha256": "b9cf4ab6fe561925dcdd137b523e70504d34e75443a958d7030148e43bc40827",
      "bytes": 1550,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Bernd Broich [bbroich]",
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
    "parts/50450.dat": {
      "sha256": "d7c461f7991b38904b24c49c8b4a09e6a0a8f8e84c5e6367eb1258645532a92e",
      "bytes": 586
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
    "parts/50746.dat": {
      "sha256": "e2be17f62c7065e4612f2005763787f0da6c6a1a23a0bd20e8ec8b746f37ca2b",
      "bytes": 692
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
    "parts/5091.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/5091.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "703b629c7385425168be1a385e45b47274222910",
      "source_sha256": "4d291aceb9e9b24a1515c988d50d2645ff7d77822a22e6e7cda626550a444c71",
      "sha256": "433a69ae1111b6120a12f252bb282c4bd71b109feedf184fae2454e6a010ea94",
      "bytes": 381,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/5092.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/5092.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "58a90e70f1e394a01f95e901cb53ab6b8b0436ff",
      "source_sha256": "5a8818232b3f361a9a6fb2f774700fa29c488c182c6d4dd2387b41ca29c888f2",
      "sha256": "36ce148c55ce3a0f9a37bb6a887b314e172b95e466bf2c7a3de91bd2ea264862",
      "bytes": 380,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/51239-702e8473f9.dat": {
      "sha256": "92eed800f58f0b3b88639492f6094bb83ea3e961fb6f11c003d2664f64e5ffab",
      "bytes": 2857
    },
    "parts/51239.dat": {
      "sha256": "067465114ace003c4358a8ca887bbb868ca0d71ffcb1c9774a2a02fe2eb6ffdd",
      "bytes": 3069
    },
    "parts/51266.dat": {
      "sha256": "46692c8c726aba3c4d9ee65041dce39c2ef3c75fa81ae378ad2cf2c3f7c91387",
      "bytes": 460
    },
    "parts/51270.dat": {
      "sha256": "f876b89fc2819ba2249b0bf48a3b6bcfa5809bc4fda196a861e442630959b791",
      "bytes": 1866
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
    "parts/52107.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/52107.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "70278f97ce227ec477ea75bce67cfaba95cd5e70",
      "source_sha256": "737d0832cdbca7968d7b178aacc82ef044bf4dbd74d06a6fa6d20db2fded37bf",
      "sha256": "9f03391af19c16e134587e85a847ea92eb161a69c2ab6b42b38f49e96f8615e1",
      "bytes": 3142,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
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
    "parts/53119.dat": {
      "sha256": "eabdacba865a5874bc84bd012e374f6e6dad52fbba2f139b4e6221b006309fad",
      "bytes": 58499
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
    "parts/57895.dat": {
      "sha256": "f56e6aaf44656bf93b62a6a9171f2ee3a01702d013c015fa6cf74bfc217dd767",
      "bytes": 709
    },
    "parts/59.dat": {
      "sha256": "942665a5fb0bdc2a3cc263fb1f89e02fe11ae50b65b0ea20643aa8a89918efb7",
      "bytes": 1868
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
    "parts/59230.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/59230.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "84750c2dc548d2f6e737d2e594360a07d8c71a39",
      "source_sha256": "a12f203e5eb44f09155e4fca9b61d8fb4ad2b5280cb1c096adb9dd5f4b0785ff",
      "sha256": "6d02d349c437844112ee56c4a873644a591fa9af9664f26f6107b9887cd48253",
      "bytes": 38118,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Andy Westrate [westrate]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/59349.dat": {
      "sha256": "5218632aa718c0033aa175e16a9159d0fd389f1ab958a8346c58823e898f8113",
      "bytes": 593
    },
    "parts/59426.dat": {
      "sha256": "51b7c8e63a53dab9b390ce18e2104d8e86cc41019d48ae5f91ef814fd212e2dc",
      "bytes": 1461
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
    "parts/6003.dat": {
      "sha256": "55eaeff2cde11782604b48460beec231da91c9d2dd9678325f7660c6eb74e7c9",
      "bytes": 13289
    },
    "parts/6005.dat": {
      "sha256": "e7951b126a0f5cb850dd5ad2060e4f0637e9a2cdc7dd5fc84ab69c5508c4ea92",
      "bytes": 4260
    },
    "parts/604552.dat": {
      "sha256": "e964be4ba536d68322eddef699f93d78f83f0b10583b90f812482bebe64efa96",
      "bytes": 3419
    },
    "parts/604615.dat": {
      "sha256": "0afb52d7ea0ef6f88e67b447a3ab6cea7dcae7ea4e765ea21db0143757f82911",
      "bytes": 2258
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
    "parts/60474.dat": {
      "source": "original_project_geometry",
      "sha256": "9d0d80416163041535a7c5ac5b4540cd9cfa48a136522f75a27d77f3a0ce87c8",
      "bytes": 17222,
      "modification": "Created as an approximate 4x4 round plate with central vertical pinhole from instruction illustration; not copied from manufacturer CAD or LDraw mesh.",
      "author": "BRICK project",
      "license": "Original project reference geometry; no third-party mesh license asserted."
    },
    "parts/60475b.dat": {
      "sha256": "dec3b1a441aba151dfecb7379334a735e207bbc46a3ac45bb3673901076b8d8f",
      "bytes": 1037
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
    "parts/60481.dat": {
      "sha256": "e06f7c526a5fd482cb23bc9412412acafd7f7acab985f723bef0b279fd4680f0",
      "bytes": 339
    },
    "parts/60481a.dat": {
      "sha256": "aedf69740c430b91afc3b3534c8e16b561792cbc86bd6c3c26762c21c4556e14",
      "bytes": 803
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
    "parts/60581.dat": {
      "sha256": "98fac48a35e3d40638d96ed47f7a330789defbf952faed9951055a8ab0d82593",
      "bytes": 847
    },
    "parts/60583b.dat": {
      "sha256": "589831d08f2640f79d3e55a2cf7ef2d214640f6d5b51fa90d4d22658dc2723de",
      "bytes": 901
    },
    "parts/60592.dat": {
      "sha256": "5ff0f6fcd47678862c5804c4a29d78be47914fa5b764ed3d7d4371edc746d66c",
      "bytes": 8089
    },
    "parts/60593.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/60593.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "769f858ffd4b03dd45ad951f6743ad0defbeff11",
      "source_sha256": "6a0e0d627e899ba519eca1b7bd9d6ac50ed684625bcdd737f3dd55095bf5aac0",
      "sha256": "1a3074de8a4c7c9cc45f68bbe73b9da6ea11dbcf0835c42e7dad9f1b7ecd2c6f",
      "bytes": 7944,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/60594.dat": {
      "sha256": "76f9c0c31d2525a0da88f948a49232b46352920f44b33b18321e76349a56a3bb",
      "bytes": 4903
    },
    "parts/60596.dat": {
      "sha256": "bd2ec0cca9db91bd6f227c1cd09edd7b25891edd9e54555e1c4403113b3c0bc3",
      "bytes": 10813
    },
    "parts/60601.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/60601.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "00303ff5c27ab16240a09d74b10526be79b16161",
      "source_sha256": "f9802551d645052a00163ba5ab8aa2eb8f6a7be85fbae58a827161182971d882",
      "sha256": "0e30ebb0788d44defa31194534e208d67184eb47a2fb99d7e772ae767c9f0f0e",
      "bytes": 711,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/60616b.dat": {
      "sha256": "3cf7af52e48fe8677e6bda6c0c7fbee1fedb9b8e5043b622206cd9eb2468a378",
      "bytes": 3018
    },
    "parts/6063.dat": {
      "sha256": "b56fefaf0210b9d920683fac52d0edafd74b3bf0de90fd9c35b579db44f6d872",
      "bytes": 2101
    },
    "parts/6081.dat": {
      "sha256": "f3ee4eca333ecad9bacd96f2988e885a4f3e99da5948ec5a349aaf1e433a5f4d",
      "bytes": 791
    },
    "parts/60897.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/60897.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "73b28c47c7793865c103553383b62b2ac6a480e4",
      "source_sha256": "5a55863184489f1ece294b75a5d51ccee2e2c8ebade1f269968ee1e768c41ebb",
      "sha256": "b54ce10a622aafb2e55e54615bf728545d35b15942ee4c893d06eaddb26e291e",
      "bytes": 1002,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/6091.dat": {
      "sha256": "f6293d39e9907d579be7c9fe5cc296229ad53de082065283d5337c8166c14f5f",
      "bytes": 2549
    },
    "parts/6106.dat": {
      "sha256": "8b7ad71f3fb0a695362cf1c2f4546ac01f2f5c63c0ba42c85ed58862d250081f",
      "bytes": 5730
    },
    "parts/6111.dat": {
      "sha256": "203734aa6f4e73ea90b10ac1d7eeacd6de073fac578000221cfe8585e484bdab",
      "bytes": 1696
    },
    "parts/6112.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/6112.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "bb41cc8f9b0cf01b0f952fd5f6a62f25ff03b5ce",
      "source_sha256": "e903ef598ca391d4481d7c117c2fc8c33294c7b59607688137d8aefaa608c710",
      "sha256": "0a0aa9469aa1aa4565d641531e7809f854c062945db65de360b4fe0a4a57c7ee",
      "bytes": 1915,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/61184.dat": {
      "sha256": "4bbb44543eb7056787a2b388ebf723e41a90d362726e81e7abb6bb4aaeb1823d",
      "bytes": 6528
    },
    "parts/6124.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/6124.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "e9b39bbc051469464033116519f02b846566d07d",
      "source_sha256": "4c2ca76f708dce3035ceb2bda0cada620ec1a5375667f942653f1406766e81ef",
      "sha256": "30a3bf74c8f22440ce5621348e47659ec6152ca06df98740bf4b84c4b89cc64f",
      "bytes": 5720,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Jaco van der Molen [Jaco]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/61252.dat": {
      "sha256": "7cf75744a1ee60944205fe2d90803dc2689dfff346d1194ba2c80eabe7d651b0",
      "bytes": 1134
    },
    "parts/6126b.dat": {
      "sha256": "3d372d19bb241e82c8e74ca0e819bc1eadaa19f9c1146f3c85661b8d6a433b88",
      "bytes": 744
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
    "parts/6134.dat": {
      "sha256": "e30cd7f5f20f6a7c745ab89b5819a45f2f7a7e7c6d8625f5d74619c7c5e0773d",
      "bytes": 2918
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
    "parts/6143.dat": {
      "sha256": "d2417613bc87dc707d3d5ebb70c39916a126485f8add27b610e8b61acb1ebe41",
      "bytes": 696
    },
    "parts/61482.dat": {
      "sha256": "305161d8b5c0ec55c79c21f6064d0f833f72f81ecaea2483a80cbfa561052be1",
      "bytes": 11187
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
    "parts/6179.dat": {
      "sha256": "33161941725eb78d5a6753490e5acdc185972d473598e5f5643e3c39ef30b561",
      "bytes": 816
    },
    "parts/6182.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/6182.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "d5d9e1ee8779c6473327ef5e4fce2f1e61b4ef98",
      "source_sha256": "57d783de53e0a7de81fc1935ea82a36453340057b66b42b310fb7a91293b096d",
      "sha256": "d7b866c318df9f0d699813cba14f5f0b4f98996a2d809d712c838ea09797328c",
      "bytes": 2546,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/6192.dat": {
      "sha256": "fc9efaac4c56daa9fe34091ce9f695e1407de3db7945a0a972b45e7df90786a9",
      "bytes": 313
    },
    "parts/6192a.dat": {
      "sha256": "573d06d6655d1c99c9536e4083ba5ac7d89eaf0a17d8539774b661cb55a93fb3",
      "bytes": 1844
    },
    "parts/6231.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/6231.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "4f829f3ae5397df9a96d231469569549df9dbcfc",
      "source_sha256": "4b78217c262c296782f5deace408b763154fe8961704279ad0ff69fa9772949e",
      "sha256": "6a511e8a2d59c331b04656b2e9538ada55e1294c94c6fca3ec5168645b2472cd",
      "bytes": 2346,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/6232.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/6232.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "e1cc19ce183f1bc9694d71b59ece7c06ffe324ea",
      "source_sha256": "df10b1debb5514f7fc58def8861bf9b57296ac7deacc0db8c4129c9e887cf2ea",
      "sha256": "9108f44252d8390e208986820f85497bf6320fca9caff9e5e8a9106aaf27cd93",
      "bytes": 1748,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/6233.dat": {
      "sha256": "9758ae41bb73a380b8be491efc15e6348348fbd9682bddf129e2187e26779458",
      "bytes": 2121
    },
    "parts/62361.dat": {
      "sha256": "c25e9afcd699ed0489b505d0fb386e6a741e3d2428ca8c7358ea8d0f5a3b3afd",
      "bytes": 22220
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
    "parts/6254.dat": {
      "sha256": "01bd8fa2d0cc8a61abb1290d8ccc18e88a248e5695441995da90c571b3e2503d",
      "bytes": 14662
    },
    "parts/6259.dat": {
      "sha256": "b5a9bdeaebe2ddff4e2286cac134c0178b01b355df5cc8918f8f394c75b6eb44",
      "bytes": 774
    },
    "parts/6266.dat": {
      "sha256": "a40747e540cd5848bc44ff3bb5a3c61cfa528014e1b1fea087689c5e2f5fb620",
      "bytes": 8219
    },
    "parts/62701.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/62701.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "c930974b30ae31d0282f24902d4114c42060fe40",
      "source_sha256": "c8f7ca66e7eb80b71e40898c66788fe7c928ac62ca4f88c0a0b0c493eeb6077a",
      "sha256": "a85b170964578f8f3972420b5d6f2823b02b92bcf27e7bdc2dccfb1080cc5cca",
      "bytes": 1517,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/64179.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/64179.dat",
      "archive_member": "ldraw/parts/64179.dat",
      "source_sha256": "7e8e131d8c7ca9387ba9f3b79d1fbd2f089c6d28b3f3b415bcbd1224e1629834",
      "sha256": "dbb5e3e6c4e5a2bbf0c3d95516a24857bed045687dd555762a8738ce1d802e2b",
      "bytes": 4241,
      "modification": "Official Git repository file downloaded at pinned commit; dependency references normalized to repository asset paths; geometry coordinates preserved.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905/ldraw"
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
    "parts/64390-03ad90cc81.dat": {
      "sha256": "c80c0abe1d119c9224dc8f62bbb4d8a8a84fb9020108bf2226ce2e2af12375c1",
      "bytes": 3084
    },
    "parts/64390.dat": {
      "sha256": "2aabb5c8d0522e907f9058955e5196f06e368f11eb89e83d107aef71e0034935",
      "bytes": 3153
    },
    "parts/64644.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/64644.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "a02a61abaf8554e7248b5bf6e790f619cf2d21f8",
      "source_sha256": "205e2597adb52875e4038022bb60f92568ae98fe944d409e0e96c925b5f60742",
      "sha256": "4288f16ff48749fa81c8414745e27634b67c7eadcf04f64176052c8f2cb25674",
      "bytes": 2078,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/64647.dat": {
      "sha256": "3e91b1acf28f8cfc87f820bdfdbc6debbf29f58f93db9f5bee5ad54d66b93a8d",
      "bytes": 662
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
    "parts/6536.dat": {
      "source": "https://github.com/ldraw-linux/ldraw-library/blob/master/ldraw/parts/6536.dat",
      "source_sha256": "a2fa16879ff87974c0164d605e404e194ade5d1368bd3f5e4911a63532babb2b",
      "sha256": "d4d261df27a8a3eb2e0ed574945ab6721c272090158efdaa5a1a611d67325cd7",
      "bytes": 3917,
      "modification": "Dependency paths normalized to the repository primitive layout; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
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
    "parts/6558.dat": {
      "source": "https://github.com/ldraw-linux/ldraw-library/blob/master/ldraw/parts/6558.dat",
      "source_sha256": "bfb280f72dbace5a21f9eeaf4879062e0d04f036d0060d2ef9ae9aa694e16a8b",
      "sha256": "d762284c67ec6c4e96bfe4f2b3d4aead9ba7750f26c337aedefdc6e12e2e0978",
      "bytes": 642,
      "modification": "Dependency paths normalized to the repository primitive layout; geometry coordinates unchanged.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/6577.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/6577.dat",
      "source_sha256": "fd7e3b88c162c47b856e774c46c8fb4d1d440ce821b5be79431ca41d3943af45",
      "sha256": "70e5734b34130e756932b3fdc5bbedf154ce3f080a044420ca7db03c8815a992",
      "bytes": 2694,
      "modification": "Dependency paths renamed to shared asset folders; geometry unchanged.",
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/6585.dat": {
      "sha256": "df9b4e40fa7f01d18c7a5d93a4a0c71c6f4cd77da5ced08ca5ad90d8c49f3f1c",
      "bytes": 1718
    },
    "parts/6587.dat": {
      "sha256": "edde7f063f2919f5d1343237581c5989f07e9eb3ff172adc8578a770f5d68f65",
      "bytes": 906
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
    "parts/67142.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/67142.dat",
      "source_sha256": "8abf444068922ae3592a4a1c08d8bb6798315487901580af146faa649862fb62",
      "sha256": "70f9a05f7b8cd42a21d81f298e53b4747a15b9abbb5fcf8393453c240bb69313",
      "bytes": 32058,
      "modification": "Official part references converted to shared assets/parts/subparts paths; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/68196.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/68196.dat",
      "source_sha256": "46aab59bd3a67c868ac87fb6c0fe7aebf8f1fb4eac8829d8af88a6987ea56233",
      "sha256": "46aab59bd3a67c868ac87fb6c0fe7aebf8f1fb4eac8829d8af88a6987ea56233",
      "bytes": 323,
      "modification": "Official geometry copied without modification.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/68211.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/68211.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "43430f20cd2bd1a83e85792c955fa60df58af072",
      "source_sha256": "d43e91a8e41fa52d0d9a05a088167a2060f1884bc563d03a63464feae0c9de97",
      "sha256": "c4e7c00cbe74d3e537858b879e191a647f79d54e7967bc91134a22d1b1b6ab9b",
      "bytes": 70811,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/7133.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/7133.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "8708e4385ac6e752c0aed8c5b17f931d8f2e6c8f",
      "source_sha256": "10bb2b47693b8a25ce15275817b81771335e38541ea7807d47f0bb29c025de2c",
      "sha256": "b622b58d99c1e3f06951af943e04985adcb18f9f88be290b985e4181238cb0fc",
      "bytes": 1638,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Rene Rechthaler [Blechtaler]",
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
    "parts/73983.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/73983.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "21746c9a641b997ecc507641bb2c0ae7b504c0fd",
      "source_sha256": "662b7910b88e16ac7ad2a1f7d2cef3435cbf28b7a0b11bd35830a0959f0dee2f",
      "sha256": "e49853508e3996a4cc1351e96f96a00813ca8c50883997986e29ff0125a7b5fc",
      "bytes": 610,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/75902p04.dat": {
      "sha256": "6e3387fd311efb75cacff60560c0dede5a7912d8a46f9449e3edda8636f6af22",
      "bytes": 45786
    },
    "parts/75937.dat": {
      "sha256": "6ca7ca62cf51cc85acb1d128ea3ef7c96c0cfd57cbab2d2b4ba59c7fc28f9f96",
      "bytes": 1750
    },
    "parts/76764.dat": {
      "sha256": "b8af074dcd2b098ecac2f00bcce4084a4bb30adcc8993a5c25392d7a2bac2642",
      "bytes": 20858
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
    "parts/79757.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/79757.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "fcc301527d56f4b4fd3ae25347be37d3e8647d48",
      "source_sha256": "5531f04194ae8d0afc266541495182da5d944d4148ece9df765b8ab7047941dd",
      "sha256": "50718d6da9dc196f408127810c5a9cc235643774b8a2cc08b47585288f6babab",
      "bytes": 5347,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
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
    "parts/80796.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/80796.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "d3aed68df03dba7cbb296f16d2645680a3b2b76b",
      "source_sha256": "c72842ab76afeafe0ce00cebcd20fb82ba208d514a0fdf65c9c19d9197f6143b",
      "sha256": "09dad2573e43427f2b9c607cf2b5285dd61710e91db7cd5c1fa326e1976d02c2",
      "bytes": 384,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/85080.dat": {
      "sha256": "18e632cf4dfff4630a6f43b798dfc0adea52329454d040db5ac2b313efc53602",
      "bytes": 6762
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
    "parts/85863.dat": {
      "sha256": "ec0719dcf277b4a043188c77ad562a8d1771e7479c1a64ab93b4db20f2518bb3",
      "bytes": 1338
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
    "parts/85975.dat": {
      "sha256": "b009edb7ec84a148aa4ab47fddb67e50dd0a1de5e1586357d1ccb8d9acb66c86",
      "bytes": 7349
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
    "parts/86210.dat": {
      "sha256": "0dc955f7a279010ab4082c633316b6d7687a4d28ce899489460997e3e695f508",
      "bytes": 1194
    },
    "parts/86876.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/86876.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "ed26a7c2aeffb1c3b0bc6721c7f32358fed51ec2",
      "source_sha256": "654b7cd52265e077e0367fcb5c1ae8c8c8f7b1261361a49d9257ea71aca365b5",
      "sha256": "0810597075ca7ccb51a7386eba3822087cf7423e1700614c59cc8705138c2416",
      "bytes": 1078,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
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
    "parts/87081.dat": {
      "sha256": "c0d669fb2cbe8b22fa46f883ff31dfb9a8d1fb66a8a3833d687d996d90e58bee",
      "bytes": 2013
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
    "parts/87421.dat": {
      "sha256": "df61e35f626b3f197bad242df1028d8f4f158f1ac4375b2070336cd76fc0ae78",
      "bytes": 9017
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
    "parts/87601.dat": {
      "sha256": "88ff9dcddcb3e2ec7741c022c1ac933452856360273705c4c64b70a305a21ea7",
      "bytes": 12990
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
    "parts/87618.dat": {
      "sha256": "05e7b363828a93cd6889b25ac45244062d0e082716985e561d4152e6c2527172",
      "bytes": 2346
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
    "parts/87693.dat": {
      "sha256": "0afcd6077f834a2519feb21ca19d1b3def48b494e5af9cf62aa5465b686c4c52",
      "bytes": 4412
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
    "parts/87926.dat": {
      "sha256": "637a9ec9fac043622f1cab17142a56ef3b2aa601c95aa3486847770b92d70ffd",
      "bytes": 3896
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
    "parts/88072.dat": {
      "sha256": "9c75cc82b53e6b475d19f7f1c346e06be4396036aa9a6862a6e7620f734cc56a",
      "bytes": 1206
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
    "parts/88646.dat": {
      "sha256": "6b7be6c23fe3b8722a93aa55ade1458e30e403a79ab2d81f8629637b1e952b5f",
      "bytes": 596
    },
    "parts/89522.dat": {
      "sha256": "cea292b2b24a0627f9fe4f1dd80fc314b82793878d18f0712cd6e4460226de38",
      "bytes": 32554
    },
    "parts/89523.dat": {
      "sha256": "ae6e9de4807028fb126f3e89c82d2a1eb7ba4c34fbd2e513105cb395db472b1c",
      "bytes": 1759
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
    "parts/90195.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/90195.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "030f6a44252486e7d50952e40654c0f2b10a8f4c",
      "source_sha256": "1a959fb40b8f15d43e4f081f2bf49bf1cfd4ab3a0d6af0756d4d4e0b54ae4488",
      "sha256": "56294878dcdb4c4c0111266af55a2b85eee1651632f98f68270cba25fdac111e",
      "bytes": 6526,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/90398.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/90398.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "bc31347a1a41f75742e9e5b73e34f0542e60248c",
      "source_sha256": "02b70e612e81a94aaacf0e3a9158df3a880c156820dbcc8204764138644de527",
      "sha256": "0c5efa2dec0571053e994c6fd38cef5e2ece091226af0c25f3a39418d90c827f",
      "bytes": 2131,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/90540.dat": {
      "sha256": "dafa72be79077422ea31f6439b2d07bc0e3acfd0d5bce3e50c6f4d93d0390d7b",
      "bytes": 2957
    },
    "parts/91405.dat": {
      "sha256": "c95c9d71e130ec37097d98340b960fc921e7be2b0c4e92079a93130e4c5aabd3",
      "bytes": 12915
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
    "parts/92262.dat": {
      "sha256": "567791161a1658d458492549f417c81044b4deebea493e63fdec2a1adcfe7c0d",
      "bytes": 366
    },
    "parts/92263.dat": {
      "sha256": "c140067770b91f96e83e48e0dbd00baa159ed7d5ba25e7aef5c6d860384addec",
      "bytes": 370
    },
    "parts/92280.dat": {
      "sha256": "079cff251c0791b854d25e615cc6af79683321ce62c4dc82d8f5546532a2797f",
      "bytes": 2125
    },
    "parts/92409.dat": {
      "sha256": "3c9597c8f9f010246b684f0e4f8bc2ca4750f79f29801bf89b5193611592d37b",
      "bytes": 4381
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
    "parts/92593.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/92593.dat",
      "source_sha256": "aff18eb900078f523e7ebed7bfe28e1c334e9b5b54dcc15ad92f725d71e75629",
      "sha256": "91205ea9f3e4ff5bc744ff37441b306885e9ad08db991a427cd1de51ba859b6b",
      "bytes": 809,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/92907.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/92907.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "d792baa87dcb8e874b5dae9aa2f5c3c1e7761483",
      "source_sha256": "aa8dd6af985cad0a80ec9c326ca49e94e00d57463f76fc407096b7caca8cbbe6",
      "sha256": "13d547db7543dc9a4b0256cffb8ed1e5764167ba5dad2365bcb307193fb3b462",
      "bytes": 11201,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/92947.dat": {
      "sha256": "ae13d3ea468f7d74b4ec57737b759e189ec4680c78685fabc0551b4c56d68514",
      "bytes": 1678
    },
    "parts/92950.dat": {
      "sha256": "a689b2d58612bd6f9c381e52c6113a6d068c3cb9fbb1b1e6aba06d64964cd904",
      "bytes": 1186
    },
    "parts/93095.dat": {
      "sha256": "c5ce09a3f4d1db9205c286e8287288ca7b8a3ba1875b79ec9d4beef576a227f9",
      "bytes": 1969
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
    "parts/93550.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/93550.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "a37688fa89d4a650459495001597c1460302c99e",
      "source_sha256": "4c845c063a8f9cc87f8a81eb879f0638a23c8e8c52dcf5418f18122849d032a4",
      "sha256": "68c05729d58d930ff536492d16a1c6e58a90463300a5da8740dce6ebb0b4e576",
      "bytes": 2054,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/93594.dat": {
      "sha256": "25f1ecbec0fbeaf4172eced8bd7e7406983b08772d7233ab7828fa3548e623cd",
      "bytes": 3069
    },
    "parts/93609.dat": {
      "sha256": "7d65ce5d9876508509f7a474ea5991d975cc6bf8bd27a16586f9bb4422c22d0b",
      "bytes": 29953
    },
    "parts/94161.dat": {
      "sha256": "9a7e10f44c42c3b7acf3e0dbbd1d4ea9df1cb62a9d456180ba9c2c631bd0772a",
      "bytes": 22085
    },
    "parts/95228.dat": {
      "sha256": "7338ae94ef82ffb4b05b870edf34bb5e951a9c05948295a4d4029b1c814702e9",
      "bytes": 427
    },
    "parts/95344.dat": {
      "sha256": "7c4dcd0947604e4957c47951ddc342f57cddbf412e30c954e7fddaa6c5c75a51",
      "bytes": 2825
    },
    "parts/95820.dat": {
      "sha256": "7846cba2949e09ccfd7c0b4c7ab5645d300281d600c4c4a1f1017150036d2131",
      "bytes": 627
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
    "parts/98138p85.dat": {
      "sha256": "f195dc3c381d93522b69e9051da96ce7e143f36bf0219178ea7925648410eb42",
      "bytes": 46718
    },
    "parts/98138p8b.dat": {
      "sha256": "ad2371865929d5f341ef0cbb7eafba08a2c92724a9cfec6d7e2ea86012aa4f70",
      "bytes": 603
    },
    "parts/98281.dat": {
      "sha256": "ad56dc1e22def83f1cb5bbb284f631ef8732b2f2162660b55fa1a483379472b4",
      "bytes": 4237
    },
    "parts/98283.dat": {
      "sha256": "c8f9d89a2996dbff76fe26ad92c5f00b6944562c591312176a4926d7fc3b25fe",
      "bytes": 4111
    },
    "parts/98313-027c3f0ff6.dat": {
      "sha256": "506f6602c78fba549d317d804fda7f683e1d6715780d6b8b766cb9b2999eaf68",
      "bytes": 6991
    },
    "parts/98313.dat": {
      "sha256": "3217f7f69727f00c780f2582e5aff74ae71d6af18be05ef4acf87dfeb2f69764",
      "bytes": 7044
    },
    "parts/98374.dat": {
      "sha256": "a4ab42000d0d5d9e14941a9dd7aa7c811a5cd3c4df566efd3dbfad8b60197e79",
      "bytes": 4094
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
    "parts/99206.dat": {
      "sha256": "ab20a6a88568471bcd561df75ab5b35acf3e8043934856fc2a11f46a1a445446",
      "bytes": 841
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
    "parts/subparts/10172s01.dat": {
      "sha256": "c054cb101e8ea56745bb5a369bceae026f2f73cf73e274e1e92a20a168ec4496",
      "bytes": 33148
    },
    "parts/subparts/10172s02.dat": {
      "sha256": "5135886b7c7ead6c59933f88acde4a445a9b97d504dc8efd460efe4fce98a844",
      "bytes": 12160
    },
    "parts/subparts/10288s01.dat": {
      "sha256": "af4818e948fece11fd332fb61b736cc4aef0d7300f2552a91719421bc4c905d4",
      "bytes": 5512
    },
    "parts/subparts/11203s01.dat": {
      "sha256": "2f548a0f38cb96b1ef46b95e9658fb0756e3fa5bce12d27d81d15d317ff2db90",
      "bytes": 3731
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
    "parts/subparts/11609s01.dat": {
      "sha256": "c3157cbf17c126ad8dd5c467dbfd90965381db16f91913fef5eded71d7cae7dd",
      "bytes": 4461
    },
    "parts/subparts/11833s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/11833s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "bf7d1ea1378dad2368eb5bc07631aa397e3a09eb",
      "source_sha256": "017a96e50f020da21f178c181cbca6ce857caabcde2b60c44a843856d146ea1b",
      "sha256": "d918d94833f6ccf42e17e434a836c77b12a40726bca606de9009e852c3cd506e",
      "bytes": 3658,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/subparts/14301k01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14301k01.dat",
      "source_sha256": "f5861c21b1b813bda1b063f5d74949fb8343ec4bb10f3eaa73a1d771611088da",
      "sha256": "e2d27135b75d1485ca30af2a950641d2b05cdf5a91a193957676cc050e4484d3",
      "bytes": 1197,
      "modification": "Official geometry retained; internal part/primitive references converted to shared asset paths; coordinates and surfaces unchanged.",
      "author": "Sylvain Sauvage [SLS]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/14301k02.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14301k02.dat",
      "source_sha256": "8314ec757c8a0ccf7514e586edc3709881e8bdd78a02b722f1247cc15336e9e8",
      "sha256": "7538e7f3829eba954794e5fa9415d28b8372196d0dbcacdcbe420d8d603932fc",
      "bytes": 886,
      "modification": "Official geometry retained; internal part/primitive references converted to shared asset paths; coordinates and surfaces unchanged.",
      "author": "Sylvain Sauvage [SLS]",
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
    "parts/subparts/14718s01.dat": {
      "sha256": "336de1466312a99b223f12e1d25e63e17767478fb8cbb66c349757c003ebfee1",
      "bytes": 2612
    },
    "parts/subparts/14719s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/14719s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "52fd70114446a8d0396d7055c0a546f315ad619d",
      "source_sha256": "cb177629961e1ed8f941ee8984a8e0068b9bce3c4638c70db58fe4752e3e2657",
      "sha256": "a03f633b40280e25cf2c9e490b2cd544d9d12f9afc6f13fdae585561653ffad3",
      "bytes": 1498,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
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
    "parts/subparts/15100s01.dat": {
      "sha256": "cf722145b9f190dadac9773238a9bc70bb0e26805354dfb511dd934bf563ab12",
      "bytes": 1775
    },
    "parts/subparts/15470s01.dat": {
      "sha256": "30429c648285a686ea8ef8bb6322b8fb60d14873a43a2d327fe398571f02c149",
      "bytes": 4857
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
    "parts/subparts/15706s01.dat": {
      "sha256": "0003ff9a1d59e6e1eecc7b52b4efb8d6551fd75c150c7aca74c3e7b6b0e07a12",
      "bytes": 1299
    },
    "parts/subparts/17485s01.dat": {
      "sha256": "fd51a1d923e16b6d98fed7c467e76cff39cfb1d89cbccc14df8bc231cc30fbd1",
      "bytes": 10949
    },
    "parts/subparts/17485s02.dat": {
      "sha256": "6b21c63e0df1e3a7b5fa2bf98339347b250eb43cad5a9ee56b919a3c9cb516e5",
      "bytes": 2187
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
    "parts/subparts/1751s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/1751s01.dat",
      "sha256": "86c6f741ca2e9775f6a6bcd650befb77208197f1375cdc954897455dba674234",
      "bytes": 812,
      "modification": "Normalized references, original author/license headers retained."
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
    "parts/subparts/18909s01.dat": {
      "sha256": "9398d58a0beaad88ff24f99a86172ba28c30c7b39d727d4c71c1203d0a38987f",
      "bytes": 6436
    },
    "parts/subparts/18920s01.dat": {
      "sha256": "8419951bd272dfdff3f6de1ca385db5330105c24d1e1301d6fba37b7ab4393be",
      "bytes": 18307
    },
    "parts/subparts/20310s01-7dfb73cc83.dat": {
      "sha256": "803174f4dc748667d1fa0644d67013512a1b92bba07636d11aa692186825d710",
      "bytes": 25038
    },
    "parts/subparts/20310s01.dat": {
      "sha256": "a1199a457e0cf7f477bf46e0a07dc601803ebd1263e1a93a93098d2ac773cdef",
      "bytes": 22929
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
    "parts/subparts/22888s01.dat": {
      "sha256": "91a1bc5db283a2af20a1a708b2aa2bcd8346721adac3864ab3465bf22b370873",
      "bytes": 2400
    },
    "parts/subparts/22888s02.dat": {
      "sha256": "1dc489f643d205c104b9fb11f7b2aa2e6cf188327b0c6bc9ec68f4f463135691",
      "bytes": 2770
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
    "parts/subparts/23986s01-d309274c11.dat": {
      "sha256": "724001b4f838681a7dd4b9605120519dea09da9b999e49be50c88d38f4c8b40d",
      "bytes": 30681
    },
    "parts/subparts/23986s01.dat": {
      "sha256": "2faec1ee2ebfc92472a49ad0165cf4ec39ccc1888705f7bd03dcf272ef1a968a",
      "bytes": 29951
    },
    "parts/subparts/24093s01.dat": {
      "sha256": "23a90a70224bb24996138cdb90300f07a7251033970d0148ac1063928c12275a",
      "bytes": 4970
    },
    "parts/subparts/24093s02.dat": {
      "sha256": "8807a9626680bdb53cbd7e45fa0e4347fc47b07b85a48acb3e20dbc19b581f5a",
      "bytes": 3451
    },
    "parts/subparts/24246s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/24246s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "77b6e204094acbe51b3d55fe5182dd98b6f51c5a",
      "source_sha256": "f0e945a2950ce1689d73db589540ff8e0b711a02105a42aa75a67a4122eb2aea",
      "sha256": "cafff5697260995eb148485cb0835930c7e44bd9a694002813b87823f3914807",
      "bytes": 671,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/24246s02.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/24246s02.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "9d0a15230c38bb897b9fa4b9a068facbfe4658ed",
      "source_sha256": "8f9ec4b434d7497a5479a73ba4db05a245323120620a4d189471a2593c0049a2",
      "sha256": "f8a37997c6cb79cd97616898ad7fb77132024a54703f1496e7731c2af960bde1",
      "bytes": 1011,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "parts/subparts/24324s01.dat": {
      "sha256": "df3bbfbfd00d7261512571037ecd6123dfed5564d38c53ceaa971bb6b8b38977",
      "bytes": 3127
    },
    "parts/subparts/24482s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/24482s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "e560e5934e1de4eb67cba8490a5ed1515a9867ce",
      "source_sha256": "c99a9e41dcafd16469cdce6e32faacdf90987ffdb23b105eb1cc4b4c9673e0fd",
      "sha256": "cccb32889cba36f74a82b2a7439e942dd3e0dd1537bbe5aa9c062cf556c735fd",
      "bytes": 5348,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/2454bs01-389ed99644.dat": {
      "sha256": "9dd1723b2cc2594db9afc623ec15c71a26173ab53da25889d3659eee73c5d3ee",
      "bytes": 1322
    },
    "parts/subparts/2454bs01.dat": {
      "sha256": "50e7128a8c484c6d53d3c0a15a51e2d1d4f92a27be15354a5f9662db47b636d7",
      "bytes": 1000
    },
    "parts/subparts/2454s01.dat": {
      "sha256": "b6c802a44303285d352bcdfec5f7fb0080610b5e6a93465ff3abf4c04e8aebf1",
      "bytes": 2867
    },
    "parts/subparts/2454s02-ce18703f98.dat": {
      "sha256": "e289d39741d270fff88118973a11c1ac31262d87ab6bddecaac337d6359d8d7e",
      "bytes": 1363
    },
    "parts/subparts/2454s02.dat": {
      "sha256": "e5ca698ade4a8ccd103d73611447cb0a1dbb07fa42611a3f8183732869674907",
      "bytes": 710
    },
    "parts/subparts/24593s01.dat": {
      "sha256": "97ce81037eafc13adb715ba7de14bef52274bb482460d7997736a16ad987182f",
      "bytes": 11167
    },
    "parts/subparts/2465s01.dat": {
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905",
      "archive_member": "ldraw/parts/s/2465s01.dat",
      "source_sha256": "192c3ea8ba73dbd62700f915a762249692886f852b466dc3aa42675727e1921a",
      "sha256": "192c3ea8ba73dbd62700f915a762249692886f852b466dc3aa42675727e1921a",
      "bytes": 2344,
      "modification": "No geometry changes; recursively referenced by parts/2465.dat.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/24866s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/24866s01.dat",
      "sha256": "d6bcd3355e0533f1b976dd029377d7f3b5876f6c0985a1216a7957cf21fa44ea",
      "bytes": 15965,
      "modification": "Normalized dependency paths; original geometry/author/license headers retained."
    },
    "parts/subparts/2489s01.dat": {
      "sha256": "0abbca694074a7c32a1647625112fc8c3fc37f47a0943cc91014100cc478986c",
      "bytes": 1391
    },
    "parts/subparts/25264s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/25264s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "974f23cdb952c29d215e2262d4719208d426bb2e",
      "source_sha256": "ff6934c3a5ef1fc071a02a6ef443be08ffd1480f0e10ed472399b0d776044d77",
      "sha256": "393dc11d940d3bae72628398d0c2184094ea3f2cfe74f5a9fe025e255dff60ad",
      "bytes": 8514,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/subparts/2551s01-3147914826.dat": {
      "sha256": "9e0db81455a5592c69fc043a08b5b1f89a8152f8928d12b4fac4f8f5299db754",
      "bytes": 286272
    },
    "parts/subparts/2551s01.dat": {
      "sha256": "74d052cc8178aec9bc9df1cfb235a19a18c98afe98dd294d5a91748619ff83db",
      "bytes": 214517
    },
    "parts/subparts/2566s01.dat": {
      "sha256": "ab180d602e707770eb230d8e479f22716b2f91b761b5c12164d12198dd2bd032",
      "bytes": 3101
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
    "parts/subparts/27507s01.dat": {
      "sha256": "26845e3026ebdc12b8749eb2455242b72321b571dd6cff96d5ef58fa95a1f4fb",
      "bytes": 18858
    },
    "parts/subparts/27925s01.dat": {
      "sha256": "90bd777e7dbd4b8cab8bfd880222c328f3d798f2c0a1e4ecce1f30545b8fe309",
      "bytes": 12263
    },
    "parts/subparts/2815s01.dat": {
      "sha256": "b63dd189553ef548df69214df47d16a3d8ce07a817610cce27a15548273d0786",
      "bytes": 2627
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
    "parts/subparts/28621s01-69822164f9.dat": {
      "sha256": "a8a84ec8e5fa2418ff90525fe7100e49f1c3bcce943e8477f25869040109b596",
      "bytes": 856
    },
    "parts/subparts/28621s01.dat": {
      "sha256": "73a9cf64a87c98f58df393bb5f1f9eb1b495bed33229ca1366edc216d4a54b2d",
      "bytes": 1040
    },
    "parts/subparts/29111s01.dat": {
      "sha256": "3b81381f95774fb4ed4d3058f74b29e7966a685789902c857151577cdb0de680",
      "bytes": 126320
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
    "parts/subparts/3007s01.dat": {
      "sha256": "d83854bf91b4e4d27e1b4d0af4445455f7f93c1b5cf50752aa77b9530fe2c3c0",
      "bytes": 1495
    },
    "parts/subparts/3008s01.dat": {
      "sha256": "b4c851180243ce7b13daafbb63ea4bfc4bbcab42a452d58b6e473cdded0dc391",
      "bytes": 1053
    },
    "parts/subparts/3009s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3009s01.dat",
      "source_sha256": "889704b3896146872fdfd6b0f759ec00c90495d94cdd4bb1bed07875024efc47",
      "sha256": "501cb5754ef48dfea41e5701d5b45ce731908af98cc7837e123ae414f78b0f2c",
      "bytes": 1753,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": "James Jessiman",
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
    "parts/subparts/30151s01.dat": {
      "sha256": "3f9fe541bdfb4741be09f3e86f9e6d7b97d6c22346ed09abb0350b344c41dfae",
      "bytes": 2590
    },
    "parts/subparts/30151s02.dat": {
      "sha256": "5fd30329c61b359cadd6ae2cca4dec076ca55c4616c34d2d6136efa5e38f06d7",
      "bytes": 1589
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
    "parts/subparts/30350bs01.dat": {
      "sha256": "c7f6bef89956d67954457ddfb7ef983f0a5b3fbdb32830cff58f4743789c8d58",
      "bytes": 1104
    },
    "parts/subparts/30355s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/30355s01.dat",
      "source_sha256": "a0e80395622b9a46b7266aa374cb65623bba3b8d5d1c1cc7c30870d43813e519",
      "sha256": "4d607efca33a830d9f0b7f2bd87009573a6b1a1cd72a55338adf77f660e9ecd2",
      "bytes": 8989,
      "modification": "Official part references converted to shared assets/parts/subparts paths; geometry coordinates unchanged.",
      "author": "Guy Vivan [guyvivan]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/subparts/30364s01.dat": {
      "sha256": "d715ff0cc306af6ddb31da4b0560c418dd89f545f781f8f52c05f8bcc8288cc8",
      "bytes": 1644
    },
    "parts/subparts/30367cs01.dat": {
      "sha256": "481026167f06ffaf64bee353182f2217270465ca348ebe0e95dc303b6c28e1d5",
      "bytes": 1249
    },
    "parts/subparts/30367s01.dat": {
      "sha256": "bc91f621b9367074136acb7fad5b88311ec84932c28593ea0c65e5f37b55de29",
      "bytes": 3005
    },
    "parts/subparts/3037s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/3037s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "92a4b7442494e145f8b1b0224f8b1a89da9c794e",
      "source_sha256": "2f508bdabed2f88761f033ee1e319dd05250c4d7f3cb25e35f22fb368ed05a96",
      "sha256": "359aefcadf598f1d0601b9fffb0e795e25bea6605ada3cb7a2ea89a07e76ca12",
      "bytes": 4482,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/30386s01.dat": {
      "sha256": "a3f265cbe7ae2124dca4143194c2337c0beb2cf4f0ef4e39b5b362bb8f060856",
      "bytes": 1944
    },
    "parts/subparts/3038s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/3038s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "56c488d5c7fb4c393a1c0358da65ae99cce69c5f",
      "source_sha256": "c12260fca55218d2c93b0ee93793aa2c08fbc9acd3617b9278c616b204b75596",
      "sha256": "20f5628509e011a5621e53458aeca20d76fb467f0aaf988724c9f2a362e4c1f8",
      "bytes": 3563,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Mark Chittenden [mdublade]",
      "license": "Licensed under CC BY 2.0 and CC BY 4.0 : see CAreadme.txt"
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
    "parts/subparts/30552s01.dat": {
      "sha256": "2f8e2c1b376cfeeddad5e04bcd4e92356c4a5a77e37334cd9d4eb60abc641113",
      "bytes": 5649
    },
    "parts/subparts/30562s01.dat": {
      "sha256": "5557b23075a9b759474d233185e072105295c64b4b0f64f3460a7b52b2cd0a84",
      "bytes": 18686
    },
    "parts/subparts/30565s01.dat": {
      "sha256": "c088837036ab522e2bc24517e84cf521c3a8954061a8e74b6118d559ec86821f",
      "bytes": 2897
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
    "parts/subparts/3065s01.dat": {
      "sha256": "9bfd704cbfde24387a073a1c55c2a69c188faa28a9c2e237e573c3a264a5a830",
      "bytes": 697
    },
    "parts/subparts/3068as01.dat": {
      "sha256": "0e247872926d41bfe73fd620329aa3fdbf5e502c5191349ab4eccbee8960645f",
      "bytes": 832
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
    "parts/subparts/3069bs01.dat": {
      "sha256": "8c202bddd3ea4fc113eee802daa1d6a942de65d2249cec22ea519732df855e5c",
      "bytes": 749
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
    "parts/subparts/32124s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/32124s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "c1a9ac4f584a6b495fc5f84250e3fe2f69cb7f09",
      "source_sha256": "1d7296ecc09e87b7702b065b540623eb1d07fbf68b17b2edd9a45da4dc424f67",
      "sha256": "03df2d9f0a753407f7ebe1d9ade381f0ef04ef1a94357028fcf0edc338440854",
      "bytes": 1949,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Rene Rechthaler [Blechtaler]",
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
    "parts/subparts/3245cs01.dat": {
      "sha256": "6daf0061cd094c200dd22ae07ddccad5adb05393e80003ac4e6d51b926492010",
      "bytes": 1249
    },
    "parts/subparts/32474s01.dat": {
      "sha256": "d14834ce4d5f562c7c95634a15c28d73b23a1979bf6bd4bb0ab60c4b4d0559de",
      "bytes": 4293
    },
    "parts/subparts/32474s02.dat": {
      "sha256": "016b72a04f03c28be75332c406fd2cb5ebb9ec748cd2dc0c57b8f33e31effcb4",
      "bytes": 3253
    },
    "parts/subparts/32498s01.dat": {
      "sha256": "292e2d80a98fdae8002d575234d7e478d4e64c4ac48eead241fe696d64c30e96",
      "bytes": 7578
    },
    "parts/subparts/32498s02.dat": {
      "sha256": "2a1098ad2c81b9a93a400acb688de291819d22b4b64fbe16c905df0be90dfd1d",
      "bytes": 3058
    },
    "parts/subparts/32531s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/32531s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "593cd62d5fa40b9ea80175f3496bac7a11b2a638",
      "source_sha256": "7564adbf21d9de9c70058f0d4ef1eccfa7025cb6caefedb25d5da38ea9f8d212",
      "sha256": "bc9a2fc54d489eb6c6a8e8ac078d01bef7704f1aea1c7d6946aea91c2b4751ba",
      "bytes": 12261,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/32532s02.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/32532s02.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "60f8955350c3abfec2b5e27a645101d221b32b22",
      "source_sha256": "0b35bbd1b7b33d88cc68672fe1ef5faf5045bd37753846bdc1301d34126a8871",
      "sha256": "1b76a6bfde09c53f6339eb5cbab446537c377d60179b8f7ab60b67a4a446a55d",
      "bytes": 1617,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
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
    "parts/subparts/33057s01.dat": {
      "sha256": "1f1048476888c908d449a3feadece3afa1898e6ca2881a91254c8c12e8a0afb4",
      "bytes": 41904
    },
    "parts/subparts/33299s01-bc94cbefc9.dat": {
      "sha256": "71ac6350c397a1551f3be0c29d05c1db9e28dc74962ddad6c5e886944c4245f6",
      "bytes": 11776
    },
    "parts/subparts/33299s01.dat": {
      "sha256": "bb545b88034fdc453710ef92269dbc398cbaafa29d60df433e4f563929a91dc2",
      "bytes": 11075
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
    "parts/subparts/35394p00s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/35394p00s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "6a9098f6594a8bb495222db9e5821304bd9cc558",
      "source_sha256": "fe7618ac5f8378762c94167f9cb396d57d3033d2c2012400eddec6138cdb07fc",
      "sha256": "82b4d55e08f6b4e59cd76d2038d08fb8a18a0ede219972460641ab02ff3fea0c",
      "bytes": 37034,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Marc Giraudet [Mad_Marc]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/35394s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/35394s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "2566f3b4116bd71a1db52720e9ded8bea4f447ca",
      "source_sha256": "46ce6e3da5e444ef9cbf38b4d6b81452d17ddf5f034ec00bafa75ebcd59922ab",
      "sha256": "c7db3df5b4ebdd85bfdcd4ed85b58ae98fefaddb3977750f635f8c3758d921b9",
      "bytes": 2460,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/35442s01.dat": {
      "sha256": "bd661b16c21ff8570e8fbb1b222b60c846ab883e42f8bc31e538e3a79c2b105e",
      "bytes": 538
    },
    "parts/subparts/35442s02.dat": {
      "sha256": "70941f91f292f30df4e7c18174d06cc52ce2e747e23c4a5174b21bb812fe525b",
      "bytes": 4469
    },
    "parts/subparts/35442s03.dat": {
      "sha256": "db10bdc45101e7269b29be4f089f6af74f85d97d71d30c0d80c37e58c610e552",
      "bytes": 2144
    },
    "parts/subparts/35443s01.dat": {
      "sha256": "3a9ca706274eb27957fc290211935d98bce874c844007e60773e22f3bf803b85",
      "bytes": 538
    },
    "parts/subparts/35443s02.dat": {
      "sha256": "a71864d2d2806e2a11a64fdca4a190e90b03768828d79562343fa2a1e0db21d0",
      "bytes": 7089
    },
    "parts/subparts/35485s01.dat": {
      "sha256": "a69dab9b3831e3cbb13dccc8ce402474c72e0c120467efa67ada1db6e1bbcab3",
      "bytes": 14903
    },
    "parts/subparts/35563s01.dat": {
      "sha256": "d3974b39ab7afb6b245fa9edc13b3543fd3cc7ea9c184be0a16acf0a9da42b6e",
      "bytes": 43762
    },
    "parts/subparts/35787s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/35787s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "784cf7820afaf0c69654ff45b29c486bc7ef14dd",
      "source_sha256": "11b63d550c632afaa6b0178c233ae8d87a624bad04ce90d86d22702af1107729",
      "sha256": "95a50ae943d2d9d0bcd6cd63e599bfcab6ada786169920ebf91348f59ae10b84",
      "bytes": 2198,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/subparts/3626cs01.dat": {
      "sha256": "0a5ec8a19654d67568a75eba8f6540a43de8c12c8cc8d7f7cf5f3e72164953ae",
      "bytes": 668
    },
    "parts/subparts/3626cs02.dat": {
      "sha256": "278a9ee2f921a9a6b5f317f6d823531845569f05585435b34764798000c5657f",
      "bytes": 626
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
    "parts/subparts/3678bs01.dat": {
      "sha256": "a16dc4f5cb7a81dcca6ba3574321808333651aa576fbb39a2b9946211416d887",
      "bytes": 2808
    },
    "parts/subparts/3680s01.dat": {
      "sha256": "15e2676bb52ec59711117f4cd017abad61f640426a68507bee44dea63e9aa018",
      "bytes": 4534
    },
    "parts/subparts/3684s01.dat": {
      "sha256": "e3e94cb98c5f9d839a62705296cd07a2e84db05f04cff4efbd3ef2b3136e5434",
      "bytes": 2687
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
    "parts/subparts/37695s01-553590374d.dat": {
      "sha256": "25d94845e6bd7fb283de03d6b03805e3c177248d8bc0d7878feff9fd52bcdab7",
      "bytes": 51487
    },
    "parts/subparts/37695s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/37695s01.dat",
      "source_sha256": "93faae8f7cff333fa15f0486b4cdf9d574ddf97548e75a689166d0cd0557b905",
      "sha256": "3b27c96c71a021646eb77a96fc0ac8819cfd6f63204c9c2e899b6d5af29d8157",
      "bytes": 51436,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3836s01.dat": {
      "sha256": "504c033d1abad9c5e4d239807b10ee9ba798cdd2ce6aa732ef58789357aa0002",
      "bytes": 6671
    },
    "parts/subparts/38585s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/38585s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "04e453a47be44c0beb33723e5e971dafab0990fe",
      "source_sha256": "256438047eebfabdf014487943eab8b5f3b0bbf4af69fffbcb7aee4b7316db54",
      "sha256": "788038cc308ec29ae8c15b318f2c17a418f30eedca33622e2242e09ea3d8ddbf",
      "bytes": 1013,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3899s01.dat": {
      "sha256": "9ec5fdd67e6ac6f96732a5c3689290107137ee21d540d30513b1d7118612e723",
      "bytes": 3003
    },
    "parts/subparts/3938s01.dat": {
      "sha256": "7a451848b3a116ae0c8d33f7a5e13e9aa29872b4c9b354943a20116a797d496f",
      "bytes": 1987
    },
    "parts/subparts/3940s01.dat": {
      "sha256": "ff9aade0ff30aa6dba4830bcbc512e5b14678da670c6468343b21f131c31ccf2",
      "bytes": 1617
    },
    "parts/subparts/3940s02.dat": {
      "sha256": "1bf1f087c94fdf43f8f02df29c23319106ab2f64a96a1f67f118e9a9fbbb1975",
      "bytes": 848
    },
    "parts/subparts/3940s03.dat": {
      "sha256": "5bb8305c9ee0dd08d58dd847d5258680b4af7c3cbf3db215da1a38d5f87b3edc",
      "bytes": 1561
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
    "parts/subparts/3960s02.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/3960s02.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "2abb6f2b2ce7d11137964fe502bb14caa87e8592",
      "source_sha256": "ba0fc9b3d096e0e44c35777d46dc0b10b0941d0ea96491451c869a7bcfe7a86c",
      "sha256": "05feeaf166bd997cca15be579f9e2d32887c74d0e2d8d28712edb0ba92d1b006",
      "bytes": 1976,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Franklin W. Cain [fwcain]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3960s03.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/3960s03.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "d92c348994399ff246499a02486dfce589de6f8f",
      "source_sha256": "a04a2c615a4db183bb62cacf8be101a0e9a71c79c95a06dc8a6955b374658f43",
      "sha256": "e5d894e1570f8c2527320900c7d26e617aad110ae668022901a5f20c2a650be6",
      "bytes": 1389,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3960s04.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/3960s04.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "303cc3e419d3ce8ac889132101bc66a0da8a6293",
      "source_sha256": "855e0607c20db6b57cc3a0cd4dbc721b3c4782f095ee9500022d0fc9d9abbee4",
      "sha256": "e5ff43b4c34b868b9c4057e29a712d6a2a52829f4ba1a708032a455e4301941d",
      "bytes": 1398,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/3960s05.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/3960s05.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "8c55e4c8f0e6b853bb00d49471b7f322d8f7df21",
      "source_sha256": "7999eba14a8122b4b428c6fa2d8a5acb4a405dd21ce498b17da0d85424cd1543",
      "sha256": "647f540d1ab966bcd5f60e3c409c7bfbc8ba6ec60af2567975577fe433bc405b",
      "bytes": 26990,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/40232s01.dat": {
      "sha256": "06a0f839ebd5281f05a3ef63ce7f326303e6876bf76da047e66ad91296ba402b",
      "bytes": 99542
    },
    "parts/subparts/40244s01.dat": {
      "sha256": "828f7be0f436a9e239d6415690d74bdc09c706653db20b95577c54873f0867b0",
      "bytes": 1880
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
    "parts/subparts/4150p03s01.dat": {
      "sha256": "0c227ee2017e8cea3f606ad266281d442a72da3e6a7de40045b33b5f736b30d6",
      "bytes": 6728
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
    "parts/subparts/41748s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/41748s01.dat",
      "sha256": "aa7b5113de1547670964a9abf8d617fa1c4b77ee742f6a9929c3df7b0f7ad1e6",
      "bytes": 36887,
      "modification": "Normalized references, original author/license headers retained."
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
    "parts/subparts/42205s01-7406d0917d.dat": {
      "sha256": "e6418e8135d1e280b46b760c7b69f7df665385d739943fb76ad4643de2aff664",
      "bytes": 2470
    },
    "parts/subparts/42205s01.dat": {
      "sha256": "8cbdbc55ee3dc82d906a50aec0af7375b05fc611cce7974baf1dae87dc1ef3ff",
      "bytes": 1449
    },
    "parts/subparts/42205s02.dat": {
      "sha256": "29bcb3aa230d77d3dd3de23f2169a84818fffb2a6068b326db47f95340b878d8",
      "bytes": 1961
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
    "parts/subparts/4286s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/4286s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "7da8a5a5cacaa746ed7490cc8b375798ed9c435e",
      "source_sha256": "558ae2b250a1f2f6e0b0196d6564f091bf65921126092f5bdb920428b5540046",
      "sha256": "0fd6680dbaa6c8120833f14850ed66d8c68c96bfebddb5173ab97dc83f98b381",
      "bytes": 2034,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Chris Böhnke [KnightOfTarenta]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/4345s01.dat": {
      "sha256": "37bfb06da34f3d788e4bcc6e1278194b69c152a5ced42be1a4ca15bf2fa2ce12",
      "bytes": 3663
    },
    "parts/subparts/4346s01.dat": {
      "sha256": "fcb143004beb9b229b916edfe38fe906773f469d57441f33dd5406580365c27c",
      "bytes": 5056
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
    "parts/subparts/43892s01.dat": {
      "sha256": "68357a45e5699815c415858e0ac1e4778243078f55438ebab66ebfb1408335c3",
      "bytes": 31299
    },
    "parts/subparts/43898s01.dat": {
      "sha256": "2fbed2315c74c235a41d4ea53d34190af946ba379df9d1bb7424e57005cb422b",
      "bytes": 9433
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
    "parts/subparts/44375p04s01-7f8760cd60.dat": {
      "sha256": "ea163615d4c10bcaf161264d2f21e9148bad1709757c534471a41e10b5433e4f",
      "bytes": 16907
    },
    "parts/subparts/44375p04s01.dat": {
      "sha256": "4fa31303e1515c9ec7e38c5525c18868ec738f80ad863cc7b9b5f3aae329d4d0",
      "bytes": 16831
    },
    "parts/subparts/44375s01.dat": {
      "sha256": "64f0ae2f82eb38d0a836826f5e58a66989e720479574dd33ccb0387297b76981",
      "bytes": 12249
    },
    "parts/subparts/4460s01.dat": {
      "sha256": "452f1cc283cc53160456b5b1447a64c0b80f38b8be5c3eb223ee5c35c63c9f0d",
      "bytes": 2472
    },
    "parts/subparts/4490s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/4490s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "013e83ca15923fc5e1969f8b6a87386d93a398de",
      "source_sha256": "13d8a45682fb2a5c8c073c592252b410bda2979f15b1178e949306806540630c",
      "sha256": "7e2207d41d6ca6054fd61cf03991ad0a2e38540c1c280fb4160db5ddf0c67cd1",
      "bytes": 2005,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/47398s01.dat": {
      "sha256": "4c91b0a6dee9ddcb1771f45bd48a73803adabec487e452c461f27895933c3335",
      "bytes": 10839
    },
    "parts/subparts/4739s01.dat": {
      "sha256": "6567e6ffc9184a6b99280880e0b1ee47ec7a8c081069da70ba575e38204495f1",
      "bytes": 21611
    },
    "parts/subparts/4740s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/4740s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "bb8ccc4ba65af64f300d05d67e7b5624a38004b3",
      "source_sha256": "f585e07aecf5eecc399752e3cceea8a4342e4e2b91671f94f1c58d51d1bf86af",
      "sha256": "2037ca1a0d9655cc185e41985793a1441e0f5ee325021432c89a3cf62a2928d9",
      "bytes": 2181,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/480s02.dat": {
      "sha256": "559edc3daa4aa4189dd9ae241ed2c3b260c67fa53c5a3b0843b972ef4aa0df72",
      "bytes": 1044
    },
    "parts/subparts/48310s01.dat": {
      "sha256": "65469c664842c86f49424b05fe29c8bc56dfb998e53fd71c1027d19d4314f59b",
      "bytes": 28084
    },
    "parts/subparts/4865bs01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/4865bs01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "bc8ecc0293cd3b2d167f5b57bf8a1d244e3b2ab5",
      "source_sha256": "6acf8a49fd3086df0ba7fb363b1f4065d67243fcd5207cfdd2b7d19ecfa205f6",
      "sha256": "1354f30494574267ad27ea1129c92328a480a17bc7942ef4c3f81851494ef674",
      "bytes": 1336,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Damien Roux [Darats]",
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
    "parts/subparts/49668s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/49668s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "361182ad1acdf93a7f238faa1072a7b6c45cbd21",
      "source_sha256": "07c5831e3968c2606a527a046ea62c5e98cf5d2ced33db4d96216915cd9be961",
      "sha256": "356b73b721cdc5379e9012fb90e2d885fd13b9b5b8b45abef8efc319d5473862",
      "bytes": 13034,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/5092s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/5092s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "8e130cee39f4eeabb216d8666c2f080a07269c5d",
      "source_sha256": "02161d4d43cf5d1a4ceb1d3c7440d75bd6789eb2b032a420750ee8363fdc6d81",
      "sha256": "f3033f58e787ea5b4bfbdb142e30de1700c49d151d2f01b7f20fc59a96e50caf",
      "bytes": 2595,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/subparts/51266s01.dat": {
      "sha256": "230a5268f28ad285c6e8a8e7f062025d67fa9c41a1d1fc75c71fa22ad6f4612d",
      "bytes": 1210
    },
    "parts/subparts/51270s01.dat": {
      "sha256": "1e11316cad66e6633eb105b63b6b3c585af40100f783f14f3dce1fecb947e557",
      "bytes": 11562
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
    "parts/subparts/57895s01.dat": {
      "sha256": "9cfa206fd1fc087107b981b45596f342bcfc290c34bdacc536badb2096f85def",
      "bytes": 1270
    },
    "parts/subparts/58381s04.dat": {
      "sha256": "5b8b29112c312288f7d53a298d18aacdb0598f7a3b012d789b0241e9a116b8ce",
      "bytes": 1835
    },
    "parts/subparts/59349s01.dat": {
      "sha256": "6f7365bf1108e4a139a436c6a8d0f9a87207053bf8543ef178aba953ae744fd7",
      "bytes": 1231
    },
    "parts/subparts/59s01.dat": {
      "sha256": "d661ecd07766437031466ca553b4a48ccf3d7818b77ceb863a668d7b9d26874c",
      "bytes": 1192
    },
    "parts/subparts/59s02.dat": {
      "sha256": "40f4a83a9bfca261837ef5aeb2854e1fc912f019e04434f21383ad543c65d246",
      "bytes": 1338
    },
    "parts/subparts/59s03.dat": {
      "sha256": "b2c646de9ca2b857d9be6e0666f218a90d521ba400f3733ba9318491a6b0e2cf",
      "bytes": 3614
    },
    "parts/subparts/604547s01.dat": {
      "sha256": "935e3626ee488156fba155fc4e66c98c749f10e24b22425ffbef0bd2f5d33def",
      "bytes": 1237
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
    "parts/subparts/60481as01.dat": {
      "sha256": "57860c8ffcb30b2aa1b6a3afa119af0a6b5219956934855a6125f586a64cff24",
      "bytes": 2827
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
    "parts/subparts/60581s01.dat": {
      "sha256": "ad4328cafc1a89db33b88821f3d6a17a7c2a2cda452b3f70d958ab7fa7ecb3f1",
      "bytes": 3029
    },
    "parts/subparts/60601s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/60601s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "c7e77afa5a3e94da94ace212f2775f1dab9aad40",
      "source_sha256": "b9a706c51be95874bcabd328ba7fddc3b0ee79423d075765976e05d7a099f7d3",
      "sha256": "960cf334a10c19f62be0cd038a594ced3c3c8a80351887a202f143787807211e",
      "bytes": 858,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Ulrich Röder [UR]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/60616s01.dat": {
      "sha256": "d84ba6eb562f67d1eae6084e850e504f1e5f536bd1b43071a2d0250c65d567ba",
      "bytes": 2315
    },
    "parts/subparts/6063s01.dat": {
      "sha256": "65ae24cf9e57f12de029c1900dd3c8c5a7e5e31a66252e4bb93d1c5e7c99170c",
      "bytes": 2485
    },
    "parts/subparts/6081s01.dat": {
      "sha256": "e6e08a6087b12c0d2782e36e665e595e5d6cddb3954638e6868b403f2f6c20d6",
      "bytes": 6602
    },
    "parts/subparts/6126s01.dat": {
      "sha256": "b41c347e01651b9f7281b18cfc1991210f90c9c9df653d6a6fdbd111f23cbcab",
      "bytes": 17539
    },
    "parts/subparts/6143s01.dat": {
      "sha256": "b985e759cbcd53b7a8e8b793032fe52f3cca82a374dc69524992c2df2f1b9144",
      "bytes": 1058
    },
    "parts/subparts/6143s02.dat": {
      "sha256": "44a78117f9b578a6669aa7865d11e456517274227ec48e8aa1b1cd3e88ccc349",
      "bytes": 3732
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
    "parts/subparts/6179s01.dat": {
      "sha256": "11b23396db4e55016c986f858c4023bc2c20f57e514b4ec2d097cf2093879a8b",
      "bytes": 941
    },
    "parts/subparts/6192s01.dat": {
      "sha256": "8d74b978efaa22bf992b8af6e3452b4068450aaadaffcad970914bc051f8b328",
      "bytes": 1210
    },
    "parts/subparts/6233s01.dat": {
      "sha256": "65babf9a57a05c9127f847728bd7941ae5f4826c33a520bffcc0d7cfe1aa2e0e",
      "bytes": 4244
    },
    "parts/subparts/6259s01.dat": {
      "sha256": "1b4ff80380fab3fe3e7e0878aecb8f252e7133689b26a94aa9fe558714e5530c",
      "bytes": 4663
    },
    "parts/subparts/6259s02.dat": {
      "sha256": "11c9ca77afe4cbf21d9626de17a78eee62d0149b88416616501445063f573deb",
      "bytes": 2841
    },
    "parts/subparts/62701s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/62701s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "1b08a5ea073e37f1be00a1c38b4c2c8f23b0ff11",
      "source_sha256": "b3cea27a50eefa7f004db02cd6e48861443a78e54611bdcb8833a7b9d991d456",
      "sha256": "90022be149a02a5cbf6aaa2ddbef3cca6f0b1c5da75e15c9afb9f46f63420de1",
      "bytes": 6471,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
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
    "parts/subparts/64179s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/64179s01.dat",
      "archive_member": "ldraw/parts/s/64179s01.dat",
      "source_sha256": "bb17d1bb2edc234ab451f3045c3f4ab9f2aea371d886b9eaa9374cd5f3e8b666",
      "sha256": "479a34306b2dbae47c20e5f9ab6187c928c2a150f9adc0a9a7c5e13942bfd3f1",
      "bytes": 4681,
      "modification": "Official Git repository file downloaded at pinned commit; dependency references normalized to repository asset paths; geometry coordinates preserved.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905/ldraw"
    },
    "parts/subparts/64390s01-3b489509d6.dat": {
      "sha256": "a82f7b232bb2adca3f1ed5741db888c2a946bb52d096976981fdcdcabfeb6ce9",
      "bytes": 13258
    },
    "parts/subparts/64390s01.dat": {
      "sha256": "bd68ba239d0a97103c0501e9b11c42a3afedef85223107e1dba110f2f12efca5",
      "bytes": 9124
    },
    "parts/subparts/64390s02-8a3eb36b01.dat": {
      "sha256": "fe5fd8aa1395e03015095268ef3fba1db5447f7e45f94010b66b6033f48557ae",
      "bytes": 2597
    },
    "parts/subparts/64390s02.dat": {
      "sha256": "98edef106228951e5a3f08e986c87b9ccff47e5c57a5cee771d31ebc3468aa7f",
      "bytes": 2733
    },
    "parts/subparts/64390s03-a7224eafd8.dat": {
      "sha256": "0889a4248dc303208fb3bb65c3dfaa9d097b5b236ad1524597d0bc2548ba4011",
      "bytes": 4751
    },
    "parts/subparts/64390s03.dat": {
      "sha256": "445c433f83e5892c7ef95a8c8510bc5e3ce043fd06b5475dc21005ac32ef5fad",
      "bytes": 4951
    },
    "parts/subparts/64390s04-98bce37f8c.dat": {
      "sha256": "4637d3c51cf3aa33d3405d2f098706e32459f952e78ef2b59fc31c3f86e0b122",
      "bytes": 1672
    },
    "parts/subparts/64390s04.dat": {
      "sha256": "68d0ffae13801ba0c5bf14463045700a8509a085000962fe1c80fa0ca070988d",
      "bytes": 1660
    },
    "parts/subparts/64647s01.dat": {
      "sha256": "faa38c9159a4a1624060890c52bc88c712929edaad4cbf049a3297eb23dbd742",
      "bytes": 17808
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
    "parts/subparts/6585s01.dat": {
      "sha256": "76941678283a1de30709e0323fc432f1406c58edcc7c4bb2990dc9b1e7c8e9dc",
      "bytes": 17969
    },
    "parts/subparts/65886s02.dat": {
      "sha256": "5e7fa83783c762783ae84fc2091b8ab6f89fd0e094817879418a78753c4214df",
      "bytes": 3081
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
    "parts/subparts/67142s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/67142s01.dat",
      "source_sha256": "89cfe910ed48e5ef326915cea67539d8b8f6ff6cdc5426d2603ca21f0aabea2c",
      "sha256": "36b9a78bc5fdcdb0eb6c056d7b554bac9cca347249180842277254e082d5fd8c",
      "bytes": 10674,
      "modification": "Official part references converted to shared assets/parts/subparts paths; geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
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
    "parts/subparts/75902s01.dat": {
      "sha256": "541679d31db8a879e1df1a8b6225f566584d5085ad79de1298c24f4fdcca147a",
      "bytes": 438
    },
    "parts/subparts/75937s01.dat": {
      "sha256": "9d36b9136a47afebfe78cf4f924c5b3c457d3fc5ca7f489b276a85a7ce50954a",
      "bytes": 6904
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
    "parts/subparts/85863s01.dat": {
      "sha256": "1819a2d856243159e6e2790eeabe2f46718fdf53353a431c882c4e3394387d12",
      "bytes": 7720
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
    "parts/subparts/86210s01.dat": {
      "sha256": "ee2063bfc18a378a66cc894928ec8c91f4a849512bb6e8115219e9fdeed916de",
      "bytes": 3603
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
    "parts/subparts/87081s01.dat": {
      "sha256": "f5be56261f47d30bb9e5660695a1a120c6a45a4c035d9e0b16e2940a5cc80d81",
      "bytes": 5688
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
    "parts/subparts/88646s01.dat": {
      "sha256": "1efdc2e4300e2f60c5afc19b2e5edc1e6a4f44f78103c82c2a6b204a1d69a183",
      "bytes": 1190
    },
    "parts/subparts/89523s01.dat": {
      "sha256": "9af3e19a3772d8511a185cca31447e332e1442c2b040e49f55fca990a7a65317",
      "bytes": 3853
    },
    "parts/subparts/90398s01.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/90398s01.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "95182fe6e1f34b99ec70e6e7f24ed8c42e49ddcd",
      "source_sha256": "d64313ee1906015c68c95d862cd96d45b903ce1173481521203da00b0e883702",
      "sha256": "429b0c1eca3863cd9da59876afdc9ec618aec405d099054fdb6ae637b248928c",
      "bytes": 56957,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/90398s02.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/parts/s/90398s02.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "795f601d00371e541eafaa5e4c36385e166e23d0",
      "source_sha256": "ad552a0b937a012c4454af17c3966b0120734e7997cef50dbc8f18e69c137f15",
      "sha256": "30b58462eb26fe296d1f369c1f0467faef6566003ecd76cad6e3f9a84ca62d1e",
      "bytes": 821,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/subparts/91405s01.dat": {
      "sha256": "5f1e9b1cbedeb44ec2a09bbbaf96d81dadf23204f01d7ac3703bf08a89ecf0df",
      "bytes": 1821
    },
    "parts/subparts/91405s02.dat": {
      "sha256": "6ccff12c4e236edaed073b11397f76b5a97e2a6923c5496f8a41e7c16aa41bdd",
      "bytes": 2618
    },
    "parts/subparts/92262s01.dat": {
      "sha256": "f8542114d4317117331b37bea58325624a961a09e9f6faa38b90f866ff984815",
      "bytes": 928
    },
    "parts/subparts/92262s02.dat": {
      "sha256": "8138f5ea49e409765ae018a68c64de1fe82194a86e8ca075c67653c8504ed039",
      "bytes": 3351
    },
    "parts/subparts/92409s01.dat": {
      "sha256": "89f29262e0b44575260eed653af7e8452166b701f29e85dc7d8e336a3d66a381",
      "bytes": 1768
    },
    "parts/subparts/92409s02.dat": {
      "sha256": "5c938939d471b3e8fae075b91532aac5b69dd9cc65d0bc4166bb0c273517777b",
      "bytes": 783
    },
    "parts/subparts/92947s00.dat": {
      "sha256": "c4110879510a0f4e089c404930f4274ccf38226490ca9d1c898840a6de93d605",
      "bytes": 4031
    },
    "parts/subparts/92950s01.dat": {
      "sha256": "ae7492dc639181c13676f83e488d91a9d4de12cd1473b4f5503e00243abf5ce7",
      "bytes": 3351
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
    "parts/subparts/93593s01.dat": {
      "sha256": "96418eca7dbbd4623982e1984f92daf54bf378546ba1097883904a61ff60253a",
      "bytes": 9919
    },
    "parts/subparts/94161s01.dat": {
      "sha256": "70ff31d0190b968d912390d92e9ab12054334975d44f75505a60268d9fbffd90",
      "bytes": 3945
    },
    "parts/subparts/95228s01.dat": {
      "sha256": "936dc313314c202aaf33f78cbe36b52b637bf4dce1baa0563de1d527702c1382",
      "bytes": 2483
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
    "parts/subparts/98138p8bs01.dat": {
      "sha256": "05c47e5be00aa491520d6f5985078741bfd29ead636bb9ff4d1edca5933ab540",
      "bytes": 4315
    },
    "parts/subparts/98138p8bs02.dat": {
      "sha256": "2142c8ae8b7cf26920d77082ab2c1f1d94811ecc1eab49c513ccce7e9c00c4a2",
      "bytes": 1118
    },
    "parts/subparts/98138p8bs03.dat": {
      "sha256": "55f20dca10df5b01ff3af31fcf05ad3c58fbd644444842556ba78d758df80065",
      "bytes": 1729
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
    "parts/subparts/98281s01.dat": {
      "sha256": "1afa50aaea0abe45b443af7a860c23a56be0a33152c42923e8b59f40e823b822",
      "bytes": 10773
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
    "primitives/1-16ring3.dat": {
      "sha256": "c5b0046cbdcd493dae73b3546c69ec4b185a15cde74edd3509de8596ff706733",
      "bytes": 404
    },
    "primitives/1-16ring4.dat": {
      "sha256": "1fde43a14833e892f881f1a30dd45445803e6b3eb3768aa94371ed019aeb81dd",
      "bytes": 442
    },
    "primitives/1-16ring6.dat": {
      "sha256": "e5233eac45cda067e33cb99341947cb38904989c23836ee09cffa0a5d99d45d3",
      "bytes": 337
    },
    "primitives/1-16ring9.dat": {
      "sha256": "f087dbe4d37279df7bdb766410245b2ec0d79ae72e38b33b39c23feb990a5c32",
      "bytes": 332
    },
    "primitives/1-16stud4.dat": {
      "sha256": "93e048da0e84458ca2da923542ee60b0aa8ec7a0905d13bafd09e8ba476b873b",
      "bytes": 537
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
    "primitives/1-4con6.dat": {
      "sha256": "d7f7ea2d96497f6f0121315be9d7f44cab20cc935e7fccbf7417d6a242fa2ad2",
      "bytes": 1097
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
    "primitives/1-4cylj2_1x2.dat": {
      "sha256": "ce144546490b06e55ba17a9fa93f69f1ab2b40282b80ec58f5a5aaf518593a91",
      "bytes": 1153
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
    "primitives/1-4cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cyls.dat",
      "source_sha256": "aaee6ffe6e4a191d6cad4496677132eb0349303d6e48c13c7a2240dcea1db621",
      "sha256": "d45980725c5d006cab357fd1afff1469b1a9fc1d2791aa6afd162a2db582c7f9",
      "bytes": 1081,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
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
    "primitives/1-4ring19.dat": {
      "sha256": "201b727e164e9e407ae939bc2def97b2794769e0b835c120e2d8c5644be51ef5",
      "bytes": 727
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
    "primitives/1-4ring20.dat": {
      "sha256": "95f985438ada71258fe54095faa9f9eff657510d30f6869f46ddeb434d213179",
      "bytes": 634
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
    "primitives/1-4ring33.dat": {
      "sha256": "1b1aff8101f5b54eb272e0f0ced08574fce45a4c0b1c2f4855a30749d2b66e0f",
      "bytes": 551
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
    "primitives/1-4ring5.dat": {
      "sha256": "a9b4ce664170ea13bde79bfdb297ea64c430c5dbfa024c367495c520f30df044",
      "bytes": 829
    },
    "primitives/1-4ring6.dat": {
      "sha256": "6e502dcb6564074f557d820f8505cb6d2db26c05b02461bd463a6180fa06aaa2",
      "bytes": 860
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
    "primitives/1-4ring8.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/1-4ring8.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "187a76011c312ab6e80200c7a563a917e054b272",
      "source_sha256": "670d5b738c8947233d3c7805ae42994116eec77a73c39d2f5a0d548d7aa5f80f",
      "sha256": "4bc9c790afc7cdb855998781e35e19cfb82bbdb0d6c6e2406dc689f977a08f74",
      "bytes": 705,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Franklin W. Cain [fwcain]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/1-4ring9.dat": {
      "sha256": "9153a766b5f71cb6aba96c40f22cd95db649b5954a29a2ea508a82430a72d34e",
      "bytes": 711
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
    "primitives/1-8con12.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/1-8con12.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "b86cc2126e673bf4b36d2eaada64d4c47b2a62fc",
      "source_sha256": "70fe01ff86b0643a0a60a5437931f54bdad152b455699271c4740a74c2f799d6",
      "sha256": "1969416f50bf8565c9d285f3eb934eef63f859cec869080ff4514493edde3407",
      "bytes": 606,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/1-8disc.dat": {
      "sha256": "6a58dce1f9265217bdc703cb29f5ee996fc1bb7391c4ed602f1814d9547195a0",
      "bytes": 618
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
    "primitives/1-8ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8ndis.dat",
      "source_sha256": "97e394834789794c8635261fa604ad8e69b4c6872d0cd8d7506408b80023f408",
      "sha256": "1b3e6cd9bfaab26e0f9c8fd5f5c16b4ae1ffeb6282ca68acf4166eade0b4c759",
      "bytes": 597,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
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
    "primitives/1-8ring12.dat": {
      "sha256": "30de4c49d00eab5ccec244a0161b6eccdc55b95ad9759b078badb20b6ea0e222",
      "bytes": 412
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
    "primitives/1-8ring5.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/1-8ring5.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "1641faefb0279b6d7947035500b484bb4186a003",
      "source_sha256": "5cd56644b846c2db874735188ba03d5aa835de4d17924680ddc726c8861b8552",
      "sha256": "c2d2602e5f29bd8237882ce7c212ca49db18f7555cb7456623845768eb360b27",
      "bytes": 473,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Chris Dee [cwdee]",
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
    "primitives/1-8ring9.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/1-8ring9.dat",
      "archive_member": "ldraw/p/1-8ring9.dat",
      "source_sha256": "315a78ca5138394333b62197ed7552aa4acd69d470f054b59a5ac06cb04427f9",
      "sha256": "315a78ca5138394333b62197ed7552aa4acd69d470f054b59a5ac06cb04427f9",
      "bytes": 600,
      "modification": "Official Git repository file downloaded at pinned commit; dependency references normalized to repository asset paths; geometry coordinates preserved.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905/ldraw"
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
    "primitives/1-8sphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8sphe.dat",
      "source_sha256": "c38f9b8df6f260a26e920d8bbfb2d6b11667026e0675733d7fc2d3653ef92c53",
      "sha256": "9bf4c4aaef057e16607706637f6768dbdfa1870446633d11a66b8ffbf9e0845b",
      "bytes": 3972,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
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
    "primitives/11-16cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/11-16cyli.dat",
      "source_sha256": "6763716ab47ebf0a16e8b40e6f1a74a32633ea22489bfc07f0e235c0bbf691bc",
      "sha256": "6763716ab47ebf0a16e8b40e6f1a74a32633ea22489bfc07f0e235c0bbf691bc",
      "bytes": 1924,
      "modification": "Official geometry copied without modification.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/11-16edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/11-16edge.dat",
      "source_sha256": "1bf8fadea1634856d2ff42b4029da1a23f8bfadacdc332e745ffa783ec0ef4d4",
      "sha256": "1bf8fadea1634856d2ff42b4029da1a23f8bfadacdc332e745ffa783ec0ef4d4",
      "bytes": 818,
      "modification": "Official geometry copied without modification.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4chrd.dat",
      "source_sha256": "3b0dfcf2cb881fae0acfe1e53b703104768878636477e540d0c893fc3fd87f8f",
      "sha256": "6b1b3d8ccc50f3477109a2dd220a151e76671c8ca3b1b276c81a72d0a4d4daf0",
      "bytes": 475,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Philippe Hurbain [Philo]",
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
    "primitives/2-4con3.dat": {
      "sha256": "b1c6d798250dbbf1db661af996feb99cddd5f1a062d7be1f28e4a11c978f7189",
      "bytes": 1585
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
    "primitives/2-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4cyli.dat",
      "source_sha256": "d486780f0f84893899d9eadcd13150f13a42e15e77a3cda38cdf24ded98862c6",
      "sha256": "57b7479c754bd98d8a17668b58dba8aed3539598da4c8374e24e417bfda885b4",
      "bytes": 1509,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
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
    "primitives/2-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4edge.dat",
      "source_sha256": "665400f76566b161c28303cdadce40d17d979a8ff9a8a133675af2d17fbe6763",
      "sha256": "ec42084755c0f7c2fa9ac3a07f088f56d1ccf218e73dffbf32115fec96f82070",
      "bytes": 661,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/2-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ndis.dat",
      "source_sha256": "7557eae598be3f530b840471535198e6b07b03486ffbcc18a00e862c3d25d925",
      "sha256": "2ef5d3fceed3513b90ede773d624acb657dee425d8ccae0ff9ae57d61a7c74ab",
      "bytes": 850,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
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
    "primitives/2-4ring12.dat": {
      "sha256": "bd65e4e50e14cfabc237614a2bfe6d3aa6833dfb2349dc3f396e81e578bda7bf",
      "bytes": 931
    },
    "primitives/2-4ring13.dat": {
      "sha256": "012c62ef3a8df358d356836c56e7577862709222404061b390ba5e8f076fea06",
      "bytes": 931
    },
    "primitives/2-4ring15.dat": {
      "sha256": "fc40f26c3236779802d4aed5325dc894b9c110f37e36021732f5507e99511ade",
      "bytes": 879
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
    "primitives/2-4ring19.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/2-4ring19.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "4b270fb8093de942f1b27b918d428a21b3870d18",
      "source_sha256": "81ae24be860bc3ba287f89bbdc720fc921f76d1f96a893190223a42200db99ac",
      "sha256": "4b484f4bdd30fbfe46231180a9a2caa70ddffe7978a8cedff038970b67ad00dc",
      "bytes": 921,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "primitives/2-4ring7.dat": {
      "sha256": "c6298c72f62c4d2441270659e7a38b6c085563541a064f075d459fc2b37b50b8",
      "bytes": 1192
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
    "primitives/2-4ring9.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/2-4ring9.dat",
      "archive_member": "ldraw/p/2-4ring9.dat",
      "source_sha256": "66c4444b0d30e8b1cb0b1a3aa0e472e28750462cb55d2c43fadcd2e14b852f36",
      "sha256": "66c4444b0d30e8b1cb0b1a3aa0e472e28750462cb55d2c43fadcd2e14b852f36",
      "bytes": 907,
      "modification": "Official Git repository file downloaded at pinned commit; dependency references normalized to repository asset paths; geometry coordinates preserved.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905/ldraw"
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
    "primitives/2-4stud4t45.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/2-4stud4t45.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "96ad45dfbd6ef24d12a88169feb36d5880012ae6",
      "source_sha256": "86dcd81d51a7537612d5703db90af852daf1f2a7eabdaaccbd87ae07c5d0b941",
      "sha256": "9ce81dca5bbfc1f01a121cc8018fc8f41842c16f8faeb31be9733ed1deed4ee5",
      "bytes": 2068,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/3-16con5.dat": {
      "sha256": "818f56c21c5a01428ec1ffb587f84450679585af05b772d1993f5453d2fc1e09",
      "bytes": 732
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
    "primitives/3-16disc.dat": {
      "sha256": "cbf62c235aed52196a3d2fda616889c8af3d53292e92760a98e1bfeefa93c8bd",
      "bytes": 537
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
    "primitives/3-16ering.dat": {
      "sha256": "e7fcb67377024e6900bbf146b9f7265ee7b1d804758d29f0d313c84fa1a707f9",
      "bytes": 779
    },
    "primitives/3-16ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16ndis.dat",
      "source_sha256": "abb7da370e72fe9e75faf5d10c637b476202dbd8ced9cb5b0f96433e1f72f529",
      "sha256": "b81a275e0600e89713c1dc84f4413b9e55e44220304525784dc99f7dd15bacf9",
      "bytes": 541,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Magnus Forsberg [MagFors]",
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
    "primitives/3-4chrd.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/3-4chrd.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "19bc99ffc4ac323b14e1e315dae574e674562a54",
      "source_sha256": "0d6ab4757a7825257f175b7eb5457897bb93487d3b1b938e1ca0ab760fb8ed9a",
      "sha256": "4c478a89ed393006441abc96a3dd0f6c97547b2b821acfa4cc09518b89a449ed",
      "bytes": 719,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-4cylc.dat": {
      "sha256": "ea14660e6fbd88ba146eeb63b167c30ea6abc637f28ba309ebd0059a25967b91",
      "bytes": 453
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
    "primitives/3-4ring4.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/3-4ring4.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "ba9bc88c8ec8331408321cbdf14c2b6bb55cddf9",
      "source_sha256": "b858e5bbfe2b86e35d3fa077e02034e4f0378b69d5c13a68c83fcc22be440ad1",
      "sha256": "98c883c9f0bc10644c5081f0d7fb8bca77531ccaa94844d53c8f86e9946a5a44",
      "bytes": 1171,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
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
    "primitives/3-8disc.dat": {
      "sha256": "276ae6ca5359e2f191bb06534acaa0215a688313074a2e00bd556cb513578b40",
      "bytes": 647
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
    "primitives/3-8ndis.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/3-8ndis.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "21eee11d8c01a61f57fdfa506dabb5c9bb68b8ce",
      "source_sha256": "eb139765fe92ae387b96c41c57802c81e6369574fe4497ac721298d73d09d77d",
      "sha256": "99ac4bf22f81d49820fd30b111263fab43982b10002827690654f54e8400c8ef",
      "bytes": 481,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/3-8rin24.dat": {
      "sha256": "8ef50d1f0b44e9bee92a29b068c789a44117ad50d5714f86ad50568324803316",
      "bytes": 753
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
    "primitives/3-8ring24.dat": {
      "sha256": "e0ba95c34c5188b91e725abbccb1ea1a7accd14ad8bc8a9bfd6a20b874bf8f5e",
      "bytes": 738
    },
    "primitives/3-8ring29-59a3379c88.dat": {
      "sha256": "0279769246b8b84c7f8928c7bda47637f93a9f643ff9180c7c171677cb0f7a11",
      "bytes": 669
    },
    "primitives/3-8ring29.dat": {
      "sha256": "ccd98b6cb664368b06663fdeffaf8451925b377b97858be6e7b985bcb8055360",
      "bytes": 673
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
    "primitives/3-8ring5.dat": {
      "sha256": "d243624fe989fa7d69e16ba70d8977e6f5a4b78dc6cc64176ec4c84cad6e3e21",
      "bytes": 606
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
    "primitives/4-4con1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con1.dat",
      "source_sha256": "b7e91225acedda94bfcf36dee83212c6b7ab845e435a375b595dc754e3fda6a7",
      "sha256": "a756e203b939c424ea1424bba9424621b30525d2ac61a68dc4fe1b05a6f4f0d2",
      "bytes": 2719,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con10.dat": {
      "sha256": "9ff22aef80c2c4f74de3cb0b377af7f1a5f02b55c792e1a6eba264eab1659969",
      "bytes": 2302
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
    "primitives/4-4con19.dat": {
      "sha256": "84e71056ba15defaaccad869db514be2b42512bcad41836d3065bfb66bb516dc",
      "bytes": 2537
    },
    "primitives/4-4con2.dat": {
      "sha256": "7e8a3019a1d748741285339cd51bdcede4517c80e1753c56e11331311efd71f1",
      "bytes": 2672
    },
    "primitives/4-4con28.dat": {
      "sha256": "d23d2b6a06a2f656ada704ac5f2994aea187fef639754421097d16aa71ec2465",
      "bytes": 2509
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
    "primitives/4-4con5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con5.dat",
      "source_sha256": "b2d6eb9f4a94b4440d5bbe4793a9f8f1b06a9d5e3bd0df8ea04260e808ae8798",
      "sha256": "b2d6eb9f4a94b4440d5bbe4793a9f8f1b06a9d5e3bd0df8ea04260e808ae8798",
      "bytes": 2424,
      "modification": "Official geometry copied without modification.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4con6.dat": {
      "sha256": "745d39a48f7dae7e1a435a7b4892bbcfde8dd882d5e267f2bde1272c88b56d16",
      "bytes": 2377
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
    "primitives/4-4con8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con8.dat",
      "source_sha256": "9c5ccecc4d79097dc58c4c67d095bcddd0c307a40239dac29e8bf780f46709df",
      "sha256": "95815b7d7421d0c9838332fd7d2738be695f8c616a4d8dd61c208ef3acb76306",
      "bytes": 2576,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Steve Bliss [sbliss]",
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
    "primitives/4-4cylc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cylc.dat",
      "source_sha256": "0183cffc7f56a2f3e5e3511f0d07ac484d3039c2d41bee802a94344ec95ec8bd",
      "sha256": "a38ea92506dfc00ccc4dcf68848caaed9af9467225526a919d67b27f0d8e4740",
      "bytes": 503,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cyli.dat",
      "source_sha256": "4a742c2765b6ebf98245baaf8a160a4ff587fc93d36c8ee2b9074712a2f968c4",
      "sha256": "f832bd6e12c156e327b20dc954562942f62eda834effb114827a7664c27f82b9",
      "bytes": 2637,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cylo.dat",
      "source_sha256": "d6ca97ee2e75918b3309a5c88aafcd2455b3a316f7cef8963517c19f1d86b38f",
      "sha256": "c52c202c30e5c728029a1df9c45303570acaefbf455e49e71448c76ac3e777c9",
      "bytes": 403,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Mark Kennedy [mkennedy]",
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
    "primitives/4-4disc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4disc.dat",
      "source_sha256": "a00b5547776f61a7389d303616987c76b3c4de86ad8ec32f22857e1bd5e5e40f",
      "sha256": "8853bc34639ef69cdaf1e2c0b090597415cec2fefe56eb93f7915e48b5782dcf",
      "bytes": 1105,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4edge.dat",
      "source_sha256": "54a52196e421fd1717d291ff52ea57553b1fb238907c1678cc1f1a84c698b1da",
      "sha256": "507d698a5890b49bf7c2f6472c847d41139529e06a2dd7bfd315dc9ec9fd9bcc",
      "bytes": 1052,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ering.dat": {
      "sha256": "18e1207ef54418e203475e1bad4279c5641b8b7fd83a3c9325d0a624e86b5d06",
      "bytes": 1735
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
    "primitives/4-4rin10.dat": {
      "sha256": "6b29ac69296bd358c80afc637f6fe2180eef5c932fe105edd1cd7ca513958d6b",
      "bytes": 1643
    },
    "primitives/4-4rin11.dat": {
      "sha256": "94b746a49227758cfc58981a5359c4d33fb6ccc5e8384077ba80d9dbf2467492",
      "bytes": 1610
    },
    "primitives/4-4rin12.dat": {
      "sha256": "5260ab944a3aea8f5f3a7dbd3707dcfabd3c6f28d7a301f1d14a7dacdd0bf801",
      "bytes": 1609
    },
    "primitives/4-4ring1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring1.dat",
      "source_sha256": "4ae21061a6d0c9c80c608decb750f16fe1d113d84e08ef2f6082bcbb0f55194c",
      "sha256": "96260830370ac6db8ca5c5e5947da20a0d052bead0a9076c0e730324e80d9ca5",
      "bytes": 1607,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring10.dat": {
      "sha256": "c809c160c6814935dd1676adf65cb405846290da81013cd1de3934289c60dd00",
      "bytes": 1628
    },
    "primitives/4-4ring11.dat": {
      "sha256": "8ea4563764c0e15f2368dbb73d3ea60bab137c1df62fc371b32768d6b25db85d",
      "bytes": 1599
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
    "primitives/4-4ring13.dat": {
      "sha256": "a882a7df5b039aff4d838ff28320210802d3ca0ceb7559ef7b86e4c60bf66904",
      "bytes": 1599
    },
    "primitives/4-4ring14.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/4-4ring14.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "29cadc98eff436d8b349c7553207a0d72313d42f",
      "source_sha256": "a5aacac2f371b96a84694d73344a5a33cf792c8ae1e042eaa024ee8b2ed7a8cd",
      "sha256": "04651cbffbe551cc2837d40bf40a9794ce8c2d70caf33c37d244fe85c03c654b",
      "bytes": 1614,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "primitives/4-4ring19.dat": {
      "sha256": "e9e539e1be117933d3173b78f4a30d9761c6c8049391d487734bfa01b7e2b1d5",
      "bytes": 1453
    },
    "primitives/4-4ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring2.dat",
      "source_sha256": "6fb38804b1f5e9bee8c0b80caf1397b09454fc58b048dc19045b6f37c8762ab0",
      "sha256": "3c59fac484babc9d0c0e0af302e80c632a780f55bb55969b192bf9a726b6c0e7",
      "bytes": 1594,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/4-4ring29.dat": {
      "sha256": "40cf7d1fbf63280ac3a67396300f81a6280c0ab9aa918fee52e544411ab1081a",
      "bytes": 1485
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
    "primitives/4-4ring36.dat": {
      "sha256": "fcbd2e545db423133af10367438401a6db4f65b76e7487acff86c20bcc744be9",
      "bytes": 1465
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
    "primitives/4-4ring5.dat": {
      "sha256": "c25ff1e87c176ac2077f2e71bb210adacf0ff860b35635a5fd8dddbc22b7a654",
      "bytes": 1740
    },
    "primitives/4-4ring6.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/4-4ring6.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "0c552ed9e29c0d38cdc339b96f3563017a810b76",
      "source_sha256": "d47607450c3e7c3efb472d11ab9a4fc0941982c7eacd152a3f1988fa536574c8",
      "sha256": "f70e7b8133c3e86354384a92d231b861addf7a640c4dd03744b6b8fe7a0b3f53",
      "bytes": 1545,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
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
    "primitives/4-8sphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-8sphe.dat",
      "source_sha256": "37fa33d0b13605e0e1a84b8e0917953d42beebee08dc444e1bd44015acd64d9e",
      "sha256": "77369ba1c6a9a027b76a184638e2ce1f26847b3eee4c0ba4cfcbfd0ffbee0313",
      "bytes": 647,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-12chrd.dat": {
      "sha256": "39221c19a6c6e3f2cdca4414533d7ec88b162656343e8c8c8e81e76818fa8c81",
      "bytes": 524
    },
    "primitives/48/1-12cyli.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-12cyli.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "aa0e0569a9b9ee19c5790c90ad36bbbfa6a15f26",
      "source_sha256": "a645a42a5ed912a059a9336ab1449d02efd067008f034549cc8c5ae488159fd3",
      "sha256": "6368f8ccbdd066bb7589b39b17f19cdfcbb84c48054f44420027bddfa689c0c1",
      "bytes": 1004,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-12cylo.dat": {
      "sha256": "fa44c20ba3d1a552dc6161fa1e2a0746377a4d89769dec22ed412fec1343a33b",
      "bytes": 435
    },
    "primitives/48/1-12edge.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-12edge.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "fc36f0754ab8e4b664f290ce2de680abab109a43",
      "source_sha256": "c1320fa098058f1bb4bb73a4bd02a9533bdcc4f22ac4a0f0a1dcd5cdf85deaed",
      "sha256": "334814c4f3e50b2fc484d487cda5510ff3ac830a640c86cb66e94a03cb4ee8e3",
      "bytes": 567,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-12ring39.dat": {
      "sha256": "ab1501e5f4a9807edfc7a120eb74dbb1b3817ce66b5d228217f31e400699b61a",
      "bytes": 558
    },
    "primitives/48/1-12tndis.dat": {
      "sha256": "8b84480135a9228f85f020e31d5ac9d1e1b6bf2c861ac7588f67d7f76c0721f7",
      "bytes": 478
    },
    "primitives/48/1-16chrd.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-16chrd.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "530b8b442bb26899cf142f09ee56e6920c6c1876",
      "source_sha256": "612846540dad896fa0610b5f7eb9ec1f7a39c0bbbd68dd7e3a9114da1737173d",
      "sha256": "5130524dca42aff120e19fab076abc9510bdb856d63290da4d98f1656ae775c8",
      "bytes": 404,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-16cyli.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-16cyli.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "725976ded58e7729f0f289e648da9f258afddec2",
      "source_sha256": "b6fb5e76f958a18c4cc88866d5e6a0502b62d3abda1a72450663b82502645330",
      "sha256": "53c0d15be43de5851f19649b5496ca5b75c9846637571302bc74008a2e63ce46",
      "bytes": 887,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-16cylo.dat": {
      "sha256": "49a6ecac69f3ac27b6507e14d733c660f4d8c12c7b63070c7e7cef84fb111ae7",
      "bytes": 435
    },
    "primitives/48/1-16edge.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-16edge.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "e85e2d48d1dcd790055fd71e190cc07f615c0ec7",
      "source_sha256": "9b3b4df68d3c0d68fd3e5c52346871867043f67522e53aaa21991562c89bdc10",
      "sha256": "ccdb6fe6fccc748c6f501fab896982340f85ae2afadf123b9af62a6f71d9a9c0",
      "bytes": 534,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-16ring60.dat": {
      "sha256": "626cde2718f9f03b1f347ad84656134c184acd18ebc8afd3b5820316d29d3ccb",
      "bytes": 495
    },
    "primitives/48/1-24chrd.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-24chrd.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "0643656e30ff729f66a24e6d3854adb594fe2b90",
      "source_sha256": "9c1442d69aa0acfe4de87e4b9cdce8b164c88289640c9aa980afafb7b4aabd74",
      "sha256": "929b64cc76c28516fcb543067885e29a0140e07e754430e14b341e351a01761a",
      "bytes": 298,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-24cyli.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-24cyli.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "dcddb6c8cd9244d22b81c68475333199ace04ec1",
      "source_sha256": "5e767152f719b094442a5e68060781c9f2b7304595c6956bf98183bda00a9a36",
      "sha256": "ecf38060e5798c8f131d36f53d0c8377e41a29622434584d1d1cfc4addfcfe87",
      "bytes": 520,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-24cylo.dat": {
      "sha256": "9dfeaebc00be87f3075c523fc6a9abf40995f13922269dfaa196d441dd0ec772",
      "bytes": 435
    },
    "primitives/48/1-24edge.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-24edge.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "d52ab951ac56c87c063b6e00cfd690536898a06d",
      "source_sha256": "0946112b54d72f44d95d9f48b652bec53468f05eaacb2503ca09f58bee518e04",
      "sha256": "70f2869161f0a555b5d8d2540c6a342be7e8978adb0f3688a572a039f6fb308c",
      "bytes": 613,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-24ring60.dat": {
      "sha256": "c604d4200bc51873e98c309c954b5355997bb44ae7964bf0248069ef4704cb36",
      "bytes": 422
    },
    "primitives/48/1-24ring9.dat": {
      "sha256": "6112fa286e194b22fd12266df416e4287207d45d5deddb4ae141b326262aee7c",
      "bytes": 548
    },
    "primitives/48/1-24tndis.dat": {
      "sha256": "f769b06c774328aa2cf54e119cebce97a4f8aeea36e71b060d9188aa34b3bb02",
      "bytes": 456
    },
    "primitives/48/1-3chrd.dat": {
      "sha256": "050869153366753715b8b3e9d32ba9c188fef1efc2e9f3ee9f1e7ddce5b9256f",
      "bytes": 883
    },
    "primitives/48/1-3edge.dat": {
      "sha256": "b510c69db75bc174820808d52b2a6ed53221e684b7414d3fe228862d125c9558",
      "bytes": 749
    },
    "primitives/48/1-48edge.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-48edge.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "5f72223e3317427b878bb373efa208fb271fdaed",
      "source_sha256": "89dbd38b8578e8fa60ce2f80e8d7aa9b20d53c31cf40d2d322519287e6eeff19",
      "sha256": "214478043d4609c3524b2605fc015e171b5553585c0eae83b682662781d22385",
      "bytes": 304,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-48ring9.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-48ring9.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "e5fd0eea5ea4f4951d401cbd9b77e65d003217bb",
      "source_sha256": "737eebf82b2c17353e2c9e499c657f58fb7f74d2745cd7d77a8651af4abb6aae",
      "sha256": "377f7e6682f2153b89ceddd43445c597a2cfa3dd1cbe4c9cf7fa77e7ba9edbe4",
      "bytes": 420,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-4aring.dat": {
      "sha256": "d3049308fc0e878c33c57cc57023e2e0fca1208846acae7272d2000274ef32de",
      "bytes": 657
    },
    "primitives/48/1-4chrd.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-4chrd.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "b7d58092bc58cd7e6e7bd74f79d90ed408992c5d",
      "source_sha256": "a735a3d5f7652eb4c1ec7fd2fc2d6fcbb0d54cd647cb92c60e64dd3ba000b0a1",
      "sha256": "0dd21d0021743aa0362b4bf352ef92bb366515827449376891e9bf655c91c7fa",
      "bytes": 888,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-4con1.dat": {
      "sha256": "5654b2cbaa3b4364f214df3f5c40ba67168e5fa8c283140e4081f78a68c52e27",
      "bytes": 2220
    },
    "primitives/48/1-4con30.dat": {
      "sha256": "f00e06482dac3f053dd855236562f5baaf27f7cc234c460f96e884d9483cc8b4",
      "bytes": 1908
    },
    "primitives/48/1-4cyli.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-4cyli.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "6d8bfaee55e3163927c20408f12b9b0154d9b1e8",
      "source_sha256": "5e8053b8ed19ced455c2dc447b227fb0fc2f52bbfd55971415972c41d24bf24a",
      "sha256": "dea4873414fa267c3d0469094432155cd5cfd8b54ea31f7ae61c68924630e2a6",
      "bytes": 2370,
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/1-4cyli.dat"
    },
    "primitives/48/1-4cylo.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-4cylo.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "38d3a23eed09d4236c71568d7e9dd1db0cb7c7cf",
      "source_sha256": "93f7305e7575678ae00336972ca5078611c37a02d9755865d38cea4ff122c345",
      "sha256": "d077c4375e995b78f434bb4c4f109123458377885400a4f819a07d7432ba6b3d",
      "bytes": 429,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-4disc.dat": {
      "sha256": "6b8ed56f674540a4cfaffc68441f7e8c37283f5ea34dd401f9124b51536de29d",
      "bytes": 1157,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/1-4disc.dat",
      "source_sha256": "cf481d56b2c13dc2a6bcfe5eadb6577f2435b3f2f50fcdca199be76525d773ca",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "primitives/48/1-4edge.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-4edge.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "916e1580f1d1a1da351d923cfce468481e047468",
      "source_sha256": "c226dbaeae1ace68469442970573d61901c3847bc2470fafb31a867900e55d3f",
      "sha256": "5f178a1d3de8ee14d0247effcde528ed65c9373673022871f0087d83e0d6346d",
      "bytes": 1166,
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/1-4edge.dat"
    },
    "primitives/48/1-4ndis.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-4ndis.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "19139ceeee4606cfa8f8974c4e16bf421e9aae16",
      "source_sha256": "4359a309a22272c7b82b284b28c99bcc0a120c34e5ea6351e59da356890b84bf",
      "sha256": "53003afcb26e28c68a612e30208ae17996d935365f104335bc4d1795e7753040",
      "bytes": 1106,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Franklin W. Cain [fwcain]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-4rin15.dat": {
      "sha256": "9c4d9fcf0fb6f58d2e06ffc71c42c6a58716f1342d0845d737da01ff471219ea",
      "bytes": 1351
    },
    "primitives/48/1-4rin29.dat": {
      "sha256": "a8701377d8fdb3e414acb2095194e2a6a06c6874aa7ef8933f03fed800d6bf1a",
      "bytes": 1230
    },
    "primitives/48/1-4ring15.dat": {
      "sha256": "6ffd77783ca6b74be3c5d01ddc44a5edc30e92f11bc3f744c9013f9ac2dd66a1",
      "bytes": 1340
    },
    "primitives/48/1-4ring17.dat": {
      "sha256": "96a8c54c3546cc7ed5f86cdd0148ce2022c86034e9798bce2aad2628d36d9af3",
      "bytes": 1239
    },
    "primitives/48/1-4ring18.dat": {
      "sha256": "4d99fdcaa74e59fc2a61040bd968be4bd8172d6ee85856d45693f0fac7b5d3c3",
      "bytes": 1466
    },
    "primitives/48/1-4ring24.dat": {
      "sha256": "1114138b69dab9c56b9d957175cd487f91bad7622fa8762cbdea09e57db217c6",
      "bytes": 1154
    },
    "primitives/48/1-4ring29.dat": {
      "sha256": "b793d694bf4704101517a49468b8d98bac002a6a122306271cfd1dc6315f391c",
      "bytes": 1219
    },
    "primitives/48/1-4ring3.dat": {
      "sha256": "9baaebeb37309ecda043b5e669dc098dbbbddb239a0a72e381e4773d513347dc",
      "bytes": 1465
    },
    "primitives/48/1-4ring4.dat": {
      "sha256": "f0c5577935219719a583b20bfa44253b963c69f4d560339be39aa4121f35fe6d",
      "bytes": 1452
    },
    "primitives/48/1-4ring5.dat": {
      "sha256": "242a22ce13c71f951a77327cff0f4cf6ee8dd54163dd6a3d6dbbb0cf4f5a441f",
      "bytes": 1389
    },
    "primitives/48/1-4ring6.dat": {
      "sha256": "44614d954a3fec6d92b8cb02db4536fe4821693d16eb0b16dc043ac519956d8f",
      "bytes": 1282
    },
    "primitives/48/1-4ring9.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-4ring9.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "777e58e46ad7c17405e434506d18b470da01cefa",
      "source_sha256": "08cf8697a97526c9636b00578b792ef8452d3f74d7615e3a1d5644417908b42a",
      "sha256": "dc71a8f9a26d4407697b27df684dc1b433ab72afcaf47a78ffb96da47a591713",
      "bytes": 1344,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-6cyli.dat": {
      "sha256": "71c9378c265ebdfcca8b665d1a2fc8c05127f7dc699da4beca489e35708815fe",
      "bytes": 1722
    },
    "primitives/48/1-6cylo.dat": {
      "sha256": "1ff68109e776e0760b2b5c3a8609527e8e59af6c2708ac9dc8336d94f189b875",
      "bytes": 431
    },
    "primitives/48/1-6edge.dat": {
      "sha256": "4377dc9062b734ec461b99bcb048bbb75ec0cada84f0ee948fa63558cc3e5973",
      "bytes": 785
    },
    "primitives/48/1-8chrd.dat": {
      "sha256": "50ee0f15eee9b2b51d09898d50a32c224129658a43bdee8eb23db4b00bf70e22",
      "bytes": 594
    },
    "primitives/48/1-8con12.dat": {
      "sha256": "c24199bcf072b6e5a55338969ae5384d00102576e69a1fc8df35a4be21988b80",
      "bytes": 1142
    },
    "primitives/48/1-8con2.dat": {
      "sha256": "4086a498bd7a55300dfee10b92e1518f7efe7c9bc55201fa3daf2f01ebdfa65a",
      "bytes": 1114
    },
    "primitives/48/1-8cyli.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-8cyli.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "f5d76751793ddd1201aa1222de82bc39630f3318",
      "source_sha256": "494069ca353e41885bf8f5b6b3ddc9b62aabeca3eedfe6aa5597ac8f12ca12b9",
      "sha256": "6c98423d311039aaa117186b97922454fa0f8a858a8827ddcf5882dcd124e396",
      "bytes": 1331,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-8cylo.dat": {
      "sha256": "eecd604dff0bbf2e299d1a9f3c5e44a6e458e4dc1564415ef84d79a1f02a23e1",
      "bytes": 430
    },
    "primitives/48/1-8disc.dat": {
      "sha256": "4546d4f66d74b36bba214910c636e3004cb40ad6175516bedab9a789bcdec2b8",
      "bytes": 667
    },
    "primitives/48/1-8edge.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/1-8edge.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "7c04934e6383dbb7698196c1f185fb4a304149fc",
      "source_sha256": "eec30153f06bac336ca71ae16b31c5d0c7ae432acb5e91befe37fdb7b6bb1c8e",
      "sha256": "86118447861aad149cf2f16c0737d34013c7ad45c0bb02a5b622375ca69ed5f0",
      "bytes": 690,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/1-8ring1.dat": {
      "sha256": "a9fd0f3c1d552143128cb3823cddffb8513bcf42979683e9746e7a20dca6e720",
      "bytes": 630
    },
    "primitives/48/1-8ring2.dat": {
      "sha256": "a4e7bd85c4f4784b3c688b7b171549fb2acf130ab0b4a9d02419f1c2d83863fe",
      "bytes": 649
    },
    "primitives/48/1-8ring4.dat": {
      "sha256": "9d38a1051746bfeb7cba6a1e1a08bb45a8d0bf03c66612b113c755fad14c52e1",
      "bytes": 620
    },
    "primitives/48/1-8ring5.dat": {
      "sha256": "ad1a24a91355974cd29c4407c1ad9c92278e359230e92db54d7dd45f1dab5a21",
      "bytes": 797
    },
    "primitives/48/1-8ring7.dat": {
      "sha256": "cc43ccae5e41789c11a5a294fb523a84087c38ff9c95e1cbbb4bf3c029d13056",
      "bytes": 630
    },
    "primitives/48/2-4aring.dat": {
      "sha256": "d739013e7a8dbf6b6c7a31c08f0723a8d51c1b6b782b85cff52729f8ece3bac8",
      "bytes": 784
    },
    "primitives/48/2-4cyli.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/2-4cyli.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "0cdd7c7fc90aa3bdba6c971f5bd42c2eee438b6d",
      "source_sha256": "685652b02ba31d357cb53ab845f0256a3d1580f530d28e57e9a34fe00e82111b",
      "sha256": "0bea7e94e2d1bdf4880ed975ccfb69f338a49c86ef3a2973b577a825cd0e4649",
      "bytes": 3613,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/2-4cylo.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/2-4cylo.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "0d91512c8d9d0341395ad4d9f85149fd99ec04fd",
      "source_sha256": "8664bb8070cc7b44b3f60c6dde9c3a96b2ef5f20e6585d340d543441d356e50c",
      "sha256": "1fb52f93304e78719db1e87a08e1ab3a1c268fb6f8e0eb65f4962b3fd5830933",
      "bytes": 424,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/2-4disc.dat": {
      "sha256": "ae6f5fd3c3a8bb9443fbb017e5782be74d01fd1ec82c98041d70717fc9127af7",
      "bytes": 1410
    },
    "primitives/48/2-4edge.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/2-4edge.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "d6e6989b77466c2b91447ef71b92a0873992ef6a",
      "source_sha256": "089135a4d800788ba85802810eef7da033a7759fd6d6fe5cf3547512d83265b1",
      "sha256": "456a16ca167c2ce29f675e46f5e3b24aa6bc3658346e794b1c218881d3d0aea3",
      "bytes": 623,
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/2-4edge.dat"
    },
    "primitives/48/2-4ndis.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/2-4ndis.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "1560641228a0270d51f7fe692ed954f49c72e3b6",
      "source_sha256": "cf41e8d57710415bc170b8b20817ee213d2f74d18e0077d2e928915539e5ad43",
      "sha256": "01eaff0d9aa4785c8e26ca0baa945d0baddd99ac4615e666690df0a879ca67f8",
      "bytes": 1431,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/2-4rin16.dat": {
      "sha256": "6771e5d515c4b7ca446f347006c422579e62845216f15d5118f6b5e28e0e7e49",
      "bytes": 2091
    },
    "primitives/48/2-4ring16.dat": {
      "sha256": "c6374564986ee8f722d283c9ccaff6eea5c9ce81e917358cbeafd828f76bcfb9",
      "bytes": 2080
    },
    "primitives/48/2-4ring34-d0ecb8923c.dat": {
      "sha256": "3444cacefffb5eb63b708abeabf03095b453c4514bc8d0efc31e56d9996f1a03",
      "bytes": 2086
    },
    "primitives/48/2-4ring34.dat": {
      "sha256": "3c5dc48c2ed72faf647f7252dd09aff742aad81219859f50530817300d87c3af",
      "bytes": 1946
    },
    "primitives/48/3-16cyli2.dat": {
      "sha256": "06cf30f20a488d5bc6ec2468dbbb149f836cfa4b34a36b397d8596d5cbf65999",
      "bytes": 824
    },
    "primitives/48/3-16tang.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/3-16tang.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "23e244e2c3cb08607710b5b347d9c580964e158f",
      "source_sha256": "722f7735056716e2c2610c785c78a4ad5f6799a86d62867829cee8741367bb08",
      "sha256": "733d64ff349d4d2f6b33ad302910e0144c017b1c294776bb55d605f6c83d9d68",
      "bytes": 661,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/3-4edge.dat": {
      "sha256": "fddb7db803f4cc7f994ed07aa3b9ef38b92ee7e349899d1b111eb845c4b2590e",
      "bytes": 1824,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/3-4edge.dat",
      "source_sha256": "e4cdc8e4b71fc79b641d5049507aac6c34da1b007c94205f80087fd7470608fd",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "primitives/48/4-4aring.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/4-4aring.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "7bc8c70153a6807c19f7349ca719ed18a9c93c45",
      "source_sha256": "4c0d575f91df941b5d3313427d699813cc3cf9f09c334cbad7a0eceeaf98f573",
      "sha256": "6b4b2c284d9791e85e5844e1673546f2ab3f13345c1e3207a314d0c127422e57",
      "bytes": 1326,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/4-4con1.dat": {
      "sha256": "655ec27e69ed53dce5149caab12984979da35d9cc6c91be6255d9d1d4bf2d935",
      "bytes": 6854,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/4-4con1.dat",
      "source_sha256": "5ca89004f2d7b650811f1a0537ca6a62f1eeecdd40052e033e76edadc0ac5061",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "primitives/48/4-4con12.dat": {
      "sha256": "e227ac04eeaa86ca457244430db686cd8c3310898ee17c21b42e04577efb2325",
      "bytes": 7064
    },
    "primitives/48/4-4con18.dat": {
      "sha256": "2d4d987d7923e673cbfdfee6874ee19bd631257f4802845a6ffd50b40c67c165",
      "bytes": 7232
    },
    "primitives/48/4-4con2.dat": {
      "sha256": "8224455d2f295cc3b8378828203bb8f160fd012c513d94b846e36e6d427312bc",
      "bytes": 6806
    },
    "primitives/48/4-4con4.dat": {
      "sha256": "788754f709cea7a3ee4148b6c983d0af1f1c93cf2357eb1eca2daaeba61ef01f",
      "bytes": 6631
    },
    "primitives/48/4-4con5.dat": {
      "sha256": "bfa2cba607cf71d891f9a6bb60002579b8df66749bc7afd34e9ec2c37f8e53a4",
      "bytes": 6599
    },
    "primitives/48/4-4con9.dat": {
      "sha256": "b018c414a9227fdfa35cc9e5a3822ca8b65d426ce38eea9a8dea4fe80714046a",
      "bytes": 6436
    },
    "primitives/48/4-4cylc.dat": {
      "sha256": "a11866589f03928663a5021063324768ff0ddb56116c7924bd09900fc81bbdbf",
      "bytes": 528,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/4-4cylc.dat",
      "source_sha256": "1535177acbdf5b04fa32a14b78ef80e6ce8f2f786261a14c2f7d3d8759265a03",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Alex Taylor [anathema]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "primitives/48/4-4cyli.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/4-4cyli.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "359725c37d886ff0540f266e7b3ceab0d225244c",
      "source_sha256": "6d5c1ce5a53103c124d5ff00564da37c9ca1ff30803c564533c67728db86658e",
      "sha256": "c8d6aeeff889882cd2d304e44fa4dfa0845cfbc230ed3e2e75b7f7c464fb9a60",
      "bytes": 708,
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/4-4cyli.dat"
    },
    "primitives/48/4-4cylo.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/4-4cylo.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "5cc29cf5232aeb3ea196819afa8114ff9fa9602e",
      "source_sha256": "61a119ff47a0e47fda2d24f93cb0296a8d834bf1af43cfe1887ef754cfc88290",
      "sha256": "b96f8e67eebc02e00355599334350543973d647c91d4d3ece0e2b2323b85a6e3",
      "bytes": 424,
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/4-4cylo.dat"
    },
    "primitives/48/4-4disc.dat": {
      "sha256": "157830fa8ffd6c889a284e780fab28d2c225f68f912613f3f1431aaa90a09720",
      "bytes": 2668,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/4-4disc.dat",
      "source_sha256": "f309e628f06a3a422234c393cd69db8fcd376f84d36ef46da5710f352efa8f68",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "primitives/48/4-4edge.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/4-4edge.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "fbd1b629999bc7ebcb9b836439eae29278046a41",
      "source_sha256": "111a5cde2897dbe23aeea7e48917323ec0573f75da04c62616277d17d83fc567",
      "sha256": "5d5acf924e5190fedd2adf32e826318087676f2f82f0cd1ec0b0ca9501739296",
      "bytes": 736,
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/4-4edge.dat"
    },
    "primitives/48/4-4ring13.dat": {
      "sha256": "1d1efbeb31126cbf837f792663cb89b8b888724a205f03a742e04e7a0cf40d29",
      "bytes": 3805
    },
    "primitives/48/4-4ring14.dat": {
      "sha256": "e4db08db80b62e88e5129f01c016013e06a35d83d5e6de054951d8aa5cf7e179",
      "bytes": 3706
    },
    "primitives/48/4-4ring19.dat": {
      "sha256": "cd03cd7f64d4402dfc324bade84c0265aa806b3d08ee70b1756388ea9a1367d1",
      "bytes": 3724
    },
    "primitives/48/4-4ring29.dat": {
      "sha256": "9cd167f84e5aec7e303c457b4424c9b7e76ec119a21f15fce757011785e48b5a",
      "bytes": 3754
    },
    "primitives/48/4-4ring37.dat": {
      "sha256": "5b9b24b36b7adf6a7b121879eed1ea60c4a1092f5d554a901aea45f91a8befab",
      "bytes": 3932
    },
    "primitives/48/4-4ring4.dat": {
      "sha256": "6647f282392d4ae624de533ff6ff781de4a1d5c857c4a959eec924cdbe02e5f7",
      "bytes": 3567
    },
    "primitives/48/4-4ring9.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/4-4ring9.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "9932c647f2331e134af89990344249b2bc8dbf2e",
      "source_sha256": "d8de1753705319aa11a189b579323b778c9b6cf4869360e698c64a8a0cdbf3d2",
      "sha256": "11fbb373c98eb8318230f051626af3c4ffe4463d027043262e47cfdaaa94104c",
      "bytes": 714,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/5-24con30.dat": {
      "sha256": "4e67cb843775f9228df2e6ba2e918ba0d9da3133463ce49a00ad6d781888d0cc",
      "bytes": 1682
    },
    "primitives/48/5-24cyli.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/5-24cyli.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "ca18301457e5803fb4d7de116f36f6a351488db9",
      "source_sha256": "32b15a6570d6f5534a620e667a26b86298596ed9d064a0a9b1886d413c345658",
      "sha256": "c49297cf451d5085432b3ab5a48bd87112abc02a3ef7e7262701addddd10373a",
      "bytes": 1784,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/5-24cylo.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/5-24cylo.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "50e87909b8bec0a7b9e98c3083ecae2f798af6f9",
      "source_sha256": "f6b98815d032ae56c7e0bcc3bd02c2295e0fea90c4bb8c8c7bf9207c0500f71a",
      "sha256": "26e92ecdc6528104acc32668da9962511f28d382be6484b4488bafda33d926b8",
      "bytes": 435,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/5-24edge.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/5-24edge.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "39b84365d6657598778e8a8c1de9129a17f4b793",
      "source_sha256": "98f6635f6593350b1a5987341291fc1cf17674c28ced8a421a69d1ec17b39575",
      "sha256": "ddb6d4a1eda5fc0bd2c2c6899abb271db2c1084675ce6f135222456ee25b89ab",
      "bytes": 579,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/5-24ndis.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/5-24ndis.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "6d2831b5fda046553f0fa949b9a36bb814ec19f1",
      "source_sha256": "5f6d791e3876e891e3f8e0b6d7e7387f73879ff25eb28fd16c4038c2607064f0",
      "sha256": "cd9822ddf511472ac1713c435b2b607026ebed4b66a2ef557798e140b7332fa1",
      "bytes": 707,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/5-24ring24.dat": {
      "sha256": "ec0b943679f27b9f1e09ef43bf5ffd43f29dea6ad489bbbee3c1dba895b4a69b",
      "bytes": 982
    },
    "primitives/48/5-24ring4.dat": {
      "sha256": "337ff283ede81f2354f469e147dacea4ad4b91d6b41054e9a37d9415706fdc36",
      "bytes": 912
    },
    "primitives/48/5-48chrd.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/48/5-48chrd.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "1ba2a3495bae26df7e8125f5da79c23c4823e157",
      "source_sha256": "2de0191722623a86aa2faecdb37db3b2350f527e8383019006241d2ad02d193e",
      "sha256": "1feb7014423c8ecc65027711b1e19304b3576225e9253e915bbb143bb69d0872",
      "bytes": 455,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/48/5-48cyli.dat": {
      "sha256": "92cd02ef8d75a989ec2d00695e5e0c66483c773b54c7931475d94193e67e6ef3",
      "bytes": 937
    },
    "primitives/48/5-48edge.dat": {
      "sha256": "49de7b7d16002fe69124628524ae62bb766817b33de2d5412706d2e9c08a68e0",
      "bytes": 406
    },
    "primitives/48/7-48cyli.dat": {
      "sha256": "3154297a7a99038407a76202a00ad77b00479365a702e504208c51445a98d190",
      "bytes": 1266
    },
    "primitives/48/7-48cylo.dat": {
      "sha256": "18059fae8e1702a8365e430176e8890f62ba763a616ea78e5e2198909cdf1ea4",
      "bytes": 435
    },
    "primitives/48/7-48edge.dat": {
      "sha256": "6a95e9ea56c6f5128ea68876b1e3ea986223b7b688813bfc79e4ec16a88ebb38",
      "bytes": 533
    },
    "primitives/48/7-48ndis.dat": {
      "sha256": "b78ebe5c7731a9bf0f93767dd6393f92ba3ccba7cb1661bc57562f0665661f9e",
      "bytes": 583
    },
    "primitives/5-16chrd.dat": {
      "sha256": "23956704d316445d12e551130f028956bb51b01d59f954b70568763aeb74e8b8",
      "bytes": 353
    },
    "primitives/5-16con12.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/5-16con12.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "042577cfe580625cca5c1c6be2e0bf9fac7b2e80",
      "source_sha256": "79a3bf15e88acc5bd4b3d70eada62f6dd14d4845eb32d7264238ae2593240162",
      "sha256": "e23c1bccb3888fcad96248822396afbf43b7ab967a71745b2173ed6b8efb2130",
      "bytes": 973,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/5-16disc.dat": {
      "sha256": "d49026914aaffaa2600f7b76932b726abfa121ae0c80618d680f22498ed9d174",
      "bytes": 446
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
    "primitives/5-16ring5.dat": {
      "sha256": "c5c6927c97347c31ca625cbca13e5b957d03237870c2ab253c295f71daa03cc7",
      "bytes": 643
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
    "primitives/7-16chrd.dat": {
      "sha256": "bb11b76d6a1dc0af22fa2f0bfaddce73c9a50d4f2adefd15360107c6493d45ed",
      "bytes": 587
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
    "primitives/7-16disc.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/7-16disc.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "5c6194204b19aff82a0ff061406ee60b3c0143f3",
      "source_sha256": "e2b7d25dd344d198c6531407a0f19889203c2f5114f18365379ac5f5a429f603",
      "sha256": "6517b683690245f5c5b653e31570a2b62df9332b3b92ffc8fe07da5a07319183",
      "bytes": 694,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "primitives/7-16ndis.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/7-16ndis.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "9a2470e33499af16079b3d6d03906c53c509f179",
      "source_sha256": "a8feb7ba9c98a9ec3a2b4cb697d4dc2142d0c0c4c11f76a8761e3533ab6b5a7e",
      "sha256": "f0f9fa3de12267aa92203ff1f5c5de2ad7e2e08a8a0dc0dea9f3589134d46de8",
      "bytes": 529,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Alex Taylor [anathema]",
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
    "primitives/7-8chrd.dat": {
      "sha256": "1c13a1b9087f8475db2ca4f136599124ea2f209f32556c65305b8ac51d0fdffc",
      "bytes": 800
    },
    "primitives/7-8cyli.dat": {
      "sha256": "bfab56f125b94840c7c159a03784d895197996d4fa43ca5a83c3cad9440f8e77",
      "bytes": 2247
    },
    "primitives/7-8cylo.dat": {
      "sha256": "a820998f280daa42c3aad4918784173dd9589701b4834d4158bde8b329895da6",
      "bytes": 403
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
    "primitives/7-8ring2.dat": {
      "sha256": "6e362c7f9144dadb002475a79d84b59a448f6e9aa8217a4b39858359f18ad8ef",
      "bytes": 1119
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
    "primitives/8/1-4cyls2.dat": {
      "sha256": "0f6d521fd732af2b4fe7d102b4190472459ae0fab372e417aed303e26dda20f6",
      "bytes": 460
    },
    "primitives/8/1-4disc.dat": {
      "sha256": "5f55f25fe218512fab98fc10c608bff9acfbed17f406a0b053ff234644fd539f",
      "bytes": 352,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/1-4disc.dat",
      "source_sha256": "cf481d56b2c13dc2a6bcfe5eadb6577f2435b3f2f50fcdca199be76525d773ca",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
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
    "primitives/8/3-8tang.dat": {
      "sha256": "86242e69be5a948db00abfb42b6159a774d5b6dbd4cb75c29d508941c9c0051d",
      "bytes": 388
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
    "primitives/axl2end.dat": {
      "sha256": "9610490f4bb2eea4e586d7b31dbcb2567118c500d6287a4c9416181285b18c98",
      "bytes": 1097
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
    "primitives/axl2hole.dat": {
      "sha256": "412dc2cf2d3676e8ac3cdbcef57001b3b32ce1ca9edf119e7f219dfd3a039812",
      "bytes": 1291
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
    "primitives/axleho10.dat": {
      "sha256": "451e6612dd6be87e5c38591ee6a9752e65c0f017c69208af56c822bfa0077ada",
      "bytes": 1714
    },
    "primitives/axleho12.dat": {
      "sha256": "52daf64b6e604f521522466f97c2edaa2e4a59a2a3852381fcce8599af48945c",
      "bytes": 2208
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
    "primitives/box3-9a.dat": {
      "sha256": "5d543ab51c261ed6763ab0982ab574d7dc54914b152050644285659c81a3e213",
      "bytes": 425
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
    "primitives/box4-3p.dat": {
      "sha256": "b5ed509673f08147f082316398a7ca42a66d6281643d3a8df8927f97610c93ce",
      "bytes": 707
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
    "primitives/bush.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/bush.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "523eddea0607bc8e9c9f7172e84e36f1ce80292d",
      "source_sha256": "1a0a36c0bf653cc22db692447cfb959c478ec10aa28b9e9ee18f111c79f6d545",
      "sha256": "86681a584181ffe7878c3cddc4f2e0c49bcd95a88406e672ff854aaaa8e72061",
      "bytes": 720,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
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
    "primitives/bush1.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/bush1.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "17f0dee4f60d5c01c0e0860b810a0d6802056d38",
      "source_sha256": "10ed5f50466caa36daec154eb76958d37a8855aba820934a2a8b8048525b5e83",
      "sha256": "8a161f6d5970dd6201f53f7d1a83b2afff5088f658740ccb326c5e732301cbe2",
      "bytes": 2085,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/bushloc2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/bushloc2.dat",
      "source_sha256": "f1dd4de70690f3811fa32802611f41cfc9702fb737690af0abec78495e5678da",
      "sha256": "c25eee43e0fdf7bb8c0b067aac4da11e484bd8b07fccd48c434c6b5f6bd438e5",
      "bytes": 8273,
      "modification": "Dependency paths renamed to shared asset folders; geometry unchanged.",
      "author": "James Jessiman",
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
    "primitives/clh1.dat": {
      "sha256": "b222f25668c5ebc6b7c4f21fe0ef7cc3d87626982f634d0f3ef01ffc96433134",
      "bytes": 5365
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
    "primitives/clh3q.dat": {
      "sha256": "a1660d40ffb8e25c069f3dfee2e5c04c3bda93d78814ae9c253abdfedf57967e",
      "bytes": 3326
    },
    "primitives/clh4.dat": {
      "sha256": "8a24ae54b153079851e9bd3d41d9ef52c867ded1d7c82630a16bbe858d15be7e",
      "bytes": 2072
    },
    "primitives/clh5.dat": {
      "sha256": "f24c7fade9701a2b8115552c9ae1c583d5b7fcd85082302657681d0905521c20",
      "bytes": 21229
    },
    "primitives/clh5s.dat": {
      "sha256": "0926dd22bcd6917739d1c57004676e70d5f75d83f87a821f38b9c88e6f2fca84",
      "bytes": 6762
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
    "primitives/clip15.dat": {
      "sha256": "9984056356bc6a4ca964823caba0e0b182fe99b5dcb37cadc2f1a0e5a42b22ad",
      "bytes": 2752
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
    "primitives/clip7.dat": {
      "sha256": "f56c239f29a484f8769627517703353d65b5552f956c6fbcd57bf9dbdf7121b6",
      "bytes": 1847
    },
    "primitives/clip8.dat": {
      "sha256": "b1e0b429281372fba149a2443691b793a7d12cecb9ea0afb8f11ae1112c2c531",
      "bytes": 2425
    },
    "primitives/confric10.dat": {
      "sha256": "be83154072905c9b41202b8e4e1c3041619d1791c838e941eada647b5283c274",
      "bytes": 1497
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
    "primitives/confric6.dat": {
      "source": "https://github.com/ldraw-linux/ldraw-library/blob/master/ldraw/p/confric6.dat",
      "source_sha256": "fa5491072e4b1f3d99219bab67145032e3ef91c9690c6bf5a8eaef5dba2816af",
      "sha256": "fa5491072e4b1f3d99219bab67145032e3ef91c9690c6bf5a8eaef5dba2816af",
      "bytes": 18696,
      "modification": "Public LDraw mirror primitive copied without coordinate or dependency-path changes.",
      "author": "Donald Sutter [technog]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "primitives/confric8.dat": {
      "source": "https://github.com/ldraw-linux/ldraw-library/blob/master/ldraw/p/confric8.dat",
      "source_sha256": "a4f8826b1cf08c19a30f91c02272b65dbe6c6b7d8cfe81cda27767ff3e39c66f",
      "sha256": "a4f8826b1cf08c19a30f91c02272b65dbe6c6b7d8cfe81cda27767ff3e39c66f",
      "bytes": 17056,
      "modification": "Public LDraw mirror primitive copied without coordinate or dependency-path changes.",
      "author": "Donald Sutter [technog]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
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
    "primitives/connectcollar1.dat": {
      "sha256": "7378d9dec34a0cd5800dfd72fb83a70d96e02e5136965376474c636dab434564",
      "bytes": 3829
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
    "primitives/connhol2.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/connhol2.dat",
      "archive_member": "ldraw/p/connhol2.dat",
      "source_sha256": "3748d67fa7aef4d3d5f6c5d78adb2f9c6b93ed403159455f7e5f702d6ad390ec",
      "sha256": "d6eb99cfcb85890403a5db50fa125dc8b6f7491d3aeb2b8a6f6748428bf08a8b",
      "bytes": 930,
      "modification": "Official Git repository file downloaded at pinned commit; dependency references normalized to repository asset paths; geometry coordinates preserved.",
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905/ldraw"
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
    "primitives/filstud2-a1f7eee4fb.dat": {
      "sha256": "c24f0f4fa6c15a132ca364145bebf5e7f3feae93ccf254b9114cd19a789f9ce6",
      "bytes": 5948
    },
    "primitives/filstud2.dat": {
      "sha256": "dbaaab1c1f34a9d5bb3f06a29f0bc86879ea9148f530212c8f71f8f076c230b0",
      "bytes": 5542
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
    "primitives/handle.dat": {
      "sha256": "cac4f224faf61142aed5f8ce531417899705ffa208288a03d5245ed2e881ba82",
      "bytes": 1426
    },
    "primitives/handle2.dat": {
      "sha256": "d28a3138c272fcbd40f296e15b909f4ee18e457a777c43069105bb5946ff6546",
      "bytes": 7680
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
    "primitives/high-resolution/1-12edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-12edge.dat",
      "source_sha256": "c1320fa098058f1bb4bb73a4bd02a9533bdcc4f22ac4a0f0a1dcd5cdf85deaed",
      "sha256": "334814c4f3e50b2fc484d487cda5510ff3ac830a640c86cb66e94a03cb4ee8e3",
      "bytes": 567,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Willy Tschager [Holly-Wood]",
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
    "primitives/high-resolution/1-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4cyli.dat",
      "source_sha256": "e2ed297feaf608b7319c2e54cd81dcb653fbb3d87b5a8e48ab2f54b32953fc6b",
      "sha256": "dea4873414fa267c3d0469094432155cd5cfd8b54ea31f7ae61c68924630e2a6",
      "bytes": 2370,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Magnus Forsberg [MagFors]",
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
    "primitives/high-resolution/1-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-4edge.dat",
      "source_sha256": "e4ebabd21711f16411b3c8b8b278995a56c5f25919cd424976357da5b19943c6",
      "sha256": "5f178a1d3de8ee14d0247effcde528ed65c9373673022871f0087d83e0d6346d",
      "bytes": 1166,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Magnus Forsberg [MagFors]",
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
    "primitives/high-resolution/4-4aring.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4aring.dat",
      "source_sha256": "4c0d575f91df941b5d3313427d699813cc3cf9f09c334cbad7a0eceeaf98f573",
      "sha256": "6b4b2c284d9791e85e5844e1673546f2ab3f13345c1e3207a314d0c127422e57",
      "bytes": 1326,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Philippe Hurbain [Philo]",
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
    "primitives/high-resolution/4-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4cyli.dat",
      "source_sha256": "6c466cd94f69ecdb3a5a83faee52ad2e5ecd9d1560975feaf854c3433de6e6a2",
      "sha256": "5dc41009fcbca8bfeb96aac5195bcda7f48fd492fadfea70ae90341020f7d3e9",
      "bytes": 760,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Paul Easter [pneaster]",
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
    "primitives/high-resolution/4-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/4-4edge.dat",
      "source_sha256": "db8fd751c8c6b1f72211903adbff3aa90be6808cc4fcff391f1c320adced5da7",
      "sha256": "e9afab2bd8e20d6ab5dd1019151961a188233097f015e2bcadb30d79c7733d00",
      "bytes": 788,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Paul Easter [pneaster]",
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
    "primitives/high-resolution/5-24chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/5-24chrd.dat",
      "source_sha256": "1d95e3c2613cb23c7ee2731d8157ba2ac850641fe8ac890eb98f1d9da4a6f936",
      "sha256": "41bec7991be023f5af9bc959349dd5d721a8583d2b01cfd0f20b8f363d20d924",
      "bytes": 643,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/5-24cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/5-24cyli.dat",
      "source_sha256": "32b15a6570d6f5534a620e667a26b86298596ed9d064a0a9b1886d413c345658",
      "sha256": "c49297cf451d5085432b3ab5a48bd87112abc02a3ef7e7262701addddd10373a",
      "bytes": 1784,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/high-resolution/5-24edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/5-24edge.dat",
      "source_sha256": "98f6635f6593350b1a5987341291fc1cf17674c28ced8a421a69d1ec17b39575",
      "sha256": "ddb6d4a1eda5fc0bd2c2c6899abb271db2c1084675ce6f135222456ee25b89ab",
      "bytes": 579,
      "modification": "Dependency paths converted to project asset layout; geometry retained.",
      "author": " Paul Easter [pneaster]",
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
    "primitives/npeghol10.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/npeghol10.dat",
      "archive_member": "ldraw/p/npeghol10.dat",
      "source_sha256": "c0afbce636428be0d8a33c1f7cd50f9ccb68af2ae506b2bd7a7a9130d6076043",
      "sha256": "628286f0663bff4a0c953876fa1736925eb86bd5562671a94ae020ed7f86a301",
      "bytes": 3519,
      "modification": "Official Git repository file downloaded at pinned commit; dependency references normalized to repository asset paths; geometry coordinates preserved.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905/ldraw"
    },
    "primitives/npeghol19.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/npeghol19.dat",
      "archive_member": "ldraw/p/npeghol19.dat",
      "source_sha256": "29879c27995254faf9abb29a802edf44de07c806e681ae3740ecc04635103dbd",
      "sha256": "71f0b00c03a4d8b3c31a3c7819ec2e628e152b88632b8c2ae89e8c417bfa67ee",
      "bytes": 3338,
      "modification": "Official Git repository file downloaded at pinned commit; dependency references normalized to repository asset paths; geometry coordinates preserved.",
      "author": "Max Murtazin [SwampKryakwa]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905/ldraw"
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
    "primitives/npeghol3.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/npeghol3.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "913f91317e135bd9f4fa05558db0531c882ac182",
      "source_sha256": "4f580204560a77a088cf345168854a0492ea2448fed88d2b63b096bb2cfabc6a",
      "sha256": "a1800a6bae0a172152eb0a5d6ff2afd7e51718a01e6445d698ed8efc790bb740",
      "bytes": 1243,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Max Murtazin [SwampKryakwa]",
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
    "primitives/npeghol8.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/npeghol8.dat",
      "archive_member": "ldraw/p/npeghol8.dat",
      "source_sha256": "4fbb5add7705e3b5b485f27c2cc35c13c17ee8b1def98b952df314b0659ba7cb",
      "sha256": "3c19c757beb50a1c16a09037ace133b2750dbeef408c40ca9935f32acdf0bffc",
      "bytes": 3797,
      "modification": "Official Git repository file downloaded at pinned commit; dependency references normalized to repository asset paths; geometry coordinates preserved.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905/ldraw"
    },
    "primitives/npeghol9.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/npeghol9.dat",
      "archive_member": "ldraw/p/npeghol9.dat",
      "source_sha256": "218a7aace2e1d2b4d3b22f1c072a694fadb8801eb5591eb6bca4197808b466b0",
      "sha256": "d1079429f73a5aee8ed303c1963d40c434e57d797ffc57655933007f780b5a1b",
      "bytes": 1434,
      "modification": "Official Git repository file downloaded at pinned commit; dependency references normalized to repository asset paths; geometry coordinates preserved.",
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt",
      "source_archive": "https://github.com/ldraw-org/official-library/tree/894bbba5e696b1554800d8e45134c57163dba905/ldraw"
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
    "primitives/phandle2.dat": {
      "sha256": "63c1bafc629415f6962cb11cb55bd8d7bdc6570d90d0a5967dd448c43f8b4033",
      "bytes": 1505
    },
    "primitives/r04o1000.dat": {
      "sha256": "ab6bb3a5b9cf5aab8b43822e6c0df251eebbe03f51bdeb1a5f4d92dc5cb8a259",
      "bytes": 4787
    },
    "primitives/r04o1375.dat": {
      "sha256": "3bc2da2b7174879b6436db0c6a1054dce0e2b1d6f7bdecf6e4afc75e943ba1f1",
      "bytes": 4977
    },
    "primitives/r04o1500.dat": {
      "sha256": "9021f3b461c7df7b56428faa502a9d841353bd0c1a8437b6c7baf8821e3a60b5",
      "bytes": 4946
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
    "primitives/ring3.dat": {
      "sha256": "b55718f75b24b55b06bea809f2d87a5ce601072bd3cc7c54b4f8f4962d888153",
      "bytes": 302
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
    "primitives/stud15.dat": {
      "sha256": "d1bf4a207ca10ad943709cade1cffca41a2dae4c1b2bb0f825869db8b3ac6fb6",
      "bytes": 1157
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
    "primitives/stud23d.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/stud23d.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "31a60d34ed8f62697c9c3c92194f5a186c028fa7",
      "source_sha256": "19c03228775da6304d563dd5e3222d3b88b3dedb093ff32bade1a8ebacd95e46",
      "sha256": "4e0b85cbe68411150d72df4acab19bc4a7fcd927944599a4e296dca5b8dae825",
      "bytes": 342,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "primitives/stud4o.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4o.dat",
      "source_sha256": "827edfc93ece0c6898443bf247207e0a5182fcdaf30e1efb85285c9ab586e884",
      "sha256": "0a0cd8e3c7065c7325747f644a0222202f640d663f55d34b705a5efdd948af2d",
      "bytes": 565,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Magnus Forsberg [MagFors]",
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
    "primitives/stud4s2.dat": {
      "sha256": "9eb6b235883d5cbc8542177613dca0ace84626c845a181f14524ed401b8f942b",
      "bytes": 1472
    },
    "primitives/stud6.dat": {
      "sha256": "3909a451b30eb1a106c7c5ff5090fa2c130a3ca6afe73e27ed265e17b22e48ee",
      "bytes": 2462
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
    "primitives/studa.dat": {
      "sha256": "ba8fd5f8a50dbd595b75b2bf01750aa5ed36011ee3dab6bf85d7f2eac3a4712f",
      "bytes": 410
    },
    "primitives/studh.dat": {
      "sha256": "1740674c7489d1559d46591ab117aa4968a04b154cdba57eed4f628e33873401",
      "bytes": 1547
    },
    "primitives/studhl.dat": {
      "sha256": "ba20ae038aa00271c97a483ad32034e0c0093dc0beab527d46dd6e231672c8ba",
      "bytes": 415
    },
    "primitives/studhr.dat": {
      "sha256": "86e2af9e24086f2e3814e7700c49996430ecee50c6e2db1e5e0cd7edf9a6ce24",
      "bytes": 415
    },
    "primitives/studxa.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/studxa.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "b9e9f5075d183f85098ccf948959b912aa85a140",
      "source_sha256": "cf952b9f293281b6994d7b92c1d80cb7ee06e02a32c859540c3e9721007ed4bd",
      "sha256": "f5a29868c454a8dc817335a1ad5ec24ef8a5707444ccea5f40f5bdf6a1e2efa5",
      "bytes": 570,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
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
    "primitives/stug-5x5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-5x5.dat",
      "source_sha256": "e2f3c9299dcda5ecb768de44b94fc9bc0bb436e501bc1e6ecd8a2b7eb5f73b21",
      "sha256": "e2f3c9299dcda5ecb768de44b94fc9bc0bb436e501bc1e6ecd8a2b7eb5f73b21",
      "bytes": 794,
      "modification": "Official geometry copied without modification.",
      "author": "Michael Heidemann [mikeheide]",
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
    "primitives/stug-6x6.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/stug-6x6.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "367f92c9083e317a78d1041ea75cf9d2e8d55b60",
      "source_sha256": "c9863cf7834123f831cccd04f5e6d9b20c7681c63f906378d7c9a1f82ba47b67",
      "sha256": "48ac334dc233285c6d5baf0f44a265b1ea54dc569e0dec69816dd774c101c655",
      "bytes": 717,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Tore Eriksson [Tore_Eriksson]",
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
    "primitives/stug15-2x2.dat": {
      "sha256": "5fa08c28e6390cf093fd11dc4f69ae1efcb277659220e7d06fb15295bf200864",
      "bytes": 758
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
    "primitives/stug2-1x4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug2-1x4.dat",
      "source_sha256": "fca792de8f55eea1b35ec581ba94cb1aa5ad0967dd6af5ad3d7ed6ba0d0543b4",
      "sha256": "8e22255c2c9fba09eb9daf7a09ca4d03142d87a405ce1ac6db0aa6330ae8333c",
      "bytes": 468,
      "modification": "Dependency paths renamed for readable folders; geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug2-1x6.dat": {
      "sha256": "48c7eeef032e4a370ca688bf17014fb47c65159dc66c18665a3bd8cdaf9ba81b",
      "bytes": 556
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
    "primitives/stug3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3.dat",
      "source_sha256": "ab1e3dc6c68a4f8d4e63b03e12ba0965eb68aa896f7850fa25729601968787e1",
      "sha256": "ab1e3dc6c68a4f8d4e63b03e12ba0965eb68aa896f7850fa25729601968787e1",
      "bytes": 307,
      "modification": "Official geometry copied without modification.",
      "author": "[PTadmin]",
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
    "primitives/stug4-1x4.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/stug4-1x4.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "87de2cd57885e17c29f1a314c25cfed2e2d1f4c1",
      "source_sha256": "cac1698d3c02ad7044142afb4e8383d4d2c0107087f8a2814b4545c3c1727003",
      "sha256": "40b58152aed9f6d77df0bfccaafd9f9f2008409670e8da0034d544d835c2c7a9",
      "bytes": 458,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
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
    "primitives/stug4-1x9.dat": {
      "sha256": "3607666abb81d8ed51ef134ab0c7f65106623cb3ab02f529a76ff0f5b2f637ea",
      "bytes": 714
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
    "primitives/stug4-4x4.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/stug4-4x4.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "969b0d5b199275b85dbccba80f6a468884a78015",
      "source_sha256": "ca2483e11b95b453690dde974a4b27f536b4dba6e544ec98a9646e997850331e",
      "sha256": "7db137e893238e27a9ccb15d24477d1894aac345c182fcd20a8e12466c811ed5",
      "bytes": 480,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug4-5x5.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/stug4-5x5.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "6a08c058c6b28547f1b3c476f7bd8635da3256b1",
      "source_sha256": "865cd23e7f1f7cdab538bb289916c1f13ea9ad3fe97a874751dc99682c3cf9ed",
      "sha256": "ce72e99e662d062f029b84ed389375c9a34084735243ac5446f1254bcafa3323",
      "bytes": 424,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
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
    "primitives/stug4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug4.dat",
      "source_sha256": "977530a161304abc45fa2dbcac0e8a7df389d8ab3838a82702032a74dca9021f",
      "sha256": "977530a161304abc45fa2dbcac0e8a7df389d8ab3838a82702032a74dca9021f",
      "bytes": 307,
      "modification": "Official geometry copied without modification.",
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug5.dat",
      "source_sha256": "597146ce96a64ba1754d0ab57d7c7fa4acf700f27c4a54b5dad9d9fca63fb6c3",
      "sha256": "597146ce96a64ba1754d0ab57d7c7fa4acf700f27c4a54b5dad9d9fca63fb6c3",
      "bytes": 307,
      "modification": "Official geometry copied without modification.",
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/stug8.dat": {
      "sha256": "898856ebf5d5c32439842f6339ac4efa6e6ac375fda342867eac8e245b30b1c9",
      "bytes": 305
    },
    "primitives/stxjcyl9.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/stxjcyl9.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "d3504faedbf1e9a85e50afddbf68cbb925088d06",
      "source_sha256": "48180773ae296e9d0ba8b0a91ace237f96f5d66a250134d22a1e5aa0813e06ec",
      "sha256": "eb341fcaaf89919b7d191199eb36b9df114cdd44a8abf68d89513759acef7147",
      "bytes": 1617,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Massimo Maso [Sirio]",
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
    "primitives/t01o2500.dat": {
      "sha256": "f6f44e19a79a8f6de34266db8132c29cffc853c48540aee78b49955daad51ba7",
      "bytes": 17616
    },
    "primitives/t01o4000.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/t01o4000.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "1248ab7d98428493a40d7b6f675d328887c52581",
      "source_sha256": "649427b40541ede62e77cdc22b775a78f51e0bd01e3a8ddeed5ad249cbc7aab9",
      "sha256": "f6d5e0fe02963989a5bd9a7f78aa5bb048a06cb20caa39ac0aaa81d3607171d0",
      "bytes": 17675,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t04i0625.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/t04i0625.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "5d24aef17721d397d05f963ac03ed170162ee077",
      "source_sha256": "48fcbc70267d2cf21b8d9d29541349be9114b2623eec6cd678941385693ece92",
      "sha256": "5a04d2db208bfee6ef735db634a2eefc19a144c6ee05e3625ec4bc880f47af6e",
      "bytes": 5219,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t04i1304.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/t04i1304.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "b75860ecd9eb5d3a9f8cb1237de625bbdcadbb12",
      "source_sha256": "e23d62de56e98c40060f11106d93688dd6a53d5d92507673c4d3690184769cfc",
      "sha256": "10667bb9d58bc710c422538a79c3d99c96b26ef89848fc2690b833a40b21f7e1",
      "bytes": 5212,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t04i2500.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/t04i2500.dat",
      "source_sha256": "16a0e74be0e6e149ea99ffd6aff98b3406c19fc7727d0453b1fe1572cf4e40bb",
      "sha256": "16a0e74be0e6e149ea99ffd6aff98b3406c19fc7727d0453b1fe1572cf4e40bb",
      "bytes": 5104,
      "modification": "Dependency paths renamed to shared asset folders; geometry unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t04i2667.dat": {
      "sha256": "d46cb3e20d08b57cfdd204975a5a5edacda3814a4dec250d01efe52c802b4fed",
      "bytes": 5104
    },
    "primitives/t04i5000.dat": {
      "sha256": "ea8492b1e78cffee407c5abd257361745710427a22071f1ea1f0040838ceebc9",
      "bytes": 5023
    },
    "primitives/t04o0625.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/t04o0625.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "5e1fdb2356dc335cc911d39cdeaa521855abd5f3",
      "source_sha256": "1ffff6acac542399a766c253765472cab0cc3400018cb086bd020bef1e437347",
      "sha256": "83ef3f87aa87bb04a8b9ccc3c331ba46f2e07ea56698249f4977adfccbd227b7",
      "bytes": 5312,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t04o1304.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/t04o1304.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "fdd8504086b6eea3d84fcc5e23ddfec0eed2caa6",
      "source_sha256": "dccc3ce8b0f30334209b8a7225471e04e5e8ad56a0e601fc7231ae28a7b9f777",
      "sha256": "df51d90302be07d795d0bdd4f0e64ec789504b25401164fe367dc028711196cd",
      "bytes": 5285,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t04o1429.dat": {
      "sha256": "c1520f0558876c270ddf4b6f61d0aa0a4fa36ac61e6c3739901800bcacc49b65",
      "bytes": 5227
    },
    "primitives/t04o3077.dat": {
      "sha256": "4cc58a252f3625c3736df972572fe32bb4fc20bc40e55515d68411d92b597f19",
      "bytes": 5133
    },
    "primitives/t04o3333.dat": {
      "sha256": "7e82506016f98f4ffcde0b5627f061e5cb28ee9ccb7796bb7154d06406754349",
      "bytes": 5206
    },
    "primitives/t04o3750.dat": {
      "sha256": "78c8948b52885d0125d717ae48a783227558b917546866177d624567ad86f0ed",
      "bytes": 5086
    },
    "primitives/t04o5000.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/t04o5000.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "e8a465c9e023121fcb71f711b056abdf3436d3cb",
      "source_sha256": "e47c277d9f12130ea1cc1f9d3b03814156d0516190cb1d6baccccc94c5493f61",
      "sha256": "bec708d2e240f34d5aa8ac6b904a16ea32597d898f4373a22a09e6fc13d5516c",
      "bytes": 5016,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t04o6250.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/t04o6250.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "3b6e153062c12a63958c5e1d7f3bbf6ec127ba47",
      "source_sha256": "c09d0c876e3b54907f2640576924316922d686fec53bb64cf7379efa0d8e9485",
      "sha256": "fb83974033d6e2a37a9024e2c3fe9ea79e5cc06334be6aaae1d90c1f61a5c96b",
      "bytes": 5149,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Paul Easter [pneaster]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/t04o7000.dat": {
      "sha256": "b7ba9af81b906e67f21c76125dce4cc1f31aa35394955ccaba72f8cedea9599a",
      "bytes": 4948
    },
    "primitives/t04o8750.dat": {
      "sha256": "14b898d7dde7f0f0bee3ed993a5259a3c655c4ea14378be62d75f822bf1c2bfb",
      "bytes": 4972
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
    "primitives/tooth8a.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/tooth8a.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "e89862039087d2bc8bf89bca36420adb5c154d6a",
      "source_sha256": "559995fd4b5f537cb38c574b95ba4e8d5450c44102e0f9bf212e04ccddd59bb0",
      "sha256": "274fb934cf215f4edfc39f4974832970181543d01f59e7cd5efc87c2bef192d8",
      "bytes": 2112,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "primitives/toothb12.dat": {
      "sha256": "78437740d67311311871f5cff6c78872aad31348fa3a504a8e7f24144bb9324f",
      "bytes": 2888
    },
    "primitives/tri3.dat": {
      "source": "https://raw.githubusercontent.com/ldraw-org/official-library/894bbba5e696b1554800d8e45134c57163dba905/ldraw/p/tri3.dat",
      "source_git_commit": "894bbba5e696b1554800d8e45134c57163dba905",
      "source_git_blob_sha1": "336a3e80f01b515c8536d027939e460cb591a0c9",
      "source_sha256": "ce426082c057b7339e20e078303d4d7b401fca4544c857e603ad8ebd785c920e",
      "sha256": "f526c03b6d7401a9ad706e5f5687dbc6fa950d2ccfe1a533a8ba22c83084e239",
      "bytes": 826,
      "modification": "Pinned official Git blob verified; dependency paths normalized, geometry coordinates unchanged.",
      "author": "James Jessiman",
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
    "primitives/wpin.dat": {
      "sha256": "3e9094e0fcbc13664cc0f49433b3b3fa37a83965d40670717b8b5df04e7cde13",
      "bytes": 7016
    },
    "primitives/wpin2.dat": {
      "sha256": "0acaeffe4dd4585878135c33f7be30aef4be32ca01096207455c29f343dd2a6f",
      "bytes": 1086
    },
    "primitives/wpin2a.dat": {
      "sha256": "1c2ed101d8ddc360c5823259b4560b71dc70542a1e9b9731c46d63cb6d0d9564",
      "bytes": 1567
    },
    "parts/41239.dat": {
      "sha256": "d096574a1328ee0efefcd64438c675d5bb94ede66d65268909b440efedb1eb54",
      "bytes": 1818
    },
    "parts/66906.dat": {
      "sha256": "bed13b5817669ce070832a31e6232d63fb1ee2824cd10dea190e817db4769495",
      "bytes": 318
    },
    "parts/6628.dat": {
      "sha256": "4e09593a78402792e22f1045b9ac060337d9a65d9672bc25a8d3b66128ef4f6d",
      "bytes": 1363
    },
    "parts/7324.dat": {
      "sha256": "e1f33c3089a7eea69829227506685be70df8ff223c83b06cc23a6310daffe811",
      "bytes": 1316
    },
    "parts/subparts/7324s01.dat": {
      "sha256": "6f70540aa074e76a331517fa9a699918bf42c6bed9387edfdd6ee53de4681391",
      "bytes": 10173
    },
    "primitives/48/tm08q1125.dat": {
      "sha256": "434bfd27bbad673f788ff14c629f1e7475d73a931289f867f32f2c28f6c90f15",
      "bytes": 26829
    },
    "parts/4275b.dat": {
      "sha256": "74a8135bac411fa7b44ecf2c53e0f6e3fa3d922a530ebdbc475eb2a577039351",
      "bytes": 1272
    },
    "primitives/h2.dat": {
      "sha256": "6153d92d82234c7637ec360b597a00795efc959f0626f9607b15c2d890fb2c69",
      "bytes": 1911
    },
    "parts/4276b.dat": {
      "sha256": "464fdd6f97840b72e0434c74bf2df955adb06fdfa9a0ee2e0144ccba90d399ea",
      "bytes": 1276
    },
    "primitives/h1.dat": {
      "sha256": "1da74f714b5fc460815134709f53fb17aaa25bb6a5d05eacf3fe7ca3d8279258",
      "bytes": 1933
    },
    "parts/44301.dat": {
      "sha256": "7242d6b7ea790093cd883fb360f94c0ba4b57e2cd1dd1033b4483bc8750e2057",
      "bytes": 348
    },
    "parts/44301a.dat": {
      "sha256": "df8f351d6b6fea3f9a561762e8bb5dd3a06ff0f9e64043def349a3931c04f28b",
      "bytes": 1154
    },
    "parts/44302.dat": {
      "sha256": "fd2fc41a83b0e690becb7ff09bf5e531936cbda960d1a7c2c8b7459b9a1f380b",
      "bytes": 374
    },
    "parts/44302a.dat": {
      "sha256": "c52afef4fefeee48f1b55d62eb90092093e152f5f3ac74a791edda8e2ac0198a",
      "bytes": 2428
    },
    "parts/3307.dat": {
      "sha256": "1f8a35123063dec41f8668b45b733cf2eeb639ab08b47a58f4daf399e7df50d0",
      "bytes": 2552
    },
    "parts/3815c01.dat": {
      "sha256": "6f2005d952f10e9d2de98e2f9e4eba8e14343a731ed04a04f607ffe00d36c930",
      "bytes": 641,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/3815c01.dat",
      "source_sha256": "746fef2bf7620205af0876c705d81cd3bebfa2d48a5d04c91357ce16cd0294e7",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/3815.dat": {
      "sha256": "bcf700ebb40722d43b3e39433b1c3f98a94f63d3e59cf2939487b45139da717c",
      "bytes": 927,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/3815.dat",
      "source_sha256": "e0a87d45e69cfc0bb9dae9347dc36accedb90f85faf2c6fb33c86b8781342318",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/3815s01.dat": {
      "sha256": "72441aab74747b799cc00c0aed19757bed5f92f6a6c644bf0c51ae93c5d34887",
      "bytes": 8394,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/3815s01.dat",
      "source_sha256": "fc082b2cb28a169052078b5ac6f788bbbabece666c8f953331f384486d325167",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/3816.dat": {
      "sha256": "57e0668531cd0ed25953ad18d67bdf79f83fa26a2f0b2c4dfce0bf4b7dc7eb0d",
      "bytes": 1503,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/3816.dat",
      "source_sha256": "cc74c509e8e9383635ceed958e7f143f962a7ac8346ee9ca61f69dc0dde72e72",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/3816s01.dat": {
      "sha256": "3596d67544a9aee48c7e4b02b1d90dc36ca9f2c19912efb18e84c51d16616390",
      "bytes": 1529,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/3816s01.dat",
      "source_sha256": "497c823e98611631ab886390dc19a8b778beb05aad2bd634fee77e038dd09cda",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/3816s02.dat": {
      "sha256": "0690eb0b58340b664de699ad091b8fdb40d3f7d583d8056b29c25d3469959fef",
      "bytes": 13506,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/3816s02.dat",
      "source_sha256": "e113ebec77c73e302042965a659a72e7a67cb1dd9ec3f22956cbb89dd5881644",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/3817.dat": {
      "sha256": "d0f1ff53b4f5032a1419f1884334b9b52877c64c20d3db9a6a1fbe09626dd042",
      "bytes": 1408,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/3817.dat",
      "source_sha256": "a19f89545e5072af9ded2c42d658ded9e90022f4596b81fe39c2b0332fd46985",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/3817s01.dat": {
      "sha256": "74bdebe7c482a76a65b77b2b0c73b2608d711fcc27dbf2d94b17fd7993dfe7e9",
      "bytes": 1463,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/3817s01.dat",
      "source_sha256": "5da12eff76621cf6e0b9eb1640078a72b450d179ca3ea4dd2da56f839d9880fe",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/3844.dat": {
      "sha256": "f0bfb49a922d7bb6ead202c607db754a343c7c50b7efc06a96ee03b838bd33d7",
      "bytes": 32152,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/3844.dat",
      "source_sha256": "b4e67043d02d29a4d7590edf09cb7e581435c08da72eb26ead5baf8e5986cf9e",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Chris Dee [cwdee]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/3849.dat": {
      "sha256": "9184e7881101ea18fb980b71b76402c1ced39346a123b4b9b6f2e9db9ba4f323",
      "bytes": 1743,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/3849.dat",
      "source_sha256": "1d880773968ae6fb19e19a134adbcf412b35667243434005d03b842a15f4e0a1",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "James Jessiman",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "primitives/1-4con4.dat": {
      "sha256": "504327502c0741e0459dee9fb3f0e800734a397be1aa0ea8467b351c8edd973a",
      "bytes": 1377,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/p/1-4con4.dat",
      "source_sha256": "504327502c0741e0459dee9fb3f0e800734a397be1aa0ea8467b351c8edd973a",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/4493c01.dat": {
      "sha256": "b711ad6517a3258f482b84287e9ff0695ef67cf9cf6db972e049c2e89c30ffd3",
      "bytes": 684,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/4493c01.dat",
      "source_sha256": "e5e431cf22387f826c2ace73342f9e2ae8a9aeb97bcda7203cbf46e5b795789f",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/4492p01.dat": {
      "sha256": "9a1030de3290b8fc96c23e5a5805588af3a5a3ac0e77c6790ca3ddf037f021fc",
      "bytes": 1365,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/4492p01.dat",
      "source_sha256": "67bd5d3558e417dd0b13afcbbcf09efa65e72a0dd1010b42b78709c14b115765",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4492s.dat": {
      "sha256": "bcc657889c0b998feedfe8a4b1bdc6522c87116048f5e6db30eb4e491dee1c95",
      "bytes": 53762,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4492s.dat",
      "source_sha256": "01b020b911040c2da4c3c3810d929877283704142a97cbe0b40c94da81aec6dc",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4492s01.dat": {
      "sha256": "d2b1839bef968815adc2bd1b0ba7cc30f1a1f5d83cd4829dccf38be6402fc621",
      "bytes": 47150,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4492s01.dat",
      "source_sha256": "b7595f2a4ab8ec3de2785994ba44f488e3010116d9de8aa70c77bf9d49f0134d",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4492e1.dat": {
      "sha256": "8bb387f6106747ba9a8864187102984a1117a652dbc0f5fb15792c9a04abfd46",
      "bytes": 2674,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4492e1.dat",
      "source_sha256": "8bb387f6106747ba9a8864187102984a1117a652dbc0f5fb15792c9a04abfd46",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4492e2.dat": {
      "sha256": "3e2e30107b56c2c5e9ad6a54fb50540de53fb288c7039aa62bbade510c4e0228",
      "bytes": 4290,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4492e2.dat",
      "source_sha256": "3e2e30107b56c2c5e9ad6a54fb50540de53fb288c7039aa62bbade510c4e0228",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4492e3.dat": {
      "sha256": "637879d4ab3c42c71249f1d7f31b65483d0f9801e1cb80095e3faf67dcf37ed5",
      "bytes": 5893,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4492e3.dat",
      "source_sha256": "637879d4ab3c42c71249f1d7f31b65483d0f9801e1cb80095e3faf67dcf37ed5",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4492b2.dat": {
      "sha256": "c0dafef088056a8b3870daeaf2b802c883675efc8b63dd5ed6329db997dfc8ab",
      "bytes": 21173,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4492b2.dat",
      "source_sha256": "c0dafef088056a8b3870daeaf2b802c883675efc8b63dd5ed6329db997dfc8ab",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4492b1.dat": {
      "sha256": "7720c0d4602a93d12be792db3def960b106a5957f8d80b50a7ebe71a8da82dfc",
      "bytes": 3927,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4492b1.dat",
      "source_sha256": "7720c0d4602a93d12be792db3def960b106a5957f8d80b50a7ebe71a8da82dfc",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4492m.dat": {
      "sha256": "86d330b1e4dc01a22d9d5fc4466098d64a219b985e71ed3ac1d0417fb9d008f1",
      "bytes": 2905,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4492m.dat",
      "source_sha256": "86d330b1e4dc01a22d9d5fc4466098d64a219b985e71ed3ac1d0417fb9d008f1",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4492h.dat": {
      "sha256": "91a6ba9efd7e4ae1a963b1839aec86c75d3564a1840f3716d87f64d4a4b720de",
      "bytes": 2534,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4492h.dat",
      "source_sha256": "7cb485449fb27ce9d19c04874cc30f9937760ec61ff4e810b46bc76d710a29e7",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/4494c01.dat": {
      "sha256": "170b2d00cdb4e81f0d532cedb805b59098450e1d0db966e5b30aa84f8c868dd3",
      "bytes": 489,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/4494c01.dat",
      "source_sha256": "196914464744aefa545602381a2e23fe30aa2bf265a20faf52cf331df720d5fa",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/4493.dat": {
      "sha256": "82facab6be2fdbe967ef80a74d6cb816984ca5487401b03780ce29432015ea78",
      "bytes": 687,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/4493.dat",
      "source_sha256": "25aef6795d8b8db7023f42e7efdf6168466ccc02bab2c1a52259c2cbc8039703",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4493s01.dat": {
      "sha256": "3b59861d253ecf7847c690c47e273c633b9b23534981ce6a97a6ffcaf01a2e70",
      "bytes": 64551,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4493s01.dat",
      "source_sha256": "ef6eab1108dc1747b14888507dd012ebf396e13a3d48f631157cf536164e205b",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4493s.dat": {
      "sha256": "e9d27b15ec36005f7a010be30a10276709879e23c7a13f39d8a987da70d4b040",
      "bytes": 25923,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4493s.dat",
      "source_sha256": "11310a03fb52b05d45768a99a1b87a43c5021eafb860264de0d6ddc17c07d087",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4493s1.dat": {
      "sha256": "94268e5fc8319e20521e723bd9206d5b0780aabaa0868b7a8bf0ca8959a533bb",
      "bytes": 2256,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4493s1.dat",
      "source_sha256": "da4fe63d7b34b05a34e57cbb3b1311c4a2e9710c5266ff5110c3d71285a4dc63",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Bernd Broich [bbroich]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4493s00.dat": {
      "sha256": "043ff3df6bc389d415401be0eba83b13a7dcc8298b4abb9a9a449dc5547f6b11",
      "bytes": 61128,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4493s00.dat",
      "source_sha256": "043ff3df6bc389d415401be0eba83b13a7dcc8298b4abb9a9a449dc5547f6b11",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/4494.dat": {
      "sha256": "d70e05424adc0b043257c90147381d9412daa07d1b54f69a648afe57ee051147",
      "bytes": 688,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/4494.dat",
      "source_sha256": "7def1ddf76589b471013828c052b16a0e37401634fbbab5c16e067182c12ce08",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4494s01.dat": {
      "sha256": "54fa204450feb01f92bcad1126955dc62b3bbb547c28d03fbb9ddb830b302bc1",
      "bytes": 45216,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4494s01.dat",
      "source_sha256": "cb5770efd10fa993efc9d39978b9ec4aafdedc03cfde0d451019d4d9167df54d",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4494t.dat": {
      "sha256": "0c6d5541142b6e0a9e817a75e68c3323af462ea8ad663a7915fd793fc3c8ccc0",
      "bytes": 137165,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4494t.dat",
      "source_sha256": "0c6d5541142b6e0a9e817a75e68c3323af462ea8ad663a7915fd793fc3c8ccc0",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Sascha Broich",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4494s.dat": {
      "sha256": "67fe5a4c0a85b265e59d5ff40460ded63c0ed4d269b2761c1e29afe3bc29fa19",
      "bytes": 1815,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4494s.dat",
      "source_sha256": "c25243488bd089ee1f782b8e70360d33263130f80076b89eac4c2c18c009c014",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Bernd Broich [bbroich]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/4494s00.dat": {
      "sha256": "2fc0f48e60139bc683df03ef1f45ef525129438dd8331f74761590d65a6dcf1d",
      "bytes": 58285,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/4494s00.dat",
      "source_sha256": "2fc0f48e60139bc683df03ef1f45ef525129438dd8331f74761590d65a6dcf1d",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Magnus Forsberg [MagFors]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/973.dat": {
      "sha256": "36142b6b412a4bda7d6d169810a50d19ad0aa026d9ef6d0a780c29f1eb92b564",
      "bytes": 1209,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/973.dat",
      "source_sha256": "901f2c4d1e5add8b4400c3470664d6bc9b7651ed4578b26dabdc6938be6dbcef",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    },
    "parts/subparts/973s01.dat": {
      "sha256": "e8593d7a11310ca07e460eed2ebdfcd8d1fd2a482bbcad3036eb8506e16137d3",
      "bytes": 11356,
      "source_archive": "https://github.com/ldraw-linux/ldraw-library/tree/e74a0f8fdbd6444316492a315d24e8bd0dfec6f9/ldraw",
      "archive_member": "ldraw/parts/s/973s01.dat",
      "source_sha256": "4d0dbcf4629d46303949a72a4850c4c67e6ccc5ce0e08ec46fa6fe4f77b2aa3a",
      "modification": "Dependency paths normalized for repository folders; geometry coordinates and source header retained.",
      "author": "Steve Bliss [sbliss]",
      "license": "Redistributable under CCAL version 2.0 : see CAreadme.txt"
    }
  }
}
```
<!-- asset-manifest:end -->
