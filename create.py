import mysql.connector
import tkinter as tk
from tkinter import messagebox
import hashing

conn = mysql.connector.connect(user='pmanager', password='Pass123!@#', database="password_manager")
cur = conn.cursor()

def createDB():
    query = "create table master_key( MasterKey varchar(50) PRIMARY KEY );"
    try:
        cur.execute(query)
    except:
        pass


main = tk.Tk()
main.title('Password Manager')
main.minsize(550, 300)
main.maxsize(550, 300)

heading = tk.Label(main, text="github.com/ar33h/PasswordManager")
heading.config(font=("Montserrat", 14, 'bold'))

mkey = tk.Label(main, text='Create a Master Key')
mkey.config(font=(20))

value = tk.Entry(main, width=45, show='*')

def submit():
    if value.get()=='':
        messagebox.showerror('Password Manager', 'Key cannot be empty!')
    else:
        mbox = messagebox.askquestion('Password Manager', 'Press Yes to confirm')
        if mbox=='yes':
            createDB()
            master_key = hashing.hashFunc(value.get())
            query = "insert into master_key values ('"+master_key+"');"
            try:
                cur.execute(query)
                conn.commit()
                messagebox.showinfo('Success', 'Password successfully created. You can Login now!')
            except:
                messagebox.showwarning('Error', 'Please try again!')
            
            


button = tk.Button(main, text='Submit', width=15, command=submit)

heading.pack(pady=40)
mkey.pack(pady=10)
value.pack(pady=10)
button.pack(pady=10)

#Executes tkinter
main.mainloop()