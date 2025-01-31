import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
root = tk.Tk()
root.geometry("700x500")
root.title("LOG IN")
root.configure(bg="red")
main_cointainer = tk.Frame(root,bg="black")
main_cointainer.pack()

def signup(password,confirm_password):
    # logic to signuo profile her
    if password == confirm_password :
        tk.messagebox.showinfo(title='',message="SIGN UP SUCCESSSFULL")

def create_signup():
    global main_cointainer
    main_cointainer.destroy()
    main_cointainer = tk.Frame(root)  # Create the frame
    main_cointainer.pack()
    username_label = tk.Label(main_cointainer,text="Username:",font=("bold",20))
    username_label.grid(row=0,column=0)
    username_input = tk.Entry(main_cointainer)
    username_input.grid(row=0,column=1)
    password_label = tk.Label(main_cointainer,text="password:",font=("bold",20))
    password_label.grid(row=1,column=0)
    password_input = tk.Entry(main_cointainer)
    password_input.grid(row=1,column=1)
    confirm_password_label = tk.Label(main_cointainer,text="confirm_password:",font=("bold",20))
    confirm_password_label.grid(row=2,column=0)
    confirm_password_input = tk.Entry(main_cointainer)
    confirm_password_input.grid(row=2,column=1)
    login_button = tk.Button(main_cointainer,text="LOGIN",command=create_login)
    login_button.grid(row=3,column=0,)
    signup_button =tk.Button(main_cointainer,text="Signup",command=lambda: signup(password_input.get(), confirm_password_input.get()))
    signup_button.grid(row=3,column=1)

def login():
    print('login succefull')

def create_login():
    global main_cointainer
    main_cointainer.destroy()
    main_cointainer = tk.Frame(root)  # Create the frame
    main_cointainer.pack()
    username_label = tk.Label(main_cointainer,text="Username:",font=("bold",20))
    username_label.grid(row=0,column=0)
    username_input = tk.Entry(main_cointainer)
    username_input.grid(row=0,column=1)
    password_label = tk.Label(main_cointainer,text="password:",font=("bold",20))
    password_label.grid(row=1,column=0)
    password_input = tk.Entry(main_cointainer)
    password_input.grid(row=1,column=1)
    login_button = tk.Button(main_cointainer,text="LOGIN",command=login)
    login_button.grid(row=3,column=0,)
    signup_button =tk.Button(main_cointainer,text="Signup",command=create_signup)
    signup_button.grid(row=3,column=1)

create_login()



root.mainloop()

# malai muji khei change agrna man layo