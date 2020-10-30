import datetime
from tkinter import *
import cx_Oracle            # https://developer.oracle.com/dsl/prez-python-queries.html
from tkinter import messagebox


# from PhoneBook.main import date
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
cur = conn.cursor()

class Display_friends_view(Toplevel):
    def __init__(self,person_id):
        self.person_id = person_id

        # test data start

        print('new data ' + person_id)
        stmt = "select * from person where id = " + person_id
        print (stmt)
        result = cur.execute(stmt).fetchone()
        print(result)
        print(result[1])

        name = result[1]
        surname = result[2]
        email  = result[3]
        phone  = result[4]
        address  = result[5]

        # test data end

        # call constructor of main class:
        Toplevel.__init__(self)
        self.geometry('500x500+150+100')
        self.title('Friend Details')
        self.resizable(False, False)

        # need two frames: topFrame  bottomFrame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=350, bg='#7fe3a7')
        self.bottomFrame.pack(fill=X)

        # top frame design:- Add Photo
        # self.top_image = PhotoImage(file='Icons/People.PNG')
        # self.top_image_label = Label(self.topFrame, image=self.top_image, bg='#737beb')
        # self.top_image_label = Label(self.topFrame)
        # self.top_image_label.place(x=120, y=10)

        self.heading = Label(self.topFrame, text='Friend Details', bg='white', fg='blue', font='arial 15 bold')
        self.heading.place(x=200, y=50)

        # self.date_lbl = Label(self.topFrame, text="Today's Date:" + date, font='arial 12 bold', fg='#5d92e8', bg='white')
        # self.date_lbl.place(x=300, y=110)

        # Bottom Frame design:

        # NAME
        self.lebel_name = Label(self.bottomFrame, text='Name', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_name.place(x=40, y=50)

        self.entry_name = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_name.insert(0, name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=150, y=50)

        # SURNAME
        self.lebel_surname = Label(self.bottomFrame, text='SurName', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_surname.insert(0, surname)
        self.entry_surname.config(state='disabled')
        self.entry_surname.place(x=150, y=80)


        # EMAIL
        self.lebel_email = Label(self.bottomFrame, text='Email', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_email.place(x=40, y=110)

        self.entry_email = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_email.insert(0, email)
        self.entry_email.config(state='disabled')
        self.entry_email.place(x=150, y=110)

        # PHONE
        self.lebel_phone = Label(self.bottomFrame, text='Phone', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_phone.place(x=40, y=140)

        self.entry_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_phone.insert(0, phone)
        self.entry_phone.config(state='disabled')
        self.entry_phone.place(x=150, y=140)


        # ADDRESS
        self.lebel_address = Label(self.bottomFrame, text='Address', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_address.place(x=40, y=170)

        self.entry_address = Text(self.bottomFrame, width=30, height=5, bd=4)
        self.entry_address.insert(1.0,address)
        self.entry_address.config(state='disabled')
        self.entry_address.place(x=150, y=170)


        btnadd_person = Button(self.bottomFrame, text='Record Viewed', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold', width=25, height=1, command=self.cls_detail)
        btnadd_person.place(x=150, y=270)

    def cls_detail(self):
        self.destroy()