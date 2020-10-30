from tkinter import *
import datetime
import cx_Oracle
from tkinter import messagebox


from addPeopple import Add_Friend
from update_Friend import *
from Display_friends import Display_friends_view


dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
cur = conn.cursor()


date = str(datetime.datetime.now().date())
print(date)

#con = sqlite3.connect('PhoneBookDB.db')
class MyPeople(Toplevel):
    def __init__(self):
        # call constructor of main class:
        Toplevel.__init__(self)
        self.geometry('500x500+150+100')
        self.title('My People')
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

        self.heading = Label(self.topFrame, text='My People', bg='white', fg='blue', font='arial 15 bold')
        self.heading.place(x=200, y=50)

        self.date_lbl = Label(self.topFrame, text="Today's Date:" + date, font='arial 12 bold', fg='#7fe3a7', bg='white')
        self.date_lbl.place(x=300, y=110)

        # Bottom Frame design:


        self.scroll = Scrollbar(self.bottomFrame, orient=VERTICAL)
        self.scroll.grid(row=0, column=1, sticky=N + S, padx=(0, 0), pady=(5, 0))


        self.listBox = Listbox(self.bottomFrame, width=30, height=15)
        self.listBox.grid(row=0, column=0, padx=(5, 0), pady=(5, 0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        #self.scroll.config(command=self.listBox.yview())

        # for i in range(40):
        #     self.listBox.insert(END, 'list:' + str(i))
        #
        # person = cur.execute("select * from person")
        # for row in person:
        #     print(row)


        friend = cur.execute("select * from person order by 1")
        cnt = 0
        for i in friend:
            self.listBox.insert(str(cnt), str(i[0]) + ' ' + i[1] + ' ' + i[2])
            cnt += 1

        self.listBox.select_set(0)

        # def CurSelet(event):
        #     widget = event.widget
        #     selection = widget.curselection()
        #     picked = widget.get(selection[1])
        #     print(picked)
        #
        # self.listBox.bind('<<self.listbox>>', CurSelet)

        # person1 = cur.execute("select * from person").fetchall()
        # print(person1)

        btnadd = Button(self.bottomFrame, text='Add Friend', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold', width=25, height=1, command = self.add_People)
        btnadd.grid(row=0, column=2, padx=20, pady=20, sticky=N)

        btn_update = Button(self.bottomFrame, text='Update Friend', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold', width=25, height=1, command=self.upd_frd)
        btn_update.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btn_disp = Button(self.bottomFrame, text='Display Friend', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold', width=25, height=1, command=self.disp_frd)
        btn_disp.grid(row=0, column=2, padx=20, pady=80, sticky=N)

        btn_del = Button(self.bottomFrame, text='Delete Record', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold', width=25, height=1, command=self.delete_rec)
        btn_del.grid(row=0, column=2, padx=20, pady=110, sticky=N)

        btn_refresh = Button(self.bottomFrame, text='Refresh Friend List', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold', width=20, height=1, command=self.refresh_list)
        btn_refresh.grid(row=1, column=0, padx=(0, 0), pady=5, sticky=N)

        btn_cls_it = Button(self.bottomFrame, text='Close Window', fg='#34507d', bg='#ebf0ed',  font='arial 8 bold', width=20, height=1, command=self.close_btn)
        btn_cls_it.grid(row=1, column=2, padx=(0, 0), pady=5, sticky=N)

    def close_btn(self):
            # messagebox.showinfo('Close App', 'Do you want to close')
            # s = messagebox.askyesnocancel('Close App', 'Do you want to close')

            # if (s==True):  self.master.quit()

            self.destroy()

    def refresh_list(self):
        self.listBox.delete(0, END)
        friend = cur.execute("select * from person order by 1")
        cnt = 0
        for i in friend:
            self.listBox.insert(str(cnt), str(i[0]) + ' ' + i[1] + ' ' + i[2])
            cnt += 1

        self.listBox.select_set(0)
        self.lebel_rec_Refreshed = Label(self.bottomFrame, text='List Refreshed             ', font='arial 11 bold', fg='blue', bg='#7fe3a7')
        self.lebel_rec_Refreshed.place(x=225, y=210)


    def add_People(self):
        add_page = Add_Friend()

    def upd_frd(self):
        # create an obj to access top level window.
        try:
            selected_item = self.listBox.curselection()
            print(selected_item)

            person = self.listBox.get(selected_item)
            person_id = person.split(' ')[0]
            print(person_id)
            add_page1 = Update_Friend(person_id)
            # self.destroy()

        except Exception as e:
            messagebox.showerror('Error', str(e))

    def disp_frd(self):
        try:
            selected_item = self.listBox.curselection()

            person = self.listBox.get(selected_item)
            person_id = person.split(' ')[0]

            disp_friend = Display_friends_view(person_id)

        except Exception as e:
            messagebox.showerror('Error', str(e))

    def delete_rec(self):
        selected_rec = self.listBox.curselection()
        print(selected_rec)
        print(selected_rec[0])

        if selected_rec[0] is None:
            print('select val from list')
        else:
            frd = self.listBox.get(selected_rec)
            frd_id = frd.split(' ')[0]
            # print('record to be deleted ' + str(frd_id))
            del_qry = "delete from person where id = {}".format(frd_id)

        # first ask question then delete.  why window disappear, how self.destory is calling itself.

        # answer = messagebox.askquestion('Rec Delete', "Do you want to delete")
        # if answer == 'yes':
        #     try:
        #         cur.execute(del_qry)
        #         conn.commit()
        #         messagebox.showinfo('Success', 'Rec Deleted.. ')
        #         # self.destroy()
        #     except Exception as e:
        #         messagebox.showinfo('Info', str(e))

            try:
                cur.execute(del_qry)
                conn.commit()
                # messagebox.showinfo('Success', 'Rec Deleted.. ')

                self.listBox.delete(0, END)
                friend = cur.execute("select * from person order by 1")
                cnt = 0
                for i in friend:
                    self.listBox.insert(str(cnt), str(i[0]) + ' ' + i[1] + ' ' + i[2])
                    cnt += 1
                # self.listBox.select_set(0)
                # print('cnt is' + str(cnt))
                # self.listBox.select_set(cnt//2)
                # print(cnt)
                try:
                    if cnt >= 8:
                        self.listBox.select_set(4)
                    elif cnt == 0:
                        print('no val select')
                    else:
                        self.listBox.select_set(0)
                except IndexError as e:
                    messagebox(str(e) + 'No Such values is selected.')

            except Exception as e:
                messagebox.showwarning('Warning', str(e))


        self.lebel_rec_deleted = Label(self.bottomFrame, text='Record Deleted', font='arial 11 bold', fg='blue', bg='#7fe3a7')
        self.lebel_rec_deleted.place(x=225, y=210)

        # self.lebel_rec_deleted.grid(row=0, column=2, padx=20, pady=140, sticky=N)


