import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import openai
from playsound import playsound
import datetime
def say(text):
    engine = pyttsx3.init()
    engine.say(f"{text}")
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Speak Anything:")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio , language="en-in")
            print("You Said:", query)
            return query
        except:
            print("Can't Recognise your voice or Some Error Occured")
say("...Hello..I am Desktop Assistant...How can i help you?")
while True:
    print("Listening..........")
    query = takecommand()
    sites = [["Gmail","https://www.gmail.com"],["Youtube","https://www.youtube.com"],["Google","https://www.google.com"],["Wikipedia","https://www.wikipedia.com"],["Facebook","https://www.facebook.com"],["Instagram","https://www.instagram.com"],["Amazon","https://www.amazon.com"],["Flipkart","https://www.flipkart.com"],["Zomato","https://www.zomato.com"],["Swiggy","https://www.Swiggy.com"],["TIT Portal","https://technocratsgroup.edu.in/"],["RGPV Portal","https://www.rgpv.ac.in/"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"Okay! I am opening {site[0]}")
            webbrowser.open(site[1])
    folders = ["Documents", "Downloads", "Pictures", "Music", "Desktop", "Videos"]
    for folder in folders:
        if f"Open {folder}".lower() in query.lower():
            say(f"@ Okay! I am opening {folder} system folder")
            d = "C:\\Users\\asus\\" + folder.capitalize()
            os.startfile(d)
    App = ["camera", "paint", "Whatsapp", "spotify", "word", "excel", "mail", "calender", "microsoft edge", "setting",
           "clock", "calculator"]
    for i in App:
        if f"Open {i}".lower() in query.lower():
            say(f"@ Okay! I am opening {i}")
            from AppOpener import open
            open(i.capitalize(), match_closest=True)
    Music_1 =["song","music"]
    for music in Music_1:
        if f"play {music}".lower() in query.lower():
            M = "C:/Users/asus/Downloads/music1/mm.mp3"
            say(f"@ Okay! I am playing {music}")
            playsound(M)
            break
    if f"what is the time".lower() in query.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strfTime)
        say(f"@ The Time is {strfTime} ")
    else:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                import webbrowser
                text = a.recognize_google(audio)
                print("You Said:", text)
                webbrowser.open("https://google.co.in/search?q=" + text)
            except:
                say("Sorry! could not recognize your voice")













