from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
         self.root=root
         self.root.title("Hostel Management System")
         self.root.geometry("1160x530+200+200")

         # ====================variables============================
         self.var_contact=StringVar()
         self.var_joinDate=StringVar()
         self.var_checkoutDate=StringVar()
         self.var_studType=StringVar()
         self.var_BlockName=StringVar()
         self.var_Year=StringVar()
         self.var_Roomtype=StringVar()
         self.var_RoomNo=StringVar()
         self.var_MesscardType=StringVar()
         self.var_paidAmount=StringVar()
       
         # ==========title==========================================
         lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="BLACK",fg="gold",bd=2,relief=RIDGE,padx=2)
         lbl_title.place(x=0,y=0,width=1295,height=50)
        
         #=================logo======================================
         img1=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\hostelimg2.png")
         img1=img1.resize((100,50),Image.ANTIALIAS)
         self.photoimg1=ImageTk.PhotoImage(img1)
        
         lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
         lblimg.place(x=0,y=0,width=100,height=50) 

         #========================labelframe============================
         labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM DETAILS",font=("times new roman",12,"bold"))
         labelframeleft.place(x=5,y=50,width=430,height=490)

         # ======================labels and entry================

        
         #Student contact
         lbl_stud_contact=Label(labelframeleft,text="Student Contact",font=("arial",12,"bold"),padx=2,pady=6)
         lbl_stud_contact.grid(row=0,column=0,sticky=W)

         enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
         enty_contact.grid(row=0,column=1,sticky=W)
        
         #Fetch the Data
         btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
         btnFetchData.place(x=347,y=4)

         #Join Date
         joinDate=Label(labelframeleft,text="Join Date",font=("arial",12,"bold"),padx=2,pady=6)
         joinDate.grid(row=1,column=0,sticky=W)
         txtjoinDate=ttk.Entry(labelframeleft,textvariable=self.var_joinDate,font=("arial",13,"bold"),width=29)
         txtjoinDate.grid(row=1,column=1)

         #Checkout Date
         checkoutDate=Label(labelframeleft,text="Checkout Date",font=("arial",12,"bold"),padx=2,pady=6)
         checkoutDate.grid(row=2,column=0,sticky=W)
         checkoutDate=ttk.Entry(labelframeleft,textvariable=self.var_checkoutDate,font=("arial",13,"bold"),width=29)
         checkoutDate.grid(row=2,column=1)

         #Student type      
         label_studType=Label(labelframeleft,text="Student Type:",font=("arial",12,"bold"),padx=2,pady=6)
         label_studType.grid(row=3,column=0,sticky=W)

         combo_studType=ttk.Combobox(labelframeleft,textvariable=self.var_studType,font=("arial",13,"bold"),width=27,state="readonly")
         combo_studType["value"]=("Select","B.tech","B.C.A","B.B.A","B.D.S","B.Pharma","Nursing")
         combo_studType.current(0)
         combo_studType.grid(row=3,column=1)

         #Block Name
         label_BlockName=Label(labelframeleft,text="Block Name",font=("arial",12,"bold"),padx=2,pady=6)
         label_BlockName.grid(row=4,column=0,sticky=W)

         combo_BlockName=ttk.Combobox(labelframeleft,textvariable=self.var_BlockName,font=("arial",13,"bold"),width=27,state="readonly")
         combo_BlockName["value"]=("Select","R.N.Tagore Boy's Hostel","Arybhatt Boy's hostel","Sarojini Naidu Girl's Hostel")
         combo_BlockName.current(0)
         combo_BlockName.grid(row=4,column=1) 

         #Year
         label_year=Label(labelframeleft,text="Course of Year",font=("arial",12,"bold"),padx=2,pady=6)
         label_year.grid(row=5,column=0,sticky=W)

         combo_year=ttk.Combobox(labelframeleft,textvariable=self.var_Year,font=("arial",13,"bold"),width=27,state="readonly")
         combo_year["value"]=("Select","First Year","Second Year","Third Year","Fourth Year","Fifth Year")
         combo_year.current(0)
         combo_year.grid(row=5,column=1)
 
         #Room type
         label_Roomtype=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
         label_Roomtype.grid(row=6,column=0,sticky=W)
         
         conn=mysql.connector.connect (host="localhost", username="root", password="Vishal@123", database="student")
         my_cursor=conn.cursor()
         my_cursor.execute("select RoomType from details")
         ide=my_cursor.fetchall()
         
         

         combo_Roomtype=ttk.Combobox(labelframeleft,textvariable= self.var_Roomtype,font=("arial",13,"bold"),width=27,state="readonly")
         combo_Roomtype["value"]=ide
         combo_Roomtype.current(0)
         combo_Roomtype.grid(row=6,column=1)   

         #Room Number
         lblRoomNo=Label(labelframeleft,text="Room Number",font=("arial",12,"bold"),padx=2,pady=6)
         lblRoomNo.grid(row=7,column=0,sticky=W)
         #txtRoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,font=("arial",13,"bold"),width=29)
         #txtRoomNo.grid(row=7,column=1)
         
         conn=mysql.connector.connect (host="localhost", username="root", password="Vishal@123", database="student")
         my_cursor=conn.cursor()
         my_cursor.execute("select roomNO from details")
         rows=my_cursor.fetchall()
         
         combo_RoomtNo=ttk.Combobox(labelframeleft,textvariable= self.var_RoomNo,font=("arial",13,"bold"),width=27,state="readonly")
         combo_RoomtNo["value"]=rows
         combo_RoomtNo.current(0)
         combo_RoomtNo.grid(row=7,column=1)   



         #Messcard Type
         label_MesscardType=Label(labelframeleft,text="Messcard Type:",font=("arial",12,"bold"),padx=2,pady=6)
         label_MesscardType.grid(row=8,column=0,sticky=W)

         combo_MesscardType=ttk.Combobox(labelframeleft,textvariable= self.var_MesscardType,font=("arial",13,"bold"),width=27,state="readonly")
         combo_MesscardType["value"]=("Select","(Lunch + Breakfast + Dinner)","(Lunch + Dinner)")
         combo_MesscardType.current(0)
         combo_MesscardType.grid(row=8,column=1)

         #Paid Amount
         lblpaidAmount=Label(labelframeleft,text="Paid Amount",font=("arial",12,"bold"),padx=2,pady=6)
         lblpaidAmount.grid(row=9,column=0,sticky=W)
         txtpaidAmount=ttk.Entry(labelframeleft,textvariable=self.var_paidAmount ,font=("arial",13,"bold"),width=29)
         txtpaidAmount.grid(row=9,column=1)
 
         #======================Total==========================================================
         
         btnTotal=Button(labelframeleft,text="Total",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
         btnTotal.grid(row=10,column=0,padx=1,sticky=W)
 
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
 
         #==============================Rightside image=====================================
         img2=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\room2.jpg")
         img2=img2.resize((550,260),Image.ANTIALIAS)
         self.photoimg2=ImageTk.PhotoImage(img2)
         
         lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
         lblimg.place(x=940,y=52,width=250,height=254)

         img3=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\room1.jpg")
         img3=img3.resize((550,260),Image.ANTIALIAS)
         self.photoimg3=ImageTk.PhotoImage(img3)
         
         lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
         lblimg.place(x=440,y=52,width=250,height=254)
 
         #=================================table frame=======================================
 
         Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIew Details And Search System",font=("arial",12,"bold"))
         Table_Frame.place(x=435,y=280,width=860,height=260)
 
         lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
         lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
 
         combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
         combo_Search["value"]=("Contact","Room")
         combo_Search.current(0)
         combo_Search.grid(row=0,column=1,padx=2)
 
         txtSearch=ttk.Entry(Table_Frame,font=("arial",13,"bold"),width=24)
         txtSearch.grid(row=0,column=2,padx=2)
 
         btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
         btnSearch.grid(row=0,column=3,padx=1)
 
         btnShowAll=Button(Table_Frame,text="ShowAll",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
         btnShowAll.grid(row=0,column=4,padx=1)
 
          # ==================show data Table=========================
 
         details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
         details_table.place(x=0,y=50,width=860,height=180)
         
         Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
         Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
         
         self.room_Table=ttk.Treeview(details_table,column=("Contact","joinDate","checkoutDate","studType","BlockName","Year","Roomtype","RoomNo"
                                                                                   ),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
         Scroll_x.pack(side=BOTTOM,fill=X)
         Scroll_y.pack(side=RIGHT,fill=Y)
         
         Scroll_x.config(command=self.room_Table.xview)
         Scroll_y.config(command=self.room_Table.yview)
        
         self.room_Table.heading("Contact",text="Student Contact")
         self.room_Table.heading("joinDate",text="Join Date")
         self.room_Table.heading("checkoutDate",text="Checkout Date")
         self.room_Table.heading("studType",text="Student Type")
         self.room_Table.heading("BlockName",text="Block Name")
         self.room_Table.heading("Year",text="Course of Year")
         self.room_Table.heading("Roomtype",text="Room Type")
         self.room_Table.heading("RoomNo",text="Room Number")
         
            
         self.room_Table["show"]="headings"
 
         self.room_Table.column("Contact",width=100)
         self.room_Table.column("joinDate",width=100)
         self.room_Table.column("checkoutDate",width=100)
         self.room_Table.column("studType",width=100)
         self.room_Table.column("BlockName",width=100)
         self.room_Table.column("Year",width=100)
         self.room_Table.column("Roomtype",width=100)
         self.room_Table.column("RoomNo",width=100)
      
        
         self.room_Table.pack(fill=BOTH,expand=1)

         self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
         self.fetch_data()

    # add data     
    def add_data(self):
         if self.var_contact.get()=="" or self.var_joinDate.get()=="":
                  messagebox.showerror("Error","All fields are requaired",parent=self.root)
         else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                           self.var_contact.get(),
                                                                           self.var_joinDate.get(),
                                                                           self.var_checkoutDate.get(),
                                                                           self.var_studType.get(),
                                                                           self.var_BlockName.get(),
                                                                           self.var_Year.get(),
                                                                           self.var_Roomtype.get(),
                                                                           self.var_RoomNo.get()

                                                                        ))
               conn.commit()
               self.fetch_data()
               conn.close()                                                              
               messagebox.showinfo("Success","Room Booked",parent=self.root) 
            except Exception as es:
                  messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
               conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
               my_cursor=conn.cursor() 
               my_cursor.execute("select * from room")
               rows=my_cursor.fetchall()
               if len(rows)!=0:
                     self.room_Table.delete(*self.room_Table.get_children())
                     for i in rows:
                        self.room_Table.insert("",END,values=i)
                        conn.commit()
                        conn.close()
                         
    #get cursor
    def get_cursor(self,event=""):
            curssor_row=self.room_Table.focus()
            content=self.room_Table.item(curssor_row)   
            row=content["values"] 

            self.var_contact.set(row[0]),
            self.var_joinDate.set(row[1]),
            self.var_checkoutDate.set(row[2]),
            self.var_studType.set(row[3]),
            self.var_BlockName.set(row[4]),
            self.var_Year.set(row[5]),
            self.var_Roomtype.set(row[6]),
            self.var_RoomNo.set(row[7])  


    #update function
    def update(self):
       if self.var_contact.get()=="":
        messagebox.showerror("Error","Plesae enter mobile number",parent=self.root)
       else:
        conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
        my_cursor=conn.cursor() 
        my_cursor.execute("update room set joinDate=%s,checkoutDate=%s,studType=%s,BlockName=%s,Year=%s,Roomtype=%s,RoomNo=%s where Contact=%s",(
                                                                                                                                                                                     
                                                                                                                                         self.var_joinDate.get(),
                                                                                                                                         self.var_checkoutDate.get(),
                                                                                                                                         self.var_studType.get(),
                                                                                                                                         self.var_BlockName.get(),
                                                                                                                                         self.var_Year.get(),
                                                                                                                                         self.var_Roomtype.get(),
                                                                                                                                         self.var_RoomNo.get(),
                                                                                                                                         self.var_contact.get()

                                                                                                                                      ))                          
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update,Room details has been updated successively",parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Hostel Management System","Do you want to delete this student",parent=self.root) 
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
            conn.commit()
            self.fetch_data()
            conn.close() 
    #rest data 
    def reset(self):
        self.var_contact.set(""),
        self.var_joinDate.set(""),
        self.var_studType.set(""),
        self.var_BlockName.set(""),
        self.var_Roomtype.set(""),
        self.var_RoomNo.set(""),
        self.var_MesscardType.set(""),


    # ====================== All data Fetch =====================   
    def Fetch_contact(self):
      if self.var_contact.get()=="":
       messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
      else:
         conn=mysql.connector.connect(host="localhost", username="root", password="Vishal@123",database="student")
         my_cursor=conn.cursor()
         query=("select Name from student where Mobile=%s")
         value=(self.var_contact.get(),)
         my_cursor.execute(query, value)
         row=my_cursor.fetchone()

      if row==None:
         messagebox.showerror("Error","This number Not Found",parent=self.root)
      else:
           conn.commit()
           conn.close()

           showDataframe=Frame(self.root, bd=4, relief=RIDGE, padx=2)
           showDataframe.place(x=690,y=50,width=250,height=235)

           lblName=Label(showDataframe, text="Name:",font=("arial", 12, "bold"))
           lblName.place(x=0,y=0)

           lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl.place(x=90,y=0)
              
           #====================Gender=========================   
           conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
           my_cursor=conn.cursor()
           query=("select Gender from student where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query, value)
           row=my_cursor.fetchone()

           lblGender=Label(showDataframe, text="Gender:",font=("arial", 12, "bold"))
           lblGender.place(x=0,y=30)

           lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl2.place(x=90,y=30)

           #=======================email============================ 
           conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
           my_cursor=conn.cursor()
           query=("select Email from student where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query, value)
           row=my_cursor.fetchone()

           lblemail=Label(showDataframe, text="Email:",font=("arial", 12, "bold"))
           lblemail.place(x=0,y=60)

           lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl2.place(x=90,y=60)

           #=====================Nationality=========================
           conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
           my_cursor=conn.cursor()
           query=("select Nationality from student where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query, value)
           row=my_cursor.fetchone()

           lblNationality=Label(showDataframe, text="Nationality:",font=("arial", 12, "bold"))
           lblNationality.place(x=0,y=90)

           lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl2.place(x=90,y=90)
           
           #=================Address====================================
           conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
           my_cursor=conn.cursor()
           query=("select Address from student where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query, value)
           row=my_cursor.fetchone()

           lbladdress=Label(showDataframe, text="Address:",font=("arial", 12, "bold"))
           lbladdress.place(x=0,y=120)

           lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl2.place(x=90,y=120)

    #search data
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student where"+str(self.search_var.get())+"LIKE'%"+str(self.text_search.get())+"%s'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_Table.delete(*self.room_Table.get_chlidren())
            for i in rows:
             self.room_Table.insert("",END,values=i)
             conn.commit()    
             conn.close()       

    def total(self):
          if(self.var_MesscardType.get()=="(Lunch + Breakfast + Dinner)" and self.var_Roomtype=="Single"):
            q1=int(36000)
            q2=int(32000)
            q3=(q1+q2)
            TT="Rs."+str("q3")
            self.var_paidAmount(TT)


          elif(self.var_MesscardType.get()=="(Lunch + Dinner)" and self.var_Roomtype=="Single"):
            q1=int(30000)
            q2=int(32000)
            q3=(q1+q2)
            TT="Rs."+str("q3")
            self.var_paidAmount(TT)

          elif(self.var_MesscardType.get()=="(Lunch + Breakfast + Dinner)" and self.var_Roomtype=="Double"):
            q1=int(36000)
            q2=int(24000)
            q3=(q1+q2)
            TT="Rs."+str("q3")
            self.var_paidAmount(TT)

          elif(self.var_MesscardType.get()=="(Lunch + Dinner)" and self.var_Roomtype=="Double"):
            q1=int(30000)
            q2=int(24000)
            q3=int(q1+q2)
            TT="Rs."+str("q3")
            self.var_paidAmount(TT)




if __name__ == "__main__":
        root=Tk()
        obj=Roombooking(root)
        root.mainloop()