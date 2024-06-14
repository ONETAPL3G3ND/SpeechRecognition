#https://github.com/ONETAPL3G3ND
import speech_recognition as sr
import pyaudio


recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Скажи что-нибудь...")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google(audio, language="ru-RU")
    print(f"Распознанная речь: {text}")
except sr.RequestErroг:
    print("Ошибка при запросе к API Google")
except sr.UnknownValueError:
    print("Не удалось распознать речь")
