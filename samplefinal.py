import sys
import pyttsx3
import os
import tkinter.font as Tkfont
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
root=tk.Tk()
root.geometry('1600x900')
canvas=tk.Canvas(root,width=300,height=160)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\Hari Bharath\\Documents\\projtest\\NNE1.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
helv36 = Tkfont.Font(family='Helvetica', size=15, weight='bold')
lbl = tk.Label(canvas, text="MULTIFACETED DIGIT RECOGNITION", font=("Arial Bold", 65))
lbl['bg'] = '#C0FFFF'
lbl.grid(column=0, row=0, padx=10, pady=10)
lbl = tk.Label(canvas, text="WELCOME TO DIGIT RECOGNITION APPLICATION. PLEASE SELECT AMONG HANDWRITTEN, SPOKEN AND WEBCAM MODULES!", font=("Arial Bold", 19), fg='#C0FFFF')
lbl['bg'] = '#000000'
lbl.grid(column=0, row=20, padx=10, pady=10)

def cnncall():
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 135)
    engine.say('YOU HAVE SELECTED HANDWRITTEN DIGIT RECOGNITION MODULE, PLEASE WAIT UNTIL IT LOADS')
    engine.runAndWait()
    os.system('guifinal.py')
    
  

B= tk.Button(canvas,text="HANDWRITTEN DIGIT RECOGNITION",command= cnncall, bg='#C0FFFF', font=helv36)
B.config(height=5, width=60)
B.grid(column=0, row=1000, padx=20, pady=20)


def lstmcall():
    engine = pyttsx3.init()
    engine.setProperty('rate', 135)
    engine.say('YOU HAVE SELECTED SPOKEN DIGIT RECOGNITION MODULE, PLEASE WAIT UNTIL IT LOADS')
    engine.runAndWait()
    os.system('sound1.py')
    
B1= tk.Button(canvas,text="SPOKEN DIGIT RECOGNITION",command= lstmcall,  bg='#C0FFFF', font=helv36)
B1.config(height=5, width=60)
B1.grid(column=0, row=1500, padx=60, pady=60)

def camcall():
    engine = pyttsx3.init()
    engine.setProperty('rate', 135)
    engine.say('YOU HAVE SELECTED WEBCAM DIGIT RECOGNITION MODULE, PLEASE WAIT UNTIL IT LOADS')
    engine.runAndWait()
    os.system('cam.py')
    
B2= tk.Button(canvas,text="WEBCAM DIGIT RECOGNITION",command= camcall,  bg='#C0FFFF', font=helv36)
B2.config(height=5, width=60)
B2.grid(column=0, row=1600, padx=40, pady=40)
canvas.grid()
engine = pyttsx3.init()
engine.setProperty('rate', 135)
root.update()
engine.say('WELCOME TO MULTIFACETED DIGIT RECOGNITION APPLICATION, PLEASE SELECT AMONG HANDWRITTEN, SPOKEN AND WEBCAM MODULES')
engine.runAndWait()
root.mainloop()
