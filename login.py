from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from tkinter import messagebox
import mysql.connector


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1270x700+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Rohan\OneDrive\Desktop\face_recognition_system\college_images\hackers2.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=540,y=150,width=270,height=380)
        
        img1=Image.open(r"C:\Users\Rohan\OneDrive\Desktop\face_recognition_system\college_images\LoginIconAppl.png")
        img1=img1.resize((70,70),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=647,y=155,width=60,height=60)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",17,"bold"),fg="white",bg="black")
        get_str.place(x=80,y=70)
        
        # label
        username=lbl=Label(frame,text="Username",font=("times new roman",13,"bold"),fg="white",bg="black")
        username.place(x=50,y=120)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))
        self.txtuser.place(x=30,y=145,width=220)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",13,"bold"),fg="white",bg="black")
        password.place(x=45,y=190)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",13,"bold"))
        self.txtpass.place(x=30,y=215,width=220)
        
        #===========Icon Images===========
        img2=Image.open(r"C:\Users\Rohan\OneDrive\Desktop\face_recognition_system\college_images\LoginIconAppl.png")
        img2=img2.resize((20,20),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=570,y=275,width=15,height=15)
        
        img3=Image.open(r"C:\Users\Rohan\OneDrive\Desktop\face_recognition_system\college_images\lock-512.png")
        img3=img3.resize((20,20),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=570,y=345,width=15,height=15)
        
        # LoginButton        
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",13,"bold"),bd=3,relief=RAISED,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=90,y=250,width=90,height=30)
        
        # registerButton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",9,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=13,y=285,width=125)
        
        # forgetpassbtn
        forgetbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",9,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=6,y=310,width=125)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.txtuser.get()=="rohan" and self.txtpass.get()=="saroj":
            messagebox.showinfo("Success","Welcome to Advanced Attendance System")
            conn=mysql.connector.connect(host="localhost",user="root",password="Roh@n123",database="face_recognizer")
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("Yes/No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Roh@n123",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                
                                                                                    ))
            
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("Yes/No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
    #============================reset password=======================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Roh@n123",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                   
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset , please login new password",parent=self.root2)
                self.root2.destroy()
            
            
            
    #=============================forget password window========================
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Roh@n123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("300x400+530+140")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",13,"bold"),fg="red",bg="white")
                l.place(x=0,y=7,relwidth=1)
                
                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",12,"bold"),bg="white",fg="black")
                security_Q.place(x=40,y=60)
                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",12,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Favourite Game","Your Pet Name")
                self.combo_security_Q.place(x=40,y=85,width=200)
                self.combo_security_Q.current(0)
                
                
                
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",12,"bold"),bg="white",fg="black")
                security_A.place(x=40,y=124)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",12))
                self.txt_security.place(x=40,y=150,width=200)
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",12,"bold"),bg="white",fg="black")
                new_password.place(x=40,y=190)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",12))
                self.txt_newpass.place(x=40,y=210,width=200)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=245)
                
                
                    
            
            


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1350x750+0+0")
        
        #===================variables===============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        #====================bg image================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Rohan\Desktop\face_recognition_system\college_images\university.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        # ===========left image=================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Rohan\Desktop\face_recognition_system\college_images\clock.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=40,y=80,width=385,height=450)
        
        # =================main frame=====================
        frame=Frame(self.root,bg="white")
        frame.place(x=425,y=80,width=700,height=450)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",16,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=15,y=15)
        
        # ==============label and entry===============
        
        # -------------row1
        fname=Label(frame,text="First Name",font=("times new roman",12,"bold"),bg="white")
        fname.place(x=40,y=80)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",12,"bold"))
        self.fname_entry.place(x=40,y=105,width=200)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",12,"bold"),bg="white",fg="black")
        l_name.place(x=340,y=80)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",12))
        self.txt_lname.place(x=340,y=105,width=200)
        
        #-----------------row2
        
        contact=Label(frame,text="Contact No",font=("times new roman",12,"bold"),bg="white",fg="black")
        contact.place(x=40,y=150)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",12))
        self.txt_contact.place(x=40,y=175,width=200)
        
        email=Label(frame,text="Email",font=("times new roman",12,"bold"),bg="white",fg="black")
        email.place(x=340,y=150)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",12))
        self.txt_email.place(x=340,y=175,width=200)
        
        #----------------row3
        
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",12,"bold"),bg="white",fg="black")
        security_Q.place(x=40,y=210)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Favourite Game","Your Pet Name")
        self.combo_security_Q.place(x=40,y=240,width=200)
        self.combo_security_Q.current(0)
        
        
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",12,"bold"),bg="white",fg="black")
        security_A.place(x=340,y=210)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",12))
        self.txt_security.place(x=340,y=240,width=200)
        
        #------------------row4
        
        pswd=Label(frame,text="Password",font=("times new roman",12,"bold"),bg="white",fg="black")
        pswd.place(x=40,y=270)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",12))
        self.txt_pswd.place(x=40,y=300,width=200)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",12,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=340,y=270)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",12))
        self.txt_confirm_pswd.place(x=340,y=300,width=200)
        
        # ===================checkbutton====================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",9,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=40,y=340)
        
        # ====================buttons=====================
        img=Image.open(r"C:\Users\Rohan\Desktop\face_recognition_system\college_images\register-now-button1.jpg")
        img=img.resize((160,40),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=10,y=377,width=160)
        
        img1=Image.open(r"C:\Users\Rohan\Desktop\face_recognition_system\college_images\loginpng.png")
        img1=img1.resize((160,40),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=300,y=377,width=160)
        
        
    # =====================Function declaration=================
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Roh@n123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
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
            messagebox.showinfo("Success","Register Successfully")
            
            
    def return_login(self):
        self.root.destroy()
            
            
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        # first image
        img=Image.open(r"college_images\Stanford.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        # third image
        img2=Image.open(r"college_images\u.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        # bg image
        img3=Image.open(r"college_images\bgimg.jpg")
        img3=img3.resize((1270,648),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1270,height=648)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1270,height=35)
        
        # ==================time====================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
            
        lbl = Label(title_lbl, font = ('times new roman',11, 'bold'),background = 'white',foreground = 'blue')
        lbl.place(x=0,y=0,width=85,height=40)
        time()
            

        # student button
        img4=Image.open(r"college_images\student.jpg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=250,width=150,height=30)

        
        # Detect face button
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=430,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=430,y=250,width=150,height=30)

        # Attendance face button
        img6=Image.open(r"college_images\attendance.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=653,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=653,y=250,width=150,height=30)

        # Help face button
        img7=Image.open(r"college_images\help.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=880,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=880,y=250,width=150,height=30)

        # Train face button
        img8=Image.open(r"college_images\Train.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=310,width=150,height=150)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=460,width=150,height=30)

        # Photos face button
        img9=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=432,y=310,width=150,height=150)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=432,y=460,width=150,height=30)

        # Developer face button
        img10=Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=653,y=310,width=150,height=150)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=653,y=460,width=150,height=30)

        # Exit face button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=881,y=310,width=150,height=150)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=881,y=460,width=150,height=30)


    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    # ========================Function Buttons===========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        
        
if __name__=="__main__":
    main()
    