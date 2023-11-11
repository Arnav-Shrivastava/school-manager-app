import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import mysql.connector

days = 5
periods = 6
recess_break_aft = 3 # recess after 3rd Period
section = None
butt_grid = []


period_names = list(map(lambda x: 'Period ' + str(x), range(1, 6+1)))
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# connecting database


def select_sec():
    global section
    section = str(combo1.get())
    print(section)
    update_table(section)



def update_table(sec):
    cursor=database.cursor()
    for i in range(days):
        for j in range(periods):
            cursor.execute(f"SELECT SUBCODE, INITIAL FROM SCHEDULE\
                WHERE DAYID={i} AND PERIODID={j} AND SECTION='{sec}'")
            record=cursor.fetchall()
            print(record)
            record = list(record)
            print(record)
            
            butt_grid[i][j]['bg'] = 'white'
            if len(record) != 0:
                subcode = record[0][0]
                print(subcode)
                cursor.execute(f"SELECT SUBTYPE FROM SUBJECT WHERE SUBCODE={subcode}")
                cur1=cursor.fetchall()
                print(cur1,"yeet")
                cur1 = list(cur1)
                subtype = cur1[0][0]
                butt_grid[i][j]['fg'] = 'white'
                if subtype == 'T':
                    butt_grid[i][j]['bg'] = '#008B45'
                elif subtype == 'P':
                    butt_grid[i][j]['bg'] = '#36648B'

                butt_grid[i][j]['text'] = str(record[0][0]) + '\n' + str(record[0][1])
                butt_grid[i][j].update()
                print(i, j, record[0][0])
            else:
                butt_grid[i][j]['fg'] = 'black'
                butt_grid[i][j]['text'] = "No Class"
                butt_grid[i][j].update()



def process_button(d, p, sec):
    details = tk.Tk()
    cursor.execute(f"SELECT SUBCODE, INITIAL FROM SCHEDULE\
                WHERE ID='{section+str((d*periods)+p)}'")
    record=cursor.fetchall()
    record = list(record)
    if len(record) != 0:
        subcode = str(record[0][0]) 
        fini =  str(record[0][1])

        cursor.execute(f"SELECT SUBNAME, SUBTYPE FROM SUBJECT\
            WHERE SUBCODE={subcode}")
        cur1=cursor.fetchall()
        cur1 = list(cur1)
        subname = str(cur1[0][0])
        subtype = str(cur1[0][1])

        cursor.execute(f"SELECT NAME, EMAIL FROM FACULTY\
            WHERE INITIAL='{fini}'")
        cur2=cursor.fetchall()
        cur2 = list(cur2)
        fname = str(cur2[0][0])
        femail = str(cur2[0][1]) 

        if subtype == 'T':
            subtype = 'Theory'
        elif subtype == 'P':
            subtype = 'Practical'

    else:
        subcode = fini = subname = subtype = fname = femail = 'None'

    print(subcode, fini, subname, subtype, fname, femail)
    tk.Label(details, text='Class Details', font=('Inter', 15, 'bold')).pack(pady=15)
    tk.Label(details, text='Day: '+day_names[d], font=('Inter'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Period: '+str(p+1), font=('Inter'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subject Code: '+subcode, font=('Inter'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subect Name: '+subname, font=('Inter'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subject Type: '+subtype, font=('Inter'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Initials: '+fini, font=('Inter'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Name: '+fname, font=('Inter'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Email: '+femail, font=('Inter'), anchor="w").pack(expand=1, fill=tk.X, padx=20)

    tk.Button(
        details,
        text="OK",
        font=("Inter"),
        width=10,
        command=details.destroy
    ).pack(pady=10)

    details.mainloop()



def student_tt_frame(tt, sec):
    title_lab = tk.Label(
        tt,
        text='T  I  M  E  T  A  B  L  E',
        font=('Inter', 20, 'bold'),
        pady=5
    )
    title_lab.pack()

    legend_f = tk.Frame(tt)
    legend_f.pack(pady=15)
    tk.Label(
        legend_f,
        text='Legend: ',
        font=('Inter', 10, )
    ).pack(side=tk.LEFT)

    tk.Label(
        legend_f,
        text='Theory Classes',
        bg='#008B45',
        fg='white',
        relief='flat',
        font=('Inter', 10,),
        height=2
    ).pack(side=tk.LEFT, padx=10)

    tk.Label(
        legend_f,
        text='Practical Classes',
        bg='#36648B',
        fg='white',
        relief='flat',
        font=('Inter', 10,),
        height=2
    ).pack(side=tk.LEFT, padx=10)
    
    global butt_grid
    global section
    section = sec

    table = tk.Frame(tt)
    table.pack()

    first_half = tk.Frame(table)
    first_half.pack(side='left')

    recess_frame = tk.Frame(table)
    recess_frame.pack(side='left')

    second_half = tk.Frame(table)
    second_half.pack(side='left')

    recess = tk.Label(
        recess_frame,
        text='\nB\n\nR\n\nE\n\nA\n\nK',
        font=('Inter', 18, 'italic'),
        width=3,
        relief='flat'
    )
    recess.pack()

    for i in range(days):
        b = tk.Label(
            first_half,
            text=day_names[i],
            font=('Inter', 12, 'bold'),
            width=9,
            height=2,
            bd=5,
            relief='flat'
        )
        b.grid(row=i+1, column=0)

    for i in range(periods):
        if i < recess_break_aft:
            b = tk.Label(first_half)
            b.grid(row=0, column=i+1)
        else:
            b = tk.Label(second_half)
            b.grid(row=0, column=i)

        b.config(
            text=period_names[i],
            font=('Inter', 12, 'bold'),
            width=9,
            height=1,
            bd=5,
            relief='flat'
        )

    for i in range(days):
        b = []
        for j in range(periods):
            if j < recess_break_aft:
                bb = tk.Button(first_half)
                bb.grid(row=i+1, column=j+1)
            else:
                bb = tk.Button(second_half)
                bb.grid(row=i+1, column=j)

            bb.config(
                text='Hello World!',
                font=('Inter', 10),
                width=13,
                height=3,
                bd=5,
                relief='flat',
                wraplength=80,
                justify='center',
                command=lambda x=i, y=j, z=sec: process_button(x, y, z)
            )
            b.append(bb)

        butt_grid.append(b)
        # print(b)
        b = []

    print(butt_grid[0][1], butt_grid[1][1])
    update_table(sec)



database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database = "timetable"
    )
global cursor
cursor=database.cursor()

if __name__ == "__main__":
    
    # connecting database

    tt = tk.Tk()
    tt.title('Student Timetable')
    tt.configure(bg = "#F4F5ED")
    tt.title("Transcend")
    tt.iconbitmap("assets\\titlebar\\icon.ico")


    student_tt_frame(tt, section)

    sec_select_f = tk.Frame(tt, pady=15)
    sec_select_f.pack()

    tk.Label(
        sec_select_f,
        text='Select section:  ',
        font=('Consolas', 12, 'bold')
    ).pack(side=tk.LEFT)

    cursor.execute("SELECT DISTINCT SECTION FROM STUDENT")
    record=cursor.fetchall()
    print(record)
    sec_li = [row[0] for row in record]
    # sec_li.insert(0, 'NULL')
    print(sec_li)
    combo1 = ttk.Combobox(
        sec_select_f,
        values=sec_li,
    )
    combo1.pack(side=tk.LEFT)
    combo1.current(0)

    b = tk.Button(
        sec_select_f,
        text="OK",
        font=('Inter', 12, 'bold'),
        padx=10,
        command=select_sec
    )
    b.pack(side=tk.LEFT, padx=10)
    b.invoke()


    tt.mainloop()