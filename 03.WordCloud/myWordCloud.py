
# 앞선 실습에서 진행한 네이버 신문기사로부터 수집한 기사 내용 가져오기
text = open("../news/mynews.txt", encoding="UTF-8").read()

# 예시 문장 출력
print(text)

# 설치한 wordcloud 외부라이브러리로부터 WordCloud 기능 사용하도록 설정
from wordcloud import WordCloud

# 설치한 matplotlib 외부라이브러리의 pyplot 기능을 사용하며, pyplot 기능을 약어로 plt로 정의
import matplotlib.pyplot as plt

# 워드 클라우드를 생성하며, 생성된 워드 클라우드를 myWC 이름의 변수에 저장하기
# 워드 클라우드를 표시하는 단어가 한글일 경우, 파이썬에서 인식 불능 현상이 발생할 수 있기 때문에 글꼴을 강제 설정함
# 원하지 않는 단어를 제외하기 위해 WordCloud 기능의 stopwords 옵션에 stopwords 변수 값을 넣어줌
myWC = WordCloud(font_path="font/NanumGothic.ttf", background_color="white").generate(text)

# 워드 클라우드의 크기 정의
plt.figure(figsize=(5, 5))

# 워드 클라우드의 이미지의 부드럽기 정도
plt.imshow(myWC, interpolation="lanczos")

# x, y축에 기본 숫자들 제거
plt.axis('off')

# 워드 클라우드 보여주기
plt.show()