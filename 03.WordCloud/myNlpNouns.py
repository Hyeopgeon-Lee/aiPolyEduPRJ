# 설치한 konlpy 외부라이브러리로부터 Hannanum 기능 사용하도록 설정
from konlpy.tag import Hannanum

# 문자열(문장) 수정을 위한 파이썬 기본 기능 추가
import re

# myHannanum 변수에 Hannanum 기능을 넣어줌
myHannanum = Hannanum()

# 앞선 실습에서 진행한 네이버 신문기사로부터 수집한 기사 내용 가져오기
text = open("../news/mynews.txt", encoding="UTF-8").read()

# 단어 분석의 정확도를 높이기 위해 특수문자 제거
# 특수문자는 키보드 상단 숫자패드의 특수문자가 발견되면 한칸 공백으로 변경
replace_text = re.sub("[!@#$%^&*()_+]", " ", text)

# 특수문자가 제거된 문장 출력
print(replace_text)

# 명사만 List 형태의 배열로 출력
print(myHannanum.nouns(replace_text))

