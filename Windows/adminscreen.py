import tkinter as tk
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pickle
import mysql.connector

def run_sub(): os.system('pythonw Windows\\subjects.py')
def run_fac(): os.system('pythonw Windows\\faculty.py')
def run_stud(): os.system('pythonw Windows\\student.py')
def run_sch(): os.system('pythonw Windows\\scheduler.py')
def run_tt_s(): os.system('pythonw Windows\\timetable_stud.py')
def run_tt_f(): os.system('pythonw Windows\\timetable_fac.py')

# connecting database
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "timetable"
)
global cursor
cursor=database.cursor()



OUTPUT_PATH = os.getcwd()
ASSETS_PATH = Path(OUTPUT_PATH+'/assets/frame0')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def forgotpass():
    f=open('faculty-login-details.bin',"wb")
    g=open('student-login-details.bin',"wb")
    cursor.execute('SELECT FID,PASSWORD FROM FACULTY')
    record=cursor.fetchall()
    for r in record:
        pickle.dump(r,f)
    f.close()
    cursor.execute('SELECT ADMISSION_ID,PASSWORD FROM STUDENT')
    record=cursor.fetchall()
    for r in record:
        pickle.dump(r,g)
    g.close()



window = Tk()

window.geometry("719x441")
window.configure(bg = "#F4F5ED")
window.title("Transcend")
window.iconbitmap("assets\\titlebar\\icon.ico")


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
    359.0,
    243.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_1.place(
    x=151.0,
    y=374.0,
    width=175.0,
    height=42.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=forgotpass,
    relief="flat"
)
button_2.place(
    x=151.0,
    y=325.0,
    width=175.0,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=run_sub,
    relief="flat"
)
button_3.place(
    x=47.0,
    y=120.0,
    width=127.0,
    height=31.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=run_fac,
    relief="flat"
)
button_4.place(
    x=48.0,
    y=170.0,
    width=127.0,
    height=31.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=run_stud,
    relief="flat"
)
button_5.place(
    x=47.0,
    y=220.0,
    width=127.0,
    height=31.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=run_sch,
    relief="flat"
)
button_6.place(
    x=280.0,
    y=120.0,
    width=172.0,
    height=31.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=run_tt_s,
    relief="flat"
)
button_7.place(
    x=279.0,
    y=170.0,
    width=172.0,
    height=31.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=run_tt_f,
    relief="flat"
)
button_8.place(
    x=279.0,
    y=220.0,
    width=172.0,
    height=31.0
)

canvas.create_text(
    84.0,
    98.0,
    anchor="nw",
    text="Modify",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    332.0,
    98.0,
    anchor="nw",
    text="Timetable",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    216.0,
    42.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    84.0,
    48.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    175.0,
    65.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    280.0,
    65.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    279.0,
    65.0,
    image=image_image_6
)
window.resizable(False, False)
window.mainloop()
