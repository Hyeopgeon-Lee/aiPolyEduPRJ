# PDF 파일 내용을 읽기 위해 설치한 라이브러리 가져오기
import PyPDF2

# 실습용 pdf01.pdf 파일 읽기
pdfReader = PyPDF2.PdfReader(open("../pdf/novel1.pdf", "rb"))

# PDF 파일의 전체 페이지수
total_pages = pdfReader.numPages
print("전체 페이지 수 : ", total_pages)

# PDF 전체 페이지수 만큼 반복하기
for page_num in range(total_pages):
    
    # 페이지별 추출된 문자를 text 변수에 저장하기
    text = pdfReader.getPage(page_num).extractText()
    
    # 저장된 Text 변수를 출력하여 인식된 문자를 보여주기
    print(text)

