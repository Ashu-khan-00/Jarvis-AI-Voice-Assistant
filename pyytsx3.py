import pyttsx3



engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)  # Change index number to switch voice
engine.say("Hello, I am now speaking in a new voice!")
engine.runAndWait()