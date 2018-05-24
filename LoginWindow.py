from tkinter import *
from pymysql import *
import subprocess

root = Tk()
root.title('Login Window')
root.geometry('400x400')

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
Uname = Label(root,text='Username: ')
Pass = Label(root,text='Password: ')
SubmitL = Button(root,text='Login',command=Login)


UnameI = Entry(root)
PassI = Entry(root,show="*")

#Placing widgets in root -Window
Uname.place(x=20,y=10)
UnameI.place(x=100,y=10)

Pass.place(x=20,y=50)
PassI.place(x=100,y=50)

SubmitL.place(x=110,y=80)





root.mainloop()