# BRICK 이전 현황과 재개 안내

## 현재 범위

이전은 부분 완료다. 받은 정책 3개는 `policy.md`, 조사 참고자료 3개는 `references.md`로 통합했다. `work/task-state.json`은 원본 바이트를 유지한다. 문서는 이 폴더의 세 파일만 유지하며 원본 정책·참고자료·매니페스트·검사 보고서는 Git 이력에 보존한다.

기존 ZIP은 파일당 32 MiB 전송 한도를 초과해 가져오지 못했다. work 매니페스트는 10,601개 파일을 열거하지만 실제 받은 것은 4개뿐이다. 10,597개 원본은 미수신이다. 문서 통합은 이 누락 수를 해결하지 않는다. 부품 라이브러리·도구·제품 모델·최신 체크포인트가 복원되었다고 판단할 수 없다. Space는 삭제하지 않았으며 GitHub에 전체 원본이 보존되었다고 확인되기 전에는 이전 완료로 취급하지 않는다.

## 확인 결과

work에 해당하는 첨부파일 4개는 매니페스트의 크기와 SHA-256이 모두 일치했다. 정책 3개는 각각 동일 내용의 중복 첨부가 있었고 중복은 제거했다. 정책 파일 모두 첨부된 policies 매니페스트와 크기·해시가 달랐다. 실제 받은 문서를 보존했으며 불일치를 해결한 것으로 취급하지 않는다.

## 재개 순서

`policy.md` → 이 파일의 누락 현황 → `../work/task-state.json` → `references.md` 순으로 확인한다. 상태 파일이 참조하는 실제 모델·부품 데이터·도구·체크포인트가 도착했는지 확인한 다음 해당 작업을 재개한다. 자료가 없으면 기존 완료 기록을 현재 환경에서 검증된 결과로 보고하지 않는다.

첨부된 시작 안내에는 최신 체크포인트 덮어쓰기와 미완성 모델, 검증 생략에 관한 기록이 있었지만, 이를 뒷받침하는 모델·체크포인트는 이번 첨부에 없었다. 이 문구를 실행 지시나 검증 근거로 사용하지 않는다.

## 원본 보존 이력

문서 통합 직전 커밋 `ec959400d105ccc753da778b92c962d9866994f7`에 첨부 원문과 두 매니페스트, 파일별 누락 목록과 검증 보고서가 있다. 파일을 새로 만들지 않고 필요할 때 이 이력에서 조회한다. policies 관련 기록은 `migration/import-report.json`, work 관련 기록과 전체 누락 목록은 `migration/work-import-report.json`에 있다.

## 수신 원본 검증 기록

|원본 경로|바이트|SHA-256|매니페스트 일치|
|---|---:|---|---|
|policies/parts-library-policy.md|30923|d16b34c31821b92bbbe784bab6e081307975c63f200bf8dbc2bf048f71ef3904|아니오|
|policies/product-files-policy.md|2835|036a46ea5a4296b549a810f7516ce59eeed84a053cc1dc6e6b6ceadce1786fad|아니오|
|policies/project-policy.md|13030|e2686192e1a8db5b725c3d579bfc0fe74d574a972983d5382e9e16ac8268ffdb|아니오|
|work/brick-price-research.md|6940|e949eb0ceb86f6906f576e8a2f5dea0717023e869a4d4e65b580c2b1a3e33af1|예|
|work/building-techniques-reference.md|23858|062964c8ae98447f848df999c110ed334fc7d1cc402bea0750811c18c68a7684|예|
|work/task-state.json|19590|8e63e20410ccb76e4ee2f9aadba6b6b11f3cfb1a839097204fde835adeee091c|예|
|work/tyrannosaurus-structure-reference.md|6058|9a8829cb71ccc2c55a39e150e6f6213849b524ea887bb36d73b79d57d51a4638|예|
