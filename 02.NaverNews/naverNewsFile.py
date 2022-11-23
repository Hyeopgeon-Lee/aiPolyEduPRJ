# 네이버 뉴스로부터 웹크롤링하기 위해 request 활용
import requests

# 네이버 뉴스 HTML 소스의 내용을 가져오기 위해 활용
from bs4 import BeautifulSoup

# 네이버는 정상적인 접근(사용자 직접 네이버 접속)이 아닌 웹 크롤링 등 비정상적인 접근을 방지 하게 위해 HTTP 해더 정보를 요구함
# HTTP 해더는 웹URL에 접속할 때, 네이버 서버에 제공하는 메타 정보
# 네이버는 HTTP 해더 정보 중 User-Agent 값의 유무를 체크함
# 따라서 네이버에 임의의 값을 넣어줌
headers = {
    "User-Agent": "Seoul Gangseo Campus of Korea Polytechnics College, Dept. of Data Analysis / Python Education"}

# 수집할 신문기사 URL
webpage = requests.get("https://entertain.naver.com/read?oid=009&aid=0004968578", headers=headers)

# URL로부터 읽은 HTML 내용을 파이썬에서 처리할 수 있게 파싱하기
soup = BeautifulSoup(webpage.content, "html.parser")

# 신문기사 본문 내용을 문자열로 저장하기
#naver_news = soup.select_one("#dic_area").get_text().strip()
naver_news = soup.select_one("#articeBody").get_text().strip()

# 신문기사 출력
print(naver_news)

#파일만 생성(내용 없음) 생성시, 파일이 존재하면 덮어쓰기함
f = open("../news/mynews.txt", "w",  encoding="UTF-8")

# 수집한 내용을 파일 내용에 저장
f.write(naver_news)

# 생성된 파일 닫기
f.close()

