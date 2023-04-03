from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",9,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=40,y=340)
        
        # ====================buttons=====================
        img=Image.open(r"C:\Users\Rohan\Desktop\face_recognition_system\college_images\register-now-button1.jpg")
        img=img.resize((160,40),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=10,y=377,width=160)
        
        img1=Image.open(r"C:\Users\Rohan\Desktop\face_recognition_system\college_images\loginpng.png")
        img1=img1.resize((160,40),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
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
                
            
            
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()