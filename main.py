#imports
from gtts import gTTS
import tkinter as tk
import os

#global lists
global lan
global en
global fr
global pt
global es

#languate picker list
lan = ["en", "fr", "pt", "es"]

#accent picker list
en = ["com", "com.au", "co.uk", "ca", "co.in", "ie", "co.za"]
fr = ["fr", "ca"]
pt = ["pt", "com.bz"]
es = ["es", "com", "com.mx"]

#def statments
def inputxt():
    return input("What would you like the bot to say?  ")

def inputlen():
    x = "len"
    while x not in lan:
        x = input("Which language would you like? (en, fr, pt, es)")
    return x

#Get the user input
txt = inputxt()
langu = inputlen()

#Robot Funny Stuff
tts = gTTS(text=txt, lang=langu, tld=en[0], slow=False)

#Makes the file playable
tts.save("example.mp3")
os.system("example.mp3")
