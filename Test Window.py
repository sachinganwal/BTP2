import random
import sys
import os
import matplotlib
import numpy as np
import pylab as pl
from tkinter import*
import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *

tempX = [1,2,3,4,5]
tempY = [1,4,9,16,25]


def plot():
    plt.title('Plot-Amplitude vs Time')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(tempX,tempY)

def scalex():  #Try to get the value till which x needs to be scaled

    while number!=entry_1:
      for number in tempX:
              plt.title('Plot-Amplitude vs Time')
              plt.xlabel('Time')
              plt.ylabel('Amplitude')
              plt.plot(tempX,tempY)
              plt.show()

def scaley():

    for i in tempY:
             temp=entry_2*i
             tempY[i]=temp
    plt.title('Plot-Amplitude vs Time')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(tempX,tempY)
    plt.show()

root=Tk()



label_1 = Label(root, text="Enter the x value")
entry_1 = Entry(root)
label_1.grid(row=1, sticky=E)
entry_1.grid(row=1, column=1)

print(entry_1)

label_2 = Label(root, text="Enter the y value")
entry_2 = Entry(root)
label_2.grid(row=2, sticky=E)
entry_2.grid(row=2, column=1)

print (entry_2)

button1= Button(text="Scale X", fg= "green", command=scalex)
button2= Button(text="Scale Y", fg= "green", command=scaley)
button3= Button(text="Exit", fg= "blue", command=quit)
button1.grid(row=4)
button2.grid(row=4, column=1)
button3.grid(row=3, column=2)
root.title("B.Tech_Project by Priyanshi Jain and Sachin Ganwal")
root.mainloop()
