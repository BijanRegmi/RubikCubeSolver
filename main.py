from tkinter import *
import moves
import cube
import kociemba
cols = ["green","blue","white","yellow","red","orange"]
Cols = ["g","b","w","y","r","o"]
selected = 0
mode = False

def show(side):
    surr = {
        0:"2435",
        1:"2534",
        2:"1405",
        3:"0415",
        4:"2130",
        5:"2031",
    }.get(side)
    side = cols[side]
    face = {
        cols[0]:cube.green,
        cols[1]:cube.blue,
        cols[2]:cube.white,
        cols[3]:cube.yellow,
        cols[4]:cube.red,
        cols[5]:cube.orange,
    }.get(side)
    n=0

    for i in range(9):
        colour = {
            "g":cols[0],
            "b":cols[1],
            "w":cols[2],
            "y":cols[3],
            "r":cols[4],
            "o":cols[5],
        }.get(face[int(n/3)][int(n%3)])
        buts[i].config(bg=colour,state="disabled")
        buts[i].grid(row=int(n/3)+6,column=int(n%3)+4)    #starts from row = 6 and column = 4
        n+=1
    """ if not mode:
        msg = "SIDE:"
        msg+=cols[selected]
        sel.config(text=msg) """
    Button(root,width=3,bg=cols[int(surr[0])],state=DISABLED).grid(row=4,column=5)
    Button(root,width=3,bg=cols[int(surr[1])],state=DISABLED).grid(row=7,column=8)
    Button(root,width=3,bg=cols[int(surr[2])],state=DISABLED).grid(row=10,column=5)
    Button(root,width=3,bg=cols[int(surr[3])],state=DISABLED).grid(row=7,column=2)

    Button(root,width=6,text="EDIT",command=edit).grid(row=1,column=1,columnspan=2,rowspan=2)
    Button(root,width=6,text="SOLVE",command=solve).grid(row=1,column=8,columnspan=2,rowspan=2)

    

    Button(root,width=3,bg=cols[0],command=lambda:selected_colour(0)).grid(row=1,column=4)
    Button(root,width=3,bg=cols[1],command=lambda:selected_colour(1)).grid(row=2,column=4)
    Button(root,width=3,bg=cols[2],command=lambda:selected_colour(2)).grid(row=1,column=5)
    Button(root,width=3,bg=cols[3],command=lambda:selected_colour(3)).grid(row=2,column=5)
    Button(root,width=3,bg=cols[4],command=lambda:selected_colour(4)).grid(row=1,column=6)
    Button(root,width=3,bg=cols[5],command=lambda:selected_colour(5)).grid(row=2,column=6)
    
def solve():
    solution = kociemba.solve(current_state())
    labe.delete(0,END)
    labe.insert(0,solution)

def selected_colour(c):
    global selected
    selected = c
    if not mode:
        show(selected)

    
def edit():
    
    global mode
    mode = not mode
    if mode:
        buts[0].config(state="normal",command=lambda:edit_colour(0))
        buts[1].config(state="normal",command=lambda:edit_colour(1))
        buts[2].config(state="normal",command=lambda:edit_colour(2))
        buts[3].config(state="normal",command=lambda:edit_colour(3))
        buts[5].config(state="normal",command=lambda:edit_colour(5))
        buts[6].config(state="normal",command=lambda:edit_colour(6))
        buts[7].config(state="normal",command=lambda:edit_colour(7))
        buts[8].config(state="normal",command=lambda:edit_colour(8))
        md.config(text="Mode:EDIT SIDE")
    else:
        md.config(text="Mode:BROWSE SIDE")
        for i in buts:
            i.config(state="disabled")

def edit_colour(i):
    cur = buts[4].cget('bg')
    face = {
        cols[0]:cube.green,
        cols[1]:cube.blue,
        cols[2]:cube.white,
        cols[3]:cube.yellow,
        cols[4]:cube.red,
        cols[5]:cube.orange,
    }.get(cur)
    face[int(i/3)][int(i%3)] = Cols[selected]
    buts[i].config(bg=cols[selected])


def current_state():
    state = ""
    for i in cube.white:
        for j in i:
            state+=selecttext(j)
    for i in cube.red:
        for j in i:
            state+=selecttext(j)
    for i in cube.green:
        for j in i:
            state+=selecttext(j)
    for i in cube.yellow:
        for j in i:
            state+=selecttext(j)
    for i in cube.orange:
        for j in i:
            state+=selecttext(j)
    for i in cube.blue:
        for j in i:
            state+=selecttext(j)
    return state
            
def selecttext(c):
    f = {
        "w":"U",
        "r":"R",
        "y":"D",
        "o":"L",
        "g":"F",
        "b":"B",
    }.get(c)
    return f

root = Tk()
root.title("RUBIK CUBE SOLVER")
buts = [
        Button(root,width=3),
        Button(root,width=3),
        Button(root,width=3),
        Button(root,width=3),
        Button(root,width=3),
        Button(root,width=3),
        Button(root,width=3),
        Button(root,width=3),
        Button(root,width=3)
    ]
md = Label(root,text="Mode:BROWSE SIDES")
md.grid(row=0,column=0,columnspan=11)
sel = Label(root)
sel.grid(row=3,column=0,columnspan=11)
Label(root).grid(row=5,column=0,columnspan=11)
Label(root).grid(row=9,column=0,columnspan=11)
Label(root).grid(row=11,column=0,columnspan=11)
Label(root).grid(row=13,column=0,columnspan=11)
labe = Entry(root,width=40)
labe.grid(row=12,column=0,columnspan=11)
show(0)
root.mainloop()