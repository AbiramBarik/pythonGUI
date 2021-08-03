from tkinter import *
import random
root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title("ROCK-PAPER-SCISSOR")
root.config(bg='seashell3')
Label(root, text='ROCK ,PAPER ,SCISSOR ', font='arial 20 bold', bg='seashell2').pack()
user_take=StringVar()
Label(root, text='YOUR CHOICE', font='arial 10 bold', bg='linen', fg='black', relief=GROOVE).place(x=10, y=80)
Label(root, text='COMPUTER', font='arial 11 bold', bg='linen', fg='black', relief=GROOVE).place(x=10, y=130)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2', width=15).place(x=120, y=80)
results = StringVar()

def play():
    comp = random.randint(1, 3)
    if comp == 1:
        comp = "ROCK"
    elif comp == 2:
        comp = "PAPER"
    else:
        comp = "SCISSOR"
    print(comp)
    Label(root, font='arial 10 bold', text=comp, bg='linen', fg='black',relief= RAISED,width=8).place(x=130, y=130)
    user_pick=user_take.get()
    if user_pick==comp:
        results.set('tie')
    elif (user_pick=='ROCK' and comp=='PAPER') or (user_pick=='PAPER' and comp=='SCISSOR')or(user_pick=='SCISSOR' and comp=='ROCK'):
        results.set('you LOSE computer wins')
    elif (user_pick == 'ROCK' and comp == 'SCISSOR') or (user_pick == 'PAPER' and comp == 'ROCK') or (user_pick == 'SCISSOR' and comp == 'PAPER'):
        results.set('you WIN')
    else:
        results.set('invalid choice')

def Reset():
    results.set("")
    user_take.set("")

Entry(root,font='arial 14 bold',textvariable=results,bg='antiquewhite2',width=27).place(x=50,y=190)
Button(root,font='ariel 13 bold',text=' PLAY ',padx=5,bg='chocolate',fg='whitesmoke',relief=RAISED,command=play,activebackground='coral',activeforeground='ivory').place(x=300,y=80)
Button(root,font='ariel 13 bold',text=' RESET ',padx=5,bg='orangered',fg='mistyrose',relief=RAISED,command=Reset,activebackground='firebrick',activeforeground='white').place(x=150,y=230)

root.mainloop()