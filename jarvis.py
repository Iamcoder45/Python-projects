import pyttsx3

# sudo apt install libespeak1 
# linux mei ye v install krna prta hai taki permission mile user ko


import speech_recognition as sr

#sudo apt install python3-pyaudio  
# ye pacakage v install krenge linux mei usne krne ke luye


import webbrowser

import datetime
import pyjokes


def speak(x):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()


speak("welcome ")

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("please speak ")
        recognizer.adjust_for_ambient_noise(source , duration=1)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data= recognizer.recognize_google(audio)
            print(data)
            return data

        except sr.UnknownValueError:
            speak("nothing")



if __name__ == '__main__':

    data1=sptext().lower()

    print(data1)
    if "your name" in data1:
        name="my name is peter"
        speak(name)
    if "your age" in data1:
        name="when you run this code lol haha"
        speak(name)

    if "time" in data1:
        time=datetime.datetime.now().strftime("%I%M%p")
        print(time)
        speak(time)

    if "youtube" in data1:
        webbrowser.open("https://www.youtube.com/")
    
    if "google" in data1:
        webbrowser.open("https://www.google.com/")

    if "search" in data1:
        data2=sptext()
        data3="https://www."+data2+".com/"
        webbrowser.open(data3)
    
    if "joke" in data1:
        j1=pyjokes.get_joke(language="en",category="natural")
        speak(j1)

        





