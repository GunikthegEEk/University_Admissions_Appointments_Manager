# import modules
from tkinter import *
import tkinter.messagebox
from pymysql import *
from pyttsx3 import *
import pyttsx3
# connect to the databse.
conn = connect(host='localhost',
               user='root',
               password='',
               db='uaam_db', )
# cursor to move around the databse
c = conn.cursor()

# empty lists to append later
number = []
name = []
course1 = []

sql = "SELECT * FROM appointments"
c.execute(sql)
res = c.fetchall()
for r in res:
    ids = r[0]
    sname = r[1]
    course = r[7]
    number.append(ids)
    name.append(sname)
    course1.append(course)


# window
class Application:
    def __init__(self, master):
        self.master = master

        self.x = 0

        # heading
        self.heading = Label(master, text="Admission Appointments", font=('Helvetica 40 bold'), bg="brown1", fg='black')
        self.heading.place(x=350, y=10)

        # button to change patients
        self.change = Button(master, text="Next Student", font="Helvetica 10 bold", width=25, height=2, bd="4", bg='#00B2EE', command=self.func)
        self.change.place(x=550, y=500)

        # button to back on main menu
        self.back = Button(master, text="Back to Main Menu", font="Helvetica 10 bold", width=20, height=2, bd="4", bg='#32cd32', command=self.btmm)
        self.back.place(x=1100, y=650)

        # empty text labels to later config
        self.n = Label(master, text="", font=('arial 80 bold'))
        self.n.place(x=30, y=100)

        self.stuname = Label(master, text="", font=('arial 80 bold'))
        self.stuname.place(x=400, y=100)

        self.co = Label(master, text="", font=('arial 40 bold'))
        self.co.place(x=480, y=300)

    # back to main menu
    def btmm(self):
       root.destroy()

    # function to speak the text and update the text
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.stuname.config(text=str(name[self.x]))
        self.co.config(text=str(course1[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)
        engine.say('Appointment Number, '+ str(number[self.x])+ str(name[self.x]+',,Course Interested is,' + str(course1[self.x])))
        engine.runAndWait()
        self.x += 1

root = Tk()
x = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()