__author__ = "hmorrin"

from Tkinter import *
import dns_checker

top=Tk()

def display_dns():
    site=e1_value.get()
    text=dns_checker.main(site)
    t1.insert(END, text)

L1 = Label(top,text="Enter Site code: ")
L1.grid( row=0, column=0 )

e1_value=StringVar()
E1=Entry(top, textvariable=e1_value)
E1.grid(row=0,column=1)

B=Button(top, text="Check DNS", command=display_dns)
B.grid(row=3, column=2)

t1=Text(top,height=4,width=20)
t1.grid(row=1,column=0)

top.mainloop()
