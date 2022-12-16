import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import pyautogui

# Name: Abhishek Laxman KOrde.
# Class:Final Year 
# Branch:CSE
# Roll: 02.
# PRN : 1967571242002.

Assistant=pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[0].id)

def Speak(audio):
    print(" ")
    Assistant.say(audio)
    print(f":{audio}")
    Assistant.runAndWait()

# It recognize Audio of Speeker and work
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold=1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query=command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except Exception as Error:
            return "none"

        return  query.lower()       

# Speak("Hello Sir , I am Jarvis, Your Personal AI Assistant , How may Ihelp you")

query= takecommand()

# if 'hello' in query:
#     Speak("Hello Sir ")

# else:
#     Speak("No command found")

def TaskExe():

    def Music():
        Speak("Tell me the music name of song ")
        musicname = takecommand()
        if 'closer' in musicname:
            os.startfile('')
        elif 'not afraid' in musicname:
            os.startfile('')    
        
        else:    
            pywhatkit.playonyt(musicname)
        
        Speak("Your Song has Been started")
 
    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I am Jarvis, Your Personal AI Assistant , How may I help you")
        
        elif 'how are you' in query:
            Speak("I am fine sir!")
            Speak("Whats About you?")

        elif 'You need a break Jarvis' in query:
            Speak("Ok sir, You can call Me Anytime !")
            break
        
        elif 'bye' in query:
            Speak("Ok sir ,Have a Good day, Bye!")
            break

        elif 'youtube search' in query:
            Speak("Ok sir , !")
            query=query.replace("jarvis","")
            web='https://www.youtube.com/results?search_query='
            webbrowser.open(web)
            Speak("Done Sir.")
        
        elif 'google search' in query:
            Speak("This Is What i found your Serarch sir!") 
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir!")    
#Open Any Website         
        elif 'website' in query:
            Speak("Ok sir , Launching....")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            web1  = query.replace("Open", "")
            web2 = 'httpps://www.'+web1+ '.com'
            webbrowser.open(web2)
            Speak("Lanched!") 

        elif 'launch' in query:
            Speak("Tell Me the name of the website!")
            name=takecommand()
            web='https://www.' +name+ '.com'
            webbrowser.open(web)
            Speak("Done Sir!")   
 #To open any link we use webbrowser        
        elif 'open instagram' in query:
            Speak("ok sir")
            webbrowser.open("https://www.instagram.com")
            Speak("Done Sir!")
        
        elif 'search music' in query:
            Music()

        # elif 'wikipedia' in query:
        #     Speak("Search wikipedia....")
        #     query= query.replace("jarvis", "")
        #     query= query.replace("wekipedia","")
        #     wiki=wikipedia.summmary(query,2)
        #     Speak(f"According to wikipedia :{wiki}")    

        # elif 'screenshot' in query:
        #     kk=pyautogui.screenshot()
        #     kk.save('D:\Git\\')  
            
TaskExe()              