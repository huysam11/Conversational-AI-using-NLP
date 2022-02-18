import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime
import requests, json
import numpy as np

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = ""
API_KEY = ""
URL = BASE_URL + "q=" + CITY + "&units=imperial" + "&appid=" + API_KEY
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    main = data['main']
    wind = data['wind']
    temperature = main['temp']
    humidity = main['humidity']
    windspeed = wind['speed']
    report = data['weather']

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[1].id)

while True:
    with speech_recognition.Microphone() as mic:
        print("robot: I'm listening")
        audio = robot_ear.record(mic, duration =3)
    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)
    if you == "":
        robot_brain = "I can't hear you, try again"
        print("Robot:" + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "thank" in you:
        robot_brain = np.random.choice(
            ["you're welcome!", "anytime!", "no problem!", "cool!", "I'm here if you need me!", "mention not"])
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.time().strftime('%I:%M %p')
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "hello" in you:
        robot_brain = np.random.choice(
            ["How are you!", "How’s it going?", "How are you doing", "Whats up"])
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "weather" in you:
        robot_brain = (f"City : {CITY}", f"Temperature : {temperature}" + "°F", f"Humidity: {humidity}" + " %",
                       f"Wind: {windspeed}" + " miles per hour", f"Weather Report: {report[0]['description']}")
        print("Robot: " + str(robot_brain))
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "bye" in you:
        robot_brain = np.random.choice(["Tata", "Have a good day", "Bye", "Goodbye", "Hope to meet soon", "peace out!"])
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Sorry I don't have answer for that question! Please try another question"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
