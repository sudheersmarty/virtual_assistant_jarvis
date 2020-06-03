import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import PyPDF2

MASTER = "Sudheer"
print("Initializing JARVIS")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    h = int(datetime.datetime.now().hour)

    if 0 <= h < 12:
        speak("Good Morning " + MASTER)

    elif 12 <= h < 17:
        speak("Good Afternoon " + MASTER)

    else:
        speak("Good Evening " + MASTER)

    # speak("Hello " + MASTER + " How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"User said : {query}\n")
    except Exception as e:
        speak("Sorry! come again")
        query = takeCommand()
    return query


def play_music():
    songs_dir = "C:/Users/HP/Music"
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[0]))


def main():
    speak("Initializing JARVIS...")
    wishMe()
    query = takeCommand()

    if 'songs' in query:
        play_music()

    if 'open youtube' in query:
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    if 'read me a story' in query:
        pdfFileObj = open("C:\\Users\\HP\\Desktop\\stories\\Short-stories-from-100-Selected-Stories.pdf", "rb")

        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        mytext = ""

        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)

            mytext += pageObj.extractText()
            print(mytext)
        pdfFileObj.close()
        speak(mytext)

    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)

    if 'how are you' in query:
        speak("I am fine and you")
        query = takeCommand()
        if 'not fine' in query:
            speak("sorry to hear that")

        else:
            speak("That is great")


main()
