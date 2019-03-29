__author__ = "hmorrin"

from Tkinter import *
import checker
import backend


#Dummy Data
db_data={"Site1" : {"tier": "App", "external_ip" : "6.6.6.6", "internal_ip" : "5.5.5.5"}, \
         "Site2" : {"tier": "db", "external_ip" : "7.7.7.7", "internal_ip" : "8.8.8.8"},}
top=Tk()

top.title("III CHECK TOOL")

def check_dns():
    List1.delete(0,END)
    print sitecode.get()
    for row in backend.search(sitecode.get()):
        List1.insert(END, row)
    #Query sqlite db for DNS data


def Update_dns_db():
    sites = db_data.keys()
    backend.connect()
    for site in sites:
        tier=db_data[site]["tier"]
        external_ip=db_data[site]["external_ip"]
        internal_ip=db_data[site]["internal_ip"]
        print(site,tier)
        backend.insert_data(site,tier,external_ip,internal_ip)

    #function to update hte sqlite database, with all subdomains of III.com, use dummy data to start.

def Check_Blacklist():
    pass

def View_All():
    List1.delete(0,END)
    for row in backend.view():
        List1.insert(END,row)

def Exit():
    pass
    #close the window

Label1=Label(top, text="Enter III Sitecode:")
Label1.grid(row=0, column=0)

sitecode=StringVar()
Entry1=Entry(top, textvariable=sitecode)
Entry1.grid(row=0,column=1)

Button1=Button(top, text="Update DNS in DB", command=Update_dns_db, width=15)
Button1.grid(row=0, column=6)

Button2=Button(top, text="Check DNS", command=check_dns, width=15)
Button2.grid(row=2, column=6)

Button3=Button(top, text="Check Blacklist", command=Check_Blacklist, width=15)
Button3.grid(row=3, column=6)

Button4=Button(top, text="SSL Check", command=Check_Blacklist, width=15)
Button4.grid(row=4, column=6)

Button5=Button(top, text="Exit", command=Exit, width=15)
Button5.grid(row=10, column=6)

Button6=Button(top, text="VIEW ALL", command=View_All, width=15)
Button6.grid(row=5, column=6)

List1=Listbox(top,height=6, width=35)
List1.grid(row=1,column=0,rowspan=10, columnspan=2)

sb1=Scrollbar(top)
sb1.grid(row=1,column=3,rowspan=10)

List1.configure(yscrollcommand=sb1.set)
sb1.configure(command=List1.yview)

top.mainloop()
