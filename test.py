import tkinter as franz

window = franz.Tk()
window.title("Profile Builder")
window.geometry("700x300")
window.config(bg= "light blue")
window.resizable(False,False)


def change_color():
    if rad_val.get() == 0:
        window.config(bg="light blue")
        frame.config(bg="light blue")
    else:
        window.config(bg="light pink")
        frame.config(bg="light pink")

def toplevel_profile():
    top = franz.Toplevel(window)
    top.title("Student ID")
    top.geometry("250x180")

    if rad_val.get() == 0:
        color = "light blue"
        gender = "Male"
    else:
        color = "light pink"
        gender = "Female"

    top.config(bg=color)

    # Frame (container)
    card = franz.Frame(top, bg="white", width=220, height=120, bd=2)
    card.place(x=20, y=25)

    # Full name
    name = frst_entry.get() + " " + mddl_entry.get() + " " + lst_entry.get()

    # Title
    franz.Label(top, text="Student ID",
                font=("Arial", 12, "bold"),
                bg=color).place(x=80, y=5)

    # Inside Frame
    franz.Label(card, text="Name:", bg="white",
                font=("Arial", 10, "bold")).place(x=10, y=20)

    franz.Label(card, text=name,
                bg="white").place(x=80, y=20)

    franz.Label(card, text="Age:", bg="white",
                font=("Arial", 10, "bold")).place(x=10, y=50)

    franz.Label(card, text=age.cget("text"),
                bg="white").place(x=80, y=50)

    franz.Label(card, text="Gender:", bg="white",
                font=("Arial", 10, "bold")).place(x=10, y=80)

    franz.Label(card, text=gender,
                bg="white").place(x=80, y=80)

def brth(event):
    birth_year = int(brth_entry.get())
    result =  2026 - birth_year
    
    age["text"] = f'You are {result} years old'


profile = franz.Label(window, text= "Profile Builder", font= ("Arial", 16, "bold"))
profile.pack(pady= 10)

frame = franz.Frame(window, bg="light green", bd=10, height=180, width= 500)
frame.pack()

frst_entry = franz.Entry(frame, bg="light gray")
frst_entry.place(x=5, y=12)

frst_name = franz.Label(frame, text="First Name", bg= "light green")
frst_name.place(x=30, y=35)

mddl_entry = franz.Entry(frame, bg= "light gray")
mddl_entry.place(x=180, y= 12)

mddl_name = franz.Label(frame, text="Middle Name", bg="light green")
mddl_name.place(x=200, y=35)

lst_entry = franz.Entry(frame, bg="light gray")
lst_entry.place(x=350, y=12)

lst_name = franz.Label(frame, text="Last Name", bg="light green")
lst_name.place(x=380,y=35)

brth_entry = franz.Entry(frame, bg="light gray")
brth_entry.place(x=5, y=60)
brth_entry.bind("<Return>", brth)

brth_yr = franz.Label(frame, text="Birth Year", bg="light green")
brth_yr.place(x=30, y=85)

gender = franz.Label(frame, text="Gender", bg="light green")
gender.place(x=40,y= 130)

male = franz.Label(frame, text="Male", bg="light green")
male.place(x=200,y=130)

female = franz.Label(frame, text="Female", bg="light green")
female.place(x=300, y=130)

age = franz.Label(frame, bg="light green", text="Computing Age....", font=("Arial", 14, "italic"))
age.place(x=300, y=90)

rad_val = franz.IntVar()

submit_bttn = franz.Button(window, text="Submit", bg="light green", activebackground="green", command=toplevel_profile)
submit_bttn.place(x=300, y=240)

male_bttn = franz.Radiobutton(frame, text="Male",bg="light green",variable=rad_val, value=0, command=change_color)
male_bttn.place(x=190, y=130)

female_bttn1 = franz.Radiobutton(frame, text="Female",bg="light green",variable=rad_val, value=1, command=change_color)
female_bttn1.place(x=290, y=130)

window.mainloop()
