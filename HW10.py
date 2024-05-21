
from gtts import gTTS
import playsound

tts=gTTS("Hello my name is park-yu-kyeong",lang="ko")

tts.save("[i-seed]환경대기과학전공 박유경.mp3")
playsound.playsound("i-seed.mp3",True)
