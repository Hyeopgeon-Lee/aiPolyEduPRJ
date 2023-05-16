import cv2

# 이미지 파일로부터 문자 인식하는 라이브러리 가져오기
import pytesseract

# 설치한 tesseract 프로그램의 실행파일 위치 설정하기
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 분석하기 위한 이미지 불러오기
image = cv2.imread("../image/news01.jpg", cv2.IMREAD_COLOR)

# 흑백사진으로 변경
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)

# 이미지로부터 한국어와 영어가 혼용된 문자열을 인식하여 text 변수에 저장하기
text = pytesseract.image_to_string(gray, lang="kor", config="--oem 3")

# 인식된 문자열 출력하기
print("<인식된 문자열> \n\n", text)

cv2.waitKey(0)
# cv2.destoryAllWindows()
