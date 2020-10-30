import datetime
from tkinter import *
import cx_Oracle            # https://developer.oracle.com/dsl/prez-python-queries.html
from tkinter import messagebox


class About_us(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('500x500+150+100')
        self.title('About Us..')
        self.resizable(False, False)

        # need two frames: topFrame  bottomFrame
        self.topFrame = Frame(self, height=150, bg='#14a0a8')
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=350, bg='#5fb3b8')
        self.bottomFrame.pack(fill=X)

        self.heading = Label(self.topFrame, text='Your Personal Book', fg='blue', font='arial 20 bold')
        self.heading.place(x=100, y=50)

        self.heading = Label(self.topFrame, text='Community 2020.1', fg='Red', font='arial 15 bold')
        self.heading.place(x=100, y=100)


        # self.date_lbl = Label(self.topFrame, text="Today's Date:" + date, font='arial 12 bold', fg='#5d92e8', bg='white')
        # self.date_lbl.place(x=300, y=110)

        # Bottom Frame design:

        self.lebel_name = Label(self.bottomFrame, text='Community 2020.1 (First Edition)', font='arial 14', fg='white', bg='#5fb3b8')
        self.lebel_name.place(x=100, y=50)


        self.lebel_name = Label(self.bottomFrame, text='Build #PC-2020.10001.98, Build on Sep 07,2020', font='arial 11 bold', fg='white', bg='#5fb3b8')
        self.lebel_name.place(x=100, y=80)

        self.lebel_name = Label(self.bottomFrame, text='Powered By Ayush Software Pvt Ltd.', font='arial 11 bold', fg='white', bg='#5fb3b8')
        self.lebel_name.place(x=100, y=120)

        self.lebel_name = Label(self.bottomFrame, text='Copyright 2010-2020', font='arial 8 bold', fg='white', bg='#5fb3b8')
        self.lebel_name.place(x=100, y=300)


        def close_btn(event=''):
            self.destroy()

        self.btn = Button(self.bottomFrame, text='Thanks :) ', command=close_btn, width=15, height=1)
        self.btn.place(x=385, y=325)     # button functionality
