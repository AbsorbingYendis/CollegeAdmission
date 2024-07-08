import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import subprocess

def open_admin_login():
  window.destroy()
  subprocess.Popen(["python", "Admin_Login.py"])

def open_applicant_login():
  window.destroy()
  subprocess.Popen(["python", "Applicant_Login.py"])

# Window Properties
window = tb.Window(themename="flatly")
window_width = int(1000)
window_height = int (600)
window.title("NSU Admission Login")
window.geometry(f"{window_width}x{window_height}")
window.resizable(False, False)

# Main Frame
main_frame = tb.Frame(window, bootstyle="light")
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False) 
main_frame.config(height=window_height, width=window_width)

# Content

login_user_label = tb.Button(main_frame, text="Login as Applicant/User ", bootstyle="success", width=30, command=open_applicant_login)
login_user_label.place(relx=0.5, rely=0.4, anchor=tb.CENTER)

tb.Separator(main_frame, orient="horizontal", bootstyle="default").place(relx=0.5, rely=0.6, anchor=tb.CENTER)

login_admin_label = tb.Button(main_frame, text="Login as Admin", bootstyle="danger",width=30, command=open_admin_login)
login_admin_label.place(relx=0.5, rely=0.6, anchor=tb.CENTER)

window.mainloop()