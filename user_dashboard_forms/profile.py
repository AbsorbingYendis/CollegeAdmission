import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def profile(content_frame):

  # remove all widgets in content_frame
  for widget in content_frame.winfo_children():
        widget.destroy()

  label = tb.Label(content_frame, text="This is profile form", bootstyle="success")
  label.pack()

  # Create notebook
  nb = tb.Notebook(content_frame, bootstyle="primary")
  nb.pack(fill=BOTH, expand=1)

  # Create frames for notebook
  edit_profile = tb.Frame(content_frame, bootstyle="light")
  edit_profile.pack(fill="both", expand=True)
  change_pass = tb.Frame(content_frame, bootstyle="light")
  change_pass.pack(fill="both", expand=True)
  logout = tb.Frame(content_frame, bootstyle="light")
  logout.pack(fill="both", expand=True)


  # Edit Profile Tab

  tb.Label(edit_profile, text="First Name", style='TLabel').grid(row=0, column=0, padx=10, pady=10, sticky='E')
  entry_first_name = tb.Entry(edit_profile)
  entry_first_name.grid(row=0, column=1, padx=10, pady=10, sticky='W')

  tb.Label(edit_profile, text="Last Name", style='TLabel').grid(row=0, column=2, padx=10, pady=10, sticky='E')
  entry_last_name = tb.Entry(edit_profile)
  entry_last_name.grid(row=0, column=3, padx=10, pady=10, sticky='W')

  tb.Label(edit_profile, text="Contact Number", style='TLabel').grid(row=1, column=0, padx=10, pady=10, sticky='E')
  entry_contact_number = tb.Entry(edit_profile)
  entry_contact_number.grid(row=1, column=1, padx=10, pady=10, sticky='W')

  tb.Label(edit_profile, text="Email", style='TLabel').grid(row=1, column=2, padx=10, pady=10, sticky='E')
  entry_email = tb.Entry(edit_profile)
  entry_email.grid(row=1, column=3, padx=10, pady=10, sticky='W')

  tb.Button(edit_profile, text="Update").grid(row=2, column=0, columnspan=4, pady=10)




  # Add frames to notebook
  nb.add(edit_profile, text="Edit Profile")
  nb.add(change_pass, text="Change Password")
  nb.add(logout, text="Logout")

