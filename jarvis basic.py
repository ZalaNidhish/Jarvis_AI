import speech_recognition as sr #listen
import pyttsx3        #text to speech  
import datetime      #wishing
import os           # open apps
import wikipedia    #wikipedia
import webbrowser   #google
import pywhatkit as kit #youtube
import sys #exit
import time
import pyjokes #jokes
import pyautogui


#voice for jarvis
engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voice",voice[0].id)
 
#speaking jarvis
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#listening jarvis
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
            print("Listening...")
            listener.pause_threshold = 1
            voice = listener.listen(source,0,10)
            
    try:
        query = listener.recognize_google(voice)
        query = query.lower()
        print(query)
        #speak(query)
        
    except:
        
        # print("sorry,didn't hear it")
        # speak("sorry,didn't hear it")
         return "None"
    return query
    
#wishing owner
def wish():

    hour = datetime.datetime.now().hour
    
    if hour<12:
        speak("good morning")
    elif hour<16:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("i am jarvis, your AI assistant, how may i help you?")
        
#working jarvis
def execute():

    while True:
    
        query = take_command()
        
        if "music" in query or "song" in query:
            speak("playing...")
            os.startfile("C:\\Users\\nidhi\\Music\\Brown Munde.mp3")
            
        elif "open code" in query:
            speak("opening...")
            os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")

        elif "youtube" in query:
            speak("what do you want to search sir...")
            item = take_command()
            kit.playonyt(item)
            
        elif "change voice" in query:
            speak("changing voice...")
            if engine.setProperty("voice",voice[0].id):
                engine.setProperty("voice",voice[1].id)
            elif engine.setProperty("voice",voice[1].id):
                engine.setProperty("voice",voice[0].id)
            speak("voice changed successfully...")
        
        elif "google" in query:
            speak("what do you want to search sir...")
            cm = take_command()
            webbrowser.open(f"{cm}")
        
        elif "who is" in query or "tell me about" in query:
            speak("searching sir, please wait.....")
            result = wikipedia.summary(query, sentences=2)
            speak("according to my search")
            speak(result)
            print(result)
            
        elif "set alarm" in query:
            speak("tell me the hour")
            alarmHour = take_command()
            speak("tell me the minute")
            alarmMin = take_command()
            speak("tell me the it is am or pm")
            alarmAm = take_command()
            speak("alarm set successfully, dont exit")
            
            if alarmAm == "pm":
                alarmHour += 12 
                   
            if int(alarmHour) == datetime.datetime.now().hour and int(alarmMin) == datetime.datetime.now().minute:
                os.startfile("C:\\Users\\nidhi\\Music\\Brown Munde.mp3")
            
        elif "volume up" in query:
            pyautogui.press("volumeup")
            
        elif "mute volume" in query:
            pyautogui.press("volumemute")
            
        elif "volume down" in query:
            pyautogui.press("volumedown")
                 
        elif "news" in query:
            speak("i will update you in just a second sir")
            cm = "current news"
            webbrowser.open(f"{cm}")
                
        elif "close" in query or "band" in query:
            speak("closing")
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            # time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif "repeat" in query:
            query = query.replace("repeat","")
            speak(query)
            
        elif "command prompt" in query:
            speak("opening...")
            os.startfile("start cmd")
            
        elif "wikipedia" in query:
            speak("searching, please wait...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("according to my search")
            speak(result)
            print(result)
        
        elif "time" in query:
            time = datetime.datetime.now()
            print(time.strftime("%H:%M:%S"))
            speak(time.strftime("%H:%M:%S:%A"))
            
        elif "date" in query:
            time = datetime.datetime.now()
            speak(time.strftime("%Y-%m-%d"))
        
        elif "joke" in query:
            speak("ok, sir")
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
            
        elif "no" in query:
            speak("if so, you may give me exit command")
            print("if so, you may give me exit command")
            
        elif "who are you" in query or "tu kaun" in query :
            speak("hello sir, i am jarvis, i am a model of artificial intelligence i can do many works like opening and closing apps,playing music,etc on just your one command. i can do many more advanced things if needed.....")
            
        elif "shut up" in query or "chup" in query:

            speak("ok sir")
            break
            
        elif "turn on monkey mode" in query:
            speak("ok sir...")
            speak("monkey mode is on now...")
            while True:
                listen = take_command()
                if "turn off monkey mode" in listen:
                    speak("turning off monkey mode...")
                    speak("monkey mode turned off successfully")
                    execute()
                else:
                    speak(listen)
            
        elif "exit" in query:
            speak("thanks sir, have a good day")
            print(".....................................................................................................................")
            sys.exit()
            
        speak("any other order, sir...")
        
# jarvis not activated
def take_permission():
    while True:
        permission = take_command()
        if "activate" in permission:
            print("jarvis activated successfully...")
            speak("jarvis activated successfully...")
            execute()
        elif "exit" in permission:
            speak("thanks sir, have a good day")
            print(".....................................................................................................................")
            sys.exit()

# run jarvis            
def run():
    wish()
    take_permission()
    
run()