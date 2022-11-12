from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.title("Administrator Login")
root.state('zoomed')

def LoginPage():
    Label(root, text="Please enter Administrator Login Details").pack()
    Label(root, text="").pack()
    Label(root, text="Username").pack()
    username_login_entry = Entry(root, textvariable="username")
    username_login_entry.pack()
    Label(root, text="").pack()
    Label(root, text="Password").pack()
    password__login_entry = Entry(root, textvariable="password", show= '*')
    password__login_entry.pack()
    Label(root, text="").pack()
    Button(root, text="Login", width=10, height=1).pack()
    root.mainloop()
LoginPage()