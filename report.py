from tkinter import*
from PIL import Image, ImageTk 
from tkinter import ttk



class help:
    def __init__(self,root):
         self.root=root
         self.root.title("Help and Desk")
         self.root.geometry("1160x530+200+200")
         
        # ==========title==========================================
         lbl_title=Label(self.root,text="HELP AND DESK",font=("times new roman",18,"bold"),bg="BLACK",fg="gold",bd=2,relief=RIDGE,padx=2)
         lbl_title.place(x=0,y=0,width=1295,height=50)
         
         ######### image #########################
         img1=Image.open(r"C:\Users\DD\Desktop\Hostel_Management_System\Maharana_Pratap_image\help.png")
         img1=img1.resize((761,485),Image.ANTIALIAS)
         self.photoimg1=ImageTk.PhotoImage(img1)
         
         lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
         lblimg.place(x=0,y=50,width=761,height=485)
        
        
         
         
         
         
         
if __name__=="__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()
         
