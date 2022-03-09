from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk 
from tkinter import messagebox  


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
        registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=5,y=360,width=160)

        #forgetpassbtn
        forgetpassbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        forgetpassbtn.place(x=20,y=380,width=120)
    
    
    
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")

        elif self.txtuser.get()=="Shivam"and self.txtpass.get()=="@123":
           messagebox.showinfo("Success","Welcome to Hostel Management System")

        else:
            messagebox.showerror("Invalid","Invalid username&password")   
        




if __name__=="__main__":
      root=Tk()
      obj=Login_Window(root)
      root.mainloop()