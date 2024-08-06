import pyttsx3

# pyttsx3 초기화
engine = pyttsx3.init()

# 사용 가능한 목소리 나열
voices = engine.getProperty('voices')

# 영어 남자 목소리 선택
for voice in voices:
    print("설치된 음성 :", voice.name.lower())
    if 'english' in voice.name.lower() and ('male' in voice.name.lower() or 'man' in voice.name.lower()):
        engine.setProperty('voice', voice.id)
        break

# 읽을 텍스트
text = "Hello, welcome to the world of Python programming!"

# 텍스트 읽기
engine.say(text)
engine.runAndWait()
