import pyttsx3  #Text to speech module
import speech_recognition as sr  # Speech to text module
import datetime
import time
import wikipedia
import webbrowser
import random
import threading
from googlesearch import search
import os
import fnmatch
import re 
import nltk
#nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import json
import winsound
import urllib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

times = ['what is the time','tell me the time','what time is it',"what's the time"]
date = ["what is today's date",'what is the date today',"what's today's date"]
goodbye = ['bye','goodbye','good night','farewell']
default = ["Sorry i don't know that","Sorry i don't understand"]
greetings = ["hey",'hi','hello','hey jarvis','hello jarvis','hi jarvis']
jokes_q = ['tell me a joke','do you know any jokes','say a joke']
jokes_a = ["I don't like computer science jokes...Not one bit.",'Two antennas got married last Saturday. The reception was fantastic.','I wanted to buy a camouflage shirt, but I didn’t see one.']

def speak(text):
    engine.say(text)
    engine.runAndWait()

#Wishes you as per current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning " + MASTER)
    elif hour>=12 and hour<17:
        speak("Good Afternoon "+MASTER)
    elif hour>=17 and hour<20:
        speak("Good Evening "+MASTER)
    speak("How may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language= 'en-in')
        print(f"{MASTER}: {query}\n")
    
    except Exception as e:
        #speak('Say that again please')
        query = ''
    
    return query

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

new_arr = []
new_arr2 = []
new_arr3 = []
new_arr4 = []   
def tell_weather(string):
    stop_words = set(stopwords.words('english')) 
    review = re.sub('[^a-zA-Z]',' ',string) 
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()

    for r in review:
        if not r in stop_words:
            new_arr.append(r)
        
        temp_words = set()  
        temp_words.add("temperature")
        temp_words.add("humidity")
        temp_words.add("pressure")
        temp_words.add("maximum")   
        temp_words.add("minimum")
    
    for m in new_arr:
        if not m in temp_words:
            new_arr2.append(m)        
        else:
            new_arr3.append(m)    

    for x in new_arr3:
        if x == "maximum":
            new_arr4.append("temp_max")
        elif x == "minimum":
            new_arr4.append("temp_min")
        elif x == "temperature":
            new_arr4.append("temp") 
        elif x == "pressure":
            new_arr4.append("pressure")
        elif x == "humidity":    
            new_arr4.append("humidity")
        else:
            new_arr4.append("temp")

def alarm_func():
    winsound.PlaySound('alarm.wav',flags=winsound.SND_FILENAME)

#Main program
print("Initializing Jarvis....")
file1 = open(r"master.txt","r+")
MASTER = file1.read()
if len(MASTER) <=0:
    MASTER = input('Enter your name:')
    file1.write(MASTER)
wishMe()
query = ''
while(query.lower() not in goodbye):
    query = takeCommand()

    if 'wikipedia' in query.lower() and 'open wikipedia' not in query.lower() :
        speak('Searching wikipedia...')
        results = wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

    elif 'open' in query.lower():
        query = query.replace('open','')
        speak('Opening '+query)
        for url in search(query, tld="com", num=1, stop=1, pause=2):
            webbrowser.open_new_tab(url)

    elif 'play music' in query.lower():
        songs_dir = r'C:\\Users\\Madhulika\\OneDrive\\Music'
        songs = find('*.mp3',songs_dir)
        os.startfile(os.path.join(songs_dir,songs[0]))
    
    elif 'search' in query.lower():
        query = query.replace('search','')
        webbrowser.open("https://google.com/search?q=%s" % query)
    
    elif 'start' in query.lower():
        exe_list=[]
        for root, dirs, files in os.walk(r"C:\Program Files"):
            for j in dirs:
                for i in files:
                    if i.endswith('.exe'):
                        p=root+'/'+j+'/'+i
                        exe_list.append(p)
        for root, dirs, files in os.walk(r"C:\Program Files (x86)"):
            for j in dirs:
                for i in files:
                    if i.endswith('.exe'):
                        p=root+'/'+j+'/'+i
                        exe_list.append(p)
        for i in range(len(exe_list)) :
            exe_list[i] = exe_list[i].split('/')[-1]
            print(i,' ',exe_list[i])
        query = query.replace('start','')
        query = query.lower().strip()
        if len(query)<=0:
            print("Application not specified")
            speak("Application not specified")
        else:
            print(query)
            if query+".exe" in exe_list:
                os.system('start '+query)
            else:
                print("Application doesn't exist.Try again!")
                speak("Application doesn't exist Try again!")
    elif 'weather' in query.lower():
        speak('What would you like to know?')
        string = takeCommand()
        tell_weather(string)
        url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.environ.get('API_KEY')}&q='+new_arr2[-1]
        response = urllib.request.urlopen(url)
        string = response.read().decode('utf-8')
        json_obj = json.loads(string)
        if json_obj['cod']==400:    #error city not specified
            print("City not specified")
            speak("City not specified")
        else:
            resu=json_obj['main'][new_arr4[-1]]-273.15
    
            p = str(int(float(str(resu))))
            q = str(new_arr2[-1])
            r = str(new_arr4[-1])

            if r == "temp_max":
                speak(q+" maximum temperature is "+ p +" degree celcius")
                print(q+" maximum temperature is "+ p +" degree celcius")
            elif r == "temp_min":
                speak(q+" minimum temperature is "+ p +" degree celcius")
                print(q+" minimum temperature is "+ p +" degree celcius")
            elif r == "humidity":
                speak(q+" humidity is "+ p)
                print(q+" humidity is "+ p)
            elif r == "temp":
                speak(q+" temperature is "+ p +" degree celcius")
                print(q+" temperature is "+ p +" degree celcius")
            elif r == "pressure":
                speak(q+" pressure is "+ p +" newton meter")
                print(q+" pressure is "+ p +" newton meter")
    elif query.lower() in times:
        e = datetime.datetime.now()
        print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
        speak("It is %s:%s" %(e.hour,e.minute))
    elif query.lower() in date:
        e = datetime.datetime.now()
        print ("Today is  %s/%s/%s" % (e.day, e.month, e.year))
        speak ("Today is  %s/%s/%s" % (e.month, e.day, e.year))
    elif query.lower() in greetings:
        greet = random.choice(greetings)+' '+MASTER
        print(greet)
        speak(greet)
    elif query.lower() in jokes_q:
        joke = random.choice(jokes_a)
        print(joke)
        speak(joke)
    elif 'set alarm' in query.lower():
        speak('what time should i set for')
        alarm_time = takeCommand()
        flag=False
        if 'p.m.' in alarm_time:
            flag = True
            alarm_time = alarm_time.replace('p.m.','')
            alarm_time = alarm_time.split(':')
            if alarm_time[0]!=12:
                alarm_time[0] = str(int(alarm_time)[0]+12)
        elif 'a.m.' in alarm_time:
            flag = True
            alarm_time = alarm_time.replace('a.m.','')
            alarm_time = alarm_time.split(':')
            if alarm_time[0]==12:
                alarm_time[0] = 0
        if(flag):
            now = datetime.datetime.now()
            alarm = datetime.datetime.combine(now.date(), datetime.time(int(alarm_time[0]), int(alarm_time[1]), 0))
            total_sec = (alarm-now).total_seconds()
            timer = threading.Timer(total_sec,alarm_func)
            timer.start()
            #time.sleep((alarm - now).total_seconds())
            #winsound.PlaySound('alarm.mp3',flags=winsound.SND_ALIAS)
        else:
            print('Something went wrong...Try again')
            speak('Somethin went wrong....Try again')
    elif len(query)>0 and query.lower() not in goodbye:
        speak(random.choice(default))
speak('goodbye')