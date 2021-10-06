from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit(*args):
    root.destroy()
    #It will cause main loop to exit when you close the window
    #this method will trigger the application to close the session

def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime('%Y-%m-%d %H:%M:%S'))

    txt.set(time)
    #after(parent, ms, function = None, *args)
    #parent is the object or main window whichever is using this function
    #ms is time in milliseconds
    #function which shall be called
    #*args other options
    root.after(1000, clock_time)

# creates the tkinter window or root window
root = Tk()
root.attributes('-fullscreen', False)
root.configure(background = 'black')
root.bind('x', quit)
#to trigger the clock
root.after(1000,clock_time)

fnt = font.Font(family = 'Helvetica', size = 100, weight = 'bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = 'white', background = 'black')
#relx and rely are geometric positions in tkinter in relative to window
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#it keeps the tkinter event loop running meaning the application running till the window is closed
root.mainloop()