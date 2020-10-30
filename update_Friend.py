import datetime
from tkinter import *
import cx_Oracle            # https://developer.oracle.com/dsl/prez-python-queries.html
from tkinter import messagebox


# from PhoneBook.main import date
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
cur = conn.cursor()

class Update_Friend(Toplevel):
    def __init__(self,person_id):
        self.person_id = person_id

        # test data start

        print('new data ' + person_id)
        stmt = "select * from person where id = " + person_id
        print (stmt)
        result = cur.execute(stmt).fetchone()
        print(result)
        print(result[1])

        db_name = result[1]
        db_surname = result[2]
        db_email  = result[3]
        db_phone  = result[4]
        db_address  = result[5]

        # test data end

        # call constructor of main class:
        Toplevel.__init__(self)
        self.geometry('500x500+150+100')
        self.title('Update Friend Details')
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

        self.heading = Label(self.topFrame, text='Update Friend Details', bg='white', fg='blue', font='arial 15 bold')
        self.heading.place(x=200, y=50)

        # self.date_lbl = Label(self.topFrame, text="Today's Date:" + date, font='arial 12 bold', fg='#5d92e8', bg='white')
        # self.date_lbl.place(x=300, y=110)

        # Bottom Frame design:

        # NAME
        self.lebel_name = Label(self.bottomFrame, text='Name', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_name.place(x=40, y=50)

        self.entry_name = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_name.insert(0, db_name)
        self.entry_name.place(x=150, y=50)

        # SURNAME
        self.lebel_surname = Label(self.bottomFrame, text='SurName', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_surname.insert(0, db_surname)
        self.entry_surname.place(x=150, y=80)


        # EMAIL
        self.lebel_email = Label(self.bottomFrame, text='Email', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_email.place(x=40, y=110)

        self.entry_email = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_email.insert(0, db_email)
        self.entry_email.place(x=150, y=110)

        # PHONE
        self.lebel_phone = Label(self.bottomFrame, text='Phone', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_phone.place(x=40, y=140)

        self.entry_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_phone.insert(0, db_phone)
        self.entry_phone.place(x=150, y=140)


        # ADDRESS
        self.lebel_address = Label(self.bottomFrame, text='Address', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_address.place(x=40, y=170)

        self.entry_address = Text(self.bottomFrame, width=30, height=5, bd=4)
        self.entry_address.insert(1.0,db_address)
        self.entry_address.place(x=150, y=170)


        btnadd_person = Button(self.bottomFrame, text='Update Record', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold', width=25, height=1, command = self.upd_recs)
        btnadd_person.place(x=150, y=270)

        btn_close = Button(self.bottomFrame, text='Close It', width=15, height=1, command=self.cls_update)
        btn_close.place(x=185, y=325)


    def cls_update(self):
        self.destroy()

    def upd_recs(self):
        # frist track if any changes then apply db conn else msg: no change found.
        id1 = self.person_id
        name1 = self.entry_name.get()
        surname1 = self.entry_surname.get()
        email1 = self.entry_email.get()
        phone1 = self.entry_phone.get()
        address1 = self.entry_address.get(1.0, 'end-1c')

        stmt = "update person set name = '{}', surname = '{}', email ='{}', phone = {}, address ='{}' where id = {}".format(
            name1, surname1, email1, phone1, address1, id1)

        try:
            print(stmt)
            cur.execute(stmt)
            conn.commit()
            #messagebox.showinfo("Success", "Record updated successfully")

            # # refresh the list after update.
            # self.listBox.delete(0, END)
            # friend = cur.execute("select * from person order by 1")
            # cnt = 0
            # for i in friend:
            #     self.listBox.insert(str(cnt), str(i[0]) + ' ' + i[1] + ' ' + i[2])
            #     cnt += 1

        except Exception as e:
            print(e)

        self.lebel_rec_added = Label(self.bottomFrame, text='Record Updated Successfully', font='arial 7 bold', fg='blue',
                                     bg='#7fe3a7')
        self.lebel_rec_added.place(x=150, y=300)
