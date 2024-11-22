import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import os
import datetime

# Initialize the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Wait for input from the user to start
input("Press Enter key to start listening...")

# Define the user's name
user_name = "Optimus Prime"

# Function to greet the user based on the time of day
def greet_user():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    speak(f"{greeting}, {user_name}! Welcome back! How can I assist you today?")

# Function to speak text without overlapping calls
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Commands and actions
commands = {
    "open google": lambda: webbrowser.open("https://www.google.com"),
    "open facebook": lambda: webbrowser.open("https://www.facebook.com"),
    "open youtube": lambda: webbrowser.open("https://www.youtube.com"),
    "open instagram": lambda: webbrowser.open("https://www.instagram.com"),
    "open linkedin": lambda: webbrowser.open("https://www.linkedin.com"),
    "play song": lambda: webbrowser.open("https://www.youtube.com/watch?v=wmUJwQNGK3k"),
    "music": lambda: webbrowser.open("https://www.youtube.com/watch?v=9UmoVnBSm5k"),
    "gana": lambda: webbrowser.open("https://www.youtube.com/watch?v=8GkPMG8IwBQ"),
    "sangeet": lambda: webbrowser.open("https://www.youtube.com/watch?v=uIMSmGZfszs"),
    "open notepad": lambda: os.startfile(r"C:\Windows\System32\notepad.exe"),
    "open calculator": lambda: os.startfile(r"C:\Windows\System32\calc.exe"),
    "open chrome": lambda: os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    "open whatsapp": lambda: os.startfile(r"C:\Users\Dhiraj Kumar\Downloads\WhatsApp Installer.exe"),
    "open twitter": lambda: webbrowser.open("https://www.twitter.com"),
    "fall": lambda: webbrowser.open("https://www.FallModz.in"),
    "open erp": lambda: webbrowser.open("https://mrei.icloudems.com/corecampus/index.php"),
    "turn off": lambda: exit(),
    "search": lambda: search_query(),
    "play": lambda: play_video(),
}

# Function to process commands
def process(command):
    if command in commands:
        commands[command]()
    else:
        speak("Sorry, I didn't understand that command.")

# Function to search on Google
def search_query():
    speak("What do you want to search for?")
    with sr.Microphone() as source:
        print("Listening for search query...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        query = recognizer.recognize_google(audio, language="en-US")
        print(f"Query: {query}")
        pywhatkit.search(query)
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        speak("There was an error with the speech recognition service.")

# Function to play video on YouTube
def play_video():
    speak("What video do you want to play?")
    with sr.Microphone() as source:
        print("Listening for video query...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        video = recognizer.recognize_google(audio, language="en-US")
        print(f"Video: {video}")
        pywhatkit.playonyt(video)
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        speak("There was an error with the speech recognition service.")

# Greet the user when the program starts
greet_user()

# Main loop to listen for commands
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, phrase_time_limit=5)
        command = recognizer.recognize_google(audio, language="en-US").lower()
        print(f"Command: {command}")
        process(command)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("There was an error with the speech recognition service.")
    except KeyboardInterrupt:
        print("Exiting...")
        break
