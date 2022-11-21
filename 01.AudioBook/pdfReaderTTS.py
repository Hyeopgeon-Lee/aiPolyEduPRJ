# PDF 파일 내용을 읽기 위해 설치한 라이브러리 가져오기
import PyPDF2

# 문자를 음성으로 변환하기는 TTS 라이브러리 가져오기
import pyttsx3

# TTS 사용하기 위해 초기화
tts = pyttsx3.init()

# 실습용 pdf01.pdf 파일 읽기
pdfReader = PyPDF2.PdfReader(open("../pdf/pdf01.pdf", "rb"))

# PDF 파일의 전체 페이지수
total_pages = pdfReader.numPages
print("total_pages : ", total_pages)

for page_num in range(total_pages):
    text = pdfReader.getPage(page_num).extractText()
    print(text)

    # 문자를 음성으로 변환하기
    tts.say(text)

    # 문자를 음성으로 다 읽어주기까지 파이썬 실행을 종료하지 않고 기다리기
    tts.runAndWait()

# 문자를 모두 다 읽었으면, 실행종료하기
tts.stop()

# 읽은 음성을 mp3 파일로 저장하기
tts.save_to_file("../mp3/myTTS.mp3")

# mp3 파일 생성이 완료되기까지 파이썬 실행을 종료하지 않고 기다리기
tts.runAndWait()
