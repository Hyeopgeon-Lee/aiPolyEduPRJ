import ollama

stream = ollama.chat(  # 라마3로부터 생성된 답변을 실시간 받기
    model="llama3",  # 사용 모델
    messages=[{"role": "user",
               "content": "2023년 '서울 강서구'에 있는 '인스타그램'의 리뷰가 매우 좋은 커피숍 3개와 그 커피숍의 주소를 알려줘"},
              {"role": "user", "content": "한글로 번역해서 알려줘"}
              ],  # 명령어

    stream=True,  # 응답결과 실시간 받기 설정
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)  # 응답 결과 실시간 출력하기
