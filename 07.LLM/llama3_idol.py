import ollama

stream = ollama.chat(  # 라마3로부터 생성된 답변을 실시간 받기
    model="llama3",  # 사용 모델
    messages=[{"role": "user", "content": "K-POP 그룹인 'LE SSERAFIM'과  'ITZY' 중 누가 더 팬들에게 인기 많을까?"},
              {"role": "user", "content": "한글로 번역해서 알려줘"}],  # 명령어
    stream=True,  # 응답결과 실시간 받기 설정
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)  # 응답 결과 실시간 출력하기
