
import speech_recognition as sr
from gtts import gTTS
import pygame


# 음성 인식 객체 생성
recognizer = sr.Recognizer()

# 마이크에서 실시간 음성 입력을 받아오는 함수
def listen_to_microphone():
    with sr.Microphone() as source:
        print("마이크에서 음성을 입력하세요...")
        recognizer.adjust_for_ambient_noise(source)  # 환경 소음 제거 (선택 사항)
        audio = recognizer.listen(source)
    return audio

# 음성을 텍스트로 변환하는 함수
def speech_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language="ko-KR")  # 한국어 인식
        with open('C:/edu_busan_202305/final_project_13/MyDrive/새 폴더/memo.txt', 'a') as f:
            f.write(str(text)+"\n")
        return text
    except sr.UnknownValueError:
        return "음성을 이해할 수 없습니다."
    except sr.RequestError as e:
        return f"오류 발생: {e}"
    
    
################################
# 메인 루프
text_list=[]
# while True:
#     audio_input = listen_to_microphone()
#     text_output = speech_to_text(audio_input)
text_list.append(text_output)

#     print("인식된 텍스트:", text_output)
#     if "굿바이" in text_output:
#         break


text ="안녕하세요, 라이브러리를 사용하여 집에 가면 머하시나요? 안녕하세요, 라이브러리를 사용하여 집에 가면 머하시나요 안녕하세요, 라이브러리를 사용하여 집에 가면 머하시나요 안녕하세요, 라이브러리를 사용하여 집에 가면 머하시나요"

tts = gTTS(text=text, lang='ko')
tts.save("./data/helloEN.mp3")



# 음성 파일 재생
pygame.mixer.init()
pygame.mixer.music.load("./data/helloEN.mp3")
pygame.mixer.music.play()

# 재생이 끝날 때까지 대기
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)