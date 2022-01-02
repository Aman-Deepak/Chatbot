from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import wikipedia
import speech_recognition as sr
r=sr.Recognizer()
import pyttsx3 

def index(request):
    return render(request, "home.html")

#def talk()

basic_que={'hello':'hi ,i am here to talk to you',
           'hi':'hi ,i am here to talk to you',
           'hai':'hi ,i am here to talk to you',
           'what\'s your name':'myself garry',
           'i am bored':'same bro',
           'what should i do':'studies',
           'i like you':'always there for you',
           'love you':'garry loves you too',
           'miss you':'then talk with me whole day who cares',
           'bye':'bye see you next time'}
def says(reply):
     print(reply)
     p =pyttsx3.init()
     p.setProperty('rate', 150)
     p.say(reply)
     p.runAndWait()
     
 
def talk(request):
 count = 1
 while(True):
   try:
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source,duration=0.2)
      if count == 1:
         says('hey lets talk')
         messages.info(request,'hey lets talk')
         count +=1
      voice=r.listen(source)
      tex=r.recognize_google(voice)
      text = tex.lower()
      messages.info(request,text)
    if text in basic_que:
        reply=basic_que[text]
        messages.info(request,reply)
        says(reply)
        
    elif text =='quit':
        says('ok bye')
        return HttpResponse("OK Bye!!!")
        break
    else:
        reply = wikipedia.summary(text, sentences=1)
        messages.info(request,reply)
        says(reply)
   except:
       says('ok bye')
       return render(request, "home.html") 
       break
