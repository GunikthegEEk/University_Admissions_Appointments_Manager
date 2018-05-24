from tkinter import *
import os
import subprocess


class mainwindow:
    def __init__(self):
        #Window Base
        root = Tk()
        root.title("University Admissions Appointments Manager")
        root.geometry("500x500")

        #defining functions

        def f_addapp():
            subprocess.call("appointment.py", shell=True)

        def f_updateapp():
            subprocess.call("update.py", shell=True)

        def f_dispapp():
            subprocess.call("display.py", shell=True)


        #Widgets

        addapp = Button(root,text="Add Appointment",height="2", width="30",command=f_addapp)
        updateapp = Button(root,text="Update Appointment",height="2",width="30",command=f_updateapp)
        dispapp = Button(root,text="Display Appointments",height="2",width="30",command=f_dispapp)

        #Placing Widgets

        addapp.place(x=80,y=50)
        updateapp.place(x=80,y=120)
        dispapp.place(x=80,y=220)


        root.mainloop()



x = mainwindow()
