# 이미지 파일로부터 문자 인식하는 라이브러리 가져오기
import pytesseract

# 설치한 tesseract 프로그램의 실행파일 위치 설정하기
pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

# tesseract 프로그램에 존재하는 언어별 학습모델 파일 확인하기(기본 제공 학습모델 : eng, osd)
# 한국어는 기본 설치되지 않기에 tesseract 공식 홈페이지에서 학습모델 다운로드 필요함
print("인식 가능한 언어(저장되어 있는 언어별 학습모델파일) : ", pytesseract.get_languages())

# 이미지로부터 한국어와 영어가 혼용된 문자열을 인식하여 text 변수에 저장하기
text = pytesseract.image_to_string("../image/news01.jpg", lang="kor+eng")

# 인식된 문자열 출력하기
print("<인식된 문자열> \n\n", text)
