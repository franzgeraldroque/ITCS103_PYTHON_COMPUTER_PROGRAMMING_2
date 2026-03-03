

# ===== Title =====
label = tk.Label(window,
                text="HI HELLO!",
                bg="#1f2d3a",
                fg="#f1f1f1",
                font=("Arial", 18, "bold"))
label.pack(pady=15)

# ===== Image =====
img = tk.PhotoImage(file=r"C:\Users\ITLAB1-StudentPC01\Desktop\1A\testtk\librun.png")
img = img.subsample(6, 6)

img_label = tk.Label(window,
                    image=img,
                    text="This is Librun",
                    compound="top",
                    bg="#2e4053",
                    fg="white",
                    font=("Arial", 12),
                    padx=30,
                    pady=20)
img_label.pack(pady=20)

# ===== Frame =====
frame = tk.Frame(window, bg="#34495e", width=300, height=120)
frame.pack(pady=15)

# ===== Username Label =====
name_label = tk.Label(frame,
                      text="Username:",
                      bg="#34495e",
                      fg="white",
                      font=("Arial", 11, "bold"))
name_label.pack(pady=(10, 5))

# ===== Entry =====
name_entry = tk.Entry(frame,
                      bg="#ecf0f1",
                      fg="#2c3e50",
                      width=20)
name_entry.pack(pady=(0, 10))

pass_label=tk.Label(frame,
                    text="Password:",
                    bg="#34495e",
                    fg="white",
                    font=("Poppins", 16, "bold"))
pass_label.pack(pady=(5,5))

pw_entry=tk.Entry(frame, show="*",
                  bg="#ecf0f1",
                  fg="#2c3e50")
pw_entry.pack(padx=10, pady=10)

def show():
    name = name_entry.get()
    gender=radio_val.get()

    label ['text'] = f"Hello Lord!,{name}.Your gender is {gender}."
    if check_val.get() == 1:
        label2=tk.Label(window,
                        text="Remember Me is Clicked!",
                        bg="#1f2d3a",
                        fg="white")
        label2.pack(pady=5)
    else:
        label2=tk.Label(window,
                        text="Remember Me is NOT Clicked!",
                        bg="#1f2d3a",
                        fg="white")
        label2.pack(pady=5)

radio_val = tk.IntVar()

female = tk.Radiobutton(frame,
                        text="Female",
                        variable=radio_val,
                        value=0,
                        bg="#34495e",
                        fg="white",
                        selectcolor="#2e4053")
female.pack(pady=3)

