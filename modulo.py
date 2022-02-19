#!/usr/bin/python3
import tkinter as tk
import math
import time

def close(event):
    root.withdraw()
    root.destroy()
    
root = tk.Tk()
root.bind('<Escape>', close)
root.bind('q', close)

w = 1920*1.5
h = 1080*1.5
r = h/2
step = 1.0/25.0
msec = 40
np = 256
plist=[[w/2+r,0]]

def _draw_mod(self, mult, mod, width, height, **kwargs):
    f = mult%np
    self.delete("all")
    self.create_text(300,100,fill="white",font="Times 20 italic bold",text="Multiplier "+"{:.2f}".format(mult))
    self.create_text(300,130,fill="white",font="Times 20 italic bold",text="Modulo "+"{:d}".format(mod))
    self.create_oval(width/2-r, height/2-r,width/2+r,height/2+r, fill="blue", outline="#DDD", width=4)
    for n in range(1, np-1):
        p = [r*math.cos(2*math.pi*n/np),r*math.sin(2*math.pi*n/np)]
        q = [r*math.cos(2*math.pi*n*f/np),r*math.sin(2*math.pi*n*f/np)]
        self.create_line(p[0]+width/2,p[1]+height/2,q[0]+width/2,q[1]+height/2, **kwargs)
tk.Canvas.draw_mod = _draw_mod

counter = 0
def counter_mod(canvas):
  counter = 0
  def count():
    global counter
    counter += step
    canvas.draw_mod(counter, np,w,h,fill="yellow")    
    canvas.after(msec, count)
  count()

def counter_reset():
    global counter
    counter = 0
  
canvas = tk.Canvas(root, width=w, height=h, borderwidth=0, highlightthickness=0, bg="black")

canvas.grid()

counter_mod(canvas)

button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.grid()
button = tk.Button(root, text='Restart', width=25, command=counter_reset)
button.grid()

root.wm_title("mod")
root.mainloop()
