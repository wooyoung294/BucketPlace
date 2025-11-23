### 오늘의 집 과제

이 프로젝트는 오늘의집(BucketPlace) 서비스의 마켓 애플리케이션 설치부터 로그인 완료, 메인 페이지 진입 후 앱 설치 버전 확인까지의 시나리오를
검증하기 위한 Python 기반의 BDD 형식의 테스트 자동화 프로젝트입니다. Pytest 프레임워크와 Appium을 이용했으며 Allure Report를 이용해 테스트 리포트를 출력하였습니다.

#### 리포트 : https://bucketplace.wooyoung.site/

#### TC : https://docs.google.com/spreadsheets/d/1FRAMgWtsoAu7ssuQRfnXZeaDeKHOW6lTFOoQhlH0plc/edit?gid=0#gid=0

#### 파이썬 버전 : 3.13.4
#### Appium 버전 : 2.19.0

#### 프로젝트 구조
```text
BucketPlace/
├── .github/workflows/       # GitHub Actions Lint
├── todays_house/            # 테스트 소스 코드 메인 디렉토리
│   ├── case/                # 개별 테스트 케이스(BDD Stub Func) (Test Cases)
│   ├── scenarios/           # 테스트 시나리오 (Scenarios)
│   ├── steps/               # 테스트 스텝 정의 (재사용 가능한 테스트 동작)
│   ├── util/                # 공통 유틸리티 및 헬퍼 함수
│   │   ├── appium_expect.py # Appium 관련 검증 유틸리티
│   │   └── wait_for_element.py # 요소 대기 관련 유틸리티
│   └── conftest.py          # Pytest 설정 및 공통 Fixture 정의
├── .pre-commit-config.yaml  # 코드 품질 관리를 위한 pre-commit 훅 설정
├── pyproject.toml           # Python 프로젝트 설정 및 도구 설정
└── requirements.txt         # 프로젝트 의존성 패키지 목록
```

#### 테스트 실행
 - pytest (Allure Report 생성하지 않고 실행)
 - pytest --alluredir=allure-results (Allure Report까지 생성)
 - allure serve ./allure-results (Allure Report 실행)
