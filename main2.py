import sys
import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
newsapi = "9487c96f727645f0a77d64ab5f343575"
client = OpenAI(api_key="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")

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text) 
    engine.runAndWait()
    engine.stop()

def ask_openai(command):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # use this model
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": command}
            ]
        )

        answer = response.choices[0].message.content
        speak(answer)
        print("Jarvis:", answer)
        return answer

    except Exception as e:
        speak("There was an issue sending your request. Please check your API key or internet.")
        print("OpenAI Error:", e)
        return None


def processCommand(c):
    c = c.lower()
    print(f"Processing command: {c}")

    # --- Browser Section ---
    if "open google" in c:
        return webbrowser.open("https://google.com")
    elif "open facebook" in c:
        return webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        return webbrowser.open("https://in.linkedin.com")
    elif "open youtube" in c:
        return webbrowser.open("https://youtube.com")

    # --- Music Section ---
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLibrary.music.get(song, None)
        if link:
            return webbrowser.open(link)
        else:
            speak("Song not found in library")
            return

    # --- News Section (only if word 'news' is said) ---
    elif "news" in c:
 
        if "sports" in c:
            category = "sports"
        elif "tech" in c or "technology" in c:
            category = "technology"
        elif "hollywood" in c or "entertainment" in c:
            category = "entertainment"
        elif "business" in c:
            category = "business"
        elif "health" in c:
            category = "health"
        elif "science" in c:
            category = "science"
        else:
            category = "general"

        speak(f"Fetching {category} news headlines...")
        url = f"https://newsapi.org/v2/top-headlines?language=en&category={category}&apiKey={newsapi}"
        r = requests.get(url)

        if r.status_code == 200:
            articles = r.json().get("articles", [])
            if articles:
                for article in articles[:5]:
                    speak(article.get("title", "No headline available"))
            else:
                speak("No news in this category at the moment.")
        return

    # --- If not news, not open, not play = Ask OpenAI ---
    else:
        speak("Let me check...")
        response = ask_openai(c)
        return




if __name__ == "__main__":
    speak("Intializing Jarvis.")
    
    # 2. CALIBRATE ONLY ONCE HERE (Not in the loop)
    with sr.Microphone() as source:
        print("Calibrating background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                # 3. Reduced timeout for faster wake-word detection
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=2)
            
            word = recognizer.recognize_google(audio)
            
            if "jarvis" in word.lower():
                # Say "Ya" immediately
                speak("Ya")
                
                with sr.Microphone() as source:
                    print("Active...")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            # Ignore silence/errors to keep the loop moving fast
            pass