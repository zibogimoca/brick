# 에셋 관리 정책

## 용도

에셋은 브릭을 화면에 그리는 데 사용하는 3D 형상 자료다. 부품 사전은 고브릭스 상품 번호·색상·가격·형상 참조를 관리하고, 에셋은 그 참조가 가리키는 실제 모양을 담는다. 형상이 있다는 사실만으로 고브릭스 실물과의 일치나 조립 가능성이 검증되는 것은 아니다.

## 현재 폴더와 파일

| 위치 | 의미 |
| --- | --- |
| `ldraw/parts/` | 부품의 형상 정의. `3001.dat`는 2×4 브릭처럼 LDraw 식별 번호로 이름을 붙인다. |
| `ldraw/parts/s/` | 부품 형상의 일부를 분리한 하위 조각. 여러 부품에서 재사용할 수 있다. |
| `ldraw/p/` | 돌기·원통·원호 등 공통 기하 조각. 파일명은 LDraw의 규칙을 따른다. |
| `ldraw/p/48/` | 곡면을 표현하는 분할 정밀도가 다른 공통 조각. |
| `ldraw/LDConfig.ldr` | 색상 번호와 화면 표시 색상·재질의 대응표. |
| `policy.md` | 사용자가 알아야 할 에셋 구조·관리 원칙·이용 조건을 모은 유일한 설명 문서. |

`.dat`는 문서가 아니라 좌표, 면, 다른 형상 파일의 배치 정보를 담는 LDraw 형상 형식이다. 현재 선택한 상위 부품은 38종이며, 나머지 형상 파일 상당수는 그 부품들이 참조하는 조각이다. 파일 수가 판매 부품 수를 뜻하지 않는다.

## 왜 나뉘어 있는가

현재 구조는 기존 LDraw 형상과 뷰어 로더를 변환 없이 사용하려고 원본 구조를 유지한 결과다. 예를 들어 `parts/3001.dat`는 `parts/s/3001s01.dat`를 참조한다. 하위 파일이 다시 공통 조각을 참조할 수도 있다. 번호와 경로는 사람이 읽기 좋은 이름 대신 참조 식별자로 쓰인다.

부품 한 종류당 독립 파일 하나로 만드는 것도 가능하다. 참조한 조각의 좌표 변환과 색상 적용을 풀어 모든 면을 해당 부품 파일에 넣으면 된다. 이렇게 하면 파일 목록은 단순해지지만 같은 돌기 등의 데이터가 부품마다 반복된다. 반대로 공통 조각을 별도로 유지하면 중복은 줄지만 파일과 참조 관계가 늘어난다. 어느 쪽이 항상 더 빠르거나 관리하기 쉬운 것은 아니다.

폴더를 단순화하려면 형상뿐 아니라 사전의 참조, 뷰어의 로딩 경로, 수집·검증 도구를 함께 수정해야 한다. 이번 문서 정리에서는 형상 배치와 파일명을 바꾸지 않았다.

## 출처와 라이선스

현재 형상은 [LDraw 공식 라이브러리](https://library.ldraw.org/)의 [전체 아카이브](https://library.ldraw.org/library/updates/complete.zip)에서 필요한 부분만 가져왔다. 직접 제작한 형상으로 표시하지 않는다. 개별 저자는 원본 형상 헤더와 이 문서 하단의 에셋 목록에 기록되어 있다.

현재 보관한 188개 `.dat` 파일의 라이선스 표시는 **CC BY 4.0**이다. [이용 조건 요약](https://creativecommons.org/licenses/by/4.0/)과 [라이선스 전문](https://creativecommons.org/licenses/by/4.0/legalcode)을 기준으로, 공유할 때 저자·출처와 라이선스 링크를 제공하고 변경했다면 그 사실을 표시한다. 저자가 이 프로젝트를 보증하는 것처럼 표현하지 않는다. 색상 설정 등 다른 자료의 조건을 이 확인 결과로 일괄 단정하지 않고 원본 고지를 따른다.

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
    "60477"
  ],
  "files": {
    "parts/54200.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/54200.dat",
      "sha256": "3f0c25da3dac0600209a032c53c040b8668e617374997546d5449528eb7099c9",
      "bytes": 1196,
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/15068.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/15068.dat",
      "sha256": "511c620c73d116a9564248a4adb0f564b90f12f1428a4a9276b4bae4f9bd7e4c",
      "bytes": 383,
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3700.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3700.dat",
      "sha256": "6cb6522c580754cf970dad0fae688bb78cb3253a7237038dad83965fe47cfec6",
      "bytes": 2367,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/60479.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/60479.dat",
      "sha256": "4cc9f46de13bd157dbbf16757bed1becee52253848fc1827d6c18477b94907b3",
      "bytes": 1484,
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4274.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4274.dat",
      "sha256": "c421cee48c7c0233371144f5a256f7a4503f008318ff523b31e0b5a9d44d9704",
      "bytes": 782,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3622.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3622.dat",
      "sha256": "9317bcec4fbcddbd38ed3972d25ea95d685101904f3ed86c7e769a9f356245d8",
      "bytes": 511,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/14417.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14417.dat",
      "sha256": "5da4fc1a13d6110876c944da429ebf2cc29d69b8942fb1dbc05ac8c65480d37c",
      "bytes": 885,
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stud3a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud3a.dat",
      "sha256": "91b1f54ed55b2f57dd73225da3198b5198e31f7587a5e8b7d3351b1478c8881c",
      "bytes": 603,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/cylj4x8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/cylj4x8.dat",
      "sha256": "9cbf5025a81af8a9cb07f56b43ec46a587256995c14aadd934b6f70262f523aa",
      "bytes": 4035,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box3u2p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u2p.dat",
      "sha256": "df73118b95f23d693c3b7d25c57c483db3bf61ae017d757848119955d28d59e0",
      "bytes": 818,
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stud.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud.dat",
      "sha256": "db037d518d7c08bcdc1f0e7497f4f98e97d99850531dd62d602965520f3bf8f4",
      "bytes": 698,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/30374.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/30374.dat",
      "sha256": "db69ea3eecc2a6f2731aaad6ac8fb072c5ecbe136d1ea8a03de593014fe2e9c0",
      "bytes": 961,
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2430.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2430.dat",
      "sha256": "7a41e19061815c561d0930d76bffb0abe38b6323cb72d183b8259042812f7610",
      "bytes": 1912,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3666.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3666.dat",
      "sha256": "f4fc83d8c3fc1df32c1a217dc09775a99fad1ced348cffc5167f9c6a69aa9bca",
      "bytes": 622,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3832.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3832.dat",
      "sha256": "4928810faf064116f14126735c7a273df15c662fe1d648991c3a3c4cc79b0d49",
      "bytes": 1917,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/6141.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/6141.dat",
      "sha256": "fb2cd4fad207392508bd2ca8b5469b1c351b692e111aa06b55da55d53fd44dd7",
      "bytes": 999,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3710.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3710.dat",
      "sha256": "1a2d17e3e35750ccf02a54c7aee0cf7485c1c8596492746fc798d341399a3a6e",
      "bytes": 622,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/60477.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/60477.dat",
      "sha256": "838a96304d5ab177a8c7bd2805eacdfdbfeab71fb86802b81b3523484f4df58b",
      "bytes": 345,
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cyli.dat",
      "sha256": "4a742c2765b6ebf98245baaf8a160a4ff587fc93d36c8ee2b9074712a2f968c4",
      "bytes": 2687,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/60478.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/60478.dat",
      "sha256": "39e307038b6a5b2f0124891de47949dc5ffb36233b5f4fa7cdf43f2d159b86bc",
      "bytes": 1074,
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box5.dat",
      "sha256": "ccb7b8a1d36692335b10ea6aa196849afcad4b15331683ed8112a10b50977318",
      "bytes": 963,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/60477s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/60477s01.dat",
      "sha256": "98b912f2b4564702bb52631f13b4b505b66d666ea9ccb8d588bbb79081a8352a",
      "bytes": 1991,
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3705.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3705.dat",
      "sha256": "ed90738971675e2dbd05b5a0aecaccf2da32e62b4e9085b886f084de890a853a",
      "bytes": 653,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cyls.dat",
      "sha256": "aaee6ffe6e4a191d6cad4496677132eb0349303d6e48c13c7a2240dcea1db621",
      "bytes": 1107,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/54200s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/54200s01.dat",
      "sha256": "cf96613781f9e09ef1e12bf1be127a99b1a8f18a5e8ee9af434ef4e757696cc7",
      "bytes": 3744,
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4ring4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring4.dat",
      "sha256": "e046737f05ca843c7fc32bbfe9f5b26f3409c5b42b786d8809aa789faf761154",
      "bytes": 1640,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cylo.dat",
      "sha256": "d6ca97ee2e75918b3309a5c88aafcd2455b3a316f7cef8963517c19f1d86b38f",
      "bytes": 383,
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3023b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3023b.dat",
      "sha256": "42f96ca69f8a0b83a877f4e128e4143ce753d038b1074835edc5aca9a9954fc9",
      "bytes": 820,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4cyls.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cyls.dat",
      "sha256": "eb26a554261899f82fda150ee70827a010b7d29206b5b577b2ee5831851d8f29",
      "bytes": 2643,
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/48/1-8cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8cyli.dat",
      "sha256": "494069ca353e41885bf8f5b6b3ddc9b62aabeca3eedfe6aa5597ac8f12ca12b9",
      "bytes": 1361,
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3001.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3001.dat",
      "sha256": "70968cb5e4baa92dc6a1939aca7526b8566a17dbea49da9b91182aa864e412c4",
      "bytes": 663,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3460.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3460.dat",
      "sha256": "a236ed5a1efb4844f2eebafc6096a90571607af30e287b307400dcdea44f438f",
      "bytes": 622,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3005.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3005.dat",
      "sha256": "f86e5f3aed432cab8f5dffcf2e41a9f2ee8c3bd4dcad1732da9630837849a4f8",
      "bytes": 670,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4032.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4032.dat",
      "sha256": "5fae837faef6e689f8933cf635de33f2c8d879c8dcd235a4affd518841249426",
      "bytes": 317,
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3020.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3020.dat",
      "sha256": "551e433cc4bcfdeeb6e390e509d52ee2e62c90d3eae625ee36928ef32291bb79",
      "bytes": 1341,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/59900.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/59900.dat",
      "sha256": "8416701912ed13937743df8dd877a2a1254925efd4adebb77950f48c3d9d5156",
      "bytes": 1663,
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/connect.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connect.dat",
      "sha256": "fa572d5b7bcdb19ea2ba74cd1a98aca913e1e556001232e484611915adf83305",
      "bytes": 7441,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4cyli.dat",
      "sha256": "4a54732476cf4eaad2c9f7b40a3cef24db025132004328e4e84c0666cd217533",
      "bytes": 2031,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/rect3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/rect3.dat",
      "sha256": "07ac46908b6668d993b6de0fb001a34cd996542106b80ebc7de63317d8dde865",
      "bytes": 605,
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3022.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3022.dat",
      "sha256": "3cd09bfe626e751ad95eab0ea83e5f3adea81f05d34993a1c4bf432ee386fe25",
      "bytes": 1088,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3001s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3001s01.dat",
      "sha256": "bee662925490666aa5956d301b7abc46df88b3cc35737326765441585c720047",
      "bytes": 1456,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/15068s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/15068s01.dat",
      "sha256": "41456734d1b26b9b448eb2fde7f0d4df463c1e2085b79ca9731a0a35554b3c58",
      "bytes": 4952,
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/2-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ndis.dat",
      "sha256": "7557eae598be3f530b840471535198e6b07b03486ffbcc18a00e862c3d25d925",
      "bytes": 874,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4con4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con4.dat",
      "sha256": "7c49737dec9819a49e43d7af5926c05d8a1a1226bc0f2cb15cbe7cddb035f00b",
      "bytes": 2722,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring2.dat",
      "sha256": "6fb38804b1f5e9bee8c0b80caf1397b09454fc58b048dc19045b6f37c8762ab0",
      "bytes": 1628,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/rect.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/rect.dat",
      "sha256": "ffeb2dd3d9b83c38841f18f1f74800fbba9e90c5fb6badfff2a795f08a96cb71",
      "bytes": 654,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4edge.dat",
      "sha256": "9ce2de7e67bbac575d52cfdc771b9d00856efc9b88002d97db8e665e50f4d467",
      "bytes": 545,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/48/1-8chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8chrd.dat",
      "sha256": "282b0d7dd4e73d273b9cbcce88e30889cce3b44aa8574a25382fe526248d5426",
      "bytes": 611,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug2-1x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug2-1x2.dat",
      "sha256": "9cd034fe99c6efd6e158c73a8a95d7b0e6ff4f1671a7ee22e2323c74a43b7f1e",
      "bytes": 341,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3023bs01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3023bs01.dat",
      "sha256": "d5d511e8fce3653ea9c0c8662952006394725f4f7a2234842946c417a737ecad",
      "bytes": 757,
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4ndis.dat",
      "sha256": "ff6685838636e7ab6152356d8f09e4f00a38af0d878b0881423f5c45fb868f0c",
      "bytes": 692,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4con7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con7.dat",
      "sha256": "a1041c95280f6b9551e6171d8090cb4e0f0dbec7a9a85fa5bb71d0a613827696",
      "bytes": 2426,
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axl3hol9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3hol9.dat",
      "sha256": "a99c7a963b46b735e36743f216efdd4916f982b4b984469de5b7e6bddb18e8c7",
      "bytes": 617,
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axl3hol8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3hol8.dat",
      "sha256": "2349b82c7dd4559a45913986e07e185035fdb48928ac13e5fd774f4c30a65e96",
      "bytes": 2605,
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug-1x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x2.dat",
      "sha256": "5842fa1baf6ea7f18fe4e355238cd733ff9bdbdc3d722be5cf8988f1c5fce414",
      "bytes": 333,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3710s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3710s01.dat",
      "sha256": "57df307f7e3843f4c702311b82e93988bab6d688cbb8ab82bb4338184696780e",
      "bytes": 618,
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/2429.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/2429.dat",
      "sha256": "65cfb3a695f389a76746cda89fdc2b487ff85e090b3cb03483cea463ddf44fbc",
      "bytes": 2396,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/joint8ball.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/joint8ball.dat",
      "sha256": "db77f15924894538364a9ef227ebeae84a2df1defa1b3bfb474ea29cd0f6f153",
      "bytes": 403,
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4cylse.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cylse.dat",
      "sha256": "3c2c53a4ffd03dba04d3410b11763a020c603eefaf5ab425c282fb18744692c8",
      "bytes": 638,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/48/1-12cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-12cylo.dat",
      "sha256": "aba0697449741a95889cb0faf8d6231777086ebed8ee1956ac304bd32b208c6a",
      "bytes": 416,
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axl3hol3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3hol3.dat",
      "sha256": "05fd46a65cb2342d3e88e3789a610b4f17f9fc8fd614f90bf8c2b3f44e13a171",
      "bytes": 743,
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axl3hol2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3hol2.dat",
      "sha256": "5d35ee8c2a5ecf50222d9e7a5a489730f4296b47e781157a7f01263b162c6901",
      "bytes": 656,
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/48/1-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-8edge.dat",
      "sha256": "eec30153f06bac336ca71ae16b31c5d0c7ae432acb5e91befe37fdb7b6bb1c8e",
      "bytes": 711,
      "author": "[PTadmin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3941.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3941.dat",
      "sha256": "d0cf49833082c39c358c248fd19c7568030ffc43d7add011feae168d5ad6e693",
      "bytes": 707,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3004.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3004.dat",
      "sha256": "e1caee3b32175393c9d6ea176a47f8869173a01d03a451e1cfe10d09167c0203",
      "bytes": 670,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-16cys2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16cys2.dat",
      "sha256": "705ec7384e735a8e7a864403831e55cb1e62f88ec09126a8b379b7e27288607a",
      "bytes": 702,
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4ring1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring1.dat",
      "sha256": "4ae21061a6d0c9c80c608decb750f16fe1d113d84e08ef2f6082bcbb0f55194c",
      "bytes": 1641,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axl3ho10.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl3ho10.dat",
      "sha256": "7799ee39b85781d7283d952136cba415605b819a87b9ec92cbfe3f348c8c1f5e",
      "bytes": 743,
      "author": "Santeri Piippo [arezey]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3032.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3032.dat",
      "sha256": "35e8b828a5bf21de83ca898a49b9725e6d08d5752ad6eb57910f27086108ca1f",
      "bytes": 2535,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-16chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16chrd.dat",
      "sha256": "2bb493e8b5b56a5d63bfa7356a0ed5d6403a68e5e9a983e13a57541783ad19c1",
      "bytes": 317,
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/14419.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14419.dat",
      "sha256": "6bc91fe4e89dd12f56ead36d7af3cf13fcbbd9798bfbe01bfd8a71d9234d1b12",
      "bytes": 597,
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3004s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3004s01.dat",
      "sha256": "e05db7f7baead09713c4296b4e4e215b3fa5ccbf526e3431cb66a3ce19e321b5",
      "bytes": 850,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4ring3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring3.dat",
      "sha256": "1f2835ac308154edc2d6f479d8e742a55be981f6167b20bfa100c195bc0731dd",
      "bytes": 1628,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3623.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3623.dat",
      "sha256": "08f74845fceb4b39976d8ba56c0d59970483b8956cc59eb08e9f01ca579467e2",
      "bytes": 616,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3034.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3034.dat",
      "sha256": "035f4ac31ecad8943fd0ac6baa155c6ff38c75a4d8ef1083fb2afa48b166a845",
      "bytes": 1704,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axleend2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axleend2.dat",
      "sha256": "cedcec0918b69285f612c94d1f6532f7352a08f18b2749dde6f6a5235c1a0c73",
      "bytes": 8085,
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8edge.dat",
      "sha256": "a590f230678d592d514a9c5e307c6a30945e50e4c529fc06accf37530d0e0ed5",
      "bytes": 615,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axlehol8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol8.dat",
      "sha256": "e3cf8856c972ecaf486a344c171cb4ab601efcb08956bd7b6cfafa39b0439493",
      "bytes": 1706,
      "author": "Steve Bliss [sbliss]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stud4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4.dat",
      "sha256": "871cdcab26e7f5113488a24c453d6fabda75b275b06de592e0bfaad4292c12a3",
      "bytes": 935,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/2-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4cyli.dat",
      "sha256": "d486780f0f84893899d9eadcd13150f13a42e15e77a3cda38cdf24ded98862c6",
      "bytes": 1543,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ndis.dat",
      "sha256": "21202dc15823f4336bc2544244d0b539b76745c89f7a59ad18cdd03ad45cc543",
      "bytes": 1219,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4edge.dat",
      "sha256": "d7f5aff979bc227b601abbb8e0226d6055d08eafb5faaf507b3055f712cd4c04",
      "bytes": 831,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4.dat",
      "sha256": "2cbfcf075ef5c87c6a5f543f837972a78d43274ac7771b92229b5fe5da797c1e",
      "bytes": 948,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stud2a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud2a.dat",
      "sha256": "61fbed54b085a30490045309778d1e2a6d95485e6558996b12674f848028d557",
      "bytes": 866,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3062b.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3062b.dat",
      "sha256": "cea4d47bad2ba17130e8fdd298f4f0b0dd4efdaf6edadd3bdd5e089e1cb60bac",
      "bytes": 920,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stud3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud3.dat",
      "sha256": "d29e9160faeaf85b2b72a098e89a81f41e0082517a82065d7b1f149b5fd2addd",
      "bytes": 710,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/phandle1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/phandle1.dat",
      "sha256": "3cd5c4eca20ef297d265e4ba7228b04a5fb7f332b89f923ead8366987021d6e2",
      "bytes": 1209,
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-16ndis.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16ndis.dat",
      "sha256": "abb7da370e72fe9e75faf5d10c637b476202dbd8ced9cb5b0f96433e1f72f529",
      "bytes": 557,
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/48/1-12cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-12cyli.dat",
      "sha256": "a645a42a5ed912a059a9336ab1449d02efd067008f034549cc8c5ae488159fd3",
      "bytes": 1027,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3460s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3460s01.dat",
      "sha256": "0d6285f8a937cef6d6e76bb00f6356f77198a5872df7554a3432120da5eaaa86",
      "bytes": 618,
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/11477.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/11477.dat",
      "sha256": "fed74af9f56bcb149a7f67af4b427c261b41d24d15ed7a3466e24170377a0ba6",
      "bytes": 374,
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/2-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4edge.dat",
      "sha256": "665400f76566b161c28303cdadce40d17d979a8ff9a8a133675af2d17fbe6763",
      "bytes": 683,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3003.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3003.dat",
      "sha256": "aed0ccd750126a58d38b012a4e8b16c172896339547c120ef67b69e1386f490d",
      "bytes": 670,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/peghole.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/peghole.dat",
      "sha256": "90c6dba9e5bcdd63955b9a5208f377761850863be9ed26cac7cd2be61ab85c92",
      "bytes": 814,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4edge.dat",
      "sha256": "54a52196e421fd1717d291ff52ea57553b1fb238907c1678cc1f1a84c698b1da",
      "bytes": 1084,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/48/1-12chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-12chrd.dat",
      "sha256": "fe2a0252d971dc65126755c4fdb7db900e229dfdce712b42ce9510c7b0390e26",
      "bytes": 539,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box2-5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-5.dat",
      "sha256": "8f297b754f87da1dbe19eec8704a5ce03a23b794ccd7cd015508e3758a206174",
      "bytes": 609,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3010.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3010.dat",
      "sha256": "7d1cb3082199042666045d92388b3b3ab697f969268e87a6c001f80f92a2e0b2",
      "bytes": 788,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4disc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4disc.dat",
      "sha256": "a00b5547776f61a7389d303616987c76b3c4de86ad8ec32f22857e1bd5e5e40f",
      "bytes": 1137,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3666s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3666s01.dat",
      "sha256": "71aefa629ca2df065d9cde349bb46a51a8e59265ad4d74e55da24611095d5538",
      "bytes": 618,
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stud2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud2.dat",
      "sha256": "5ed3702c7d7000bfac2906f12b74ae312c59194a8e3b504952820c826b51c810",
      "bytes": 930,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/14418.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/14418.dat",
      "sha256": "50df1a37eb8dd726ea0796c6ca6f88f3ab581f81e2682aa3aad24a3b0e881588",
      "bytes": 491,
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3024.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3024.dat",
      "sha256": "e053af4f232374b0c8da2dc0f9620bedf0576ca43d7c3ceebc6676050ae61da8",
      "bytes": 668,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/rect2p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/rect2p.dat",
      "sha256": "faac2b36241a9de0c0108471e59c45734df6c79813332d9cacf97f6391886acc",
      "bytes": 594,
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3622s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3622s01.dat",
      "sha256": "bb4e34ea6d2c7b7f7591b6051d69fd09f18a52486c2495b27c5baed67ea616f7",
      "bytes": 984,
      "author": "Takeshi Takahashi [RainbowDolphin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/14418s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/14418s01.dat",
      "sha256": "43c34331b9b44b63f90a268506c5d7c44368b07d83c64b1a352cc027e831da11",
      "bytes": 1348,
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/4032a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/4032a.dat",
      "sha256": "ac5774e2a8eeb9811db795707f6c03cc0b834313b9b9ac5ba25dbb576c9851cb",
      "bytes": 1497,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-16edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16edge.dat",
      "sha256": "c08dd83bb7fe90b61f7cd0b10ebef0d9a9ba33b497676dedd2e2e968cb8248f9",
      "bytes": 586,
      "author": "Donald Sutter [technog]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/2-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4cylo.dat",
      "sha256": "4fa9f597d775c7f15e3fc66f60e20d914134d13004b485488b7dbff684776232",
      "bytes": 387,
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box2-11.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-11.dat",
      "sha256": "7f29fb8601b419207b5c855af8fad8abb55a967ec73f3d8be841d370c360b97c",
      "bytes": 489,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug-1x4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x4.dat",
      "sha256": "e88852b15ca37121e12f7052a234e4a90dc99a8c6d22d45e041f47103c2fb71c",
      "bytes": 414,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/11477s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/11477s01.dat",
      "sha256": "bc00e46f3d79f0569d3952eb20b91ae2402121d483945fce7e51f3322fdaea21",
      "bytes": 3191,
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/connect2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/connect2.dat",
      "sha256": "34ff327f32629d65ae37d8ed1f24d9be5951876ca418cfa219c98aca63dc0506",
      "bytes": 6529,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box4-1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4-1.dat",
      "sha256": "2ed58df5da841827dfc5f9ac11c0bd7ffd8a455e46f166638e635f61a014b44d",
      "bytes": 973,
      "author": "Tore Eriksson [Tore_Eriksson]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box3u4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box3u4a.dat",
      "sha256": "15463f41f9947dd75486dc7af3231b1037704f1b654c2555e3ba705817a2db75",
      "bytes": 545,
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/48/1-12edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/48/1-12edge.dat",
      "sha256": "c1320fa098058f1bb4bb73a4bd02a9533bdcc4f22ac4a0f0a1dcd5cdf85deaed",
      "bytes": 584,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/4032s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/4032s01.dat",
      "sha256": "0b12443c9f5975afabecf7ad9e50384a0237deb74d3fc641705e25cf3a544bb3",
      "bytes": 1637,
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cyli.dat",
      "sha256": "5a7168952a5a3570327873b9a5802fa7b3be40967ab78c03b6a2bfd4419a1f10",
      "bytes": 1044,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/3031.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/3031.dat",
      "sha256": "e67436538e47cb38b8352e91c2b5b7c7c274e070912603e5e9fc0b4513962338",
      "bytes": 1938,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3005s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3005s01.dat",
      "sha256": "ed6218c566690622fed39b8fb3dac9ae9a36df66cac106e2e1d4b5862567841a",
      "bytes": 903,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/recte4.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/recte4.dat",
      "sha256": "183b28b7586ffce3049e9248301668b4e16a84671b0f423efd792fb84a969dfe",
      "bytes": 340,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4con13.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4con13.dat",
      "sha256": "340b30ba8205ef76e4457aaba4620b9a1a2ad13e14bbcacac63dae1dd224812d",
      "bytes": 2435,
      "author": "Michael Heidemann [mikeheide]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4tang.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4tang.dat",
      "sha256": "4eb5b51b824675756efd7e74e1141aaeaa9520517754d3bd0cfc1f591a0e04b4",
      "bytes": 585,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug-1x8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x8.dat",
      "sha256": "e592fd59bdd7333f0430cdd7bebb0d25bfdb3f244af03a17b0be2861c62205b7",
      "bytes": 576,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3623s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3623s01.dat",
      "sha256": "87c2404623acb5ab59cdebe1d0c4a16b471855380a1715ab831b8f1bb2e769f8",
      "bytes": 659,
      "author": "Massimo Maso [Sirio]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug-1x3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x3.dat",
      "sha256": "f24de368545aa96580b811daa6c25e18f5bfdbaca1d4b11addcfa7cbb625f4c9",
      "bytes": 372,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-16tang.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16tang.dat",
      "sha256": "3bf6430f99195afabdaaab755a660c0978080851fd6f514f50ef0e578e6f82e2",
      "bytes": 309,
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box2-9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-9.dat",
      "sha256": "4ebaa1a0a59a2e219b61d376e86cad06dbd36845a3c15bcde3e3d44cd3be473d",
      "bytes": 398,
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4ring12.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4ring12.dat",
      "sha256": "3308fbae0dbb0ac056ed5322a416e37ef39ae9200201cc71cbe6e81ec504a1b4",
      "bytes": 1629,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box4-2p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4-2p.dat",
      "sha256": "a4cb5395b3ec8bba18d81e36c32f43cb9349a55fe97729c367afaa5e1e8b7f0f",
      "bytes": 756,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box2-9p.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-9p.dat",
      "sha256": "6c68301a34e42d105e716e5ae5edf02e3d58978db24619f0364887c339edd331",
      "bytes": 539,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/8-8sphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/8-8sphe.dat",
      "sha256": "27a7d82cce6d579b6a83ddcccee1c38ec1e37781831dae65b2cdf704d84d64b1",
      "bytes": 881,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-8ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8ring2.dat",
      "sha256": "c65d4b41084dd68c63f74ca1f92d7ae9e7a79e5b1632823f24739f3ff8196691",
      "bytes": 934,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug10-2x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug10-2x2.dat",
      "sha256": "860d8586325b33654acf4b20d9275ff078955468eaf86af3c6d7adc624446512",
      "bytes": 790,
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-8cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8cyli.dat",
      "sha256": "9224d4e5edc6f5b0f75f6fa358fd1368a4fd65f676b74fe1bb6e3bbb05046206",
      "bytes": 1303,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug3-1x7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3-1x7.dat",
      "sha256": "381169c4592a6ed096c0011e06e6000c65200492fe6126b3aa9e6a51ae2ba244",
      "bytes": 553,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-4ring1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4ring1.dat",
      "sha256": "e40c29daf302d57b488bb8168aab6755d80adb4e30bc8df24ed34cd42b34dd5c",
      "bytes": 1196,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axl5hol9.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl5hol9.dat",
      "sha256": "d46a457be819e6b46b7fc85f8610b8850e0d0a40556c65b74dbda04179b68a20",
      "bytes": 677,
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cylo.dat",
      "sha256": "792a01362608c3f385dd7f01a1bd7d19cf9ed8a40f793266345cc86d1d98f3af",
      "bytes": 388,
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3941s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3941s01.dat",
      "sha256": "0285481f2422f6e098a36f26cb5337338a26048c348a266a2220e154e6f3a7a2",
      "bytes": 4846,
      "author": "Gerald Lasser [GeraldLasser]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-4cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4cylo.dat",
      "sha256": "b7ff6f92e06cea3815be42f757f17cd28350f2a4ff18dd1a11de0db3626ec44b",
      "bytes": 384,
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-8ring12.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-8ring12.dat",
      "sha256": "3480b87412d6592fcbcfbbea7e1c1120c63b13b96a88bf64a0cbc689ce2aec00",
      "bytes": 986,
      "author": "Niels Karsdorp [nielsk]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/2-4ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4ring2.dat",
      "sha256": "dc1748fff34bb0cae3ba1d480921c2f73de4ea1d0532799356b2014a28c8f393",
      "bytes": 977,
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug3-1x5.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3-1x5.dat",
      "sha256": "85d37bfc3cbb90f12a55dfe2543f507c1763f0336962c712cbec327d688b5624",
      "bytes": 470,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3010s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3010s01.dat",
      "sha256": "f4616eee36d2474da47fae07a5e1ca59888e580854be17a1a9220d0f88c75333",
      "bytes": 914,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4cylc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cylc.dat",
      "sha256": "fdcb54ba2e2731cbb86ea6b2fddb25c7dda060a7780629a72003e0278805dd30",
      "bytes": 430,
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-8cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8cylo.dat",
      "sha256": "870bbbf6052e075598de7dce7efe7a139ea5189820e7a296442fe2b3318c18bf",
      "bytes": 381,
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box2-7.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box2-7.dat",
      "sha256": "e0474c5ad7fb9ff77b67883a5b1e327d028e3eb4e59921a626b4215632dd9f00",
      "bytes": 577,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box4t.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4t.dat",
      "sha256": "9e85c281fff9c33ce26931d772310c8faeeaba4dca1036acf1e6ac578dc50c00",
      "bytes": 963,
      "author": "Tore Eriksson [Tore_Eriksson]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug3-1x3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3-1x3.dat",
      "sha256": "80f86a2ea87dfabc79c3daf963a14c7757caceea6b402ac4f2178a6088de08ac",
      "bytes": 387,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/2-4chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4chrd.dat",
      "sha256": "3b0dfcf2cb881fae0acfe1e53b703104768878636477e540d0c893fc3fd87f8f",
      "bytes": 490,
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axl5ho10.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl5ho10.dat",
      "sha256": "5658b3df4183184a5d5104624ff85b3048a658972991b1dfc489dc05728278ba",
      "bytes": 1173,
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4chrd.dat",
      "sha256": "ccba3a97b5cc358754e476b78b4ce61cce5f404cd15e37471b73df3e81784aec",
      "bytes": 743,
      "author": "Max Martin Richter [MMR1988]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/box4-4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/box4-4a.dat",
      "sha256": "58c69e00462c0a74c1bd6d75d757d826ae13e98bd3928b0e685209003bfbee54",
      "bytes": 1067,
      "author": "Willy Tschager [Holly-Wood]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4disc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4disc.dat",
      "sha256": "3b8faa77185c576085c38f37b13c6a04e2e889eea6a7dc8c4db2d1699a33bcda",
      "bytes": 584,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/4-4cyl1sph2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/4-4cyl1sph2.dat",
      "sha256": "5899ab994c9e2c2a6ed54f01d195c3ff2990f617b64243c06e6b53abfbb3771a",
      "bytes": 1554,
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3024s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3024s01.dat",
      "sha256": "a706692e2c838f20f3b3e4bd5ff03c4ab6c5c0d5816b0944ac39d6100fd85275",
      "bytes": 572,
      "author": "Tore Eriksson [Tore_Eriksson]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/recte3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/recte3.dat",
      "sha256": "e7f5ccbb040191aaa4cd469a25b086299cba4a3eaa8d3b0fbf71240e3de0359a",
      "bytes": 319,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3062bs01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3062bs01.dat",
      "sha256": "b1c8fbaebfab27230569a83c3e47853b7b7b98f9229c2d9540f4f86e9aff0325",
      "bytes": 846,
      "author": "Takeshi Takahashi [RainbowDolphin]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/2-4cylc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4cylc.dat",
      "sha256": "a5b68e5d662209f4139803034f45330ba677b1aff449fb609d95a6f27ddc5469",
      "bytes": 428,
      "author": "Alex Taylor [anathema]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-16ring2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16ring2.dat",
      "sha256": "39481beacecc688590dff4d877e177657d133fbaee449ad60f346c18ccce3d3d",
      "bytes": 580,
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3003s01.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3003s01.dat",
      "sha256": "58f0af5b23ccd2bf3b7569a1b6de0b62cb1ae95520994ba7aa0b37c35b2a8744",
      "bytes": 461,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axlehol3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol3.dat",
      "sha256": "81caa1e48cb356fd74575f2a37a4422d75cafb930fae19182783f48381e48d2f",
      "bytes": 1117,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axl5hol8.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axl5hol8.dat",
      "sha256": "95b2d384c0697cd5dd4ebcc9fd4ab2d005307af5aa611bea20ce832a91f8bc68",
      "bytes": 2237,
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-8sphe.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8sphe.dat",
      "sha256": "c38f9b8df6f260a26e920d8bbfb2d6b11667026e0675733d7fc2d3653ef92c53",
      "bytes": 4040,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug3-1x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug3-1x2.dat",
      "sha256": "e78926d1494fa67b984f390aa1c05d01c35eff99030209e9bbee4e15bfcc0ecb",
      "bytes": 347,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-16cylo.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16cylo.dat",
      "sha256": "a5c8370842299035a9cc14308301614c6fb169fb873a7950c888928cd8d9181c",
      "bytes": 386,
      "author": "J.C. Tchang [tchang]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/joint8socket1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/joint8socket1.dat",
      "sha256": "e86c9edd5355ee2c95b50a29c9e62f5a308279c1dcbe3d10202b9ef509d3d745",
      "bytes": 5733,
      "author": "Tim Gould [timgould]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axlehol2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehol2.dat",
      "sha256": "9d3e161068b049c3a21fbb8c0970d8264215c08bfcefd3508b8bbff47974a319",
      "bytes": 762,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug-1x6.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-1x6.dat",
      "sha256": "907b74bad03688f6d2f22220db6ec4a6c922203a3e3001aa24f214c6ed48a226",
      "bytes": 495,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stud4a.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4a.dat",
      "sha256": "29e414ab757f2a79073aa0d5d10c4c925da1fc239d20019d7615c06db612e2f6",
      "bytes": 871,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-4cyls2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-4cyls2.dat",
      "sha256": "77a3bf3859fa972a5d047721ef18603694f1a6f83543f955240990be9c9ee9bd",
      "bytes": 1189,
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-8chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8chrd.dat",
      "sha256": "7694157b725563188a6efd69b3f558b00533b375b8a4e82f469497a03e471e74",
      "bytes": 561,
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/rect1.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/rect1.dat",
      "sha256": "48fdcd3181587b4bdc89d356a5aee21268688f3f2fcdd4d6f5c1a3d49b1a1ceb",
      "bytes": 556,
      "author": "Chris Dee [cwdee]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/axlehole.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/axlehole.dat",
      "sha256": "8dfcdd5058a66fba2ea4f59ddc7fd4510118baca9f745e5dfe341ccf0e24b49e",
      "bytes": 1974,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stud10.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud10.dat",
      "sha256": "f7dc3947e0f3b81fadffe6509c52723940dfd4d36e30049874d95784a864315a",
      "bytes": 1787,
      "author": "Orion Pobursky [OrionP]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "parts/s/3003s02.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/parts/s/3003s02.dat",
      "sha256": "ceb77e4263964fc1658630d9533118d8feeddf2aeb7d0a1116c6e5bc2318a92f",
      "bytes": 712,
      "author": "Owen Burgoyne [C3POwen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-8cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8cyli.dat",
      "sha256": "46def63dc8293ad9a2dd1d1a5cb720b9ba883850e65d3280d2093c664a6140c4",
      "bytes": 806,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-8edge.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8edge.dat",
      "sha256": "50436a0bce461198c342dccbccb658a1bffae13e44b7c48689b158c946c2c2ab",
      "bytes": 480,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stud4od.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stud4od.dat",
      "sha256": "6f6ba215655349845b069f9647fffa22fbc43cf083dff46900353c3dc579ec72",
      "bytes": 559,
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-4disc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-4disc.dat",
      "sha256": "86c45014c54ad4c82fcf8a96553942c756e39e6b2b109aeccb9f47873f5f3f52",
      "bytes": 916,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/3-16cyli.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/3-16cyli.dat",
      "sha256": "f50d12a37a22ae4a5f37a017b8e39d1e729577b0a4aa376ca685b210806b49c8",
      "bytes": 942,
      "author": "Mark Kennedy [mkennedy]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/joint8socket3.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/joint8socket3.dat",
      "sha256": "1ca3edcebff34b3cd646933c4c92830c3e31528dc8cb71c189c366a6fa7bff0a",
      "bytes": 31171,
      "author": "Magnus Forsberg [MagFors]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/2-4disc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/2-4disc.dat",
      "sha256": "1d4662b73e3196fadeb5ecf2fd27f3dbf7cecce0802cf3d7108ab67bb380eb15",
      "bytes": 803,
      "author": "James Jessiman",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-16chrd.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-16chrd.dat",
      "sha256": "e429dd760eb6f0cf460a74e6ebf52c023bedbdea82de7801efa1694b5a1a82e8",
      "bytes": 701,
      "author": "Philippe Hurbain [Philo]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/stug-2x2.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/stug-2x2.dat",
      "sha256": "16114159ea25719341a852d5403dc9982a6211f2fcb23f5c4c3eac05a2ad43f7",
      "bytes": 765,
      "author": "Steffen [Steffen]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/1-8sphc.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/1-8sphc.dat",
      "sha256": "7de34335dafbbb745901dcfced234f81b4ffaa629c6796837c99dbd375f768c2",
      "bytes": 2451,
      "author": "Franklin W. Cain [fwcain]",
      "license": "Licensed under CC BY 4.0 : see CAreadme.txt"
    },
    "p/empty.dat": {
      "source_archive": "https://library.ldraw.org/library/updates/complete.zip",
      "archive_member": "ldraw/p/empty.dat",
      "sha256": "192c9b9ee2e425cfbc9e9b12ff61ee0f05ae1cb0c12dc37d5590adb6abb65128",
      "bytes": 825,
      "author": "Steffen [Steffen]",
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
