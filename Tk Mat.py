import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy
import tkinter as tk
from tkinter import ttk
import pylab as pl
from tkinter import*

root = Tk()
TopFrame = Frame(root)
TopFrame.pack()
BottomFrame = Frame(root, width=250, height=300)
BottomFrame.pack(side=BOTTOM)
button1 = Button(TopFrame, text="Plot", fg="red")
button2 = Button(BottomFrame, text="Exit", fg="blue", command=TopFrame.quit)
button1.pack(side=LEFT)
button2.pack(side=LEFT)

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)
a.plot([1, 2, 3, 4, 5, 6, 7, 5], [5, 6, 7, 1, 8, 5, 3, 2])
canvas = FigureCanvasTkAgg(f)
canvas.show()
canvas.get_tk_widget().pack(side=TOP)

root.mainloop()