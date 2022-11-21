# PDF 파일 내용을 읽기 위해 설치한 라이브러리 가져오기
import PyPDF2

# 실습용 pdf01.pdf 파일 읽기
pdfReader = PyPDF2.PdfReader(open("../pdf/pdf01.pdf", "rb"))

# PDF 파일의 전체 페이지수
total_pages = pdfReader.numPages
print("total_pages : ", total_pages)

for page_num in range(total_pages):
    text = pdfReader.getPage(page_num).extractText()
    print(text)

