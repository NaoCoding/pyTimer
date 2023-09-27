import tkinter as tk
import plyer.platforms.win.notification
from plyer import notification
from functools import partial
import threading
import time

gui = tk.Tk()
gui.geometry("700x450")
gui.title("PlyerTimer")
gui.resizable(0,0)
title_frame = tk.Frame(gui)
title_frame.pack()
time_ = "00:00:00"
time_int = [0,0,0]
set_time = tk.StringVar()
set_time.set(time_)
start_stop = tk.StringVar()
start_stop.set(" Start ")
status = 0
sec = 0
cont = 0

def time_counter():
    global time_, set_time, time_int,sec,status,start_stop,cont
    sec = time_int[0] * 3600 + time_int[1] * 60 + time_int[2]
    while(sec>0):
        time.sleep(1)
        sec = sec - 1
        time_int[2] -= 1
        while(time_int[2]<=0):
            time_int[1] -= 1
            time_int[2] += 60
            while(time_int[1] <= 0):
                time_int[0] -= 1
                time_int[1] += 60
        time_ = [str(time_int[0]), ":", str(time_int[1]), ":", str(time_int[2])]
        time_ = "".join(time_)
        set_time.set(time_)
    reset_cmd()
    start_stop.set(" Start ")
    if(cont == 0):
        for i in range(3):
            print(1)
            notification.notify("Times Up !!!!!!", "Times Up !!!!!!",timeout=1)
            time.sleep(3)
    status = 0

def start_counter():
    global time_, set_time, time_int,start_stop,status,sec,cont
    if status == 0:
        status = 1
        cont = 0
        notification.notify("Timer Has Start!", "Set Time :  " + time_, timeout=1)
        start_stop.set(" Stop ")
        added_thread = threading.Thread(target=time_counter)
        added_thread.start()
    else:
        status = 0
        sec = 0
        cont = 1
        notification.notify("Timer Has Stop!", "Timer Has Stop!",timeout=1)
        start_stop.set(" Start ")
        reset_cmd()

def reset_cmd():
    global time_, set_time, time_int
    time_int = [0, 0, 0]
    time_ = [str(time_int[0]), ":", str(time_int[1]), ":", str(time_int[2])]
    time_ = "".join(time_)
    set_time.set(time_)
def time_change(value):
    global time_ , set_time,time_int
    for i in range(3):
        time_int[i] *= 10
    time_int[2] += value
    time_int[1] += int(time_int[2] / 100)
    time_int[2] %= 100
    time_int[0] += int(time_int[1] /100)
    time_int[1] %= 100
    time_int[0] %= 100
    time_ = [str(time_int[0]),":",str(time_int[1]),":",str(time_int[2])]
    time_ = "".join(time_)



    set_time.set(time_)


title = tk.Label(title_frame,text = "PlyerTimer",font=("Times New Roman",32),fg="blue")
title.pack()

author_frame = tk.Frame(gui)
author_frame.pack()

author = tk.Label(author_frame,text = "Github : NaoCoding",font=("Times New Roman",25))
author.pack()
author_frame.place(x=20,y=385)



set_time_label = tk.Label(title_frame,textvariable = set_time,font=("Times New Roman",25))
set_time_label.pack()



button9_frame = tk.Frame()
button9_frame.pack()

button9 = tk.Button(button9_frame,text=" 9 ",font=("Times New Roman",25),command=partial(time_change,9))
button9.pack()
button9_frame.place(x=400,y=125)




button8_frame = tk.Frame()
button8_frame.pack()

button8 = tk.Button(button8_frame,text=" 8 ",font=("Times New Roman",25),command=partial(time_change,8))
button8.pack()
button8_frame.place(x=315,y=125)


button7_frame = tk.Frame()
button7_frame.pack()

button7 = tk.Button(button7_frame,text=" 7 ",font=("Times New Roman",25),command=partial(time_change,7))
button7.pack()
button7_frame.place(x=230,y=125)


button6_frame = tk.Frame()
button6_frame.pack()

button6 = tk.Button(button6_frame,text=" 6 ",font=("Times New Roman",25),command=partial(time_change,6))
button6.pack()
button6_frame.place(x=400,y=210)


button5_frame = tk.Frame()
button5_frame.pack()

button5 = tk.Button(button5_frame,text=" 5 ",font=("Times New Roman",25),command=partial(time_change,5))
button5.pack()
button5_frame.place(x=315,y=210)


button4_frame = tk.Frame()
button4_frame.pack()

button4 = tk.Button(button4_frame,text=" 4 ",font=("Times New Roman",25),command=partial(time_change,4))
button4.pack()
button4_frame.place(x=230,y=210)


button3_frame = tk.Frame()
button3_frame.pack()

button3 = tk.Button(button3_frame,text=" 3 ",font=("Times New Roman",25),command=partial(time_change,3))
button3.pack()
button3_frame.place(x=400,y=295)

button2_frame = tk.Frame()
button2_frame.pack()

button2 = tk.Button(button2_frame,text=" 2 ",font=("Times New Roman",25),command=partial(time_change,2))
button2.pack()
button2_frame.place(x=315,y=295)


button1_frame = tk.Frame()
button1_frame.pack()

button1 = tk.Button(button1_frame,text=" 1 ",font=("Times New Roman",25),command=partial(time_change,1))
button1.pack()
button1_frame.place(x=230,y=295)


button0_frame = tk.Frame()
button0_frame.pack()

button0 = tk.Button(button0_frame,text=" 0 ",font=("Times New Roman",25),command=partial(time_change,0))
button0.pack()
button0_frame.place(x=485,y=295)

reset_frame = tk.Frame()
reset_frame.pack()

reset = tk.Button(reset_frame,text=" Reset ",font=("Times New Roman",25),bg="red",command=reset_cmd)
reset.pack()
reset_frame.place(x=485,y=210)

start_frame = tk.Frame()
start_frame.pack()

start = tk.Button(start_frame,textvariable=start_stop,font=("Times New Roman",25),command=partial(start_counter))
start.pack()
start_frame.place(x=485,y=125)


gui.mainloop()