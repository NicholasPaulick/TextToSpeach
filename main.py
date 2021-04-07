#imports
from gtts import gTTS
import os
import random as rng
import tkinter as tk
from mutagen.mp3 import MP3
import time

#global lists
global lan
global acclist

#Creates the stuff used in tk
root = tk.Tk()
root.geometry("400x300")

#creates frames
frame = tk.Frame(root)
frame.pack()

midframe = tk.Frame(root)
midframe.pack()

bottomframe = tk.Frame(root)
bottomframe.pack()

#languate list
lan = ["en", "fr", "pt", "es"]

#accent list
en = ["com", "com.au", "co.uk", "ca", "co.in", "ie", "co.za"]
fr = ["fr", "ca"]
pt = ["pt", "com.bz"]
es = ["es", "com", "com.mx"]

acclist =[en, fr, pt, es]

#Def Statements
def converter(runorplay):
    if runorplay == "run":
        #Get the user input
        txt = txtx.get()
        txtx.delete(0,tk.END)
        selection = var.get()

        #selects a random accent based on length of list
        c = 0
        for e in acclist:
            if lan[selection] == "en" and c == 0:
                aclen = len(e)
                ranac = rng.randint(1, aclen)
                ranac -= 1
                break
            elif lan[selection] == "fr" and c == 1:
                aclen = len(e)
                ranac = rng.randint(1, aclen)
                ranac -= 1
                break
            elif lan[selection] == "pt" and c == 2:
                aclen = len(e)
                ranac = rng.randint(1, aclen)
                ranac -= 1
                break
            elif lan[selection] == "es" and c == 3:
                aclen = len(e)
                ranac = rng.randint(1, aclen)
                ranac -= 1
                break
            c+=1
        acchoice = acclist[c]

        #Robot Funny Stuff
        try:
            tts = gTTS(text=txt, lang=lan[selection], tld=acchoice[ranac], slow=False)
            tts.save("example.mp3")
            os.system("example.mp3")
        except:
            EOFError
    elif runorplay != "run":
        try:
            os.system("example.mp3")
        except:
            EOFError

#frame parts
#Lable asking what they want the bot to say
L1 = tk.Label(frame, text = "What would you like the bot to say?")
#Text box for the user to input text
txtx = tk.Entry(frame, width=35, bd = 5)
#Label asking what language they want it in.
L2 = tk.Label(midframe, text = "Please Select a language from the options provided:")
#Radiobuttons to have them select a language
var = tk.IntVar()
R1 = tk.Radiobutton(midframe, text="English", variable=var, value="0")
R2 = tk.Radiobutton(midframe, text="French", variable=var, value="1")
R3 = tk.Radiobutton(midframe, text="Portugeese", variable=var, value="2")
R4 = tk.Radiobutton(midframe, text="Spanish", variable=var, value="3")

#Button to tell the program to run and collect all of the data and play the audio
returntxt = tk.Button(bottomframe, text="Start", command=lambda : converter("run"))

#Plays previous input
playprev = tk.Button(bottomframe, text="Play Previous", command=lambda : converter("play"))

#packs the parts
#Label 1 pack
L1.pack()
#Text input pack
txtx.pack()
#Label 2 pack
L2.pack()
#Radio Buttons pack
R1.pack()
R2.pack()
R3.pack()
R4.pack()
#Button pack
returntxt.pack()
playprev.pack()

#Creates the Window
root.mainloop()