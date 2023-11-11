from pathlib import Path

import Windows.timetable_stud as timetable_stud
import Windows.timetable_fac as timetable_fac

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox
import tkinter as tk
import os
import mysql.connector

OUTPUT_PATH = os.getcwd()
ASSETS_PATH = Path(OUTPUT_PATH+'/assets/frame1')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("719x441")
window.configure(bg = "#F4F5ED")
window.title("Transcend")
window.iconbitmap("assets\\titlebar\\icon.ico")

def getdata():
    print(entry_1.get())
    print(type(entry_1.get()))
    print(entry_2.get())
    print(type(entry_2.get()))

    x=int(entry_1.get())
    print(x)
    print(type(x))

def challenge():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database = "timetable"
    )

    cursor=database.cursor()
    
    user=str(combo1.get())
    if entry_1.get()=="" or entry_2.get()=="":
         messagebox.showwarning("INVALID","ENTER USERNAME OR PASSWORD")
    if user == "Student":
        admission_id=int(entry_1.get())
        cursor.execute(f"SELECT PASSWORD, SECTION, NAME, ROLL FROM STUDENT WHERE ADMISSION_ID='{admission_id}';")
        record = cursor.fetchall()
        print(record)
        if record==[]:
                messagebox.showwarning('INVALID', 'WRONG USERNAME OR PASSWORD')
        
        for r in record:
            r=list(r)
            print(r)
            password=r[0]
            
            if entry_2.get()==password:
                nw = tk.Tk()
                tk.Label(
                    nw,
                    text=f'{r[2]}\tSection: {r[1]}\tRoll No.: {r[3]}',
                    font=('Consolas', 12, 'italic'),
                ).pack()
                window.destroy()
                print(f'{r[2]}\tSection: {r[1]}\tRoll No.: {r[3]}')
                timetable_stud.student_tt_frame(nw, r[1])
                nw.mainloop()
            else:
                messagebox.showwarning('INVALID', 'WRONG USERNAME OR PASSWORD')
    
    elif user == "Faculty":
        cursor.execute(f"SELECT PASSWORD, INITIAL, NAME, EMAIL FROM FACULTY WHERE FID='{entry_1.get()}'")
        record = cursor.fetchall()
        print(record)
        if record==[]:
                messagebox.showwarning('INVALID', 'WRONG USERNAME OR PASSWORD')
        for r in record:
            r=list(r)
            print(r)
            password=r[0]
            
            if entry_2.get()==password:
                nw = tk.Tk()
                tk.Label(
                    nw,
                    text=f'{r[2]} ({r[1]})\tEmail: {r[3]}',
                    font=('Consolas', 12, 'italic'),
                ).pack()
                window.destroy()
                timetable_fac.fac_tt_frame(nw, r[1])
                nw.mainloop()
    
    elif user == "Admin":
        if entry_1.get() == 'admin' and entry_2.get() == 'admin':
            window.destroy()
            os.system('python Windows\\adminscreen.py')
            # sys.exit()
        else:
            messagebox.showerror('INVALID', 'Incorret Username/Password!')

canvas = Canvas(
    window,
    bg = "#F4F5ED",
    height = 441,
    width = 719,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    190.0,
    291.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    360.0,
    27.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    360.0,
    72.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    321.0,
    104.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    426.0,
    104.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    425.0,
    104.0,
    image=image_image_6
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    575.0,
    221.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E6E7DE",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=463.0,
    y=202.0,
    width=224.0,
    height=36.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    575.0,
    292.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E6E7DE",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=463.0,
    y=273.0,
    width=224.0,
    height=36.0
)

canvas.create_text(
    458.0,
    178.0,
    anchor="nw",
    text="Username/ID",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    458.0,
    252.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 14 * -1)
)
combo1 = ttk.Combobox(
    window,
    values=['Student', 'Faculty', 'Admin']
)
combo1.place(x=500,y=145)
combo1.current(0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=challenge,
    relief="flat"
)

button_1.place(
    x=529.0,
    y=332.0,
    width=92.0,
    height=25.0
)


window.resizable(False, False)
window.mainloop()
