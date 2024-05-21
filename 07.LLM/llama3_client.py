from ollama import Client

print("LLAMA3를 통해 분석을 시작합니다.")

# 내컴퓨터에 설치된 LLAMA3 부르기
# localhost: 내 컴퓨터를 의미하며, 외부 컴퓨터(서버)에 LLAMA3 설치되었다면, 그 컴퓨터 IP 작성
# 11434 : LLAMA3가 기본적으로 사용하는 통신 포트
client = Client(host='http://localhost:11434')

result = client.chat(model='llama3', messages=[
    {
        "role": "user",
        "content": "2024년 현재 대한민국의 대통령 이름은 무엇이니?",
    },
])

print("LLAMA3를 통해 분석이 종료되었습니다.")

message = result["message"]["content"]
print("결과 : ", message)  # 결과 출력하기

