import tkinter as franz

window = franz.Tk()
window.title("Profile Builder")
window.geometry("700x300")
window.config(bg= "light blue")
window.resizable(False,False)


def brth():
    brth_yr = brth_entry.get()
    result = brth_yr.get()

    age["text"] = f'You are {result} years old'
# def change_color():


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

brth_entry = franz.Entry(frame, bg="light gray", show=brth)
brth_entry.place(x=5, y=60)

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

bttn = franz.Button(window, text="Submit", bg="light green", activebackground="green")
bttn.place(x=300, y=240)

rad_bttn = franz.Radiobutton(frame, text="Male",bg="light green", value=0)
rad_bttn.place(x=190, y=130)

rad_bttn1 = franz.Radiobutton(frame, text="Female",bg="light green", value=1)
rad_bttn1.place(x=290, y=130)

window.mainloop()