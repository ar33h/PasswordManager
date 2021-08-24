import mysql.connector
import tkinter as tk
from tkinter import ttk
import hashing

#To establish a connection

conn = mysql.connector.connect(user='pmanager', password='Pass123!@#', database="password_manager")

cur = conn.cursor()

#Creates Database if not created
def createDB():
    query = "create table PMANAGER (Username varchar(255) NOT NULL, Password varchar(255), NOT NULL, Account varchar(50));"
    try:
        cur.execute(query)

    except:
        pass


#SQL Query to Display Records
def display():
    # query_username = "select Username from PMANAGER;"
    # query_password = "select Password from PMANAGER;"
    # query_account = "select Account from PMANAGER;"
    query = "select * from PMANAGER;"
    try:
        cur.execute(query)
        result = cur.fetchall()
        # print(result)
        for i, (Username, Password, Account, SNo) in enumerate(result, start=1):
            listbox.insert("", "end", values=(Username, Password, Account, SNo))

    except:
        print("Error in displaying")
        

def delete():
    row = listbox.selection()[0]
    rownum = row[-1]
    # print(account)
    query = "delete from PMANAGER where SNo = '"+rownum+"';"
    try:
        cur.execute(query)
        conn.commit()
        listbox.delete(row)

    except:
        print("Error")


def insertBox():
    
    box = tk.Tk()
    box.title("Add New Password")

    box.minsize(500, 200)
    box.maxsize(500, 200)

    label1 = tk.Label(box, text='Username').grid(row=0, column=1, padx=10, pady=10)
    entry1 = tk.Entry(box, width=45)
    entry1.grid(row=0, column=2, padx=10, pady=10)
    

    label2 = tk.Label(box, text='Password').grid(row=1, column=1, padx=10, pady=10)
    entry2 = tk.Entry(box, width=45)
    entry2.grid(row=1, column=2, padx=10, pady=10)
    

    label3 = tk.Label(box, text='Account').grid(row=2, column=1, padx=10, pady=10)
    entry3 = tk.Entry(box, width=45)
    entry3.grid(row=2, column=2, padx=10, pady=10)
    
    
    #SQL Query to Insert Records
    def insert():
        uname = entry1.get()
        password = entry2.get()
        account = entry3.get()
        global sno
        sno+=1
        query = "insert into PMANAGER values ('"+uname+"', '"+password+"', '"+account+"', "+str(sno)+");"
        try:
            cur.execute(query)
            conn.commit()
            box.destroy()
            listbox.insert("", "end", values=(uname, password, account, sno))
            
        except:
            conn.rollback()
            print("Error")

    
    addbttn = tk.Button(box, text="Add", width=6, command=insert)
    
    addbttn.grid(row=3, column=2, padx=10, pady=10)

    box.mainloop()
    

main = tk.Tk()
main.title('Password Records')
main.minsize(800, 300)
main.maxsize(800, 300)

cols = ('Username', 'Password', 'Account', 'S.No.')
listbox = ttk.Treeview(main, columns=cols, show='headings')

sno = 0

for col in cols:
    listbox.heading(col, text=col)
    listbox.grid(row=1, column=0, columnspan=3)

logout = tk.Button(main, text="Logout", width=10, command=exit)
logout.grid(row=2, column=2, pady=10)

add = tk.Button(main, text="Add Password", width=18, command=insertBox)
add.grid(row=2,column=0, pady=10)

rem = tk.Button(main, text="Delete Password", width=20, command=delete)
rem.grid(row=2,column=1, pady=10)

createDB()
display()
main.mainloop()

conn.close()
