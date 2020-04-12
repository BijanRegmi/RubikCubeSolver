from tkinter import *
from tkinter import ttk
import timer
import solver

if __name__ == "__main__":
    window = Tk()
    window.title("Rubik Cube")
    window.geometry("1366x768")
    tabctrl = ttk.Notebook(window)
    tabA = ttk.Frame(tabctrl)
    tabB = ttk.Frame(tabctrl)
    solver.main(tabA)
    x = Frame(tabB,width = 950, height = 670)
    x.place(relx=0.5, rely=0.5,anchor = "center")
    timer.main(x)
    tabctrl.add(tabA,text = "Solver")
    tabctrl.add(tabB,text = "Timer")
    tabctrl.pack()
    window.mainloop()
