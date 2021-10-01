#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import numpy as np
import os
import random
from smtplib import SMTP
import urllib.request
import regex as re


# In[11]:


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# In[12]:


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# In[13]:


def time():
    Time  = datetime.datetime.now().strftime('%I:%M:%S')
    speak(f' {Time}')

def date():
    date = (datetime.datetime.now().day)
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    if month == 1:
        month = 'January'
    elif month == 2:
        month = 'february'
    elif month == 3:
        month = 'March'
    elif month == 4:
        month = 'April'
    elif month == 5:
        month = 'May'
    elif month == 6:
        month = 'June'
    elif month == 7:
        month = 'July'
    elif month == 8:
        month = 'Aaugust'
    elif month == 9:
        month = 'September'
    elif month == 10:
        month = 'October'
    elif month == 11:
        month = 'November'
    elif month == 12:
        month = 'December'
        
    
    speak(f'{date},{month},{year}')


# In[14]:


def wishme():
    hour = datetime.datetime.now().hour
    if hour >=6 & hour < 12:
        speak('Good Morning Mr Kumar ! I am jarvis , It''s my pleasure meeting you . How may I help you ')
    elif hour >=12 & hour < 18:
        speak('Good Afternoon Mr Kumar ! I am jarvis , It''s my pleasure meeting you . How may I help you')
    elif hour >=18 & hour <24:
        speak('Good Evening sir Mr Kumar ! I am jarvis , It''s my pleasure meeting you . How may I help you ')
    else:
        speak('According to you schedule you should sleep sir!')


    
wishme()


# In[15]:


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as microphone:
        print('Listening ..')
        r.pause_threshold = 1
        audio = r.listen(microphone)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language = 'en-in')
        print(f'User said {query}\n')
        
    except Exception as e:
        #print(e)
        print('Say that again please...')
        return 'None'
    return query


# In[16]:


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    serve.login('youremail@gmail.com','your - password - here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


# In[17]:


search_keyword = 'iron-man'
html = urllib.request.urlopen('https://www.youtube.com/results?search_query=iron+man' + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
print('https://www.youtube.com/watch?v=' + video_ids[0])


# In[18]:


if __name__=='__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2)
            speak('According to wikipedia')
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/watch?v=Yhvdvn_aWvw')
            
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Ankit Kumar\\OneDrive\\Desktop\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(1,len(songs))]))
            
        elif 'the time' in query:
            
            speak('Mr Kumar The current time is')
            time()
            
        elif 'date' in query:
            speak('Mr Kumar Today''s date is ')
            date()
            
        elif 'stop' in query:
            break
        
        elif 'quit' in query:
            break
        
        elif 'excel' in query:
            excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excelPath)
            
        elif 'email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'ankitkumar3.1428@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('I am sorry sir, I was not able to excute the email.')
                
 


# In[19]:


if __name__=='__main__':
    #wishme
    while True:
        query = takeCommand().lower()
        query_output = query.split(' ')
        if 'open' in query:
            index_open = query_output.index('open')
            #print(index_open)
            web = query_output[index_open + 1]
            speak(f'opening {web}...')
            #print(web)
            if 'open' in query:
                True
                #webbrowser.open(f'{web}.com')    
                if web =='youtube':
                    speak('Which video you want me to play for you ?')
                    query = takeCommand().lower()
                    query_output = query.split(' ')
                    if 'play' in query:
                        index_open = query_output.index('play')
                        web = query_output[index_open + 1]
                        speak(f'playing {web}...')
                        search_keyword = web
                        html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + f'{web}')
                        video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
                        video_init_link = 'https://www.youtube.com/watch?v='
                        video_last_link = video_ids[random.randint(1,8)]
                        video =  video_init_link + video_last_link
                        print(video)
                        webbrowser.open(video)
                    
        break
        


# In[70]:


if 'wikipedia' in query:
    speak('Searching wikipedia...')
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences = 2)
    speak('According to wikipedia')
    speak(results)
    
elif 'open youtube' in query:
    webbrowser.open('https://www.youtube.com/watch?v=Yhvdvn_aWvw')
    
elif 'open stack overflow' in query:
    webbrowser.open('stackoverflow.com')
    
elif 'play music' in query:
    music_dir = 'C:\\Users\\Ankit Kumar\\OneDrive\\Desktop\\Songs'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[random.randint(1,len(songs))]))
    
elif 'the time' in query:
    
    speak('Mr Kumar The current time is')
    time()
    
elif 'date' in query:
    speak('Mr Kumar Today''s date is ')
    date()
    
elif 'stop' in query:
    break

elif 'quit' in query:
    break

elif 'excel' in query:
    excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
    os.startfile(excelPath)
    
elif 'email' in query:
    try:
        speak('What should I say?')
        content = takeCommand()
        to = 'ankitkumar3.1428@gmail.com'
        sendEmail(to, content)
        speak('Email has been sent!')
    except Exception as e:
        print(e)
        speak('I am sorry sir, I was not able to excute the email.')
        
 

