#!/usr/bin/python3
import tkinter as tk
import math
import time

def close(event):
    root.withdraw()
    root.destroy()
    
w = 1920
h = 1080
r = h/2

root = tk.Tk()
root.config(width=w,height=h+200)
root.bind('<Escape>', close)
root.bind('q', close)
sli1 = tk.Scale(root, from_=2, to=5000, tickinterval=100,orient=tk.HORIZONTAL)
sli2 = tk.Scale(root, from_=2, to=100, tickinterval=10, orient=tk.HORIZONTAL)

step = 1.0/25.0
msec = 40
plist=[[w/2+r,0]]

def _draw_mod(self, mult, np, width, height, **kwargs):
    f = mult%np
    self.delete("all")
    self.create_text(300,100,fill="white",font="Times 20 italic bold",text="Multiplier "+"{:.2f}".format(mult))
    self.create_text(300,130,fill="white",font="Times 20 italic bold",text="Modulo "+"{:d}".format(np))
    self.create_oval(width/2-r, height/2-r,width/2+r,height/2+r, fill="blue", outline="#DDD", width=4)
    for n in range(1, np-1):
        p = [r*math.cos(2*math.pi*n/np),r*math.sin(2*math.pi*n/np)]
        q = [r*math.cos(2*math.pi*n*f/np),r*math.sin(2*math.pi*n*f/np)]
        self.create_line(p[0]+width/2,p[1]+height/2,q[0]+width/2,q[1]+height/2, **kwargs)

tk.Canvas.draw_mod = _draw_mod
cont = 0
counter = 2


def counter_mod(canvas):
    counter = 0
    def count():
        global counter
        global cont
        np = sli1.get()
        
        canvas.draw_mod(counter, np,w,h,fill="yellow")    
        if cont ==1 :
            counter += step
            sli2.set(int(counter))
        else :
            counter = sli2.get()
        canvas.after(msec, count)
    count()
    
def counter_reset():
    global counter
    global cont
    counter = 0
    cont =1

def counter_start():
    global cont
    cont = 1

def counter_stop():
    global cont
    cont = 0



canvas = tk.Canvas(root, width=w, height=h, borderwidth=0, highlightthickness=0, bg="black")

canvas.place(x=0, y=0, width=w, height=h)

button1 = tk.Button(root, text='Start', width=25, command=counter_start)
button2 = tk.Button(root, text='Stop', width=25, command=counter_stop)
button3 = tk.Button(root, text='Restart', width=25, command=counter_reset)
sli1.set(2)
sli1.place(x=0, y=h+20, width=w, height=60)
button1.place(x=0, y=h+80, width=w/3, height=60)
button2.place(x=w/3, y=h+80, width=w/3, height=60)
button3.place(x=2*w/3, y=h+80, width=w/3, height=60)
sli2.place(x=0, y=h+140, width=w, height=60)
counter_mod(canvas)

root.wm_title("mod")
root.mainloop()
