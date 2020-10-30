from tkinter import *
from tkinter import messagebox
import datetime

from mypeople import *

from addPeopple import Add_Friend
# from addPeopple import *

# from About_pg import About_us
from About_pg import *


date = str(datetime.datetime.now().date())
print(date)


class Application(object):
    def __init__(self, master):
        self.master = master

        # need two frames:
        self.topFrame = Frame(master, height=150, bg='white')
        self.topFrame.pack(fill=X)

        self.bottomFrame = Frame(master, height=350, bg='#5d92e8', width=10)
        self.bottomFrame.pack(fill=X)

        # top frame design:- Add Photo
        self.top_image = PhotoImage(file='Icons/People.png')
        self.top_image_label = Label(self.topFrame, image=self.top_image, bg='#737beb')
        self.top_image_label = Label(self.topFrame)
        self.top_image_label.place(x=130, y=85)

        self.heading = Label(self.topFrame, text='My Phonebook', bg='white', fg='blue', font='arial 15 bold')
        self.heading.place(x=200, y=50)

        self.date_lbl = Label(self.topFrame, text="Today's Date:"+date, font='arial 12 bold', fg='#5d92e8', bg='white')
        self.date_lbl.place(x=300, y=110)

        # Button1 : View People

        self.veiwButton = Button(self.bottomFrame, text='My People', fg='#34507d', bg='#ebf0ed', font='arial 9 bold', width=25, height=1, command=self.my_people)
        self.veiwButton.place(x=150, y=60)

        # Button2 : Add People

        self.addButton = Button(self.bottomFrame, text='Add People', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold', width=25, height=1, command=self.Add_Pep)
        self.addButton.place(x=150, y=100)

        # Button3 : About Us

        self.aboutUs = Button(self.bottomFrame, text='About Us', fg='#34507d', bg='#ebf0ed', font='arial 8 bold', width=25, height=1, command=self.About_us)
        self.aboutUs.place(x=150, y=140)

        # sim_text = StringVar()
        # sim_text.set("PhoneBook")
        # self.top_label1 = Label(self.topFrame, text = 'HELLO')
        # self.top_label1.place(x=278, y=40)


        def close_btn(event=''):
            # messagebox.showinfo('Close App', 'Do you want to close')
            s = messagebox.askyesnocancel('Close App', 'Do you want to close')

            # if (s==True):  self.master.quit()

            if (s==True):
                self.master.quit()

        master.bind('<Alt-c>', close_btn)
        # self.btn = Button(self.bottomFrame, text='Close it', command=master.quit)

        self.btn = Button(self.bottomFrame, text='Close', command=close_btn, width=15, height=1)
        self.btn.place(x=385, y=325)     # button functionality

        self.db_btn = Button(self.bottomFrame, text='Db Connection', width=15, height=1)
        self.db_btn.place(x=270, y=325)

    def my_people(self):
        people = MyPeople()

    def Add_Pep(self):
        add_friend = Add_Friend()

    def About_us(self):
        abt_us = About_us()

def main():
    root = Tk()
    Application(root)
    root.title('Phone Book App')
    root.geometry('500x500+150+100')
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
