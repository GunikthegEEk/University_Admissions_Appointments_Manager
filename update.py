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

class Application:

    def __init__(self, master):
        self.master = master
        #frame_full
        self.left = Frame(master, width=1200, height=720)
        self.left.pack(side=LEFT)
        # heading label
        self.heading = Label(master, text="Update Your Appointment", bg='brown1',  fg='black', font=('Helvetica 30 bold'))
        self.heading.place(x=350, y=10)

        # search criteria -->name
        self.name = Label(master, text="Enter Your Name:", font=('arial 18 bold'))
        self.name.place(x=380, y=90)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=610, y=98)

        # search button
        self.search = Button(master, text="Search", font='Helvetica 10 bold', width=12, height=1, bd="2", bg='#00B2EE',command=self.search_db )
        self.search.place(x=550, y=140)

        # back button
        self.back = Button(master, text="Back to Main Menu", font="Helvetica 10 bold", width=20, height=2, bd="4", bg='#32cd32', command= self.btmm)
        self.back.place(x=1100, y=650)

    # back to main menu
    def btmm(self):
        root.destroy()
    # function to search
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql

        sql = "SELECT * FROM appointments WHERE name LIKE  '"+ self.input +"'    "
        c.execute(sql)
        self.res = c.fetchall()

        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.phone = self.row[5]
            self.time = self.row[6]
            self.course = self.row[7]
            self.marks = self.row[8]

        ####
            # creating the update form
            self.uname = Label(self.master, text="Student's Name", font=('arial 18 bold'))
            self.uname.place(x=340, y=240)

            self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
            self.uage.place(x=340, y=280)

            self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
            self.ugender.place(x=340, y=320)

            self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
            self.ulocation.place(x=340, y=360)

            self.utime = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
            self.utime.place(x=340, y=400)

            self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
            self.uphone.place(x=340, y=440)

            self.ucourse = Label(self.master, text="Course Interested", font=('arial 18 bold'))
            self.ucourse.place(x=340, y=480)

            self.umarks = Label(self.master, text="Marks +2", font=('arial 18 bold'))
            self.umarks.place(x=340, y=520)


            # entries for each labels==========================================================
            # ===================filling the search result in the entry box to update
            self.ent1 = Entry(self.master, width=30)
            self.ent1.place(x=650, y=248)
            self.ent1.insert(END, str(self.name1))

            self.ent2 = Entry(self.master, width=30)
            self.ent2.place(x=650, y=288)
            self.ent2.insert(END, str(self.age))

            self.ent3 = Entry(self.master, width=30)
            self.ent3.place(x=650, y=328)
            self.ent3.insert(END, str(self.gender))

            self.ent4 = Entry(self.master, width=30)
            self.ent4.place(x=650, y=368)
            self.ent4.insert(END, str(self.location))

            self.ent5 = Entry(self.master, width=30)
            self.ent5.place(x=650, y=408)
            self.ent5.insert(END, str(self.time))

            self.ent6 = Entry(self.master, width=30)
            self.ent6.place(x=650, y=448)
            self.ent6.insert(END, str(self.phone))

            self.ent7 = Entry(self.master, width=30)
            self.ent7.place(x=650, y=488)
            self.ent7.insert(END, str(self.course))

            self.ent8 = Entry(self.master, width=30)
            self.ent8.place(x=650, y=528)
            self.ent8.insert(END, str(self.marks))


        ###

            # button to execute update
            self.update = Button(self.master, text="Update", font="Helvetica 10 bold", width=20, height=2, bd="4", bg='#00B2EE',command=self.update_db)
            self.update.place(x=620, y=599)

            # button to delete
            self.delete = Button(self.master, text="Delete", font="Helvetica 10 bold", width=20, height=2, bd='4', bg='red', command=self.delete_db)
            self.delete.place(x=380, y=600)



    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get()  # updated name
        self.var2 = self.ent2.get()  # updated age
        self.var3 = self.ent3.get()  # updated gender
        self.var4 = self.ent4.get()  # updated location
        self.var5 = self.ent5.get()  # updated phone
        self.var6 = self.ent6.get()  # updated time
        self.var7 = self.ent7.get()  # updated course
        self.var8 = self.ent8.get()  # updated marks

        query = "UPDATE appointments SET name= '"+self.var1+"'  , age='"+self.var2+"', " \
                    "gender='"+self.var3+"', location='"+self.var4+"', phone='"+self.var5+"'," \
                    " scheduled_time='"+self.var6+"',course='"+self.var7+"',marks='"+self.var8+"' WHERE name LIKE '"+self.namenet.get()+"' "
        c.execute(query)
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")

    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE '"+self.namenet.get()+"'"
        c.execute(sql2)
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
        self.ent7.destroy()
        self.ent8.destroy()




# creating the object
root = Tk()
root.title("Update Appointments - UAAM")
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()