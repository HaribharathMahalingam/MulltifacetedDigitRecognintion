# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:54:57 2020

@author: Hari Bharath
"""

from tensorflowTesting import testing
##import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
import os
import pyttsx3
from winsound import *

from PIL import ImageTk, Image, ImageDraw
import PIL
import tkinter as tk
from tkinter import *

classes=[0,1,2,3,4,5,6,7,8,9]
width = 500
height = 500
center = height//2
white = (255, 255, 255)
green = (0,128,0)

def paint(event):
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=40)
    draw.line([x1, y1, x2, y2],fill="black",width=40)
def model():
    filename = "image.png"
    image1.save(filename)
    pred=testing()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say('THE PREDICTED DIGIT is    ' + str(np.argmax(pred[0])) + 'with an accuracy of ' + str(round(pred[0][np.argmax(pred[0])]*100,3)))
    engine.runAndWait()
    print('argmax',np.argmax(pred[0]),'\n',
          pred[0][np.argmax(pred[0])],'\n',classes[np.argmax(pred[0])])
    txt.insert(tk.INSERT,"{}\nAccuracy: {}%".format(classes[np.argmax(pred[0])],round(pred[0][np.argmax(pred[0])]*100,3)))
    
def clear():
    cv.delete('all')
    draw.rectangle((0, 0, 500, 500), fill=(255, 255, 255, 0))
    txt.delete('1.0', END)

root = Tk()
##root.geometry('1000x500') 

root.resizable(0,0)
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

txt=tk.Text(root,bd=3,exportselection=0,bg='WHITE',font='Helvetica',
            padx=10,pady=10,height=5,width=20)

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

##button=Button(text="save",command=save)
btnModel=Button(text="CLICK TO PRPEDICT THE DIGIT WRITTEN",command=model, bg='#A3A3A3')
btnModel.config(height=3, width=60)
btnClear=Button(text="CLICK TO CLEAR THE SCREEN FOR A NEW DIGIT",command=clear, bg='#A3A3A3')
btnClear.config(height=3, width=60)
##button.pack()
btnModel.pack()
btnClear.pack()
txt.pack()
root.title('HANDWRITTEN DIGIT RECOGNITION CNN')
engine = pyttsx3.init()
engine.setProperty('rate', 135)
root.update()
engine.say('WRITE ANY DIGIT FROM 0 TO 9 ON THE GIVEN BLANK SPACE')
engine.runAndWait()
root.mainloop()
