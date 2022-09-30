'''

    데이터 분석

    데이터 수집
    -DB
    -파일( 로컬 파일) ex) txt,csv,xsl
    -특정 사이트에서 제공하는 Data (사기업: 카카오,naver,... , 공기업:국가 ) -> * .csv, *xml, *json
                            (캐글)
    - 크롤링 - 웹사이트의 임의의 data를 몰래 수집

    -> dataFrame  - sql의 table 형식 데이터 구조
        => sql 의 테이블과는 차이가 있다. column header 뿐만 아니라 행과 열 단위로 index 또한 존재함
        => pandas 의 인덱스는 기본은 1,2,3.. 그러나 변경이 가능하다. 숫자 뿐만 아니라 문자도 가능하다.
        => 행의 index는 보통 행 label 이라고 칭한다.
        => 컬럼명은 컬럼 label 이라고 칭한다.
        => 진짜 위치 값이 존재한다. -> 우리가 알고 있는 index가 이에 해당한다. 따라서 변경되지 않는다.
            => 처음 만들어지는 행 label은 위치값과 같은 값이 되기 때문에 헷갈릴 수 있다.
    -> Series : 한 개의 행 또는 열 을 의미 한다 (한 개라는 것이 중요)
        => 따라서 dataFrame은 여러개의 Series가 모여서 만들어졌다고 생각하면 된다.

    시각화
    1. matplotlib 라이브러리 : 초창기에 나왔고
                            사용하기 어렵다
                            pandas, numpy 연동 어렵다.
    2. seaborn 라이브러리 : 조금 더 최신에 나왔다.
        matplotlib 기반
        pandas, numpy 연동 가능

    3. pandas 시각화  내부적으로 matplotlib 연동

'''