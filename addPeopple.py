from tkinter import *
import datetime
import cx_Oracle            # https://developer.oracle.com/dsl/prez-python-queries.html
from tkinter import messagebox

dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
cur = conn.cursor()
cur_select = conn.cursor()

date = str(datetime.datetime.now().date())
print(date)

# con = sqlite3.connect('PhoneBookDB.db')


class Add_Friend(Toplevel):
    def __init__(self):
        # call constructor of main class:
        Toplevel.__init__(self)
        self.geometry('500x500+150+100')
        self.title('Add New Person')
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

        self.heading = Label(self.topFrame, text='Add New Person', bg='white', fg='blue', font='arial 15 bold')
        self.heading.place(x=200, y=50)

        self.date_lbl = Label(self.topFrame, text="Today's Date:" + date,
                              font='arial 12 bold', fg='#7fe3b7', bg='white')

        self.date_lbl.place(x=300, y=110)

        # Bottom Frame design:

        # NAME
        self.lebel_name = Label(self.bottomFrame, text='Name', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_name.place(x=40, y=50)

        self.entry_name = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_name.insert(0, 'Enter Name')
        self.entry_name.place(x=150, y=50)

        # SURNAME
        self.lebel_surname = Label(self.bottomFrame, text='SurName', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_surname.insert(0, 'Enter Surname')
        self.entry_surname.place(x=150, y=80)

        # EMAIL
        self.lebel_email = Label(self.bottomFrame, text='Email', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_email.place(x=40, y=110)

        self.entry_email = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_email.insert(0, 'Enter email@gmail.com')
        self.entry_email.place(x=150, y=110)

        # PHONE
        self.lebel_phone = Label(self.bottomFrame, text='Phone', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_phone.place(x=40, y=140)

        self.entry_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_phone.insert(0, '098251')
        self.entry_phone.place(x=150, y=140)

        # ADDRESS
        self.lebel_address = Label(self.bottomFrame, text='Address', font='arial 13 bold', fg='white', bg='#7fe3a7')
        self.lebel_address.place(x=40, y=170)

        self.entry_address = Text(self.bottomFrame, width=30, height=5, bd=4)
        self.entry_address.insert(1.0, 'Bangalore')
        self.entry_address.place(x=150, y=170)

        btnadd_person = Button(self.bottomFrame, text='Add Friend', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold',
                               width=25, height=1, command=self.add_people)

        btnadd_person.place(x=150, y=270)

        btn_close = Button(self.bottomFrame, text='Close it', width=25, height=1, command=self.close_add_peo_win)
        btn_close.place(x=150, y=320)

        # for max_id in cur.execute('select max(id) from person'):
        #     print('*************')
        #     if max_id[0] is None:
        #         max_id = 1
        #         print(max_id)
        #     else:
        #         max_id += 1

    def close_add_peo_win(self):
        self.destroy()
        # my people, frd list should get refresh.

    def add_people(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0, 'end-1c')

        # find latest id from person table:
        try:
            cur.execute('select max(id) from person')

            for max_id in cur:
                print(max_id[0])

            if max_id[0] is None:
                new_id = 1
                print(new_id)
            else:
                new_id = max_id[0]
                new_id += 1
            stmt = "insert into person (id, name, surname, email, phone, address)" \
                            "values (:new_id, :name, :surname, :email, :phone, :address ) "
            cur_select.execute(stmt, (new_id, name, surname, email, phone, address))
            conn.commit()

            self.lebel_rec_added = Label(self.bottomFrame, text='Record Added Successfully', font='arial 7 bold', fg='blue', bg='#7fe3a7')
            self.lebel_rec_added.place(x=150, y=300)

        except Exception as e:
                messagebox.showerror('db err', str(e))


        # if name and surname and email and phone and address != "":
        #     # not working in case of pass
        #     try:
        #         cur.bindarraysize = 1
        #         cur.setinputsizes(int, 40)
        #
        #         stmt = "insert into person ( name, surname, email, phone, address)" \
        #                "values (:name, :surname, :email, :phone, :address ) "
        #
        #         rows = [(name, surname, email, phone, address)]
        #
        #         cur.executemany(stmt, rows)
        #
        #         # cur.executemany("insert into person (name, surname, email, phone, address)
        #         # values (:name, :surname, :email, :phone, :address)", rows)
        #
        #         conn.commit()
        #         cur.close()
        #
        #         self.lebel_name = Label(self.bottomFrame, text='Record Added',
        #                                 font='arial 9 bold', fg='blue', bg='#7fe3a7')
        #
        #         self.lebel_name.place(x=150, y=300)
        #     except Exception as e:
        #         messagebox.showerror('db err', str(e))
        # else:
        #     messagebox.showerror('Error', 'All fields are mandotery', icon='warning')
