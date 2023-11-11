import shutil
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
import os

OUTPUT_PATH = os.getcwd()
ASSETS_PATH = Path(OUTPUT_PATH+'/assets/frame2')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

fid = passw = conf_passw = name = ini = email = subcode1 = subcode2 = None


'''
    LIST OF FUNCTIONS USED FOR VARIOUS FUNCTIONS THROUGH TKinter INTERFACE
        * create_treeview()
        * update_treeview()
        * parse_data()
        * update data()
        * remove_data()
        * show_passw()
'''

# create treeview (call this function once)
def create_treeview():
    tree['columns'] = list(map(lambda x: '#' + str(x), range(1, 5)))
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("#1", width=70, stretch=tk.NO)
    tree.column("#2", width=200, stretch=tk.NO)
    tree.column("#3", width=80, stretch=tk.NO)
    tree.column("#4", width=80, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('#1', text="Fid")
    tree.heading('#2', text="Name")
    tree.heading('#3', text="Subject 1")
    tree.heading('#4', text="Subject 2")
    tree['height'] = 15


# update treeview (call this function after each update)
def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT FID, NAME, SUBCODE1, SUBCODE2 FROM FACULTY")
    record=cursor.fetchall()
    for row in record:
        tree.insert(
            "",
            0,
            values=(row[0], row[1], row[2], row[3])
        )
    tree.place(x=530, y=120)


# Parse and store data into database and treeview upon clcicking of the add button
def parse_data():
    fid = str(entry_1.get())
    passw = str(entry_2.get())
    conf_passw = str(entry_3.get())
    name = str(entry_4.get()).upper()
    ini = str(entry_5.get()).upper()
    email = str(entry_6.get())
    subcode1 = str(combo1.get())
    subcode2 = str(combo2.get())

    if fid == "" or passw == "" or \
        conf_passw == "" or name == "":
        messagebox.showwarning("Bad Input", "Some fields are empty! Please fill them out!")
        return

    if passw != conf_passw:
        messagebox.showerror("Passwords mismatch", "Password and confirm password didnt match. Try again!")
        entry_2.delete(0, tk.END)
        entry_3.delete(0, tk.END)
        return

    if subcode1 == "NULL":
        messagebox.showwarning("Bad Input", "Subject 1 cant be NULL")
        return
    
    cursor.execute(f"REPLACE INTO FACULTY (FID, PASSWORD, NAME, INITIAL, EMAIL, SUBCODE1, SUBCODE2)\
        VALUES ('{fid}','{int(passw)}','{name}', '{ini}', '{email}', '{subcode1}', '{subcode2}')")
    database.commit()
    update_treeview()
    
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)
    entry_5.delete(0, tk.END)
    entry_6.delete(0, tk.END)
    combo1.current(0)
    combo2.current(0)
    

# update a row in the database
def update_data():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)
    entry_5.delete(0, tk.END)
    entry_6.delete(0, tk.END)
    combo1.current(0)
    combo2.current(0)
    cursor=database.cursor()
    try:
        # print(tree.selection())
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one faculty at a time to update!")
            return

        q_fid = tree.item(tree.selection()[0])['values'][0]
        cursor.execute(f"SELECT * FROM FACULTY WHERE FID = '{q_fid}'")
        record=cursor.fetchone()
        print(record)
        record = list(record)
        entry_1.insert(0, record[0])
        entry_2.insert(0, record[1])
        entry_3.insert(0, record[1])
        entry_4.insert(0, record[2])
        entry_5.insert(0, record[3])
        entry_6.insert(0, record[4])
        combo1.current(subcode_li.index(record[5]))
        combo2.current(subcode_li.index(record[6]))

        cursor.execute(f"DELETE FROM FACULTY WHERE FID = '{cursor[0][0]}'")
        database.commit()
        update_treeview()

    except IndexError:
        messagebox.showerror("Bad Select", "Please select a faculty from the list first!")
        return


# remove selected data from databse and treeview
def remove_data():
    if len(tree.selection()) < 1:
        messagebox.showerror("Bad Select", "Please select a faculty from the list first!")
        return
    for i in tree.selection():
        # print(tree.item(i)['values'][0])
        cursor.execute(f"DELETE FROM FACULTY WHERE FID = '{tree.item(i)['values'][0]}'")
        database.commit()
        tree.delete(i)
        update_treeview()


def export_csv():
    f=open('faculty.csv','w',newline='')
    csvw=csv.writer(f)
    cursor.execute('SELECT FID,NAME,INITIAL,EMAIL,SUBCODE1,SUBCODE2 FROM FACULTY')
    record=cursor.fetchall()
    csvw.writerow(["FID,NAME,INITIAL,EMAIL,SUBCODE1,SUBCODE2"])
    for r in record:
        r=list(r)
        csvw.writerow(r)
    f.close()
    shutil.move("faculty.csv","Export\\faculty.csv")

def export_txt():
    f=open('faculty.txt','w',newline='')
    cursor.execute('SELECT FID,NAME,INITIAL,EMAIL,SUBCODE1,SUBCODE2 FROM FACULTY')
    record=cursor.fetchall()
    f.writelines("[FID,NAME,INITIAL,EMAIL,SUBCODE1,SUBCODE2]\n")
    for r in record:
        r=list(r)
        f.writelines(f"{r}\n")
    f.close()
    shutil.move("faculty.txt","Export\\faculty.txt")
    




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

    # creating Tabe in the database


    '''
        TKinter WINDOW SETUP WITH WIDGETS
            * Label(1-11)
            * Entry(6)
            * ComboBox(1-2)
            * Treeview(1)
            * Button(1-3)
    '''

    # TKinter Window
    window = Tk()

    window.geometry("1000x550")
    window.configure(bg = "#F4F5ED")
    window.title("Transcend")
    window.iconbitmap("assets\\titlebar\\icon.ico")


    canvas = Canvas(
        window,
        bg = "#F4F5ED",
        height = 550,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        279.0,
        103.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        755.0,
        91.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        163.0,
        295.0,
        image=image_image_3
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        345.5,
        199.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#E7E8DE",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=247.0,
        y=188.0,
        width=197.0,
        height=20.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        345.5,
        226.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#E7E8DE",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=247.0,
        y=215.0,
        width=197.0,
        height=20.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        345.5,
        256.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#E7E8DE",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=247.0,
        y=245.0,
        width=197.0,
        height=20.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        345.5,
        283.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#E7E8DE",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=247.0,
        y=272.0,
        width=197.0,
        height=20.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        345.5,
        310.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#E7E8DE",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=247.0,
        y=299.0,
        width=197.0,
        height=20.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        345.5,
        337.0,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#E7E8DE",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=247.0,
        y=326.0,
        width=197.0,
        height=20.0
    )

    # get subject code list from the database
    cursor.execute("SELECT SUBCODE FROM SUBJECT")
    record = cursor.fetchall()
    subcode_li = [row for row in record]
    subcode_li.insert(0, 'NULL')

    # ComboBox1
    combo1 = ttk.Combobox(
        window,
        values=subcode_li,
    )
    combo1.place(x=272, y=353)
    combo1.current(0)

    # ComboBox2
    combo2 = ttk.Combobox(
        window,
        values=subcode_li,
    )
    combo2.place(x=272, y=380)
    combo2.current(0)

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
        x=265.0,
        y=471.0,
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
        x=440.0,
        y=471.0,
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
        x=610.0,
        y=471.0,
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
        x=776.0,
        y=455.0,
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
        x=776.0,
        y=486.0,
        width=138.0,
        height=22.0
    )
    window.resizable(False, False)
    window.mainloop()
    database.close()