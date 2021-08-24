import tkinter as tk
import mysql.connector
import webbrowser
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
main.minsize(570, 330)
main.maxsize(570, 330)

def callback(url):
   webbrowser.open_new_tab(url)

heading = tk.Label(main, text="github.com/ar33h/PasswordManager")
heading.config(font=("Montserrat", 14, 'bold'), cursor="hand2")
heading.bind("<Button-1>", lambda e: callback("github.com/ar33h/PasswordManager"))

mkey = tk.Label(main, text='Enter your Master Key')
mkey.config(font=(20))

value = tk.Entry(main, width=45, show='*')

def validate():

    query = "select * from master_key;"
    cur.execute(query)
    result = cur.fetchone()
    
    if hashing.hashFunc(value.get())==result[0]:
        main.destroy()
        import data
    
    else:
        messagebox.showerror('Invalid', 'Password Incorrect. Try Again')
# ----------------------------------------------

def create_pass():
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

# ----------------------------------------------------

create = tk.Label(main, text="Don't have a Master Key? Create Now!")
create.bind("<Button-1>", lambda e: create_pass())
create.config(fg='blue')

def authenticate():
    if value.get()=='':
        messagebox.showerror('Password Manager', 'Key cannot be empty!')
    else:
        validate()
        main.destroy()
        


button = tk.Button(main, text='Authenticate', width=15, command=authenticate)

heading.pack(pady=40)
mkey.pack(pady=10)
value.pack(pady=10)
create.pack(pady=12)
button.pack(pady=10)

#Executes tkinter
main.mainloop()