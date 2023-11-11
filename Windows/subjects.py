import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import shutil

OUTPUT_PATH = os.getcwd()
ASSETS_PATH = Path(OUTPUT_PATH+'/assets/frame4')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# inputs in this window
subcode = subname = subtype = None

'''
    LIST OF FUNCTIONS USED FOR VARIOUS FUNCTIONS THROUGH TKinter INTERFACE
        * create_treeview()
        * update_treeview()
        * parse_data()
        * update_data()
        * remove_data()
'''

# create treeview (call this function once)
def create_treeview():
    tree['columns'] = ('one', 'two', 'three')
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=70, stretch=tk.NO)
    tree.column("two", width=300, stretch=tk.NO)
    tree.column("three", width=60, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('one', text="Code")
    tree.heading('two', text="Name")
    tree.heading('three', text="Type")


# update treeview (call this function after each update)
def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM SUBJECT")
    record=cursor.fetchall()
    for row in record:
        # print(row[0], row[1], row[2])
        if row[2] == 'T':
            t = 'Theory'
        elif row[2] == 'P':
            t = 'Practical'
        tree.insert(
            "",
            0,
            values=(row[0],row[1],t)
        )
    tree.place(x=500, y=100)
    


# Parse and store data into database and treeview upon clcicking of the add button
def parse_data():
    subcode = str(entry_1.get())
    subname = str(entry_2.get())
    subtype = str(radio_var.get()).upper()

    if subcode=="":
        subcode = None
    if subname=="":
        subname = None

    if subcode is None or subname is None:
        messagebox.showerror("Bad Input", "Please fill up Subject Code and/or Subject Name!")
        entry_1.delete(0, tk.END)
        entry_2.delete("1.0", tk.END)
        return

    cursor.execute(f"REPLACE INTO SUBJECT (SUBCODE, SUBNAME, SUBTYPE)\
        VALUES ('{subcode}','{subname}','{subtype}')")
    database.commit()
    update_treeview()
    
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)


# update a row in the database
def update_data():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    try:
        # print(tree.selection())
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one subject at a time to update!")
            return

        row = tree.item(tree.selection()[0])['values']
        entry_1.insert(0, row[0])
        entry_2.insert(0, row[1])
        if row[2][0] == "T":
            R1.select()
        elif row[2][0] == "P":
            R2.select()

        cursor.execute(f"DELETE FROM SUBJECT WHERE SUBCODE = '{row[0]}'")
        database.commit()
        update_treeview()

    except IndexError:
        messagebox.showerror("Bad Select", "Please select a subject from the list first!")
        return

# remove selected data from databse and treeview
def remove_data():
    if len(tree.selection()) < 1:
        messagebox.showerror("Bad Select", "Please select a subject from the list first!")
        return
    for i in tree.selection():
        # print(tree.item(i)['values'][0])
        cursor.execute(f"DELETE FROM SUBJECT WHERE SUBCODE = '{tree.item(i)['values'][0]}'")
        database.commit()
        tree.delete(i)
        update_treeview()

def export_csv():
    f=open('subject.csv','w',newline='')
    csvw=csv.writer(f)
    cursor.execute('SELECT * FROM SUBJECT')
    record=cursor.fetchall()
    csvw.writerow(["subcode","subname","subtype"])
    for r in record:
        r=list(r)
        csvw.writerow(r)
    f.close()
    shutil.move("subject.csv","Export\subject.csv")

def export_txt():
    f=open('subject.txt','w',newline='')
    cursor.execute('SELECT * FROM SUBJECT')
    record=cursor.fetchall()
    f.writelines("[subcode,subname,subtype]\n")
    for r in record:
        r=list(r)
        f.writelines(f"{r}\n")
    f.close()
    shutil.move("subject.txt","Export\subject.txt")
    




# main
if __name__ == "__main__":  

    '''
        DATABASE CONNECTIONS AND SETUP
    '''

    # connecting database
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database = "timetable"
    )
    global cursor
    cursor=database.cursor()
    

    '''
        TKinter WINDOW SETUP WITH WIDGETS
            * Label(1-6)
            * Entry(1)
            * Text(1)
            * Radiobutton(1-2)
            * Treeview(1)
            * Button(1-2)
    '''

    # TKinter Window
    window = Tk()

    window.geometry("1000x450")
    window.configure(bg = "#F4F5ED")
    window.title("Transcend")
    window.iconbitmap("assets\\titlebar\\icon.ico")


    canvas = Canvas(
        window,
        bg = "#F4F5ED",
        height = 450,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        276.0,
        84.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        763.0,
        84.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        160.0,
        195.0,
        image=image_image_3
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        270.2,
        154.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#E7E8DE",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=170.0,
        y=143.0,
        width=197.0,
        height=20.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        270.2,
        190.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#E7E8DE",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=170,
        y=179.0,
        width=197.0,
        height=20.0
    )
    
    # RadioButton variable to store RadioButton Status
    radio_var = tk.StringVar()

    # RadioButton1
    R1 = tk.Radiobutton(
        window,
        variable=radio_var,
        value="T"
    )
    R1.place(x=200.0, y=205.50)
    R1.select()

    # RadioButton2
    R2 = tk.Radiobutton(
        window,
        variable=radio_var,
        value="P"
    )
    R2.place(x=200.0, y=227.90)
    R2.select()

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=parse_data,
        relief="flat"
    )
    button_1.place(
        x=258.0,
        y=371.0,
        width=109.0,
        height=22.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=update_data,
        relief="flat"
    )
    button_2.place(
        x=433.0,
        y=371.0,
        width=132.0,
        height=22.0
    )

    # Treeview1
    tree = ttk.Treeview(window)
    create_treeview()
    update_treeview()

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=remove_data,
        relief="flat"
    )
    button_3.place(
        x=603.0,
        y=371.0,
        width=138.0,
        height=22.0
    )

    button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=export_txt,
        relief="flat"
    )
    button_4.place(
        x=775.0,
        y=355.0,
        width=138.0,
        height=22.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=export_csv,
        relief="flat"
    )
    button_5.place(
        x=775.0,
        y=386.0,
        width=138.0,
        height=22.0
    )
    window.resizable(False, False)
    window.mainloop()
    database.close() # close database ad=fter all operations
    