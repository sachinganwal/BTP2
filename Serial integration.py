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

#tempX = []
#tempY = []

data=serial.Serial('com4', 115200) # 115200-baud rate, creating our serial object for the incoming data
plt.ion() # tell matplotlib that we want interactive mode to plot live data

def makeFig(): #create a function that makes the desired plot
    while True:
       while (data.inWaiting==0): #wait here untill there is data
        pass #do nothing if there's no data
    dataString = data.readline() #read the text from the Serial Port

    print (dataString)
'''
    dataArray = dataString.split(',')
    temp = int (dataArray[0]) #typecasting string of characters into a number
    temp1 = int (dataArray[1])
    tempX.append(temp)
    tempY.append(temp1)
    drawnow(plot)            #call drawnow to update our live graph
    plt.pause(.0001)

def plot():
    plt.title('Plot-Amplitude vs Time')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(tempX,tempY)

def scalex():  #Try to get the value till which x needs to be scaled
    label_1 = Label(root, text="Enter the x value")
    entry_1 = Entry(root)
    while number!=entry_1:
      for number in tempX:
              plt.title('Plot-Amplitude vs Time')
              plt.xlabel('Time')
              plt.ylabel('Amplitude')
              plt.plot(tempX,tempY)


def scaley():
    label_2 = Label(root, text="Enter the y value")
    entry_2 = Entry(root)
    for number in tempY:
              temp=entry_2*number
              plt.title('Plot-Amplitude vs Time')
              plt.xlabel('Time')
              plt.ylabel('Amplitude')
              plt.plot(tempX,temp)

'''
'''root=Tk()
theLabel = Label(root, text="B.Tech_Project by Priyanshi Jain and Sachin Ganwal")
theLabel.pack()

topframe= Frame(root)
topframe.pack()
bottomframe= Frame(root, width= 250, height= 300)
bottomframe.pack(side=BOTTOM)
button1= Button(topframe,text="Plot", fg= "red", command=makeFig)
button2= Button(topframe,text="Scale X", fg= "green", command=scalex)
button3= Button(topframe,text="Scale Y", fg= "green", command=scaley)
button4= Button(bottomframe,text="Exit", fg= "blue", command=topframe.quit)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
e1=Entry(root)
e1.pack()

root.mainloop()
'''
