import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import pywhatkit
import pyautogui
import keyboard

assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voices', voices[0].id)
newVoiceRate = 180
assistant.setProperty('rate', newVoiceRate)


def speak(audio):
    print(f": {audio}")
    assistant.say(audio)
    print("  ")
    assistant.runAndWait()


speak('Hello Sir')
print("  ")
speak("I Am Tom, Mr. Sinha's High-Tech Ai")


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        command.pause_threshold = 1
        command.energy_threshold = 350
        audio = command.listen(source)

    try:
        print("Recognizing...")
        query = command.recognize_google(audio, language='en-in')
        print(f'Sir You Said: {query}')

    except Exception as Error:
        return "none"

    return query.lower()


def TaskExe():
    def Music():
        speak("tell me name of the song")
        musicName = takecommand()

        if 'song' in musicName:
            os.startfile('F:\\beliver.mp4')
        elif 'my one' in musicName:
            os.startfile('C:\\Users\\client\\Desktop\\PARTY SONGS\\Baahubali - Kaun Hain Voh.mp3')

        else:
            pywhatkit.playonyt(musicName)
        speak('Your song has been played. Enjoy!')

    def YoutubeAuto():

            speak('whats your command ?')
            comm = takecommand()
            if 'pause' in comm:
                keyboard.press("space bar")
            if 'play' in comm:
                keyboard.press("space bar")
            if 'restart' in comm:
                keyboard.press('0')
            elif 'mute' in comm:
                keyboard.press('m')
            elif 'skip' in comm:
                keyboard.press('l')
            elif 'back' in comm:
                keyboard.press('i')
            elif 'full screen' in comm:
                keyboard.press('f')
            elif 'flim mode' in comm:
                keyboard.press('f')
            elif 'thank you' in comm:
                quit()

    # def screenshot():
    #     speak("ok sir, what will i name the screenshot?")
    #     path = takecommand()
    #     path1name = path + " .png"
    #     path1 = ("F:\\screen shot\\") + path
    #     kk = pyautogui.screenshot()
    #     kk.save(path1)
    #     os.startfile("F:\\screen shot\\") + path1name
    #     speak("here's your screen shot sir")

    while True:
        query = takecommand()

        if 'hello' in query:
            speak("Hello Sir , I Am Tom.")
            speak("Your High-Tech Personal AI Assistant!")
            speak("how May I Help You?")

        if 'learning codes' in query:
            os.startfile('C:\\Users\\client\\Desktop\\learning codes')
            speak('Ok sir wait a second')

        if 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")
            speak("ok sir")
        elif 'how are you' in query:
            speak('I Am Fine Sir!')
            speak('What About You?')

        elif 'you need a break tom' in query:
            speak('Ok Sir')
            speak('You Can Call Me Anytime')
            break

        elif 'kya hal hai' in query:
            speak("Main Badiya Apna Sunao")

        elif 'bye' in query:
            speak('Ok Sir Bye')
            break

        elif 'main achcha hun' in query:
            speak('Main Bhie')

        elif 'open youtube' in query:
            '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"'
            speak('Ok Sir , This what I found in Youtube')
            query = query.replace("tom", "")
            query = query.replace("open youtube ", "")
            web = 'https:\\www.youtube.com\\results?search_query=' + query
            webbrowser.open(web)
            speak("Done Sir")

        elif 'google search' in query:
            '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"'
            speak("This What I found in google")
            query = query.replace("Tom", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak('Done Sir')

        elif 'website' in query:
            '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"'
            speak("Ok sir. Give Some Time.....")
            query = query.replace("Tom", "")
            query = query.replace('website', "")
            web = query.replace('open', "")
            web2 = 'https:\\www.' + web + '.com'
            webbrowser.open(web2)
            speak("Opened")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("Tom", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query)
            speak(f"According to wikipedia : {wiki}")

        elif 'take a screenshot' in query:
            path = "F:\\screen shot\\"
            kk = pyautogui.screenshot()
            kk.save("F:\\screen shot\\")


        elif 'music' in query:
            Music()

        elif 'chrome' in query:
            os.startfile('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')
            speak('Chrome Will Be Launched In A While')

        elif 'instagram' in query:
            hh = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"'
            webbrowser.open('https\\www.instagram.com')
        elif 'maps' in query:
            webbrowser.open(
                'https:\\www.google.com\\maps\\place\\Jangalpur,+West+Bengal+711302\\@22.5930399,88.2175877,16z\\data=!3m1!4b1!4m5!3m4!1s0x3a027f694d97f347:0xe456f6dad31385e!8m2!3d22.5948426!4d88.2234458')
        elif 'youtube' in query:
            webbrowser.open('https:\\www.youtube.com\\results?search_query=')
        elif 'open maps' in query:
            webbrowser.open(
                'https:\\www.google.com\\maps\\place\\Jangalpur,+West+Bengal+711302\\@22.5930399,88.2175877,16z\\data=!3m1!4b1!4m5!3m4!1s0x3a027f694d97f347:0xe456f6dad31385e!8m2!3d22.5948426!4d88.2234458')
        elif 'automation' in query:
            YoutubeAuto()
TaskExe()






