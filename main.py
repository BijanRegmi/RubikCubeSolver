from tkinter import *
import moves
import cube

cols = ["green","blue","white","yellow","red","orange"]

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

    #surroundings
    Button(root,width=3,bg=cols[int(surr[0])],state=DISABLED).grid(row=4,column=5)
    Button(root,width=3,bg=cols[int(surr[1])],state=DISABLED).grid(row=7,column=8)
    Button(root,width=3,bg=cols[int(surr[2])],state=DISABLED).grid(row=10,column=5)
    Button(root,width=3,bg=cols[int(surr[3])],state=DISABLED).grid(row=7,column=2)

    Button(root,width=6,text="EDIT").grid(row=1,column=1,columnspan=2,rowspan=2)
    Button(root,width=6,text="SOLVE").grid(row=1,column=8,columnspan=2,rowspan=2)

    Label(root).grid(row=0,column=0,columnspan=11)
    Label(root).grid(row=3,column=0,columnspan=11)
    Label(root).grid(row=5,column=0,columnspan=11)
    Label(root).grid(row=9,column=0,columnspan=11)
    Label(root).grid(row=11,column=0,columnspan=11)
    Label(root).grid(row=13,column=0,columnspan=11)
    
    Entry(root,width=40).grid(row=12,column=0,columnspan=11)
    

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

Button(root,width=3,bg=cols[0]).grid(row=1,column=4)
Button(root,width=3,bg=cols[1]).grid(row=2,column=4)
Button(root,width=3,bg=cols[2]).grid(row=1,column=5)
Button(root,width=3,bg=cols[3]).grid(row=2,column=5)
Button(root,width=3,bg=cols[4]).grid(row=1,column=6)
Button(root,width=3,bg=cols[5]).grid(row=2,column=6)

labs = [1,2,3,4,5]
#for i in range(5):
#    labs[i] = Label(root,text="").grid(row=i,column=0)
show(1)
root.mainloop()
