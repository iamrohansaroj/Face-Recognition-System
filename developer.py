from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1270,height=35)

        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1270,590),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1270,height=590)
        
        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=420,height=500)
        
        img_top1=Image.open(r"college_images\20211230_202153.jpg")
        img_top1=img_top1.resize((170,170),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=220,y=0,width=170,height=170)
        
        # Developer info
        dev_label=Label(main_frame,text="Hello my name is Rohan",font=("times new roman",14,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="I am full stack developer",font=("times new roman",14,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=30)
        
        
        img2=Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((400,330),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=180,width=400,height=330)


    
    
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
