from pdf2docx import Converter

# PDF 내 문장을 가져오기
cv = Converter("../pdf/report1.pdf")

# 가져온 문장을 docx 파일로 변환하기
cv.convert("../docx/report1.docx")

# 사용 완료하여 닫기
cv.close()
