from tkinter import *
root = Tk()
#Title for calc
root.title("Scientific Calculator")

#Taking user input
user_input = Entry(root,width =30,borderwidth=5,relief=RIDGE)
user_input.grid(row=0,column=0,columnspan=5)

def sc(event):
    key = event.widget
    text = key['text']
    no = user_input.get()
    result = ''
    if text=="deg":
        result = str(m.degrees(float(no)))
    if text =="sin":
        result = str(m.sin(float(no)))
    if text=="cos":
        result = str(m.cos(float(no)))
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
            result=str(float(no)* m.pi)
    if text=="user_input":
        if no=="":
            result=str(m.user_input)
        else:
            result=str(m.user_input**float(no))

    user_input.delete(0,END)
    user_input.insert(0,result)



def click(to_click):
    old = user_input.get()
    user_input.delete(0,END)
    user_input.insert(0,old+to_click)
    return

lg = Button(root,text = 'lg')
lg.bind("<Button-1>",sc)
lg.grid(row=0,column=0)

Zero = Button(root,text = "0",width =30,relief =RIDGE,command = lambda : click("0"))
Zero.grid(row =7,column =2)






def clear():
    user_input.delete(0,END)
    return

def bkspace():
    current = user_input.get()
    length = len(current)-1
    user_input.delete(length,END)

def evaluate():
    ans = user_input.get()
    ans = eval(ans)
    user_input.delete(0,END)
    user_input.insert(0,END)



root.mainloop()