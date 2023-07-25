import speech_recognition as sr
import os

def say (text):
    os.system(f"say {text}")

def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-in")
        print(f"User said = {query}")
        return query

if __name__ == '__main__':
    print('PyCharm')
    say ("Hello I am Jarvis A.I") 
    print("Listening")
    text = takeCommands()
    say(text)