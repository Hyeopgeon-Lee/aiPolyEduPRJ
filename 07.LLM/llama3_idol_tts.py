# 문자를 음성으로 변환하기는 TTS 라이브러리 가져오기
import pyttsx3
import ollama

print("LLAMA3를 통해 분석을 시작합니다.")
result = ollama.chat(  # 라마3로부터 생성된 답변을 실시간 받기
    model="llama3",  # 사용 모델
    messages=[{"role": "user", "content": "K-POP 그룹인 'LE SSERAFIM'과  'ITZY' 중 누가 더 팬들에게 인기 많을까?"},
              {"role": "user", "content": "한글로 번역해서 알려줘"}],  # 명령어
)

print("LLAMA3를 통해 분석이 종료되었습니다.")

message = result["message"]["content"]
print(message)  # 결과 출력하기

# TTS 사용하기 위해 초기화
tts = pyttsx3.init()

# 말하기 속도 조절(기본값 : 200 / 값이 클수록 말속도가 빠르며, 작으면 느림)
tts.setProperty("rate", 180)

# 말하기
tts.say(message)

# 파이썬이 종료되는 것을 막기 위해 말 끝날 때까지 대기
tts.runAndWait()

# 종료하기
tts.stop()
