from rembg import remove
from PIL import Image
from io import BytesIO
import requests

# 인터넷 상에 존재하는 배경을 삭제하고 싶은 이미지 URL 주소
url = "https://file2.nocutnews.co.kr/newsroom/image/2023/04/07/202304071105133719_0.jpg"

myImage = requests.get(url)  # url에 접속하여 배경을 삭제하고 싶은 이미지 파일을 가져오기

# 인공지능을 통해 배경이 삭제된 이미지, 반드시 이미지 파일은 배경이 제거되기에 png 파일로 생성되게 함
resultImage = "../remove_image/03_result.png"

input = Image.open(BytesIO(myImage.content)).convert("RGB")  # 실습에 사용될 이미지가 RGBA 파일일까봐 강제로 RGB로 변환
output = remove(input)  # 배경 삭제
output.save(resultImage)  # 배경삭제된 이미지 저장

print("이미지의 배경이 삭제되었습니다.")
