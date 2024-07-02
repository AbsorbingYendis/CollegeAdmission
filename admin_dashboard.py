import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

# Functions

# Window
window = tb.Window(themename="flatly")

# Global
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width/1.5)
window_height = int (screen_height/1.5)
x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)

# Window properties
window.title("Admin Dashboard")
window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
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
profile_frame.config(width=350, height=50)


admin_name_label = tb.Label(profile_frame, text="(Admin Name)", bootstyle="info-inverse", font=("Arial",10,"bold"), width=20)
admin_name_label.pack(padx=10, side=LEFT) 

notification_button = tb.Button(profile_frame, text="Notifications", bootstyle="success")
notification_button.pack(side=RIGHT, padx=10)

profile_button = tb.Button(profile_frame, text="Profile", bootstyle="warning")
profile_button.pack(side=RIGHT)



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
home_option = tb.Button(left_bar,text="Home",width=20, bootstyle="default", style="default.TButton")
home_option.pack(pady=(10,0))

course_option = tb.Button(left_bar,text="Course",width=20, style="default.TButton")
course_option.pack()

reg_users = tb.Button(left_bar,text="Registered Users",width=20, style="default.TButton")
reg_users.pack()

application_option = tb.Button(left_bar,text="Admission Application",width=20, style="default.TButton")
application_option.pack()

search_application_option = tb.Button(left_bar,text="Search Application",width=20, style="default.TButton")
search_application_option.pack()

public_notice_option = tb.Button(left_bar,text="Public Notice",width=20, style="default.TButton")
public_notice_option.pack()

enquiry_option = tb.Button(left_bar,text="Enquiry",width=20, style="default.TButton")
enquiry_option.pack()

pages_option = tb.Button(left_bar,text="Pages",width=20, style="default.TButton")
pages_option.pack()

subscriber_option = tb.Button(left_bar,text="Subscriber",width=20, style="default.TButton")
subscriber_option.pack()

reports_option = tb.Button(left_bar,text="Search Application",width=20, style="default.TButton")
reports_option.pack()









# Main Frame
label = tk.Label(main_frame, text="Main frame")
label.pack()








window.mainloop()