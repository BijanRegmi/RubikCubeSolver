from tkinter import *
from tkinter import ttk
import tkinter.font as font
import time
class Timer():
    def __init__(self,master):
        self.start = 0
        self.elapsed = 0
        self.isrunning = 0
        self.label = Label(master,text=self.set_time(), height = 2, font = font.Font(size = 20, weight = "bold"), fg = "red")
        self.label.grid(row = 0, column = 0,columnspan = 3,rowspan = 3,sticky = NSEW)
    
    def run(self):
        self.isrunning = 1
        self.btnupdate()
        self.start = time.time()
        self.update()
    
    def set_time(self):
        mm = self.elapsed/60
        ss = self.elapsed%60
        ms = (self.elapsed * 100) % 100
        curr = "%.2d:%.2d:%.2d"%(mm,ss,ms)
        return curr
    
    def update(self):
        if self.isrunning:
            self.elapsed = time.time() - self.start
            self.label.config(text=self.set_time())
            self.label.after(75,self.update)
    
    def pause(self):
        if self.isrunning:
            self.isrunning = 0
        else:
            print("lol")
            self.isrunning = 1
            self.start = time.time() - self.elapsed
        self.btnupdate()
        self.update()
    def btnupdate(self):
        if self.isrunning:
            pausebtn.config(text = "Pause")
        else:
            pausebtn.config(text = "Resume")
    def reset(self):
        self.isrunning = 0
        self.btnupdate()
        self.elapsed = 0
        self.label.config(text = self.set_time())

def main(root):
    global pausebtn
    tim = Timer(root)
    start = Button(root,text = "Start",command=lambda:tim.run()).grid(row = 3, column = 0)
    pausebtn = Button(root,text = "Pause",command=lambda:tim.pause(), width = 6)
    pausebtn.grid(row = 3, column = 1)
    reset = Button(root,text = "Reset",command=lambda:tim.reset()).grid(row = 3, column = 2)

if __name__ == "__main__":
    root = Tk()
    main(root)
    root.mainloop()