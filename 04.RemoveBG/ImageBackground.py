from rembg import remove
from PIL import Image

myImage = "../image/02.jpg" # 배경을 삭제하고 싶은 이미지

# 인공지능을 통해 배경이 삭제된 이미지, 반드시 이미지 파일은 배경이 제거되기에 png 파일로 생성되게 함
resultImage = "../remove_image/02_result.png"

input = Image.open(myImage).convert("RGB") # 실습에 사용될 이미지가 RGBA 파일일까봐 강제로 RGB로 변환
output = remove(input) # 배경 삭제
output.save(resultImage) # 배경삭제된 이미지 저장

print("이미지의 배경이 삭제되었습니다.")

