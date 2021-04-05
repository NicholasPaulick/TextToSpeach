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
def inputs():
    return input("What would you like the bot to say?  ")

#Get the user input
txt = inputs()

#Robot says thing
tts = gTTS(text=txt, lang=lan[0], tld=en[0], slow=False)

tts.save("example.mp3")

os.system("example.mp3")