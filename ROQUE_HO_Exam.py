import tkinter as franz

window = franz.Tk()
window.title("ROQUE HO Exam")
window.config(bg='white')

def register_bttn():
    rgistr = franz.Toplevel(window)
    rgistr.config(bg="white")

    message = franz.Label(rgistr, text="",fg="white",bg="white")
    message.grid(column=0,row=0,columnspan=2)

    uname = franz.Label(rgistr, text="Username:", fg="black", bg="white")
    uname.grid(column=0, row=1)

    uname_entry = franz.Entry(rgistr, bg="white", width=20)
    uname_entry.grid(column=1,row=1)

    password = franz.Label(rgistr, text="Password:",fg="black" ,bg="white")
    password.grid(column=0,row=2)

    pass_entry = franz.Entry(rgistr, bg="white", width=20, show="*")
    pass_entry.grid(column=1,row=2)

    def change_color():
        psword = pass_entry.get()
        
        if len(psword) >= 8:
            rgistr.config(bg="green")
            message.config(text="You have successfully registered!", bg="green")
            uname.config(bg="green")
            password.config(bg="green")
            
        else:
            len(psword) <= 8
            rgistr.config(bg="red")
            message.config(text="The characters is less than 8!", bg="red")
            uname.config(bg="red")
            password.config(bg="red")
        

    chck_var = franz.IntVar()
    def check_bttn():
        if chck_var.get() == 1:
            pass_entry.config(show="")
        else:
            pass_entry.config(show="*")

    chck_bttn = franz.Checkbutton(rgistr, text="See Password", variable=chck_var, command=check_bttn)
    chck_bttn.grid(column=1,row=3)

    rgster_bttn = franz.Button(rgistr, text="Register", bg="white", fg="black",width=20, command=change_color)
    rgster_bttn.grid(column=0,row=4,columnspan=2)


def login_bttn():
    rgistr = franz.Toplevel(window)
    rgistr.config(bg="white")

    message = franz.Label(rgistr, text="",fg="white",bg="white")
    message.grid(column=0,row=0,columnspan=2)

    uname = franz.Label(rgistr, text="Username:", fg="black", bg="white")
    uname.grid(column=0, row=1)

    uname_entry = franz.Entry(rgistr, bg="white", width=20)
    uname_entry.grid(column=1,row=1)

    password = franz.Label(rgistr, text="Password:",fg="black" ,bg="white")
    password.grid(column=0,row=2)

    pass_entry = franz.Entry(rgistr, bg="white", width=20, show="*")
    pass_entry.grid(column=1,row=2)


    def change_login():
        user = uname_entry.get()
        psword = pass_entry.get()
        
        
        if uname == user and password == psword:
            rgistr.config(bg="green")
            message.config(text="You have successfully logged in!", bg="green")
            uname.config(bg="green")
            password.config(bg="green")
            
        else:
            uname != user and password != psword
            rgistr.config(bg="red")
            message.config(text="Invalid Credentials!!", bg="red")
            uname.config(bg="red")
            password.config(bg="red")
        
    chck_var = franz.IntVar()
    def check_bttn():
        if chck_var.get() == 1:
            pass_entry.config(show="")
        else:
            pass_entry.config(show="*")


    chck_bttn = franz.Checkbutton(rgistr, text="See Password", variable=chck_var, command=check_bttn)
    chck_bttn.grid(column=1,row=3)

    lgin_bttn = franz.Button(rgistr, text="Register", bg="white", fg="black",width=20, command=change_login)
    lgin_bttn.grid(column=0,row=4,columnspan=2)


wlcm = franz.Label(window, text="Welcome!", font=("Arial", 16, "bold"),bg="white", fg="black")
wlcm.grid(column=0,row=0, columnspan=2)

rgstr_bttn = franz.Button(window, text="Register", font=("Arail", 16, "bold"),bg="blue",fg="black",width=20, command=register_bttn)
rgstr_bttn.grid(column=0,row=1, columnspan=2, pady=10)

lgin_bttn = franz.Button(window, text="Log In", font=("Arial", 16, "bold"),bg="green", fg="black",width=20,command=login_bttn)
lgin_bttn.grid(column=0,row=2,columnspan=2)

window.mainloop()