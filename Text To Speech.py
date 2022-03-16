from gtts import gTTS
import playsound

while True:
    mytext = input("Enter your Text Here:   ")
    tts = gTTS(text=mytext, lang='en')
    filename = "welcome.mp3"
    tts.save(filename)
    playsound.playsound(filename)


