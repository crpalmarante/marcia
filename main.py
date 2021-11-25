from speech_recognition import Recognizer
import speech_recognition

r = Recognizer()
with speech_recognition.Microphone as source:
    audio = r.listen(source)
    print(r.recognize_google(audio))
    