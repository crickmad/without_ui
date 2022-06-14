from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import time
import os
import subprocess
import wmi
from datetime import datetime

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>vosk model<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
modelUS = Model(r"vosk-model-small-en-us-0.15")

recognizer = KaldiRecognizer(modelUS, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16 , channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>engine<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
engine = pyttsx3.init('sapi5')
# Set Rate
engine.setProperty('rate', 150)
# Set Volume
engine.setProperty('volume', 1.0)
# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#>>>>>>>>>>>>>>>>>>>>>>>>>>speech<<<<<<<<<<<<<<<<<<<<<<<<<<<
def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    print(f">> {text}")
    engine.runAndWait()
    #time.sleep(1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>bot name<<<<<<<<<<<<<<<<<<<<<<<<<<<
botname = 'hello'

#>>>>>>>>>>>>>>>>>>>>>>>>>>main function<<<<<<<<<<<<<<<<<<<<<<<<

def wakeoff():
    try:
        data = stream.read(4096, exception_on_overflow = False)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            query = text[14:-3]
            q = list(query.split(" "))
            c = list(botname.split(" "))
            if query == "":
                print("waiting..........")
            if len(query) == len(botname) and query == botname:
                speak("yes i am here")
            if len(query) >len(botname) and q[0] == c[0]:
                listen(query)
                append_dataonlogfile(query)
    except:
        print('exit')
        os._exit(0)  
    

#>>>>>>>>>>>>>>>>>>>>>>>>listen fuction<<<<<<<<<<<<<<<<<<<<<<<<<<
def listen(query):
    print("@@@@@@@@@@@@@@@")
    print(query)
    try:
        if (f'{botname} open cmd' in query or f'{botname} open c m d' in query or f'{botname} open command prompt' in query):
            print("cmd")
            speak("opening cmd")
            open_cmd_off()
        
        elif(f'{botname} close cmd' in query or f'{botname} close c m d' in query or f'{botname} close command prompt' in query):
            speak("closing cmd")
            close_cmd_off()

        elif(f'{botname} open notepad' in query or f'{botname} open not bad' in query):
            print("notepad")
            speak("opening notpad")
            open_notepad_off()

        elif(f'{botname} close notepad' in query or f'{botname} close not bad' in query):
            speak("closing notpad")
            close_notepad_off()
        
        elif(f'{botname} open camera' in query):
            print("camera")
            speak("opening camera")
            open_camera_off()
        
        elif(f'{botname} close camera' in query):
            speak('closing camera')
            close_camera_off()
        
        elif(f'{botname} open calculator' in query or f'{botname} open calculated' in query):
            print("calc")
            speak("opening calculator")
            open_calc_off()

        elif(f'{botname} close calculator' in query or f'{botname} close calculated'in query):
            speak('closing calculator')
            close_calc_off()

        elif(f'{botname} open task manager' in query):
            print("tm")
            speak("opening task manager")
            open_taskmanager_off()
        
        elif(f'{botname} close task manager' in query):
            speak('closing task manager')
            close_taskmanager_off()

        
        elif(f'{botname} exit' in query or f'{botname} quit' in query or f'{botname} stop' in query):
            speak("terminating, you're welcome.")
            exit_stop()
        else:
            speak("wrong command, try again")
    except Exception:
        speak("Something i couldn't fetch now, try again later.")
        exit_stop()

#>>>>>>>>>>>>>>>>>>>>exit function<<<<<<<<<<<<<<<<<<<
def exit_stop():
    hour = datetime.now().hour
    if hour >= 21 and hour < 6:
        speak("terminating, Good night buddy, take care!")
    else:
        speak('Have a good day buddy!')
    exit()

#>>>>>>>>>>>>>>>>>>>>data to logfile<<<<<<<<<<<<<<<<<<<
def append_dataonlogfile(logfiledata):
    global logdata
    hr = datetime.now()
    logdata = open("data\offlineSpeechLogfile.txt", "a")
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
#>>>>>>>>>>>>>>>open functions<<<<<<<<<<<<<<<<<<<<<<
paths = {
    'notepadoff' : 'C:\\Windows\\System32\\notepad.exe',
    'calcoff' : "C:\\Windows\\System32\\calc.exe",
    'taskmgroff' : 'C:\\Windows\\System32\\Taskmgr.exe',
}

def open_cmd_off():
    os.system('start cmd')
    print("cmd opened successfully")
    time.sleep(5)

def open_notepad_off():
    os.startfile(paths['notepadoff'])
    print("notepad open successfully")
    time.sleep(5)

def open_camera_off():
    subprocess.run('start microsoft.windows.camera:', shell = True)
    print("camera opened successfully")
    time.sleep(5)

def open_calc_off():
    os.startfile(paths['calcoff'])
    print("calc opened successfully")
    time.sleep(5)

def open_taskmanager_off():
    os.startfile(paths['taskmgroff'])
    print("tm opened successfully")
    time.sleep(5)

#>>>>>>>>>>>>>>>>termination function define<<<<<<<<<<<<<<<<<<<<<<<<
def terminateoff(curpro):
    try:
        f = wmi.WMI()
        flag = 0
        for p in f.Win32_Process():
            if curpro == p.Name:
                p.Terminate()
                flag = 1
        speak("process terminated.")
    except:
        speak("no process found.")

#>>>>>>>>>>>>>>>>>>>close functions<<<<<<<<<<<<<<<<<<<<<<<<<<<
def close_cmd_off():
    terminateoff('cmd.exe')

def close_notepad_off():
    terminateoff('notepad.exe')

def close_camera_off():
    terminateoff('camera.exe')

def close_calc_off():
    terminateoff('calc.exe')

def close_taskmanager_off():
    terminateoff('Taskmgr.exe')
