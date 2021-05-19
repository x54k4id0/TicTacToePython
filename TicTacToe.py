from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ActivePlayer=1
P1=[]
P2=[]

root=Tk()
root.title('Tic Tac Toe : P1')
style=ttk.Style()
style.theme_use('classic')


bu1=ttk.Button(root,text=' ')
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda :BuC(1))

bu2=ttk.Button(root,text=' ')
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda :BuC(2))

bu3=ttk.Button(root,text=' ')
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda :BuC(3))

bu4=ttk.Button(root,text=' ')
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda :BuC(4))

bu5=ttk.Button(root,text=' ')
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda :BuC(5))

bu6=ttk.Button(root,text=' ')
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda :BuC(6))

bu7=ttk.Button(root,text=' ')
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda :BuC(7))

bu8=ttk.Button(root,text=' ')
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda :BuC(8))

bu9=ttk.Button(root,text=' ')
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda :BuC(9))

def BuC(id):
    global ActivePlayer
    global P1
    global P1
    if ActivePlayer==1:
        setLayout(id,'X')
        P1.append(id)
        ActivePlayer=2
        root.title('Tic Tac Toe : P2')
        print(f"P1={P1}")
    elif ActivePlayer==2:
        setLayout(id,'O')
        P2.append(id)
        ActivePlayer=1
        root.title('Tic Tac Toe : P1')
        print(f"P2={P2}")
    WinnerCheck()
        
def setLayout(id,txt):
    if id==1:
        bu1.config(text=txt)
        bu1.state(['disabled'])

    elif id==2:
        bu2.config(text=txt)
        bu2.state(['disabled'])

    elif id==3:
        bu3.config(text=txt)
        bu3.state(['disabled'])

    elif id==4:
        bu4.config(text=txt)
        bu4.state(['disabled'])

    elif id==5:
        bu5.config(text=txt)
        bu5.state(['disabled'])

    elif id==6:
        bu6.config(text=txt)
        bu6.state(['disabled'])

    elif id==7:
        bu7.config(text=txt)
        bu7.state(['disabled'])

    elif id==8:
        bu8.config(text=txt)
        bu8.state(['disabled'])

    elif id==9:
        bu9.config(text=txt)
        bu9.state(['disabled'])

def WinnerCheck():
    winner= -1
    if (1 in P1) and (2 in P1) and (3 in P1):
        winner=1
    if (1 in P2) and (2 in P2) and (3 in P2):
        winner=2

    if (4 in P1) and (5 in P1) and (6 in P1):
        winner=1
    if (4 in P2) and (5 in P2) and (6 in P2):
        winner=2

    if (7 in P1) and (8 in P1) and (9 in P1):
        winner=1
    if (7 in P2) and (8 in P2) and (9 in P2):
        winner=2
        
    if (3 in P1) and (6 in P1) and (9 in P1):
        winner=1
    if (3 in P2) and (6 in P2) and (9 in P2):
        winner=2
        
    if (2 in P1) and (5 in P1) and (8 in P1):
        winner=1
    if (2 in P2) and (5 in P2) and (8 in P2):
        winner=2
        
    if (1 in P1) and (5 in P1) and (9 in P1):
        winner=1
    if (1 in P2) and (5 in P2) and (9 in P2):
        winner=2
        
    if (7 in P1) and (5 in P1) and (3 in P1):
        winner=1
    if (3 in P2) and (5 in P2) and (3 in P2):
        winner=2
        
    if (1 in P1) and (4 in P1) and (7 in P1):
        winner=1
    if (1 in P2) and (4 in P2) and (7 in P2):
        winner=2

        
    if winner == 1:
        messagebox.showinfo(title='Winner',message='The winner is P1')
    if winner == 2:
        messagebox.showinfo(title='Winner',message='The winner is P2')

# Abdessamad KERROU
