from tkinter import *
expression = ""
r= Tk()
r.title('Calculator')
r.geometry('500x500')
label= Label(r, text= "CALCULATOR").grid(columnspan=5, row=0)
equation= StringVar()

#FUNCTIONs
def press(num):
    global expression
    expression= expression + str(num)
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set(" error ")
        expression = ""

def last_clear():
    equation.set( equation.get()[:-1] )



#entery text
txt=Entry(r,width=30,border=4, textvariable=equation).grid(columnspan=5,row=1,pady=3)

#first row button row=2
bt= Button(r, text="%", width=6, bg='black', fg='white',command= lambda :press('%')).grid(column=0,row=2)
bt= Button(r, text="/", width=6, bg='black', fg='white',command= lambda :press('/')).grid(column=1,row=2)
bt1= Button(r, text="CE", width=6, bg='black', fg='white',command=clear).grid(column=2,row=2) 

bt2= Button(r, text="C", width=6, bg='black', fg='white', command=last_clear).grid(column=3,row=2)


#second row button row=3
bt= Button(r, text="7", width=6, bg='black', fg='white',command= lambda :press('7')).grid(column=0,row=3)
bt1= Button(r, text="8", width=6, bg='black', fg='white',command= lambda :press('8')).grid(column=1,row=3)
bt2= Button(r, text="9", width=6, bg='black', fg='white',command= lambda :press('9')).grid(column=2,row=3)
bt3= Button(r, text="*", width=6, bg='black', fg='white',command= lambda :press('*')).grid(column=3,row=3)

#third row button row=4
bt= Button(r, text="4", width=6, bg='black', fg='white',command= lambda :press('4')).grid(column=0,row=4)
bt1= Button(r, text="5", width=6, bg='black', fg='white',command=lambda :press('5')).grid(column=1,row=4)
bt2= Button(r, text="6", width=6, bg='black', fg='white',command= lambda :press('6')).grid(column=2,row=4)
bt3= Button(r, text="-", width=6, bg='black', fg='white',command= lambda :press('-')).grid(column=3,row=4)

#fourth row button row=5
bt= Button(r, text="1", width=6, bg='black', fg='white',command= lambda :press('1')).grid(column=0,row=5)
bt1= Button(r, text="2", width=6, bg='black', fg='white',command= lambda :press('2')).grid(column=1,row=5)
bt2= Button(r, text="3", width=6, bg='black', fg='white',command= lambda :press('3')).grid(column=2,row=5)
bt3= Button(r, text="+", width=6, bg='black', fg='white',command= lambda :press('+')).grid(column=3,row=5)

#fifth row button row=6

bt1= Button(r, text="0", width=14, bg='black', fg='white',command= lambda :press('0')).grid(column=0,row=6, columnspan=2)
bt2= Button(r, text=".", width=6, bg='black', fg='white',command= lambda :press('.')).grid(column=2,row=6)
bt3= Button(r, text="=", width=6, bg='blue', fg='white', command=equalpress).grid(column=3,row=6)
r.mainloop()