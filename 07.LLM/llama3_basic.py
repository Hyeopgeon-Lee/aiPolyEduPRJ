import ollama

stream = ollama.chat(  # 라마3로부터 생성된 답변을 실시간 받기
    # 사용 모델
    model="llama3",

    # 명령어
    messages=[{"role": "user", "content": "Between 'llama3 AI' and 'chatgpt4 AI', who provides accurate information?"}],

    # 응답결과 실시간 받기 설정
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)  # 응답 결과 실시간 출력하기

