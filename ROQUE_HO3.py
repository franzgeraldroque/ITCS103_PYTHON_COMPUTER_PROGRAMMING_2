import tkinter as franz

window = franz.Tk()
window.title("Simple Calculator")
window.config(bg="white")
window.resizable(False, False)

def add():
    frst_number = frst_entry.get()
    scnd_number = scnd_entry.get()
    result = int(frst_number) + int(scnd_number)

    output["text"] = f'The sum of {frst_number} and {scnd_number} is {result}'

def multiply():
    frst_number = frst_entry.get()
    scnd_number = scnd_entry.get()
    result = int(frst_number) * int(scnd_number)

    output["text"] = f'The sum of {frst_number} x {scnd_number} is {result}'

def substract():
    frst_number = frst_entry.get()
    scnd_number = scnd_entry.get()
    result = int(frst_number) - int(scnd_number)

    output["text"] = f'The sum of {frst_number} - {scnd_number} is {result}'

def division():
    frst_number = frst_entry.get()
    scnd_number = scnd_entry.get()

    if int(scnd_number) != 0:
        result = int(frst_number) / int(scnd_number)
        output["text"] = f'The quotient of {frst_number} / {scnd_number} is {round(result, 2)}'

    else:
        output["text"] = 'Cannot be divided by 0'

output = franz.Label(window, text="Simple Calculator")
output.grid(column=0, row=0, columnspan=3)

frame = franz.Frame(window, bg="light pink", bd=10)
frame.grid(column=0, row=1)

frst_number = franz.Label(frame, text= "Enter 1st Number", bg= "light blue")
frst_number.grid(column=0, row=2, columnspan=1, pady= 5)

frst_entry = franz.Entry(frame, bg="light gray", width= 10)
frst_entry.grid(column=2,row=2, pady=5)

scnd_number = franz.Label(frame, text="Enter 2nd Number",bg= "light blue")
scnd_number.grid(column=0, row=3, columnspan=1, pady=5)

scnd_entry = franz.Entry(frame, 
                         bg="light gray", 
                         width= 10)
scnd_entry.grid(column=2, row=3, pady=5)
    

add_bttn = franz.Button(frame, 
                        text="Add",
                         bg="Dark Gray", 
                         fg="black", 
                         command=add,
                         activebackground="Red")
add_bttn.grid(column=0, row=4, pady=5)

mltply_bttn = franz.Button(frame, 
                           text="Multiply", 
                           bg="Dark Gray", 
                           fg="black", 
                           command=multiply,
                           activebackground="red")
mltply_bttn.grid(column=0,row=5,pady=5)

sbtrct_bttn = franz.Button(frame,
                           text="Substract",
                           bg="Dark Gray",
                           fg="black",
                           command=substract,
                           activebackground="red")
sbtrct_bttn.grid(column=2, row=4, pady=5)

dvsn_bttn = franz.Button(frame,
                         text="Division",
                         bg="Dark Gray",
                         fg="black",
                         command=division,
                         activebackground="red")
dvsn_bttn.grid(column=2, row=5,pady=5)

window.mainloop()