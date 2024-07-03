import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sqlite3
from tkinter import messagebox

# Functions
def submit_form():

  # Collect data from the form
  first_name = first_name_entry.get()
  middle_name = middle_name_entry.get()
  surname = surname_entry.get()
  suffix = suffix_entry.get()
  bday = bday_entry.entry.get()
  email = email_entry.get()
  civilstatus = civilstatus_entry.get()
  place_of_birth = pob_entry.get()
  disability = disability_entry.get()
  ethnicity = ethnicity_entry.get()
  mother_tongue = mt_entry.get()
  religion = religion_entry.get()
  height = height_entry.get()
  weight = weight_entry.get()
  landline = landline_entry.get()
  mobile_no = mobileno_entry.get()
  country = country_entry.get()
  region = region_entry.get()
  city = city_entry.get()
  barangay = barangay_entry.get()
  area = area_entry.get()
  cp_name = cp_name_entry.get()
  cp_contact = cp_contact_entry.get()
  cp_address = cp_address_entry.get()
  lastschool = lastschool_entry.get()
  school_address = school_address_entry.get()
  year_of_grad = yog_entry.get()
  school_type = school_type_entry.get()
  firstsem_gwa = firstsem_entry.get()
  secondsem_gwa = secondsem_entry.get()

   # Insert values into the database
  conn = sqlite3.connect('Application_form.db')
  cursor = conn.cursor()
    
  cursor.execute("""
        INSERT INTO Applicant (
    First_name,
    Middle_name,
    Surname,
    Suffix,
    Bday,
    Email,
    Civil_status,
    Place_of_birth,
    Disability,
    Ethnicity,
    Mother_tongue,
    Religion,
    Height,
    Weight,
    Landline,
    Mobile_no,
    Country,
    Region,
    City,
    Barangay,
    Area,
    Contact_person_name,
    Contact_person_address,
    Last_school_attended,
    School_address,
    Year_of_grad,
    School_type,
    firstsem_gwa,
    secondsem_gwa
) VALUES (
    ?,
     ?, 
     ?, 
     ?, 
     ?
    , ?
    , ?
    , ?, 
    ?, 
    ?, 
    ?, 
    ?
    , ?, 
    ?, 
    ?, 
    ?, 
    ?
    , ?, 
    ?, 
    ?, 
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?
    
);
    """, (first_name, middle_name, surname, suffix, bday, email, civilstatus, place_of_birth, disability, ethnicity, mother_tongue, religion, height, weight, landline, mobile_no, country, region, city, barangay, area, cp_name, cp_address, lastschool, school_address, year_of_grad, school_type, firstsem_gwa, secondsem_gwa)
                 )
    
  conn.commit()
  conn.close()


  # Show success message
  tk.messagebox.showinfo("Success", "Form submitted successfully!")
  

def application_form():

  global first_name_entry, middle_name_entry, surname_entry, suffix_entry, bday_entry, email_entry, sex_var, civilstatus_entry, pob_entry, disability_entry, ethnicity_entry, mt_entry, religion_entry, height_entry, weight_entry, landline_entry, mobileno_entry, country_entry, region_entry, city_entry, barangay_entry, area_entry, cp_name_entry, cp_contact_entry, cp_address_entry, lastschool_entry, school_address_entry, yog_entry, school_type_entry, firstsem_entry, secondsem_entry

  # remove all widgets in content_frame
  for widget in content_frame.winfo_children():
        widget.destroy()


  # Contents
  header = tb.Label(content_frame, text="Admission Application Form", font=("Arial",20,"bold"))
  header.pack(side=TOP, pady=(10,0))

  app_form_notebook = tb.Notebook(content_frame, bootstyle="primary")
  app_form_notebook.pack(fill=BOTH, expand=1,padx=10,pady=(0,50))

  submit_button = tb.Button(content_frame, text="Submit", bootstyle="danger", command=submit_form)
  submit_button.pack(pady=(0,80))


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
  sex_mb.grid(row=5, column=1, padx=5, pady=5,sticky='w')

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
  tb.Label(personal_info_frame, text="Height (CM):", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=11, column=0, padx=5, pady=5, sticky='w')
  height_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
  height_entry.grid(row=11, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(personal_info_frame, text="Weight (KG):", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=11, column=2, padx=5, pady=5, sticky='w')
  weight_entry = tb.Entry(personal_info_frame, bootstyle="default", font=("Arial", 12))
  weight_entry.grid(row=11, column=3, padx=5, pady=5, sticky='ew')

  # Row 13
  tb.Separator(personal_info_frame, orient="horizontal", bootstyle="default").grid(row=12, columnspan=4, sticky="ew", pady=(10, 0), padx=10)
  
  # Row 14
  tb.Label(personal_info_frame, text="ID Picture(2x2):", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=13, column=0, padx=5, pady=5, sticky='w')
  submitpic_button = tb.Button(personal_info_frame, bootstyle="info", text="Attach a file")
  submitpic_button.grid(row=13, column=1, padx=20, pady=5, sticky='ew')



  # CONTACT INFO TAB

  contact_info_frame = tb.Frame(content_frame, bootstyle="light")
  contact_info_frame.pack(fill="both", expand=True)
  contact_info_frame.grid_columnconfigure(1, weight=1)
  contact_info_frame.grid_columnconfigure(3, weight=1)

  # Row 1
  tb.Label(contact_info_frame, text="Landline Number: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky='w')
  landline_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  landline_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(contact_info_frame, text="Mobile Number: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5, pady=5, sticky='w')
  mobileno_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  mobileno_entry.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

  # Row 2
  tb.Separator(contact_info_frame, orient="horizontal", bootstyle="default").grid(row=1, columnspan=4, sticky="ew", pady=(10, 10), padx=10)

  # Row 3
  tb.Label(contact_info_frame, text="Address", bootstyle="light-inverse", font=("Arial", 15, "bold")).grid(row=2, columnspan=4, padx=10)
  

  # Row 4
  tb.Label(contact_info_frame, text="Country: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=5, pady=5, sticky='w')
  country_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  country_entry.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(contact_info_frame, text="Region: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=3, column=2, padx=5, pady=5, sticky='w')
  region_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  region_entry.grid(row=3, column=3, padx=5, pady=5, sticky='ew')

  # Row 5
  tb.Label(contact_info_frame, text="City/Municipality: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=4, column=0, padx=5, pady=5, sticky='w')
  city_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  city_entry.grid(row=4, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(contact_info_frame, text="Barangay: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=4, column=2, padx=5, pady=5, sticky='w')
  barangay_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  barangay_entry.grid(row=4, column=3, padx=5, pady=5, sticky='ew')
  
  # Row 6
  tb.Label(contact_info_frame, text="Subdivision/Area/St./House no. ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='w')
  area_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  area_entry.grid(row=5, column=1,columnspan=2, padx=5, pady=5, sticky='ew')

  # Row 7
  tb.Label(contact_info_frame, text="Contact Person", bootstyle="light-inverse", font=("Arial", 15, "bold")).grid(row=6, columnspan=4, padx=10)

  # Row 8
  tb.Label(contact_info_frame, text="Full Name: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=7, column=0, padx=5, pady=5, sticky='w')
  cp_name_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  cp_name_entry.grid(row=7, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(contact_info_frame, text="Contact number: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=7, column=2, padx=5, pady=5, sticky='w')
  cp_contact_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  cp_contact_entry.grid(row=7, column=3, padx=5, pady=5, sticky='ew')

  # Row 9
  tb.Label(contact_info_frame, text="Address: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=8, column=0, padx=5, pady=5, sticky='w')
  cp_address_entry = tb.Entry(contact_info_frame, bootstyle="default", font=("Arial", 12))
  cp_address_entry.grid(row=8, column=1, padx=5, pady=5, sticky='ew')



  # SCHOOL GRADUATED TAB
  school_grad_frame = tb.Frame(content_frame, bootstyle="light")
  school_grad_frame.pack(fill="both", expand=True)
  school_grad_frame.grid_columnconfigure(1, weight=1)
  school_grad_frame.grid_columnconfigure(3, weight=1)

  # Row 1
  tb.Label(school_grad_frame, text="School Name: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky='w')
  lastschool_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  lastschool_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(school_grad_frame, text="School Address", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5, pady=5, sticky='w')
  school_address_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  school_address_entry.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

  # Row 2
  tb.Label(school_grad_frame, text="Year of graduation: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky='w')
  yog_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  yog_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(school_grad_frame, text="School type: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=1, column=2, padx=5, pady=5, sticky='w')
  school_type_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  school_type_entry.grid(row=1, column=3, padx=5, pady=5, sticky='ew')
  
  grades_frame = tb.Frame(content_frame, bootstyle="light")
  grades_frame.pack(fill="both", expand=True)
  grades_frame.grid_columnconfigure(1, weight=1)
  grades_frame.grid_columnconfigure(3, weight=1)

  # Row 1
  tb.Label(grades_frame, text="Report Card", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky='w')
  rc_attach_button = tb.Button(grades_frame, bootstyle="info", text="Attach File")
  rc_attach_button.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

  # Row 2
  tb.Label(grades_frame, text="Grade 11 Grades", bootstyle="light-inverse", font=("Arial", 15, "bold")).grid(row=1, columnspan=4, padx=10)

  # Row 3
  tb.Label(grades_frame, text="First Semester GWA: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky='w')
  firstsem_entry = tb.Entry(grades_frame, bootstyle="default", font=("Arial", 12))
  firstsem_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(grades_frame, text="Second Semester GWA: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=2, column=2, padx=5, pady=5, sticky='w')
  secondsem_entry = tb.Entry(grades_frame, bootstyle="default", font=("Arial", 12))
  secondsem_entry.grid(row=2, column=3, padx=5, pady=5, sticky='ew')




  app_form_notebook.add(personal_info_frame, text="Personal Information")
  app_form_notebook.add(contact_info_frame, text="Contact Information")
  app_form_notebook.add(school_grad_frame, text="Last School Attended")
  app_form_notebook.add(grades_frame, text="Grades")

# Window
window = tb.Window(themename="flatly")

# Global
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

screen_width = 1920
screen_height = 1080
window_width = int(screen_width/1.5)
window_height = int (screen_height/1.5)
# x = (screen_width/2) - (window_width/2)
# y = (screen_height/2) - (window_height/2)

x = (1280/2) - (1280/2)
y = (720/2) - (720/2)

# Window properties
window.title("User Dashboard")
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
profile_frame.config(width=300, height=50)


user_name_label = tb.Label(profile_frame, text="(Applicant Full Name)", bootstyle="inverse-info", font=("Arial",10,"bold"), width=25)
user_name_label.pack(padx=10, side=LEFT) 

profile_button = tb.Button(profile_frame, text="Profile", bootstyle="warning")
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
home_option = tb.Button(left_bar,text="Home",width=20, bootstyle="default", style="default.TButton")
home_option.pack(pady=(10,0))

application_option = tb.Button(left_bar,text="Application Form",width=20, style="default.TButton", command=application_form)
application_option.pack()

# Content
content_frame = tb.Frame(main_frame, bootstyle="default")
content_frame.pack(side=LEFT)
content_frame.pack_propagate(False) # Without this, we can't change the frame's size
content_frame.configure(width=window_width, height=window_height)
scrollbar = tb.Scrollbar(content_frame, orient="vertical", bootstyle=DEFAULT)
scrollbar.pack(side=RIGHT, fill="y")

label = tk.Label(content_frame, text="Main frame")
label.pack()



window.mainloop()