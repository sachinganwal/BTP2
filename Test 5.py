import random
import sys
import os
import matplotlib
import numpy as np
import pylab as pl
from tkinter import*

def plot():


    datax=[1,2,3,4,5]
    datay=[1,4,9,16,25]

    pl.title('Plot-Amplitude vs Time')
    pl.xlabel('Time')
    pl.ylabel('Amplitude')
    pl.plot(datax,datay)
    pl.show()

def slide():
    slidex=[0]
    slidey=[0]

root=Tk()
#theLabel = Label(root, text="BTP")
#theLabel.pack()

topframe= Frame(root)
topframe.pack()
bottomframe= Frame(root, width= 250, height= 300)
bottomframe.pack(side=BOTTOM)
button1= Button(topframe,text="Plot", fg= "red", command=plot)
button2= Button(bottomframe,text="Exit", fg= "blue", command=topframe.quit)
button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop()

