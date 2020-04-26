# 코로나 웹 사이트 CSS 분석기로 보여주고
# 실제 우리기 크롬에서 엔터칠때 일어나는 일들 설명
# 첫번째 HTML 받아옴
# HTML 에서 필요한 CSS/이미지/JS 받아옴
# CSS/이미지 출력, JS 실행
# 끝.

# 검색엔진 입장에서 생각하기
# 주로 파악하는 것, HTML 의 생김새
# 이미지가 이쁜지 아직 모름. 글씨크기가 적당한지 가독성이 어떤지 잘모름
# 이미지 같은거 하기에 너무 무거움. HTML 엄청가벼움
# 즉 HTML 을 잘 다듬어야한다
# HTML 태그 이쁘게 열고 닫기, 접근성 높여주기, 표준에 맞추기 등.

# 코로나 근황 출력
# CSS 셀렉터이야기
# 네이버 실시간 검색어 가져오기
# 유튜브 검색어별 채널/구독자수 가져오기

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://coronaboard.kr')
