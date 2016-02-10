from tkinter import *

root = Tk()
label1=Label(root, text="First")
label1.grid(row=0, sticky=W)

label2=Label(root, text="Second")
label2.grid(row=1, sticky=W)

entry1=Entry(root)
entry1.grid(row=0, column=1)

entry2=Entry(root)
entry2.grid(row=1, column=1)

button1=Button(root)
button1.grid(row=2, column=2)

button2=Button(root)
button2.grid(row=2, column=3)

# widgets can take up more than one cell with columnspan and rowspan
#c = Checkbutton(root, text="Keep me logged in")
#c.grid(columnspan=2)

root.mainloop()