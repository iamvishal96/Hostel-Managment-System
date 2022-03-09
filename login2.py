from atexit import register
from cProfile import label
from pdb import lasti2lineno
from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk 
from tkinter import messagebox
from front import HostelManagementSystem
from student import Stu_Win
from room import Roombooking
from details import DeatailsRoom
from report import help


from numpy import row_stack  

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login") 
        self.root.geometry("1550x800+0+0")
        

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\login_1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=80,width=340,height=450)

        img1=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\login_2.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=569,y=82,width=100,height=100)

        get_str=Label(frame,text="Get Login",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        # ==================Icon Images====================
        img2=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\login_3.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=494,y=234,width=25,height=25)

        img3=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\login_4.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=494,y=303,width=25,height=25)
        
        #LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registration
        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=5,y=360,width=160)

        #forgetpassbtn
        forgetpassbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        forgetpassbtn.place(x=20,y=380,width=120)
    
    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")

        elif self.txtuser.get()=="vishal@gmail.com"and self.txtpass.get()=="123":
           messagebox.showinfo("Success","Welcome to Hostel Management System")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                self.txtuser.get(),
                                                                                self.txtpass.get()
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HostelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return    
                conn.commit()
                conn.close()

    #=========================reset password===========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
            my_cursor=conn.cursor()
            qury=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,please login new password",parent=self.root2)
                self.root2.destroy()


    #=======================forget password============================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")

        else:
        
            conn=mysql.connector.connect(host="localhost",username="root",password="Vishal@123",database="student")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            
            if row==None:
                messagebox.showerror("My Error","please enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+450+80")
                
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="red",activebackground="white")
                l.place(x=0,y=10,relwidth=1) 
                
                security_Q=Label(self.root2,text=" Select Security Questions",font=("times  new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Favourite food ","Your Pat Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                security_A=Label(self.root2,text="Security Answer",font=("times  new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times  new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)




               
                
            
        
    
                
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
        b1=Button(frame,image=self.photoimage2,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
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

    def return_login(self):
        self.root.destroy()




class HostelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1550x800+0+0")
        
        
        # =============================1stlogo============================================
        img1=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\hostel2.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        #===================== right================================
        img2=Image.open(r"C:\\Users\\DD\\Desktop\\Hostel_Management_System\\Maharana_Pratap_image\\hostelimg2.png")
        img2=img2.resize((210,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=210,height=140)
        
        # ==========title==========================================
        lbl_title=Label(self.root,text="HOSTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="blue",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=130,width=1400,height=60)
        
        # =====================main frame=================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1500,height=550)
        
        # ================================================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",18,"bold"),bg="red",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        
        #=====================button frame =============================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=198)
        
        stu_btn=Button(btn_frame,text="STUDENT",command=self.Stu_details,width=22,font=("times new roman",14,"bold"),bg="blue",fg="gold",bd=0,cursor="hand1")
        stu_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="blue",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
    
        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="blue",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="HELP",command=self.help,width=22,font=("times new roman",14,"bold"),bg="blue",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="blue",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        
        # ================right side image ====================
        img3=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\hostel3.jpg")
        img3=img3.resize((1100,490),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=250,y=0,width=1100,height=490)
    
    
    
    
    def Stu_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Stu_Win(self.new_window)
        
        
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DeatailsRoom(self.new_window)
    
    
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)

    def logout(self):
        self.root.destroy()  
    
    
if __name__=="__main__":
      main()