from tkinter import*
from PIL import Image,ImageTk
from student import Stu_Win
from room import Roombooking
from details import DeatailsRoom
from report import help
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
    
if __name__ == "__main__":
        root=Tk()
        obj=HostelManagementSystem(root)
        root.mainloop()