from speech import *
import pyttsx3 as ts
from behave import *


def main():
    engines = ts.init()
    voicess = engine.getProperty('voices')
    engines.setProperty('voice', voicess[1].id)
    main.name = input("Enter the name you would like to be called ")
    script = 'Hi ' + main.name + ', My name is Alice , How may I help you?'
    print(script)
    engines.say(script)
    engines.runAndWait()
    run_alice()


main()





