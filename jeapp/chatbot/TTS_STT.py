
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


#     print("인식된 텍스트:", text_output)
#     if "굿바이" in text_output:
#         break

def  text_mp3_save(text1):

    tts = gTTS(text=text1, lang='ko')
    tts.save("/static/stt/player.mp3")


def text_to_speech():
    # 음성 파일 재생
    pygame.mixer.init()
    pygame.mixer.music.load("/static/stt/player.mp3")
    pygame.mixer.music.play()

    # 재생이 끝날 때까지 대기
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
