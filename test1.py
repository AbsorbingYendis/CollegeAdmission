import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Global variables
first_name_entry = None

# Functions
def submit_form():
    global first_name_entry
    if first_name_entry:
        first_name = first_name_entry.get()
        print(f"First name: {first_name}")
    else:
        print("First name entry not found.")

def application_form():
    global first_name_entry
    # remove all widgets in content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Contents
    header = tb.Label(content_frame, text="Admission Application Form", font=("Arial", 20, "bold"))
    header.pack(side=TOP, pady=(10, 0))

    app_form_notebook = tb.Notebook(content_frame, bootstyle="primary")
    app_form_notebook.pack(fill=BOTH, expand=1, padx=10, pady=(0, 50))

    submit_button = tb.Button(content_frame, text="Submit", bootstyle="danger", command=submit_form)
    submit_button.pack(pady=(0, 80))

    # Personal info tab
    personal_info_frame = tb.Frame(content_frame, bootstyle="light")
    personal_info_frame.pack(fill="both", expand=True)
    personal_info_frame.grid_columnconfigure(1, weight=1)
    personal_info_frame.grid_columnconfigure(3, weight=1)

    # Row 1
    tb.Label(personal_info_frame, text="First Name: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky='w')
    first_name_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    first_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    tb.Label(personal_info_frame, text="Middle Name: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5, pady=5, sticky='w')
    middle_name_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    middle_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

    # Row 2
    tb.Label(personal_info_frame, text="Surname: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky='w')
    surname_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    surname_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

    tb.Label(personal_info_frame, text="Suffix: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=1, column=2, padx=5, pady=5, sticky='w')
    suffix_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    suffix_entry.grid(row=1, column=3, padx=5, pady=5, sticky='ew')

    # Row 3
    tb.Separator(personal_info_frame, orient="horizontal", bootstyle="default").grid(row=2, columnspan=4, sticky="ew", pady=(10, 0), padx=10)

    # Row 4
    tb.Label(personal_info_frame, text="Date of Birth:  ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=5, pady=5, sticky='w')
    bday_entry = tb.DateEntry(personal_info_frame, bootstyle="default")
    bday_entry.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

    tb.Label(personal_info_frame, text="Email Address: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=3, column=2, padx=5, pady=5, sticky='w')
    email_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    email_entry.grid(row=3, column=3, padx=5, pady=5, sticky='ew')

    # Row 5
    tb.Separator(personal_info_frame, orient="horizontal", bootstyle="default").grid(row=2, columnspan=4, sticky="ew", pady=(10, 0), padx=10)

    # Row 6
    tb.Label(personal_info_frame, text="Sex: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=5, column=0, padx=5, pady=5, sticky='w')
    sex_mb = tb.Menubutton(personal_info_frame, bootstyle="default", text="Select Option")
    sex_mb.grid(row=5, column=1, padx=5, pady=5, sticky='w')

    sex_menu = tb.Menu(sex_mb)
    sex_var = tk.StringVar()
    sex_menu.add_radiobutton(label="Male", variable=sex_var)
    sex_menu.add_radiobutton(label="Female", variable=sex_var)
    sex_mb['menu'] = sex_menu

    tb.Label(personal_info_frame, text="Civil Status: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=5, column=2, padx=5, pady=5, sticky='w')
    civilstatus_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    civilstatus_entry.grid(row=5, column=3, padx=5, pady=5, sticky='ew')

    # Row 7
    tb.Label(personal_info_frame, text="Place of Birth: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=6, column=0, padx=5, pady=5, sticky='w')
    pob_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    pob_entry.grid(row=6, column=1, padx=5, pady=5, sticky='ew')

    # Row 8
    tb.Separator(personal_info_frame, orient="horizontal", bootstyle="default").grid(row=7, columnspan=4, sticky="ew", pady=(10, 0), padx=10)

    # Row 9
    tb.Label(personal_info_frame, text="Disability:", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=8, column=0, padx=5, pady=5, sticky='w')
    disability_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    disability_entry.grid(row=8, column=1, padx=5, pady=5, sticky='ew')

    tb.Label(personal_info_frame, text="Ethnicity:", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=8, column=2, padx=5, pady=5, sticky='w')
    ethnicity_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    ethnicity_entry.grid(row=8, column=3, padx=5, pady=5, sticky='ew')

    # Row 10
    tb.Label(personal_info_frame, text="Mother Tongue:", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=9, column=0, padx=5, pady=5, sticky='w')
    mt_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    mt_entry.grid(row=9, column=1, padx=5, pady=5, sticky='ew')

    tb.Label(personal_info_frame, text="Religion:", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=9, column=2, padx=5, pady=5, sticky='w')
    religion_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    religion_entry.grid(row=9, column=3, padx=5, pady=5, sticky='ew')

    # Row 11
    tb.Separator(personal_info_frame, orient="horizontal", bootstyle="default").grid(row=10, columnspan=4, sticky="ew", pady=(10, 0), padx=10)

    # Row 12
    tb.Label(personal_info_frame, text="Height:", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=11, column=0, padx=5, pady=5, sticky='w')
    height_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    height_entry.grid(row=11, column=1, padx=5, pady=5, sticky='ew')

    tb.Label(personal_info_frame, text="Weight:", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=11, column=2, padx=5, pady=5, sticky='w')
    weight_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    weight_entry.grid(row=11, column=3, padx=5, pady=5, sticky='ew')

    # Row 13
    tb.Separator(personal_info_frame, orient="horizontal", bootstyle="default").grid(row=12, columnspan=4, sticky="ew", pady=(10, 0), padx=10)

    # Row 14
    tb.Label(personal_info_frame, text="Mobile Number:", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=13, column=0, padx=5, pady=5, sticky='w')
    mobile_num_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    mobile_num_entry.grid(row=13, column=1, padx=5, pady=5, sticky='ew')

    tb.Label(personal_info_frame, text="Landline Number:", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=13, column=2, padx=5, pady=5, sticky='w')
    landline_num_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
    landline_num_entry.grid(row=13, column=3, padx=5, pady=5, sticky='ew')

    # Adding personal_info_frame to the notebook
    app_form_notebook.add(personal_info_frame, text="Personal Info")

# GUI
root = tb.Window(themename="litera")
root.geometry("700x700")

# Styles
root.style.configure('lefttab.TNotebook', tabposition='wn', tabmargins=[10, 10, 10, 0])

# Frames
content_frame = tb.Frame(root, bootstyle="default")
content_frame.pack(fill=BOTH, expand=1)

# Admission Application Form Button
admission_form_button = tb.Button(root, text="Admission Form", bootstyle="primary", command=application_form)
admission_form_button.pack(pady=10)

# Run
root.mainloop()
