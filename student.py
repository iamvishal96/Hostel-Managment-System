from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox




class Stu_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System") 
        self.root.geometry("1160x530+200+200")

       #=========================veriables=======================================
        self.var_reg=StringVar()
        x=random.randint(1000,9999)
        self.var_reg.set(str(x))
        
        self.var_Stu_name=StringVar()
        self.var_father=StringVar()
        self.var_gender=StringVar()
        self.var_address=StringVar()
        self.var_mobile=StringVar()
        self.var_pincode=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_email=StringVar()

        # ==========title==========================================
        lbl_title=Label(self.root,text="ADD STUDENT DETAILS",font=("times new roman",18,"bold"),bg="BLACK",fg="gold",bd=2,relief=RIDGE,padx=2)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        
       #=================logo======================================
        img1=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\hostelimg2.png")
        img1=img1.resize((100,50),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)
        
        #========================labelframe============================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=430,height=490)
        
        # ======================labels and entry====================
        # stureg
        lbl_title=Label(labelframeleft,text="Registraion",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_title.grid(row=0,column=0,)

        enty_reg=ttk.Entry(labelframeleft,textvariable=self.var_reg,font=("arial",13,"bold"),width=29)
        enty_reg.grid(row=0,column=1)
        
        #stu name
        sname=Label(labelframeleft,text="Student Name",font=("arial",12,"bold"),padx=2,pady=6)
        sname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_Stu_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)
        
        #fathername
        lblfathername=Label(labelframeleft,text="Father Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblfathername.grid(row=2,column=0,sticky=W)
        txtfathername=ttk.Entry(labelframeleft,textvariable=self.var_father,font=("arial",13,"bold"),width=29)
        txtfathername.grid(row=2,column=1)
        
        #gender combobox
        label_gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",13,"bold"),width=27)
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        
        #======================address====================================================
        lblPostCode=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)
        
        
        #mobilemuber
        lblMobile=Label(labelframeleft,text="Mobile",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)
        
        #pincode
        lblpincode=Label(labelframeleft,text="Pin Code",font=("arial",12,"bold"),padx=2,pady=6)
        lblpincode.grid(row=6,column=0,sticky=W)
        txtpincode=ttk.Entry(labelframeleft,textvariable=self.var_pincode,font=("arial",13,"bold"),width=29)
        txtpincode.grid(row=6,column=1)

        #nationality
        lblNationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        
        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",13,"bold"),width=27)
        combo_Nationality["value"]=("Indian")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

       
        # =============================id proof type combobox==================
        lblIdProof=Label(labelframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Aadhar","X Marksheet","Pan Card")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
      
      # =========================id number=========================================================
        lblIdNumber=Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

       #================== Email====address====================================================
        lblemailAddress=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        lblemailAddress.grid(row=10,column=0,sticky=W)
        txtemailAddress=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtemailAddress.grid(row=10,column=1)
        
        
       

       #========================================btns===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

       
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)

        #=================================table frame search=======================================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Registration")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=1)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="ShowAll",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        # ==================show data Table=========================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)
        
        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Stu_Details_Table=ttk.Treeview(details_table,column=("Registration","name","father","gender","address","mobile","pincode",
                                                                   "nationality","idproof","idnumber","email"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        
        Scroll_x.config(command=self.Stu_Details_Table.xview)
        Scroll_y.config(command=self.Stu_Details_Table.yview)
        
        self.Stu_Details_Table.heading("Registration",text="Registration No")
        self.Stu_Details_Table.heading("name",text="Student Name")
        self.Stu_Details_Table.heading("father",text="Father Name")
        self.Stu_Details_Table.heading("gender",text="Gender")
        self.Stu_Details_Table.heading("address",text="Address")
        self.Stu_Details_Table.heading("mobile",text="Mobile")
        self.Stu_Details_Table.heading("pincode",text="Pin Code")
        self.Stu_Details_Table.heading("nationality",text="Nationality")
        self.Stu_Details_Table.heading("idproof",text="Id Proof")
        self.Stu_Details_Table.heading("idnumber",text="Id Number")
        self.Stu_Details_Table.heading("email",text="Email")
        
        

        
        self.Stu_Details_Table["show"]="headings"

        
        self.Stu_Details_Table.column("Registration",width=100)
        self.Stu_Details_Table.column("name",width=100)
        self.Stu_Details_Table.column("father",width=100)
        self.Stu_Details_Table.column("gender",width=100)
        self.Stu_Details_Table.column("address",width=100)
        self.Stu_Details_Table.column("mobile",width=100)
        self.Stu_Details_Table.column("pincode",width=100)
        self.Stu_Details_Table.column("nationality",width=100)
        self.Stu_Details_Table.column("idproof",width=100)
        self.Stu_Details_Table.column("idnumber",width=100)
        self.Stu_Details_Table.column("email",width=100)
        
        self.Stu_Details_Table.pack(fill=BOTH,expand=1)
        self.Stu_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_father.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_reg.get(),
                                                                                self.var_Stu_name.get(),
                                                                                self.var_father.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_address.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_pincode.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_idproof.get(),
                                                                                self.var_idnumber.get(),
                                                                                self.var_email.get()
                                                                            ))
                                                                            
                conn.commit()
                self.fetch_data()
                conn.close()                                                              
                messagebox.showinfo("Success","student has been added",parent=self.root) 
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from student")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Stu_Details_Table.delete(*self.Stu_Details_Table.get_children())
            for i in rows:
                self.Stu_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()

    def get_cuersor(self,event=""):
        cusrsor_row=self.Stu_Details_Table.focus()
        content=self.Stu_Details_Table.item(cusrsor_row)   
        row=content["values"]   

        self.var_reg.set(row[0]),
        self.var_Stu_name.set(row[1]),
        self.var_father.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_address.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_pincode.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_email.set(row[10])
            
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Plesae enter mobile number",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
           my_cursor=conn.cursor() 
           my_cursor.execute("update student set Name=%s,Father=%s,Gender=%s,Address=%s,Mobile=%s,Pincode=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Email=%s where Registration=%s",(
                                                                                                                                                                                     
                                                                                                                                                                self.var_Stu_name.get(),
                                                                                                                                                                self.var_father.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_pincode.get(),
                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                self.var_idproof.get(),
                                                                                                                                                                self.var_idnumber.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_reg.get()
                                                                                                                                                            ))                          
           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("Update,Student details has been updated successfully",parent=self.root)                                                              

                                                                                                                                                                                                                                                          
    def mDelete(self):
        mDelete=messagebox.askyesno("Hostel Management System","Do you want to delete this student",parent=self.root) 
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
            my_cursor=conn.cursor()
            query="delete from student where Registration=%s"
            value=(self.var_reg.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_Stu_name.set(""),
        self.var_father.set(""),
        #self.var_gender.set(""),
        self.var_address.set(""),
        self.var_mobile.set(""),
        self.var_pincode.set(""),
        #self.var_nationality.set(""),
        #self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_email.set(""),


        x=random.randint(1000,9999)
        self.var_reg.set(str(x))


    
    
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student where"+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Stu_Details_Table.delete(*self.Stu_Details_Table.get_chlidren())
            for i in rows:
             self.Stu_Details_Table.insert("",END,values=i)
            conn.commit()    
        conn.close()       






if __name__=="__main__":
     root=Tk()
     obj=Stu_Win(root)
     root.mainloop()


       