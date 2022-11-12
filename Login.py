from tkinter import *
import customtkinter
from PIL import ImageTk, Image
#from AdminLogin import *
#from LibLogin import *
#from StudentLogin import *

customtkinter.set_appearance_mode("light")

root = customtkinter.CTk()
root.title("Login Portal")
#root.iconbitmap("admin.jpg")
root.state('zoomed')

#Defining image
admin_image = ImageTk.PhotoImage(Image.open("admin.jpg").resize((200,200), Image.ANTIALIAS))
librarian_image = ImageTk.PhotoImage(Image.open("librarian.jpg").resize((200,200), Image.ANTIALIAS))
student_image = ImageTk.PhotoImage(Image.open("student.jpg").resize((200,200), Image.ANTIALIAS))

#Creating buttons
button_1 = customtkinter.CTkButton(master=root, image=admin_image, text="Administrator Login" ,width=250, height=250, compound="top",  fg_color="blue", hover_color="cyan")
button_1.pack(side=LEFT, padx=100)

button_2 = customtkinter.CTkButton(master=root, image=librarian_image, text="Librarian Login", width=250, height=250, compound="top", fg_color="blue", hover_color="cyan")
button_2.pack(side=LEFT, padx=100)

button_3 = customtkinter.CTkButton(master=root, image=student_image, text="Student Login", width=250, height=250, compound="top",  fg_color="blue", hover_color="cyan")
button_3.pack(side=LEFT, padx=100)

root.mainloop()