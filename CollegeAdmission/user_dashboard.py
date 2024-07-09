import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sqlite3
from tkinter import messagebox
from user_dashboard_forms.application_form import *
from user_dashboard_forms.home import *
from user_dashboard_forms.profile import *
from user_dashboard_forms.application_form import *
import sys


# Window
window = tb.Window(themename="flatly")

# Global
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
window_width = int(1280)
window_height = int (720)
# x = (screen_width/2) - (window_width/2)
# y = (screen_height/2) - (window_height/2)

# Window properties
window.title("User Dashboard")
# window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
window.geometry(f"{window_width}x{window_height}")

window.resizable(False, False)

# Main Frame
main_frame = tb.Frame(window, bootstyle="default")
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False) 
main_frame.config(height=window_height, width=window_width)

# Top Bar

top_bar = tb.Frame(main_frame, bootstyle="info")
top_bar.pack(side=TOP)
top_bar.pack_propagate(False)
top_bar.config(width=window_width, height=50)

# Top Bar items
nsu_label_frame = tb.Frame(top_bar, bootstyle="info")
nsu_label_frame.pack(side=LEFT)
nsu_label_frame.pack_propagate(False)
nsu_label_frame.config(width=250, height=50)

nsu_label = tb.Label(nsu_label_frame, text="NSU Admission System",bootstyle="inverse-info", font=("Arial",14,"bold"),width=250)
nsu_label.pack(padx=15,side=LEFT)

sep = tb.Separator(top_bar, orient="vertical")
sep.pack(fill=tb.Y, side=LEFT)



profile_frame = tb.Frame(top_bar, bootstyle="info")
profile_frame.pack(side=RIGHT)
profile_frame.pack_propagate(False)
profile_frame.config(width=300, height=50)


user_name_label = tb.Label(profile_frame, text="(Applicant Full Name)", bootstyle="inverse-info", font=("Arial",10,"bold"), width=25)
user_name_label.pack(padx=10, side=LEFT) 

profile_button = tb.Button(profile_frame, text="Profile", bootstyle="warning", command=lambda: profile(content_frame))
profile_button.pack(side=RIGHT, padx=20)

sep1 = tb.Separator(top_bar, orient="vertical")
sep1.pack(fill=tb.Y, side=RIGHT)



# Left Bar
left_bar = tb.Frame(main_frame, bootstyle="primary") 
left_bar.pack(side=LEFT)
left_bar.pack_propagate(False) # Without this, we can't change the frame's size
left_bar.configure(width=250, height=window_height)


# Styles
style_home_option = tb.Style()
style_home_option.configure('default.TButton', font=("Arial", 13))


# Left bar menu items
home_option = tb.Button(left_bar,text="Home",width=20, bootstyle="default", style="default.TButton", command=lambda: home(content_frame))
home_option.pack(pady=(10,0))
print(sys.argv[1])
application_option = tb.Button(left_bar,text="Application Form",width=20, style="default.TButton", command=lambda: application_form(content_frame, sys.argv[1]))
application_option.pack()

# Content
content_frame = tb.Frame(main_frame, bootstyle="default")
content_frame.pack(side=LEFT)
content_frame.pack_propagate(False) # Without this, we can't change the frame's size
content_frame.configure(width=window_width, height=window_height)

label = tk.Label(content_frame, text="Main frame")
label.pack()



window.mainloop()