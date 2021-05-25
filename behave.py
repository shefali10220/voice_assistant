import speech_recognition as sr
import pyttsx3 as ts
import pywhatkit as pk
import datetime
import pyjokes

listener = sr.Recognizer()
engine = ts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text)
    print(text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source, )
        listener.pause_threshold = 0.7
        print("detecting...")
        try:
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'alice' in cmd:
                newc = cmd.replace('alice', '')
                talk(newc)

            else:
                # s = 'Say Alice in your command'
                newc = cmd
                talk(cmd)
                # listen()
        except:
            t = "Sorry try again"
            talk(t)
            listen()
    return newc


def run_alice():
    command = listen()
    # print("hi")
    if 'play' in command:
        song = command.replace('play', ' ')
        print("playing" + song)
        pk.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk("current timw is " + time)
    elif 'you are' in command:
        talk("Aww ,You are all these things too .I love you ")
    elif 'search' in command:
        search = command.replace('search', ' ')
        pk.search(search)
    elif 'joke' in command:
        user_jo = pyjokes.get_joke(language='en', category='all')
        talk(user_jo)
    elif 'how are' in command:
        talk("very well ,thank you...How are you")
    elif 'i am fine' or 'i am good ' or 'iam great' in command:
        talk("i am glad for you")

    elif 'exit' or 'bye' in command:
        talk("I hope i could help you ,have a good day")
        exit()
    else:
        talk("sorry i did not understand. talk again")

def maintt():
    while True:
        run_alice()
