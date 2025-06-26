from tkinter import *

def button_press(value):
    cal_display.configure(state="normal")
    cal_display.insert(END,value)
    cal_display.configure(state="readonly")

def clear_display():
    cal_display.configure(state="normal")
    cal_display.delete(0,END)
    cal_display.configure(state="readonly")

def evaluate():
    cal_display.configure(state="normal")
    try:
        result = eval(cal_display.get())
        cal_display.delete(0,END)
        cal_display.insert(0,str(result))
    except:
        cal_display.delete(0,END)
        cal_display.insert(0,"Error")
        cal_display.configure(state="readonly")

screen =Tk() # Created a window
screen.title("Calculator") # Set window title as calculator
screen.configure(bg="gray")
screen.geometry("250x290")
# Calculator screen
cal_display = Entry(screen,justify="center",width=30,state="readonly") # Calculator screen align center and give a width and set in as readomly
cal_display.pack(pady=15,ipady=10) # Give it a padding

# Buttons layout
buttons = [
    ('C',40,70),
    ('1',40,110),('2',85,110),('3',130,110),('+',175,110),
    ('4',40,150),('5',85,150),('6',130,150),('-',175,150),
    ('7',40,190),('8',85,190),('9',130,190),('*',175,190),
    ('.',40,230),('0',85,230),('=',130,230),('/',175,230)
        ]

for (text, x, y) in buttons:
    if text == '=':
        Button( screen,text=text,
width=3,height=1, command=evaluate).place(x=x ,y=y)
    elif text == 'C' :
        Button(screen, text=text,
width=3,height=1, command=clear_display).place(x=x, y=y)
    else:
        Button(screen, text=text, width=3, height=1, command=lambda
val=text: button_press(val)).place(x=x ,y=y)

screen.mainloop()
