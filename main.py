from tabnanny import check

import requests
from functions.Online_ops import *
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from functions.os_ops import *
from random import choice
from functions.utils import opening_text,verify_text
from pprint import pprint
import time
import socket
#import keyboard
from logging import raiseExceptions
import cv2

from functions.Offlinecmd import *
from Face_recognition import *

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from modules import *

USERNAME ="Noobtech"
BOTNAME = "zia"


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 150)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

global count
# Text to Speech Conversion
def speak(text):
    engine.say(text)
    print(f">>>>>>  {text}")
    engine.runAndWait()


# Greet the user
def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

        try:
            global query
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            if query in verify_text:
                speak(choice(opening_text))
            elif 'exit' in query or 'stop' in query:
                hour = datetime.now().hour
                if hour >= 21 and hour < 6:
                    speak("Good night sir, take care!")
                else:
                    speak('Have a good day sir!')
                os._exit(0)
        except Exception:
            speak('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
        return query
    except:
        print("Could'nt recognizing (input)")
        os._exit(0)


def exit_stop():
    hour = datetime.now().hour
    if hour >= 21 and hour < 6:
        speak("terminating, Good night buddy, take care!")
    else:
        speak('Have a good day buddy!')
    os._exit(0)

    #REACTIVATE
def reactivate():
    try:
        b = sr.Recognizer()
        with sr.Microphone() as source:
            print('waiting....')
            b.pause_threshold = 1
            b.adjust_for_ambient_noise(source, duration=0.5)
            audio = b.listen(source)        

        try:
            print('Recognizing...')
            global react
            react = b.recognize_google(audio, language='en-in')
            if 'exit' in react or 'stop' in react:
                exit_stop()

        except Exception:
            reactivate().lower()
        return react
    except:
        print("Could'nt recognizing")

def append_dataonlogfile(logfiledata):
    global logdata
    hr = datetime.now()
    logdata = open("data\logfile.txt", "a")
    logdata.write(hr.strftime("%c"))
    logdata.write(" >>>>> ")
    logdata.write(logfiledata)
    logdata.write("\n")
    logdata.close()

def append_dataonwordfile(wordfiledata):
    global worddata
    hr = datetime.now()
    worddata = open("data\wordfile.txt", "a")
    worddata.write(hr.strftime("%c"))
    worddata.write(" ########### ")
    worddata.write(wordfiledata)
    worddata.write("\n")
    worddata.close()

def wakeon():
    try:
        #print("wakeup")
        react = reactivate().lower()

        wakeme = "hello"
        wake = list(wakeme.split())
        #print(wakeme)
        r = list(react.split())
        #print(r)
        while wake[0] == r[0] :
            if len(r) > len(wake):
                query = react
                speak("working out")
                #print(query)
                append_dataonlogfile(query)
                c = list(query.split())
                c.pop(0)
                d=" "
                query=d.join(c)
                #print(query)
                listen(query)

            elif len(r) == len(wake):
                speak("yes i am here")
                query = take_user_input().lower()
                if 'none' in query:
                    pass
                else:
                    #print(query)
                    append_dataonlogfile(query)
                    listen(query)
            r =[]
        if "none" in react:
            pass        
        elif not wakeme in react:
            append_dataonwordfile(react)
    except:
        pass


def listen(query):
    try:
        print(f'{query}')
        if 'hi' in query:
            speak("Hi sir")
        elif 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
                    
        elif 'open camera' in query:
            open_camera()
            
        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}') 

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
                
        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)
            
        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")    

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")    

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)    

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)    

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')    

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')   

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        
        elif 'search' in query:
            statement = query.replace("search","")
            search(statement)

        elif 'open task manager' in query:
            open_taskmanager()
        
        elif 'open chrome' in query:
            open_chrome()
        
        elif 'open settings' in query:
            open_settings()
        
        elif 'open edge' in query:
            open_msedge()
        
        elif 'open browser' in query:
            open_browser()

        elif 'trash data' in query:
            try:
                trash_logfile()
            except:
                print("NO DATABASE FOUND")     
        elif 'detect the language' in query or 'language detection' in query:
            det()
            
        elif 'take a note' in query:
            writter()

        elif 'shut'and 'down' in query:
            speak("After how many minutes should the computer be turned off?")
            time = listen()
            if "minute" in time:
                time = time.replace("minute","")
            time = int(time)
            os.system("shutdown -s -f -%d " %time)
            speak('PC is going to shut down after %d minute '%time)

        elif "cancel"  in query:
            os.system("shutdown /a")
            speak('it is cancelled')

        else:
            speak("wrong Command, it not programmed for me")    
                
    except:
        speak("Something i couldn't fetch now, try again later")                       


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        
    def run(self):
        self.mainfunc()
    def mainfunc(self):
        try:   
            if True:
                if(check_int() == True):
                    print("-----------------Voice Assistant Initiated--------------------")#greet_user()
                    print(">>>>>>> Working in online")
                    while True:
                        wakeon()
                
                else:
                    Print("-----------------Voice Assistant Initiated--------------------")
                    print(">>>>>>> Working in offline")
                    while True:
                        wakeoff()
                                        
            else:
                speak("Access Denied")
                os._exit(0)
        except:
            os._exit(0)

startExc = MainThread()
##############################################
def check_int():
    
    try:
        request = requests.get('https://www.google.com/', timeout = 10)
        return True
    except(requests.ConnectionError, requests.Timeout) as Exception:
        return False


def quit():
    try:
        if keyboard.is_pressed('q'):
            print('You Pressed A Key!')
            sys.exit(app.exec_())

    except:
        sys.exit(app.exec_())
    
def face():
    try:
        result = look()
        if result == "unknown":
            return False

        speak("verification successfull, Welcome back " + result)

        return True
    except:
        return False
###################################################
def det():
    print("press 1 for text input\npress 2 for voice input")
    if input() == 1:
        query=input()
    elif input() == 2:
        query = take_user_input().lower()
    print("detecting")
    h=detect(query)
    if h == 'en':
        speak("It's English")
###################################################
