from customtkinter import *
from tkinter import messagebox


def loginn():
    root.destroy()
    win=CTk()
    app=login(win)
    win.mainloop()


class login:
    def __init__(self,win):
        self.win=win
        self.win.title("فرم ثبت نام")
        self.win.geometry("650x300+550+250")
        self.win.resizable(0,0)

        self.lbl_name=CTkLabel(win,text=":نـــــــــــــــــــــام",
                        font=("B Esfehan",20))
        self.lbl_name.place(x=500,y=20)

        self.lbl_lname=CTkLabel(win,text=":نام خانوادگی",
                        font=("B Esfehan",20))
        self.lbl_lname.place(x=500,y=60)

        self.lbl_dname=CTkLabel(win,text=":نام کاربری",
                        font=("B Esfehan",20))
        self.lbl_dname.place(x=225,y=20)

        self.lbl_rname=CTkLabel(win,text=":رمز ورود",
                        font=("B Esfehan",20))
        self.lbl_rname.place(x=225,y=60)

        self.ent_name=CTkEntry(win)
        self.ent_name.place(x=350,y=30)

        self.ent_lname=CTkEntry(win)
        self.ent_lname.place(x=350,y=70)

        self.ent_dname=CTkEntry(win)
        self.ent_dname.place(x=70,y=30)

        self.ent_rname=CTkEntry(win)
        self.ent_rname.place(x=70,y=70)


        self.btn_add=CTkButton(win,text="تایید",width=200,
                            font=("B nazanin",16),)
        self.btn_add.place(x=360,y=120)

        self.btn_cleer=CTkButton(win,text="بازنشانی",width=200,
                            font=("B nazanin",16),)
        self.btn_cleer.place(x=100,y=120)

        self.btn_v=CTkButton(win,text="ورود",width=200,
                            font=("B nazanin",16))
        self.btn_v.place(x=360,y=160)

        self.btn_gh=CTkButton(win,text="خروج",width=200,
                            font=("B nazanin",16),command=exit)
        self.btn_gh.place(x=100,y=160)
        
    def exit():
        c=messagebox.askyesno("خروج","آیا مطمئن هستید؟")
        if c == True:
            self.win.destroy()

root=CTk()
root.title("خوش برگشتید")
root.geometry("300x200+550+250")

#widget
ent_name=CTkEntry(root)
ent_name.place(x=40,y=30)

ent_lname=CTkEntry(root)
ent_lname.place(x=40,y=70)

lbl_dname=CTkLabel(root,text=":نام کاربری",
                  font=("B Esfehan",20))
lbl_dname.place(x=180,y=20)

lbl_rname=CTkLabel(root,text=":رمز ورود",
                  font=("B Esfehan",20))
lbl_rname.place(x=180,y=60)

btn_e=CTkButton(root,text="ثبت نام",width=100,
                     font=("B nazanin",16),command=loginn)
btn_e.place(x=50,y=130)

btn_v=CTkButton(root,text="ورود",width=100,
                     font=("B nazanin",16))
btn_v.place(x=160,y=130)

root.resizable(0,0)
root.mainloop()



