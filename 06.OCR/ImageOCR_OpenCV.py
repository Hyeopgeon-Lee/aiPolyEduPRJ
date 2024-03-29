import cv2

# 이미지 파일로부터 문자 인식하는 라이브러리 가져오기
import pytesseract

# 설치한 tesseract 프로그램의 실행파일 위치 설정하기
pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

# 분석하기 위한 이미지 불러오기
image = cv2.imread("../image/number3.png", cv2.IMREAD_COLOR)

# 흑백사진으로 변경
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 완전한 흑백으로 변환하기
ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.medianBlur

cv2.imshow("gray", thresh1)

# 이미지로부터 한국어와 영어가 혼용된 문자열을 인식하여 text 변수에 저장하기
text = pytesseract.image_to_string(thresh1, lang="kor", config="--oem 3 --psm 4")

# 인식된 문자열 출력하기
print("<인식된 문자열> \n\n", text)

cv2.waitKey(0)
# cv2.destoryAllWindows()
