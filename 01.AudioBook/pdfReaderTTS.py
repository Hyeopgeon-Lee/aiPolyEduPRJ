# 문자를 음성으로 변환하기는 TTS 라이브러리 가져오기
import pyttsx3

# TTS 사용하기 위해 초기화
tts = pyttsx3.init()

# 2022.03 기준 업데이트된 PyPDF2 v3.0 프로그램 소스
from PyPDF2 import PdfReader

reader = PdfReader("../pdf/novel1.pdf")

total_pages = len(reader.pages)
print("전체 페이지 수 : ", total_pages)

# PDF 전체 페이지수 만큼 반복하기
for page_num in range(total_pages):

    # 페이지별 추출된 문자를 text 변수에 저장하기
    text = reader.pages[page_num].extract_text()

    # 저장된 Text 변수를 출력하여 인식된 문자를 보여주기
    print(text)

    # 말하기 속도 조절(기본값 : 200 / 값이 클수록 말속도가 빠르며, 작으면 느림)
    tts.setProperty("rate", 180)

    # 문자를 음성으로 변환하기
    tts.say(text)

    # 문자를 음성으로 다 읽어주기까지 파이썬 실행을 종료하지 않고 기다리기
    tts.runAndWait()

# 문자를 모두 다 읽었으면, 실행종료하기
tts.stop()


