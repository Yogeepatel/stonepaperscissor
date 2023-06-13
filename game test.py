from tkinter import *
from random import randint
import random
def chance():
    l=['stone','paper','sessior','paper','stone','sessior','paper','sessior','stone','sessior','stone','paper','sessior','paper','stone','sessior','paper','sessior','stone','sessior','stone','paper','sessior','paper','stone','sessior','paper','sessior','stone','sessior','stone','paper','sessior','paper','stone','sessior','paper','sessior','stone','sessior','stone','paper','sessior','paper','stone','sessior','paper','sessior','stone','sessior']
    random.shuffle(l)
    r=randint(0,49)
    b=l[r]
    return(b)
def ad():
    global a
    a=a+1
    label1.configure(text ="{}".format(a))
def cd():
    global c
    c=c+1
    label2.configure(text ="{}".format(c))
def ch():
    global i
    if (a+c)>=5:
        i=False
        if a>c:
            label4.configure(text = "you won", font=('normal', 40))
        else:
            label4.configure(text = "cpu won", font=('normal', 40))        
def call():
    if i == True:
        label3.configure(text='stone',font=('normal', 40))
        b=chance()
        label5.configure(text="{}".format(b), font=('normal', 40))
        if b=="sessior" and i==True:
            label4.configure(text = "stone", font=('normal', 40))
            d=ad()
            ch()
        elif b=="paper" and i==True:
            label4.configure(text = "paper", font=('normal', 40))
            d=cd()
            ch()
        elif b=="stone" and i==True:
            label4.configure(text = "Draw", font=('normal', 40))
            ch()
def kall():
    if i == True:
        label3.configure(text='paper',font=('normal', 40))
        b=chance()
        label5.configure(text="{}".format(b),font=('normal', 40))
        if b=="sessior" and i==True:
            label4.configure(text = "sessior", font=('normal', 40))
            d=cd()
            ch()
        elif b=="paper" and i==True:
            label4.configure(text = "Draw", font=('normal', 40))
            ch()
        elif b=="stone" and i==True:
            label4.configure(text = "paper", font=('normal', 40))
            d=ad()
            ch()
def pall():
    if i == True:
        label3.configure(text='sessior',font=('normal', 40))
        b=chance()
        label5.configure(text="{}".format(b), font=('normal', 40))
        if b=="sessior" and i==True:
            label4.configure(text = "Draw", font=('normal', 40))
            ch()
        elif b=="paper" and i==True:
            label4.configure(text = "sessior", font=('normal', 40))
            d=ad()
            ch()
        elif b=="stone" and i==True:
            label4.configure(text = "stone", font=('normal', 40))
            d=cd()
            ch()
root =Tk()
root.title("Stone-Paper-Scissor Game")
label= Label(text = 'score',font=('normal', 40))
label1=Label(text = '0',font=('normal', 40))
label2 =Label(text = '0',font=('normal', 40))
label3 = Label(text = '',font=('normal', 40), width=7)
label4 = Label(text = '',font=('normal', 40), width=8)
label5 = Label(text = '',font=('normal', 40), width=7)
label6 = Label(text = 'Your Response',font=('normal', 25), width=15)
label7 = Label(text = 'CPU Response',font=('normal', 25), width=15)
label8 = Label(text = 'Result',font=('normal', 25), width=15)
button1 = Button(text = "stone" ,font=('normal', 40), width=7, bg='yellow', command=call)
button2 = Button(text = "paper" ,font=('normal', 40), width=7, bg='red', command=kall)
button3 = Button(text = 'scissor',font=('normal', 40), width=7, bg='green', command=pall)
button1.grid(row = 4, column = 2)
button2.grid(row = 5, column = 2)
button3.grid(row = 6, column = 2)
label.grid(row = 1, column = 7,columnspan = 2)
label1.grid(row = 2, column = 7)
label2.grid(row = 2, column = 8)
label3.grid(row = 5, column = 4)
label4.grid(row = 5, column = 7, columnspan = 3)
label5.grid(row = 5, column =10)
label6.grid(row = 4, column = 3, columnspan = 4)
label7.grid(row = 4, column = 10, columnspan = 4)
label8.grid(row = 4, column = 7, columnspan = 2)
a=0
c=0
i=True
mainloop()
