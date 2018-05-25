from tkinter import *
from pymysql import *
import subprocess

# Window
root = Tk()
root.title('Login Window')
root.geometry('1366x768')

#defining Login Button

def Login():
    userdb = UnameI.get()
    passdb = PassI.get()
    con = connect(host='localhost',
                  user='root',
                  password='',
                  db='PMP_login_up', )
    cursor = con.cursor()

    sql_uname = "SELECT uname from userpass WHERE uname='" + userdb + "' "
    cursor.execute(sql_uname)
    result_uname = cursor.fetchone()

    sql_pass = "SELECT pass from userpass WHERE pass = '"+ passdb +"' "
    cursor.execute(sql_pass)
    result_pass = cursor.fetchone()

    # Checking the obtained credentials as result
    # print(result_uname)
    # print(result_pass)

    if result_uname.__contains__(userdb) and result_pass.__contains__ (passdb):
        root.destroy()
        subprocess.call("Main.py", shell=True)


    con.close()

#Creating Widgets for Use
Uname = Label(root,text='Enter your Username: ', font="Helvetica 16 bold")
Pass = Label(root,text='Enter your Password: ', font="Helvetica 16 bold")
SubmitL = Button(root,text='Login', height="2",width="10", bd="4", highlightcolor="blue", command=Login)
Head= Label(root, text="UNIVERSITY ADMISSION APPOINTMENT MANAGER", font="Helvetica 40 bold",  fg='black', bg='brown1')
star= Label(root, text="*********************", font="Helvetica 26 bold",  fg='black')
login= Label(root, text="LOGIN", font="Helvetica 25 bold",  fg='#ff9933', bg='black')
UnameI = Entry(root, width="30")
PassI = Entry(root, width="30", show="*")

#Placing widgets in root -Window
Uname.place(x=450,y=200)
UnameI.place(x=700,y=206)
Pass.place(x=450,y=245)
PassI.place(x=700,y=251)
SubmitL.place(x=630,y=300)
Head.place(x=23, y=10)
star.place(x=520, y=135)
login.place(x=620, y=90)

root.mainloop()