import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
## print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis sir Please tell me how may i help you")

def takeCommands():

     #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("say that again please..")
        query=None
    return query


if __name__ == "__main__":
  wishMe()
  while True:

      query = takeCommands()
      # logic for executing tasks based on query
      if 'wikipedia' in None:
    
        speak("Searching wikipedia..")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=1)
        speak("According to wikipedia")
        print(result)
        speak(result)

      elif"open youtube" in query:
          webbrowser.open("youtube.com")

      elif "open google" in query:
          webbrowser.open("google.com")


      elif "play music" in query:
          music_dir = 'C:\\music'
          song = os.listdir(music_dir)
          print(song)
          os.startfile(os.path.join(music_dir, song[1]))

      elif "the time" in query:
          strTime = datetime.datetime.now().strftime("%H,%M,%S")
          speak(F'Sir the time is {strTime}')
