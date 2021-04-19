import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Time Counter")
root.configure(background='#005780')

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root, width=3, font=("Arial", 18, ""),
                  textvariable=hour, bg='#ccefff')
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=minute, bg='#ccefff')
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=second, bg='#ccefff')
secondEntry.place(x=180, y=20)


def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time has Ended!")
        temp -= 1

btn = Button(root, text='Set Time Countdown', bd='5',
             command=submit, bg='#4dc6ff')
btn.place(x=83, y=90)

root.mainloop()