from customtkinter import *



def lohinn():
    root.destroy()
    win=CTk()
    win.title("فرم ثبت نام")
    win.geometry("650x300+550+250")

    #widget
    lbl_name=CTkLabel(win,text=":نـــــــــــــــــــــام",
                    font=("B Esfehan",20))
    lbl_name.place(x=500,y=20)

    lbl_lname=CTkLabel(win,text=":نام خانوادگی",
                    font=("B Esfehan",20))
    lbl_lname.place(x=500,y=60)

    lbl_dname=CTkLabel(win,text=":نام کاربری",
                    font=("B Esfehan",20))
    lbl_dname.place(x=225,y=20)

    lbl_rname=CTkLabel(win,text=":رمز ورود",
                    font=("B Esfehan",20))
    lbl_rname.place(x=225,y=60)

    ent_name=CTkEntry(win)
    ent_name.place(x=350,y=30)

    ent_lname=CTkEntry(win)
    ent_lname.place(x=350,y=70)

    ent_dname=CTkEntry(win)
    ent_dname.place(x=70,y=30)

    ent_rname=CTkEntry(win)
    ent_rname.place(x=70,y=70)

    #btn_allsee=CTkButton(win,text="مشاهده همه",
    #                    font=("B nazanin",16))
    #btn_allsee.place(x=430,y=120)

    btn_add=CTkButton(win,text="تایید",width=200,
                        font=("B nazanin",16))
    btn_add.place(x=360,y=120)

    btn_cleer=CTkButton(win,text="بازنشانی",width=200,
                        font=("B nazanin",16))
    btn_cleer.place(x=100,y=120)

    btn_allsee=CTkButton(win,text="حذف",width=200,
                        font=("B nazanin",16))
    btn_allsee.place(x=360,y=160)

    btn_allsee=CTkButton(win,text="خروج",width=200,
                        font=("B nazanin",16))
    btn_allsee.place(x=100,y=160)

    btn_allsee=CTkButton(win,text="ورود",width=200,
                        font=("B nazanin",16))
    btn_allsee.place(x=235,y=220)

    win.resizable(0,0)
    win.mainloop()







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
#btn_allsee=CTkButton(win,text="مشاهده همه",
 #                    font=("B nazanin",16))
#btn_allsee.place(x=430,y=120)

btn_allsee=CTkButton(root,text="ثبت نام",width=100,
                     font=("B nazanin",16),command=lohinn)
btn_allsee.place(x=50,y=130)

btn_allsee=CTkButton(root,text="ورود",width=100,
                     font=("B nazanin",16))
btn_allsee.place(x=160,y=130)

root.resizable(0,0)
root.mainloop()


