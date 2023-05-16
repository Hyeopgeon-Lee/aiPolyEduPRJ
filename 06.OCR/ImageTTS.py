# 이미지 파일 불러오기
from PIL import Image

# 이미지 파일로부터 문자 인식하는 라이브러리 가져오기
import pytesseract

# 문자를 음성으로 변환하기는 TTS 라이브러리 가져오기
import pyttsx3

# 설치한 tesseract 프로그램의 실행파일 위치 설정하기
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# tesseract 프로그램에 존재하는 언어별 학습모델 파일 확인하기(기본 제공 학습모델 : eng, osd)
# 한국어는 기본 설치되지 않기에 tesseract 공식 홈페이지에서 학습모델 다운로드 필요함
print("인식 가능한 언어(저장되어 있는 언어별 학습모델파일) : ", pytesseract.get_languages(config=''))

# 이미지로부터 한국어와 영어가 혼용된 문자열을 인식하여 text 변수에 저장하기
text = pytesseract.image_to_string(Image.open("../image/news01.jpg"), lang="kor+eng")

# 인식된 문자열 출력하기
print("<인식된 문자열> \n\n", text)

# TTS 사용하기 위해 초기화
tts = pyttsx3.init()

# 말하기 속도 조절(기본값 : 200 / 값이 클수록 말속도가 빠르며, 작으면 느림)
tts.setProperty("rate", 180)

# 말하기
tts.say(text)

# 파이썬이 종료되는 것을 막기 위해 말 끝날 때까지 대기
tts.runAndWait()

# 종료하기
tts.stop()
