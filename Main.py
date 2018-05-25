from tkinter import *
import os
import subprocess


class mainwindow:
    def __init__(self):
        #Window Base
        root = Tk()
        root.title("University Admissions Appointments Manager")
        root.geometry("1366x768")

        #defining functions

        def f_addapp():
            subprocess.call("appointment.py", shell=True)

        def f_updateapp():
            subprocess.call("update.py", shell=True)

        def f_dispapp():
            subprocess.call("display.py", shell=True)


        #Widgets
        label= Label(root, text="WELCOME TO UNIVERSITY ADMISSION APPOINTMENT MANAGER", font="Helvetica 30 bold", bg="brown1")

        addapp = Button(root,text="Add Appointment", font="Helvetica 14 bold", height="2", width="30", bd="4", bg="#00ced1",command=f_addapp)
        updateapp = Button(root,text="Update Appointment", font="Helvetica 14 bold", height="2",width="30", bd="4", bg="#00ced1",command=f_updateapp)
        dispapp = Button(root,text="Display Appointments", font="Helvetica 14 bold",height="2",width="30", bd="4", bg="#00ced1",command=f_dispapp)

        #Placing Widgets
        label.place(x=40, y=10)
        addapp.place(x=300,y=200)
        updateapp.place(x=700,y=200)
        dispapp.place(x=490,y=285)


        root.mainloop()



x = mainwindow()
