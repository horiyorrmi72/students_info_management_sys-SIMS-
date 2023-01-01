from ast import Delete
from cgitb import text
from importlib.metadata import PathDistribution
from msilib import Table
from sqlite3 import PARSE_DECLTYPES
from tkinter import *
from tokenize import String
from turtle import bgcolor, title
from tkinter import ttk
from mysqlx import Row
import pymysql
from tkinter import messagebox



class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Stundent Information Management System")
        self.root.geometry('1366x768+0+0')

        title = Label(self.root, text="Student Information Management System", bd=10,
                      relief=GROOVE, font=("times new roman", 40, "bold"), bg='yellow', fg='red')
        title.pack(side=TOP, fill=X)

        author = Label(self.root, text='Author: Yusuf Ridwan - Matric No:F/HD/20/3410018 \t\t\t\t\t #horla_tech',
                       bd=2, relief=GROOVE, font=('times new roman', 15, 'bold'), bg='yellow', fg='red')
        author.pack(side=BOTTOM, fill=X)

        #============= Variables ============
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.sex_var = StringVar()
        self.phone_var = StringVar()
        self.dob_var = StringVar()
        self.department_var = StringVar()
        self.matric_no_var = StringVar()
        self.falcuty_var = StringVar()

        self.search_by = StringVar()
        self.search_txt=StringVar()
        
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='crimson')
        Manage_Frame.place(x=20, y=98, width=450, height=560)

        m_title = Label(Manage_Frame, text='Manage Students', bg='crimson',
                        fg='white', font=('times new roman', 20, 'bold'))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text='Roll No/ID', bg='crimson',
                         fg='white', font=('times new roman', 10, 'bold'))
        lbl_roll.grid(row=1, column=0, pady=5, padx=10, sticky='w')

        txt_roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=2, pady=5, padx=10, sticky='w')
#------------------------========================name=============================------------------------------------
        lbl_name = Label(Manage_Frame, text='Name', bg='crimson',
                         fg='white', font=('times new roman', 10, 'bold'))
        lbl_name.grid(row=2, column=0, pady=5, padx=10, sticky='w')

        name_roll = Entry(Manage_Frame, textvariable=self.name_var, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        name_roll.grid(row=2, column=2, pady=5, padx=10, sticky='w')
#------------=========================email===========================================--------------------------
        lbl_email = Label(Manage_Frame, text='Email', bg='crimson',
                          fg='white', font=('times new roman', 10, 'bold'))
        lbl_email.grid(row=3, column=0, pady=5, padx=10, sticky='w')

        email_roll = Entry(Manage_Frame, textvariable=self.email_var, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        email_roll.grid(row=3, column=2, pady=5, padx=10, sticky='w')
#-------------==========================-matric number================================-----------------
        lbl_matric = Label(Manage_Frame, text='Matric No', bg='crimson',
                           fg='white', font=('times new roman', 10, 'bold'))
        lbl_matric.grid(row=4, column=0, pady=5, padx=10, sticky='w')

        matric_no = Entry(Manage_Frame,textvariable=self.matric_no_var, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        matric_no.grid(row=4, column=2, pady=5, padx=10, sticky='w')
 #-------------===========================sex/Gender======================================------------------
        lbl_sex = Label(Manage_Frame, text='Sex', bg='crimson',
                        fg='white', font=('times new roman', 10, 'bold'))
        lbl_sex.grid(row=5, column=0, pady=5, padx=10, sticky='w')

        combo_sex = ttk.Combobox(Manage_Frame, textvariable=self.sex_var, font=(
            'times new roman', 10, 'bold'), state='readonly')
        combo_sex['values'] = ('Male', 'Female', 'Others')
        combo_sex.grid(row=5, column=2, pady=5, padx=10, sticky='w')
#---------------=========================-date of birth=====================================---------------
        lbl_DOB = Label(Manage_Frame, text='D.O.B', bg='crimson',
                        fg='white', font=('times new roman', 10, 'bold'))
        lbl_DOB.grid(row=6, column=0, pady=5, padx=10, sticky='w')

        DOB_roll = Entry(Manage_Frame, textvariable=self.dob_var, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        DOB_roll.grid(row=6, column=2, pady=5, padx=10, sticky='w')
#-----------===============================Faculty============================================------------------
        lbl_faculty = Label(Manage_Frame, text='Faculty', bg='crimson',
                            fg='white', font=('times new roman', 10, 'bold'))
        lbl_faculty.grid(row=7, column=0, pady=5, padx=10, sticky='w')

        faculty_roll = Entry(Manage_Frame,textvariable=self.falcuty_var, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        faculty_roll.grid(row=7, column=2, pady=5, padx=10, sticky='w')

        # ====================-Department ---==============================================================
        lbl_department = Label(Manage_Frame, text='Department', bg='crimson',
                               fg='white', font=('times new roman', 10, 'bold'))
        lbl_department.grid(row=8, column=0, pady=5, padx=10, sticky='w')

        self.department_roll = Entry(Manage_Frame, textvariable=self.department_var, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        self.department_roll.grid(row=8, column=2, pady=5, padx=10, sticky='w')
 #--------------=============================phone number============================================-------------
        lbl_phone_no = Label(Manage_Frame, text='Phone No', bg='crimson',
                          fg='white', font=('times new roman', 10, 'bold'))
        lbl_phone_no.grid(row=9, column=0, pady=5, padx=10, sticky='w')

        phone_no = Entry(Manage_Frame,textvariable=self.phone_var, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        phone_no.grid(row=9, column=2, pady=5, padx=10, sticky='w')
 #------------=================================Address==================================================--------------
        lbl_address = Label(Manage_Frame, text='Address', bg='crimson',
                            fg='white', font=('times new roman', 10, 'bold'))
        lbl_address.grid(row=10, column=0, pady=5, padx=10, sticky='w')

        self.txt_address = Text(Manage_Frame, width=20, height=4, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        self.txt_address.grid(row=10, column=2, pady=5, padx=10, sticky='w')

#----------==================================   Action Buttons frame ==========================------------------------
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg='crimson')
        btn_Frame.place(x=15, y=500, width=420)

        Addbtn = Button(btn_Frame, text='Add', width=10, command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
        Updatebtn = Button(btn_Frame, text='Update', width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text='Clear', width=10, command=self.clear).grid(row=0, column=2, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text='Delete', width=10,command=self.delete_data).grid(row=0, column=3, padx=10, pady=10)
#============================================  end of manage frame  =====================================================


#-----##########################-----   detail frame  ----------------########################################----
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg='crimson')
        detail_frame.place(x=500, y=98, width=800, height=580)

        lbl_search = Label(detail_frame, text='Search By', bg='crimson',
                           fg='white', font=('times new roman', 20, 'bold'))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        combo_search = ttk.Combobox(detail_frame,textvariable=self.search_by,font=(
            'times new roman', 10, 'bold'), state='readonly')
        combo_search['values'] = ('Name', 'Contact', 'id','matric_no')
        combo_search.grid(row=0, column=1, pady=5, padx=10, sticky='w')

        txt_search = Entry(detail_frame,textvariable=self.search_txt, width=15, font=(
            'times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=10, sticky='w')

        search_btn = Button(detail_frame, text='Search', width=10,command=self.search_data).grid(
            row=0, column=3, padx=10, pady=10)
        showAll_btn = Button(detail_frame, text='Show All', width=10,command=self.fetch_data).grid(
            row=0, column=4, pady=10, padx=10)

        #===============---- Table Frame==========
        Table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg='crimson')
        Table_frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_frame, columns=('roll', 'name', 'email', 'matric', 'sex', 'DOB','faculty','department', 'phone', 'address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading('roll', text='Roll No/ID')
        self.Student_table.heading('name', text='NAME')
        self.Student_table.heading('email', text='Email')
        self.Student_table.heading('matric', text='Matric No')
        self.Student_table.heading('sex', text='Sex')
        self.Student_table.heading('DOB', text='D.O.B')
        self.Student_table.heading('faculty', text='Faculty')
        self.Student_table.heading('department', text='Department')
        self.Student_table.heading('phone', text='Phone No')
        self.Student_table.heading('address', text='Address')
        self.Student_table['show'] = 'headings'
        self.Student_table.column('roll', width=100)
        self.Student_table.column('name', width=100)
        self.Student_table.column('email', width=100)
        self.Student_table.column('matric', width=100)
        self.Student_table.column('sex', width=100)
        self.Student_table.column('DOB', width=100)
        self.Student_table.column('faculty', width=100)
        self.Student_table.column('department', width=100)
        self.Student_table.column('phone', width=100)
        self.Student_table.column('address', width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_students(self):
        if self.Roll_No_var.get()==""or self.name_var.get()=="":
            messagebox.showerror('Error', 'All fields are required so fill !')
        else:
            con = pymysql.connect(host='127.0.0.1', user='root',password='Princekid426', database='sims')
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
            self.name_var.get(),
            self.email_var.get(),
            self.matric_no_var.get(),
            self.sex_var.get(),
            self.dob_var.get(),
            self.falcuty_var.get(),
            self.department_var.get(),
            self.phone_var.get(),
            self.txt_address.get('1.0', END)
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo('Success', 'Recorded successfully')

    def fetch_data(self):
        con = pymysql.connect(host='127.0.0.1', user='root',password='Princekid426', database='sims')
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                con.commit()

        con.close()
        
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.sex_var.set("")
        self.dob_var.set("")
        self.department_var.set("")
        self.falcuty_var.set("")
        self.phone_var.set("")
        self.matric_no_var.set("")
        self.txt_address.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.matric_no_var.set(row[3])
        self.sex_var.set(row[4])
        self.dob_var.set(row[5])
        self.department_var.set(row[6])
        self.falcuty_var.set(row[7])
        self.phone_var.set(row[8])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[9])
        # print(row)
        # con = pymysql.connect(host='127.0.0.1', user='root',password='Princekid426', database='sims')
        # cur = con.cursor()
        # cur.execute("select * from students where id=%s",self)
        # rows=cur.fetchall()
        # if len(rows)!=0:
        #     self.Student_table.delete(*self.Student_table.get_children())
        #     for row in rows:
        #         self.Student_table.insert('',END,values=row)
        #         con.commit()

        # con.close()
    
    def update_data(self):
        con=pymysql.connect(host="127.0.0.1",user="root",password='Princekid426',database='sims')
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,matric_no=%s,sex=%s,dob=%s,faculty=%s,department=%s,phone=%s,address=%s where id=%s",(
        self.name_var.get(),
        self.email_var.get(),
        self.matric_no_var.get(),
        self.sex_var.get(),
        self.dob_var.get(),
        self.falcuty_var.get(),
        self.department_var.get(),
        self.phone_var.get(),
        self.txt_address.get('1.0', END),
        self.Roll_No_var.get()

        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo('Updated','Data Updated Successfully')
    def delete_data(self):
        con = pymysql.connect(host='127.0.0.1', user='root',password='Princekid426', database='sims')
        cur = con.cursor()
        cur.execute("delete from students where id=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host='127.0.0.1', user='root',password='Princekid426', database='sims')
        cur = con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                con.commit()

        con.close()

root = Tk()
ob = Student(root)
root.mainloop()
