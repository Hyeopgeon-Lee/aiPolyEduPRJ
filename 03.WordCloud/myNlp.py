# 설치한 konlpy 외부라이브러리로부터 Hannanum 기능 사용하도록 설정
from konlpy.tag import Hannanum

# myHannanum 변수에 Hannanum 기능을 넣어줌
myHannanum = Hannanum()

# 앞선 실습에서 진행한 네이버 신문기사로부터 수집한 기사 내용 가져오기
text = open("../news/mynews.txt", encoding="UTF-8").read()

# 형태소 분석에 대한 자연어 처리 결과 출력
print(myHannanum.analyze(text))

