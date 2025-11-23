Feature: 오늘의집 마켓 애플리케이션 설치부터 로그인 완료, 메인 페이지 진입 후 앱 설치 버전 확인까지의 시나리오


  Scenario: 최초 페이스북으로 가입한 이메일로 카카오로 로그인
    When TC_001 Playstore [검색] 버튼 클릭
    When TC_002 Playstore "오늘의 집" 검색
    When TC_003 Playstore 검색 결과 목록에서 [오늘의 집] 클릭
    When TC_004 Playstore [오늘의 집] 앱 버전 "25.36.1" 확인
    When TC_005 Playstore [오늘의 집] 앱 설치
    When TC_006 Playstore 오늘의 집 앱 [열기] 버튼 클릭
    When TC_007 [카카오톡으로 계속하기] 버튼 클릭
    When TC_010 [기존 계정 로그인] 버튼 클릭
    When TC_012 오늘의집 집요한 BLACK FRIDAY 페이지 닫기
    When TC_013 [마이페이지] 버튼 클릭
    When TC_014 오감지수 서비스 오픈 바텀시트 닫기
    When TC_015 [설정] 버튼 클릭
    Then TC_016 앱 마켓과 동일한 버전 노출


  Scenario: 최초 페이스북으로 가입한 이메일로 페이스북으로 로그인
    When TC_001 Playstore [검색] 버튼 클릭
    When TC_002 Playstore "오늘의 집" 검색
    When TC_003 Playstore 검색 결과 목록에서 [오늘의 집] 클릭
    When TC_004 Playstore [오늘의 집] 앱 버전 "25.36.1" 확인
    When TC_005 Playstore [오늘의 집] 앱 설치
    When TC_006 Playstore 오늘의 집 앱 [열기] 버튼 클릭
    When TC_011 [페이스북] 아이콘 버튼 클릭
    When TC_012 오늘의집 집요한 BLACK FRIDAY 페이지 닫기
    When TC_013 [마이페이지] 버튼 클릭
    When TC_014 오감지수 서비스 오픈 바텀시트 닫기
    When TC_015 [설정] 버튼 클릭
    Then TC_016 앱 마켓과 동일한 버전 노출

  Scenario: 최초 페이스북으로 가입한 이메일로 네이버로 로그인
    When TC_001 Playstore [검색] 버튼 클릭
    When TC_002 Playstore "오늘의 집" 검색
    When TC_003 Playstore 검색 결과 목록에서 [오늘의 집] 클릭
    When TC_004 Playstore [오늘의 집] 앱 버전 "25.36.1" 확인
    When TC_005 Playstore [오늘의 집] 앱 설치
    When TC_006 Playstore 오늘의 집 앱 [열기] 버튼 클릭
    When TC_008 [네이버] 아이콘 버튼 클릭
    When TC_009 네이버 오늘의집 전체 약관 동의 후 [동의하기] 버튼 클릭
    When TC_010 [기존 계정 로그인] 버튼 클릭
    When TC_012 오늘의집 집요한 BLACK FRIDAY 페이지 닫기
    When TC_013 [마이페이지] 버튼 클릭
    When TC_014 오감지수 서비스 오픈 바텀시트 닫기
    When TC_015 [설정] 버튼 클릭
    Then TC_016 앱 마켓과 동일한 버전 노출
