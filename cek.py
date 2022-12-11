import tkinter as tk
from tkinter import *
import os

os.system("cls")

window = Tk()

window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)

# Mancari ukuran layar
lebar = 500
tinggi = 500
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

# Membuat window muncul di tengah
centerx = int((screenWidth/2)-(lebar/2))
centery = int((screenHeight/2)-(tinggi/2))

window.geometry(f"{lebar}x{tinggi}+{centerx}+{centery}")
window.configure(background="Gray")

# Variabel & Function
UTS = tk.IntVar()
UAS = tk.IntVar()
QUIZ = tk.IntVar()
FINAL = tk.IntVar()

def click(uts,uas,quiz,final):
    '''Click Button'''
    totalNilai = uts+uas+quiz+final
    rata_rata = totalNilai/4
    
    hasil = Label(window,text=f"Rata - Rata : {rata_rata}",font="Arial 13",background="Darkgray",foreground=labelForground)
    hasil.grid(ipadx=10,ipady=5,row=6,column=0,columnspan=5,sticky="we")


# Configurasi untuk rowspan and colspan
for columm in range(5):
    window.columnconfigure(columm,weight=1)

for row in range(10):
    window.rowconfigure(row,weight=1)


title = Label(window,text="MENGHITUNG RATA - RATA",background="maroon",foreground="white",font="Arial 15 bold")
title.grid(column=0,row=0,sticky="wens", columnspan=5)

# Entry Style COLOR
entryBackground = "#eaeaea"
labelBackground = "Gray"

entryForground = "Gray"
labelForground = "White"



# Input UTS
label1 = Label(window,text="UTS : ",font="Arial 13",background=labelBackground,foreground=labelForground)
label1.grid(column=0,row=1,ipadx=10,ipady=5)

entry1 = Entry(window,textvariable=UTS,background=entryBackground,foreground=entryForground,font="Arial 13")
entry1.grid(column=1,row=1,ipadx=10,ipady=5,columnspan=3,sticky="we")

# Input UAS
label2 = Label(window,text="UTS : ",font="Arial 13",background=labelBackground,foreground=labelForground)
label2.grid(column=0,row=2,ipadx=10,ipady=5)

entry2 = Entry(window,textvariable=UAS,background=entryBackground,foreground=entryForground,font="Arial 13")
entry2.grid(column=1,row=2,ipadx=10,ipady=5,columnspan=3,sticky="we")

# Input QUIZ
label3 = Label(window,text="UTS : ",font="Arial 13",background=labelBackground,foreground=labelForground)
label3.grid(column=0,row=3,ipadx=10,ipady=5)

entry3 = Entry(window,textvariable=QUIZ,background=entryBackground,foreground=entryForground,font="Arial 13")
entry3.grid(column=1,row=3,ipadx=10,ipady=5,columnspan=3,sticky="we")

# Input FINAL
label4 = Label(window,text="UTS : ",font="Arial 13",background=labelBackground,foreground=labelForground)
label4.grid(column=0,row=4,ipadx=10,ipady=5)

entry4 = Entry(window,textvariable=FINAL,background=entryBackground,foreground=entryForground,font="Arial 13")
entry4.grid(column=1,row=4,ipadx=10,ipady=5,columnspan=3,sticky="we")

# Button Submit
button = Button(window,text="SUBMIT",font="Arial 13",background="maroon",foreground="white",activebackground="salmon",activeforeground="white",command=lambda : click(UTS.get(),UAS.get(),QUIZ.get(),FINAL.get()))
button.grid(ipadx=10,ipady=3,row=5,column=1,columnspan=1,sticky="we")

window.mainloop()