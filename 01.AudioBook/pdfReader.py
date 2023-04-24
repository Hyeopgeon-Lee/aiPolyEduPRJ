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

