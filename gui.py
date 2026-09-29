import calendars
import classes
import optimise
import scrape
import os
import json

from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

if not os.path.isdir("class_lists"):
    os.mkdir("class_lists")
if not os.path.isdir("schedules"):
    os.mkdir("schedules")
f = open("block_time.json",'a+')
f.close()
f=open("professor.json","a+")
f.close()

counter = 0
clasesss = []
semester = "202630"

def calculate(*args):
    global clasesss
    global counter
    global semester
    try:
        clas1 = class1.get()
        clas2 = class2.get()
        clas3 = class3.get()
        clas4 = class4.get()
        clas5 = class5.get()
        clas6 = class6.get()
        clas7 = class7.get()
        clas8 = class8.get()
        year = Current_Year.get()
        semester = Current_Semester.get()
        clases=list(filter(None,[clas1,clas2,clas3,clas4,clas5,clas6,clas7,clas8]))
        if len(clases)!=0:
            f=open("classes.json","w+")
            f.write(str(clases).replace("'",'"'))
            f.close()
        else:
            f=open("classes.json","r")
            clases = json.loads(f.read())
            f.close()
        test.set(str(clases))

        semester = classes.get_semester_g(year,semester) #change this later to actually use the gui

        clasesss = classes.get_all_classes_lazy(semester)
        counter = 0
        plt = optimise.show_cal(clasesss[0],semester)

        canvas = FigureCanvasTkAgg(plt, master=root)
        canvas_widget = canvas.get_tk_widget()

        canvas_widget.grid(column=0,row=8)

    except ValueError:
        pass
def prev(*args):
    global counter
    global clasesss
    global semester
    counter -=1
    if counter < 0:
        counter=0
    plt = optimise.show_cal(clasesss[counter],semester)

    canvas = FigureCanvasTkAgg(plt, master=root)
    canvas_widget = canvas.get_tk_widget()

    canvas_widget.grid(column=0,row=8)

def next(*args):
    global counter
    global clasesss
    global semester
    counter +=1
    if counter >= len(clasesss):
        counter=len(clasesss)-1
    plt = optimise.show_cal(clasesss[counter],semester)

    canvas = FigureCanvasTkAgg(plt, master=root)
    canvas_widget = canvas.get_tk_widget()

    canvas_widget.grid(column=0,row=8)

def select(*args):
    global counter
    global clasesss
    global semester
    calendars.make_calendar(clasesss[counter],semester)
    tcounter = 0
    for i in range(len(clasesss[counter])):
        ttk.Label(mainframe, text=optimise.print_class_information(clasesss[counter][i], semester)).grid(column=0+tcounter, row=10, sticky=W)
        tcounter+=1


root = Tk()
root.title("NMT-Schedule-Maker")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

class1 = StringVar()
class2 = StringVar()
class3 = StringVar()
class4 = StringVar()
class5 = StringVar()
class6 = StringVar()
class7 = StringVar()
class8 = StringVar()
Current_Year = StringVar()
Current_Semester = StringVar()
class_entry1 = ttk.Entry(mainframe, width=7, textvariable=class1)
class_entry2 = ttk.Entry(mainframe, width=7, textvariable=class2)
class_entry3 = ttk.Entry(mainframe, width=7, textvariable=class3)
class_entry4 = ttk.Entry(mainframe, width=7, textvariable=class4)
class_entry5 = ttk.Entry(mainframe, width=7, textvariable=class5)
class_entry6 = ttk.Entry(mainframe, width=7, textvariable=class6)
class_entry7 = ttk.Entry(mainframe, width=7, textvariable=class7)
class_entry8 = ttk.Entry(mainframe, width=7, textvariable=class8)
year_entry = ttk.Entry(mainframe, width = 7, textvariable=Current_Year)
semester_entry = ttk.Entry(mainframe, width = 7, textvariable=Current_Semester)

class_entry1.grid(column=2, row=1, sticky=(W, E))
class_entry2.grid(column=2, row=2, sticky=(W, E))
class_entry3.grid(column=2, row=3, sticky=(W, E))
class_entry4.grid(column=2, row=4, sticky=(W, E))
class_entry5.grid(column=2, row=5, sticky=(W, E))
class_entry6.grid(column=2, row=6, sticky=(W, E))
class_entry7.grid(column=2, row=7, sticky=(W, E))
class_entry8.grid(column=2, row=8, sticky=(W, E))
year_entry.grid(column=4, row=1, sticky=(W, E))
semester_entry.grid(column=4, row=2, sticky=(W, E))

test = StringVar()
ttk.Label(mainframe, textvariable=test).grid(column=7, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Create Schedule", command=calculate).grid(column=4, row=9, sticky=W)
ttk.Button(mainframe, text="Next Schedule", command=next).grid(column=3, row=9, sticky=W)
ttk.Button(mainframe, text="Previous Schedule", command=prev).grid(column=1, row=9, sticky=W)
ttk.Button(mainframe, text="Select Schedule", command=select).grid(column=2, row=9, sticky=W)

ttk.Label(mainframe, text="Class One (eg. 'CSE 3077')").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Class Two").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Class Three").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Class Four").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="Class Five").grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, text="Class Six").grid(column=3, row=6, sticky=W)
ttk.Label(mainframe, text="Class Seven").grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, text="Class Eight").grid(column=3, row=8, sticky=W)
ttk.Label(mainframe, text="Current Year (eg: '2026')").grid(column=5, row=1, sticky=W)
ttk.Label(mainframe, text="Semester (eg: 'fall' 'winter' 'spring')").grid(column=5, row=2, sticky=W)


ttk.Label(mainframe, text="classes").grid(column=1, row=2, sticky=E)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

class_entry1.focus()
root.bind("<Return>", calculate)

root.mainloop()
