from tkinter import*
from tkinter import ttk
import mysql.connector
from PIL import Image,ImageTk
from tkinter import  messagebox




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register") 
        self.root.geometry("1600x900+0+0")

    #=============veraible======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        


        #  =========bg image=========
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\reg_1.jpeg" )        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #  =========left image=========
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\reg_3.jpeg")      
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=60,y=100,width=380,height=450)

        #===============main frame========
        frame=Frame(self.root,bg="white")
        frame.place(x=400,y=100,width=800,height=450)

        register_lbl=Label(frame,text="WELCOME REGISTER HERE",font=("times new roman",20,"bold"),fg="violet",bg="white")
        register_lbl.place(x=20,y=20)

        #========== label and entry=============

        #----------------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=70)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=100,width=250)

        l_name=Label(frame,text="Last Name", font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=70)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15))
        self.txt_lname.place(x=370,y=100,width=250)

        #----------------row2

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=140)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_email.place(x=50,y=170,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=140)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=170,width=250)

        #------------------row3

        security_Q=Label(frame,text=" Select Security Questions",font=("times  new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=210)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Favourite food ","Your Pat Name")
        self.combo_security_Q.place(x=50,y=240,width=250)
        self.combo_security_Q.current(0)




        security_A=Label(frame,text="Security Answer",textvariable=self.var_securityA,font=("times  new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=210)

        self.text_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.text_security.place(x=370,y=240,width=250)


        #-------------------row4

        pswd=Label(frame,text="Password", font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=280)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=310,width=250)

        confirm_pswd=Label(frame,text="Confirm Paasword",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=280)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=310,width=250)

        #===================check button==============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=340)

        #===============buttons=============
        img1=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\reg_4.jpeg")     
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=10,y=380,width=200)

        img2=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\reg_5.jpeg")     
        img2=img2.resize((200,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimage2,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=330,y=380,width=200)

    #============function decleartion=========================
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password Must Be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")  
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
            my_cursor=conn.cursor()
            query="select * from register where email=%s"
            value=(self.var_email.get(),)
            row=my_cursor.execute(query,value)
            my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_email.get(),
                                                                                self.var_securityQ.get(),
                                                                                self.var_securityA.get(),
                                                                                self.var_pass.get()
                                                                            ))
                conn.commit()
                conn.close()                                                              
                messagebox.showinfo("Success","Register Seccessfully") 
            
                                                                                
                    
            





if __name__=="__main__":
     root=Tk()
     obj=Register(root)
     root.mainloop()
