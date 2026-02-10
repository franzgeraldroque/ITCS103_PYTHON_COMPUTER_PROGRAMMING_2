import tkinter as franz

window = franz.Tk()
window.title("GoGli")
window.geometry("600x600")
window.resizable(True,True)
window.config(bg= "light pink", cursor= "arrow")

label = franz.Label(window, 
                    text= "STUDENT PROFILE", 
                    font= ("Arial", 20, "bold"), 
                    fg= "black", 
                    bg= "light pink")
label.pack(padx= 20, pady= 10)

label = franz.Label(window, 
                    text= "Name: Franz Gerald L. Roque", 
                    font= ("Arial", 11), 
                    fg= "black", 
                    bg= "light pink", 
                    anchor= "w", 
                    width= 100)
label.pack(padx= 50, pady= 10)

label = franz.Label(window, 
                    text = "Age: 18", 
                    font= ("Arial", 11), 
                    fg= "black", 
                    bg= "light pink", 
                    anchor= "w", 
                    width= 100)
label.pack(padx= 50, pady= 10)

label = franz.Label(window, 
                    text = "Course and Section: BSIT-1A", 
                    font= ("Arial", 11), 
                    fg= "black", 
                    bg= "light pink", 
                    anchor= "w", 
                    width= 100)
label.pack(padx= 50, pady= 10)

label = franz.Label(window, 
                    text= "Birthday: June 17, 2007", 
                    font= ("Arial", 11), 
                    fg= "black", 
                    bg= "light pink", 
                    anchor= "w", 
                    width= 100)
label.pack(padx= 50, pady= 10)

label = franz.Label(window, 
                    text= "Motto: 'Worry less, smile more'", 
                    font= ("Arial", 11), 
                    fg= "black", 
                    bg= "light pink", 
                    anchor= "w", 
                    width= 100)
label.pack(padx= 50, pady= 10)

window.mainloop()
