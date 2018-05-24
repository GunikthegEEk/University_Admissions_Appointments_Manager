# import modules
from tkinter import *
import tkinter.messagebox
from pymysql import *

# connect to the databse.
conn = connect(host='localhost',
               user='root',
               password='',
               db='uaam_db', )
# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []


# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='lavender')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="University Admission Appointments Manager", font=('Helvetica 26 bold'),
                             fg='black',
                             bg='brown1')
        self.heading.place(x=15, y=10)

        # enter_details
        self.age = Label(self.left, text="Please Enter the following details to book an appointment:",
                         font=('Times 12'), fg='black', bg='lavender')
        self.age.place(x=0, y=70)

        # name
        self.name = Label(self.left, text="Name", font=('arial 15 bold'), fg='white', bg='black')
        self.name.place(x=0, y=100)

        # age
        self.age = Label(self.left, text="Age", font=('arial 15 bold'), fg='white', bg='black')
        self.age.place(x=0, y=140)

        # gender
        self.gender = Label(self.left, text="Gender", font=('arial 15 bold'), fg='white', bg='black')
        self.gender.place(x=0, y=180)

        # location
        self.location = Label(self.left, text="City/Location", font=('arial 15 bold'), fg='white', bg='black')
        self.location.place(x=0, y=220)

        # appointment time
        self.time = Label(self.left, text="Appointment Time", font=('arial 15 bold'), fg='white', bg='black')
        self.time.place(x=0, y=260)

        # phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 15 bold'), fg='white', bg='black')
        self.phone.place(x=0, y=300)

        # course
        self.course = Label(self.left, text="Course Interested:", font=('arial 15 bold'), fg='white', bg='black')
        self.course.place(x=0, y=340)

        # marks
        self.marks = Label(self.left, text="Marks +2:", font=('arial 15 bold'), fg='white', bg='black')
        self.marks.place(x=0, y=380)

        # Entries for all labels============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        self.course_ent = Entry(self.left, width=30)
        self.course_ent.place(x=250, y=340)

        self.marks_ent = Entry(self.left, width=30)
        self.marks_ent.place(x=250, y=380)

        # button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue',
                             command=self.add_appointment)
        self.submit.place(x=340, y=500)

        ######
        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments"
        #self.result = c.execute(sql2)
        c.execute(sql2)
        self.result = c.fetchall()
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]

        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=120, y=0)

        self.box = Text(self.right, width=40, height=30)
        self.box.place(x=40, y=50)
        self.box.insert(END, "Total Appointments till now :  " + str(self.final_id))


        ######
        # function to call when the submit button is clicked

    def add_appointment(self):
            # getting the user inputs
            self.val1 = self.name_ent.get()
            self.val2 = self.age_ent.get()
            self.val3 = self.gender_ent.get()
            self.val4 = self.location_ent.get()
            self.val5 = self.time_ent.get()
            self.val6 = self.phone_ent.get()
            self.val7 = self.course_ent.get()
            self.val8 = self.marks_ent.get()



            # checking if the user input is empty
            if self.val1 == '': #or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
                tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                # now we add to the database
                sql = "INSERT INTO appointments (name, age, gender, location, scheduled_time, phone, course, marks)" \
                      " VALUES('"+ self.val1 +"','"+ self.val2 +"','"+ self.val3 +"','"+ self.val4 +"','"+ self.val5 +"','"+ self.val6 +"','"+ self.val7 +"','"+ self.val8 +"')"

                c.execute(sql)
                conn.commit()
                tkinter.messagebox.showinfo("Success", "Appointment for " + str(self.val1) + " has been created")

                self.box.insert(END, ' \n Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))





'''creating the object'''
root = Tk()
x = Application(root)
root.title("University Admission Appointments Manager")
# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
