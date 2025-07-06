import pyttsx3 as p 
import datetime, time
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import pyautogui as py
import os
import sys
import pyjokes as j


engine = p.init()

voices = engine.getProperty('voices')
change_voice = engine.setProperty('voice', voices[1].id)   
rate= engine.getProperty('rate')
engine.setProperty('rate', 158)
 
def choose_voice():
    voice_in = input("Choose the type of voice you would like to use(Male or Female): ")
    if voice_in == "Male" or "male":
        change_voice = engine.setProperty('voice', voices[0].id)
    elif change_voice == "Female" or "female":
        change_voice = engine.setProperty('voice', voices[1].id)
    else:
        print("Incorrect Parameter !")

choose_voice()
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
        
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
 
    speak("How can I help you?")

def takevoice():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Go on, I'm Listening....")
        audio = recognizer.listen(source)

    try:
        print("Recognizing....")
        text = recognizer.recognize_google(audio, language='en-in')
        print("You said: {}".format(text))
    except Exception as e:
        print(e)
        print("Sorry, I didn't understood what you just said")
        return "None"
    return text

def joke():
    joker = j.get_joke(language="en", category="all")
    speak(joker)
    print(joker)




if __name__ == "__main__":

    
        text = takevoice().lower()# Converting user query into lower case
        # Logic for executing tasks based on query
        if "search" in text:  #if wikipedia found in the query then this block will be executed
            speak('Searching...')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3) 
            speak("here you go, According to Wikipedia")
            print(results)
            speak(results)

# Basic Commands ---->
        if "open chrome" in text:
            speak("Opening chrome")
            webbrowser.open("https://www.google.com")
            
        if "open gmail" in text:
            speak("Okay, opening your gmail...")
            webbrowser.open("https://mail.google.com/")  

        if "open yahoo" in text:
            speak("Okay, opening yahoo...")
            webbrowser.open("https://in.yahoo.com/")
         
        if "open map" in text:
            speak("Okay, opening maps....")
            webbrowser.open("https://www.google.com/maps/")
        
        if "open youtube" in text:
            speak("What do you want me to search in it?")
            sniff = takevoice()
            speak("Okay opening youtube and searching for "+sniff)
            webbrowser.open("https://www.youtube.com/results?search_query="+sniff)
        
        if "open google" in text:
            speak("What do you want to search on google ?")
            google1 = takevoice()
            speak("Okay opening google and looking for"+google1)
            result=webbrowser.open("https://www.google.com/search?q="+google1)
        
        if "open calculator" in text:
            speak("Okay, opening calculator...")
            os.system("calc.exe")
        
        if "start recording" in text:
            py.hotkey('win', 'alt', 'r')
       
        if "open notepad" in text: 
            subprocess.call("notepad.exe")
        
        if "open command prompt" or "open cmd " in text:
            subprocess.call("cmd.exe")

# Windows Commands ---->   

        if "shutdown" in text:
            speak("Okay, shuting down the computer in 5 seconds....")
            os.system("shutdown /s /t 5 /c goodbye")
        
        if "restart" in text:
            speak("Okay, restarting the computer in 5 seconds")
            os.system("shutdown /r /t 5")

        if "log out" in text:
            speak("Okay,logging out....")
            os.system("shutdown /l")

        if "close" in text: 
            py.hotkey('alt', 'f4')

        if "disconnect wifi" in text:
            os.system("netsh wlan disconnect")
            speak("wifi disconnected")
  

# Social Training ---->  
        if "joke" in text:
            speak("Okay here's one") or speak("here it comes")
            joke()

        if "what can you do" in text:
            speak("I can perform some basic tasks for you, like you can ask me Hey Cassandra, shutdown my pc or Hey Cassandra, Open Gmail, I can also tell you jokes, just ask, Hey Cassandra tell me a joke")

        if "who created you" in text:
            speak("I was created by Harshit Singh.")

        if "are you male or female" in text:
            speak("I am a virtual assistant designed by Harshit, how can I help you?")

        if "thanks" or "thank you" in text:
            speak("You're Welcome")

        if "i am fine" in text:
            speak("good to hear that, can I help you with something?")

        if "how are you" in text:
            speak("Thanks for asking, I am doing great, can I do something for you?")

        if "Goodbye" or "shut up" in text:
            speak("Okay, Call me anytime you want.....")
            sys.exit()
                
        if "repeat" in text:
            speak("Okay, go on....")
            repeat = takevoice()
            speak(repeat)

        if "day" in text:
            day = datetime.datetime.now()
            speak("today the day is "+ day.strftime("%A"))

        if "time" in text:
            now3 = datetime.datetime.now()
            real_time = now3.strftime("%H:%M")
            speak("The time now is "+real_time)

        if "hello" in text:
            speak("Hey there, I hope you are fine...")
        
        if "hey" in text:
            speak("Hi, how can I help you ?")

        if "hi" in text:
            speak("hey there, I hope you are fine. How can I help you ?")

        if "what is your name" in text:
            speak("I am your personal assistant Cassandra, how can I help you??") 
            
        if "switch window" in text:
            py.hotkey('alt', 'tab')
        
        if "good morning" in text:
            wishme()

        if "good afternoon" in text:
            wishme()
        
        if "good evening" in text:
            wishme()
        
        

            
