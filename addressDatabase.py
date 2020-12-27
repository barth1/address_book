from tkinter import *
from collections import namedtuple
#from PIL import ImageTK,Image
import sqlite3
root=Tk()
root.title('address book')

root.geometry("400x400")

#Database
#create database or to one
conn=sqlite3.connect('address_booking.db')
#create cursor
c=conn.cursor()

#create table

'''c.execute("CREATE TABLE addresses(\n"
          "       First_name text,\n"
          "       Last_name text,\n"
          "       Address text,\n"
          "       City text,\n"
          "       State text,\n"
          "       Zip_code integer\n"
          ")")'''
#submit function
def submit ():
   # create database or to one
    conn = sqlite3.connect('address_booking.db')
    # create cursor
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :state, :city, :zipcode)",
              dict(f_name=f_name.get(), l_name=l_name.get(), address=address.get(), state=state.get(), city=city.get(),
                   zipcode=zipcode.get())
              )

    # commit changes
    conn.commit()
    # close connection
    conn.close()
   # cleat text area after entry record


    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)

#create Query function
def item(tokyo):
    pass


def query ():
# create database or to one
    conn = sqlite3.connect('address_booking.db')
    # create cursor
    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    F_name = namedtuple('F_name', 'l_name address state city zipcode')
    tokyo = F_name(records[0], records[1], records[2],records[3], records[4] )

    for key, value in item(tokyo):
    #print(ords)
        print_record= key + ':',value
#loop through the record
    '''for record in records:
        print_record+='% %' %str(record)'''

    query_label=Label(root,text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)
# commit changes
    conn.commit()
    # close connection
    conn.close()





#create text boxes
f_name=Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name=Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address=Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

state=Entry(root, width=30)
state.grid(row=3, column=1, padx=20)

city=Entry(root, width=30)
city.grid(row=4, column=1, padx=20)

zipcode=Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)


# to create text lable

f_namelable=Label(root, text='First Name')
f_namelable.grid(row=0,column=0)

l_namelable=Label(root, text='Last Name')
l_namelable.grid(row=1,column=0)

addresslable=Label(root, text='Address')
addresslable.grid(row=2,column=0)

statelable=Label(root, text='State')
statelable.grid(row=3,column=0)

citylable=Label(root, text='City')
citylable.grid(row=4,column=0)

zipcodelable=Label(root, text='Zipcode')
zipcodelable.grid(row=5,column=0)

#create submit button

submit_btn=Button(root, text='Add Record To Database',command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10,pady=10, ipadx=100)

#create a query button
query_btn=Button(root,text='Show Records', command=query)
query_btn.grid(row=7,column=0, columnspan=2,padx=10, pady=10, ipadx=137)





#commit changes
conn.commit()
#close connection
conn.close()







mainloop()
