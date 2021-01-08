from tkinter import *
import math as m
root = Tk()
#Title for calc
root.title("Scientific Calculator")

#Taking user input
e = Entry(root,width =30,borderwidth=5,relief=RAISED)
e.grid(row=0,column=0,columnspan=5)
#functions

def click(to_click):
    old = e.get()
    e.delete(0,END)
    e.insert(0,old+to_click)
    return


def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result = ''

    if text=="deg":
        result = str(m.degrees(float(no)))
    if text =="sin":
        result = str(m.sin(float(no)))
    if text=="cos":
        result = str(m.cos(float(no)))
    if text=="x!":
        result = str(m.factorial(float(no)))
    if text=="tan":
        result = str(m.tan(float(no)))
    if text=="lg":
        result = str(m.log10(float(no)))
    if text=="ln":
        result = str(m.log(float(no)))
    if text=="Sqrt":
        result = str(m.degrees(float(no)))
    if text=="pi":
        if no=="":
            result = str(m.pi)
        else:
            result=str(float(no) * m.pi)
    if text == "e":
        if no=="":
            result = str(m.e)
        else:
            result = str(m.e**float(no))


    e.delete(0,END)
    e.insert(0,result)


def clear():
    e.delete(0,END)
    return

def bkspace():
    current = e.get()
    length = len(current)-1
    e.delete(length,END)

def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0,END)
    e.insert(0,ans)

#button detailes
log = Button(root,text = 'log',width =10)
log.bind("<Button-1>",sc)
log.grid(row=2,column=1)

pi = Button(root,text='Pi',width=10)
pi.bind("<Button-1>",sc)
pi.grid(row=5,column=0)

sin= Button(root,text='sin',width=10)
sin.bind("<Button-1>",sc)
sin.grid(row=2,column=0)

cos = Button(root,text='cos',width=10)
cos.bind("<Button-1>",sc)
cos.grid(row=3,column=0)

tan = Button(root,text='tan',width=10)
tan.bind("<Button-1>",sc)
tan.grid(row=4,column=0)

Sqrt = Button(root,text = 'Sqrt',width =10)
Sqrt.bind("<Button-1>",sc)
Sqrt.grid(row=6,column=0)

x = Button(root,text = 'x!',width =10)
x.bind("<Button-1>",sc)
x.grid(row=3,column=1)

deg = Button(root,text = 'Deg',width =10)
deg.bind("<Button-1>",sc)
deg.grid(row=7,column=0)



clear = Button(root,text="C",width=10)
clear.bind("<Button-1>",sc)
clear.grid(row=2,column=4)

plus = Button(root,text="+",width=10,relief=RAISED,bg="grey53",command = lambda : click("+"))
plus.grid(row=6,column=4)

min= Button(root,text="-",width=10,relief=RAISED,bg="grey53",command = lambda : click("-"))
min.grid(row=3,column=4)

mul= Button(root,text="*",width=10,relief=RAISED,bg="grey53",command = lambda : click("*"))
mul.grid(row=4,column=4)

div= Button(root,text="/",width=10,relief=RAISED,bg="grey53",command = lambda : click("/"))
div.grid(row=5,column=4)

bracket= Button(root,text="(",width=10,relief=RAISED,command = lambda : click("("))
bracket.grid(row=3,column=2)

bracket1= Button(root,text=")",width=10,relief=RAISED,command = lambda : click(")"))
bracket1.grid(row=3,column=3)



equal = Button(root,text="=",width=10,relief=RIDGE,bg="blue",command = lambda : evaluate())
equal.grid(row=7,column=4)

Backspace=Button(root,text="<-",width=10,relief=RIDGE,command = lambda : bkspace())
Backspace.grid(row=7,column=3)
#button from 0

Zero = Button(root,text = "0",width =10,relief =RAISED,command = lambda : click("0"))
Zero.grid(row =7,column =2)
one = Button(root,text = "1",width =10,relief =RAISED,command = lambda : click("1"))
one.grid(row =6,column =1)
two = Button(root,text = "2",width =10,relief =RAISED,command = lambda : click("2"))
two.grid(row =6,column =2)
three = Button(root,text = "3",width =10,relief =RAISED,command = lambda : click("3"))
three.grid(row =6,column =3)
four = Button(root,text = "4",width =10,relief =RAISED,command = lambda : click("4"))
four.grid(row =5,column =1)
five = Button(root,text = "5",width =10,relief =RAISED,command = lambda : click("5"))
five.grid(row =5,column =2)
six = Button(root,text = "6",width =10,relief =RAISED,command = lambda : click("6"))
six.grid(row =5,column =3)
seven = Button(root,text = "7",width =10,relief =RAISED,command = lambda : click("7"))
seven.grid(row =4,column =1)
eight = Button(root,text = "8",width =10,relief =RAISED,command = lambda : click("8"))
eight.grid(row =4,column =2)
nine = Button(root,text = "9",width =10,relief =RAISED,command = lambda : click("9"))
nine.grid(row =4,column =3)

dot = Button(root,text = ".",width =10,relief =RAISED,command = lambda : click("9"))
dot.grid(row =7,column =1)



root.mainloop()