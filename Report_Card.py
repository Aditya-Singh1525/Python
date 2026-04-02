import customtkinter as ctk
import tkinter.messagebox as tkmb
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Report Card!")
root.geometry("595x455")
root.configure(fg_color="#555555")

label = ctk.CTkLabel(root, text="", font=("Helvetica", 24))
label.pack(pady=40)

txt_box_grid = ctk.CTkFrame(root,fg_color="#555555")
txt_box_grid.pack(pady=20)

def submit():
    # Show a message box while waiting (simulating processing)
    tkmb.showinfo("Processing", "Submitting details... Please wait.")
    
    app = ctk.CTkToplevel(root)
    app.geometry("300x200")
    app.configure(fg_color="#555555")
    app.title("Result")
    
    pass_fail = ("Pass","Fail")
    pass_fail2 = random.choice(pass_fail)
    
    txt = ctk.CTkLabel(app, text="All details are submitted, you are:")
    txt.pack(pady=10)
    
    txt2 = ctk.CTkLabel(app, text=pass_fail2, font=("Arial", 40))
    txt2.pack(pady=20)

# Create a 3x3 grid of Entry widgets
entry = ctk.CTkEntry(txt_box_grid,placeholder_text="Enter your Full Name",height=30,width=150)
entry.grid(row=0,column=0)

entry2 = ctk.CTkEntry(txt_box_grid,placeholder_text="Enter your Age",height=30,width=150)
entry2.grid(row=0,column=1,padx=10)

entry3 = ctk.CTkEntry(txt_box_grid,placeholder_text="Enter your Class",height=30,width=150)
entry3.grid(row=1,column=0,pady=10)

entry4 = ctk.CTkEntry(txt_box_grid,placeholder_text="Enter your Division",height=30,width=150)
entry4.grid(row=1,column=1,pady=10,padx=10)

entry5 = ctk.CTkEntry(txt_box_grid,placeholder_text="Enter your Roll.No",height=30,width=150)
entry5.grid(row=2,column=0,pady=10,padx=10)

entry6 = ctk.CTkEntry(txt_box_grid,placeholder_text="Enter your CC",height=30,width=150)
entry6.grid(row=2,column=1,pady=10,padx=10)

button = ctk.CTkButton(root, text="Submit", command=submit, width=315,fg_color="aqua",hover_color="blue",text_color="black")
button.pack(pady=10,padx=20)

root.mainloop()
