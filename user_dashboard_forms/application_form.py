import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import time

# Global variables

user_info_state = 1
guardian_info_state = 1
economic_status_state = 1
school_state = 1
grades_state = 1


def destroy_final_form(finalize_frame,):
    for widget in finalize_frame.winfo_children():
      widget.destroy()

def generate_final_frame():
    form_labels = [("Personal and Contact Information",user_info_state), ("Guardian Information",guardian_info_state), ("Economic Status Information",economic_status_state), ("School Information", school_state), ("Grade Information",grades_state)]
    form_labels[0]

    num = 0
    for item in form_labels:
      finalize_row = tb.Frame(finalize_frame, bootstyle="light")
      finalize_row.pack(pady=5)

      status = ""
      if item[1] == 1:
        status = "Not yet submitted"
      elif item[1] == 2:
        status = "Submitted"
      elif item[1] == 3:
        status = "For evaluation"
      

      tb.Label(finalize_row, text=f"{item[0]}", bootstyle="light-inverse", font=("Arial",12,"bold")).grid(row=num, column=0, padx=25, pady=10, sticky='ew')
      user_info_status = tb.Label(finalize_row, text=status, bootstyle="danger", font=("Arial", 12))
      user_info_status.grid(row=num,column=1, padx=25, pady=10, sticky='ew')

      num = num + 1

    # num = num + 1
    finalize_button = tb.Button(finalize_frame, text="Finalize Application", bootstyle="danger")
    finalize_button.pack(pady=20)

def user_state(accountID):
  global user_info_state
  if user_info_state == 1:
    insert_user_info(accountID)
    user_info_state = 2
  elif user_info_state == 2:
    pass
  else:
    pass
  destroy_final_form(finalize_frame)
  generate_final_frame()
  
  
def guardian_state():
  global guardian_info_state
  if guardian_info_state == 1 and user_info_state == 2:
    insert_guardian_info()
    guardian_info_state = 2
  elif guardian_info_state == 2:
    pass
  else:
    pass

  destroy_final_form(finalize_frame)
  generate_final_frame()

def economic_state():
  global economic_status_state
  if economic_status_state == 1 and user_info_state == 2:
    insert_economic_info()
    economic_status_state = 2
  elif economic_status_state == 2:
    pass
  else:
    pass

  destroy_final_form(finalize_frame)
  generate_final_frame()

def school_state_function():
  global school_state
  if school_state == 1 and user_info_state == 2:
    insert_school_info()
    school_state = 2
  elif school_state == 2:
    pass
  else:
    pass

  destroy_final_form(finalize_frame)
  generate_final_frame()

def grades_state_function(accountID):
  global grades_state
  if grades_state == 1:
    insert_grades_info(accountID)
    grades_state = 2
  elif grades_state == 2:
    pass
  else:
    pass

  destroy_final_form(finalize_frame)
  generate_final_frame()

    
def submit_form(content_frame, accountID):

  # Collect data from the form
  

   # Insert values into the database
  conn = sqlite3.connect('Database/CAS.db')
  cursor = conn.cursor()
  
  cursor.execute(f"""SELECT infoID from User_Info where accountID = {int(accountID)}
""")
  
  infoID = cursor.fetchone()
  
  
  
  
  
    
  conn.commit()
  conn.close()


  # Show success message
  tk.messagebox.showinfo("Success", "Form submitted successfully!")
  
def insert_user_info(accountID):

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


  conn = sqlite3.connect('Database/CAS.db')
  cursor = conn.cursor()

  cursor.execute("""
        INSERT INTO User_Info(
    accountID,                      
    firstName,           
    lastName,            
    middleName,          
    suffix,              
    image,              
    emailAddress,       
    sex,                 
    civilStatus,         
    placeOfBirth,        
    birthDate,           
    disability,         
    ethnicity,          
    motherTongue,       
    religion,           
    heightcm,            
    addressLine1,      
    weightkg,            
    addressLine2,        
    addressMunicipality, 
    addressBarangay,     
    addressRegion,       
    landline,            
    mobileNumber      
) VALUES (
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
    
);
    """, (int(accountID),first_name, surname, middle_name, suffix,img_data,email, "Male", civilstatus, place_of_birth,bday, disability, ethnicity, mother_tongue, religion, height, area, weight, "Text", city, barangay, region, landline, mobile_no )
                 )
  conn.commit()
  cursor.execute(f"""SELECT infoID from User_Info where accountID = {int(accountID)}
""")
  

  global infoID
  infoID = cursor.fetchone()
  conn.close()

  tk.messagebox.showinfo("Successful", "Submitted user info successfully")

def insert_guardian_info():

  cp_name = cp_name_entry.get()
  cp_contact = cp_contact_entry.get()
  cp_address = cp_address_entry.get()

  conn = sqlite3.connect('Database/CAS.db')
  cursor = conn.cursor()
  cursor.execute("""
INSERT INTO Guardian_Info (
    infoID,
    fullName,
    contactNO,
    address
)VALUES(?,?,?,?)
""",(infoID[0],cp_name, cp_contact, cp_address))

  conn.commit()
  conn.close()

def insert_economic_info():

  income_source = income_source_entry.get()
  annual_income = annual_income_entry.get()

  conn = sqlite3.connect('Database/CAS.db')
  cursor = conn.cursor()
  cursor.execute("""
                 INSERT INTO Economic_Status (
    infoID,
    incomeSource,
    annualIncome
) VALUES (
                 ?,?,?
)

""",(infoID[0],income_source, annual_income))
  conn.commit()
  conn.close()

  messagebox.showinfo("Success", "Economic status successfully submitted")
  
def insert_school_info():

  school_id = school_id_entry.get()
  lastschool = lastschool_entry.get()
  year_of_grad = yog_entry.get()
  school_address = school_address_entry.get()
  school_type = school_type_entry.get()


  conn = sqlite3.connect('Database/CAS.db')
  cursor = conn.cursor()
  cursor.execute("""
                 INSERT INTO School (
    infoID,
    depedID,
    schoolName,
    yearOfGraduation,
    schoolAddress,
    schoolType)
                 VALUES (
                 ?,?,?,?,?,?
                 )

""",(infoID[0],school_id,lastschool,year_of_grad,school_address,school_type))
  messagebox.showinfo("Success", "School successfully submitted")
  conn.commit()
  conn.close()

  messagebox.showinfo("Success", "School successfully submitted")
  
def insert_grades_info(accountID):

  firstsem_gwa = firstsem_entry.get()
  secondsem_gwa = secondsem_entry.get()

  conn = sqlite3.connect('Database/CAS.db')
  cursor = conn.cursor()
  cursor.execute("""
                 INSERT INTO Grades (
    accountID,
    secondSemGWA,
    firstSemGWA,
    gradeDoc
)
                 VALUES(
                 ?,?,?,?
                 )
""",(int(accountID),secondsem_gwa,firstsem_gwa,pdf_data))
  
  conn.commit()
  conn.close()

  messagebox.showinfo("Success", "Grades successfully submitted")

def application_form(content_frame, infoID):

  global first_name_entry, middle_name_entry, surname_entry, suffix_entry, bday_entry, email_entry, sex_var, civilstatus_entry, pob_entry, disability_entry, ethnicity_entry, mt_entry, religion_entry, height_entry, weight_entry, landline_entry, mobileno_entry, country_entry, region_entry, city_entry, barangay_entry, area_entry, cp_name_entry, cp_contact_entry, cp_address_entry, lastschool_entry, school_address_entry, yog_entry, school_type_entry, firstsem_entry, secondsem_entry, school_id_entry, income_source_entry, annual_income_entry

  def upload_image():
    global img_data, pdf_data
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
      return  # User cancelled

    # Open the image
    image = Image.open(file_path)

    # Resize image to fit within the specified dimensions
    image.thumbnail((200, 200))

    # Display the image in the GUI
    img_display = ImageTk.PhotoImage(image)
    img_label.config(image=img_display)
    img_label.image = img_display

    # Convert image to binary data
    with open(file_path, 'rb') as file:

      img_data = file.read()

    img_label.grid(row=13, column=3, sticky='ew')

  def upload_pdf():
    global pdf_data
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
      with open(file_path, 'rb') as file:
        pdf_data = file.read()
      pdf_label.config(text=file_path.split("/")[-1])
  
  def download_pdf():
    global pdf_data
    if pdf_data:
      file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
      if file_path:
        with open(file_path, 'wb') as file:
          file.write(pdf_data)
        messagebox.showinfo("Success", "PDF downloaded successfully!")
    else:
      messagebox.showerror("Error", "No PDF uploaded to download.")

  # remove all widgets in content_frame
  for widget in content_frame.winfo_children():
        widget.destroy()


  # Contents
  header = tb.Label(content_frame, text="Admission Application Form", font=("Arial",20,"bold"))
  header.pack(side=TOP, pady=(10,0))

  app_form_notebook = tb.Notebook(content_frame, bootstyle="primary")
  app_form_notebook.pack(fill=BOTH, expand=1,padx=10,pady=(0,50))



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
  submitpic_button = tb.Button(personal_info_frame, bootstyle="info", text="Attach a file", command=upload_image)
  submitpic_button.grid(row=13, column=1, padx=20, pady=5, sticky='ew')

  img_label = tb.Label(personal_info_frame,)
  img_label.grid_forget()


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
  submit_personal_contact_info = tb.Button(contact_info_frame, text="Submit contact and personal information", bootstyle="danger",command=lambda: user_state(infoID))
  submit_personal_contact_info.grid(row=6, columnspan=4, sticky="ew", padx=300, pady=100)
  

  

  # GUARDIAN INFO
  guardian_info_frame = tb.Frame(content_frame, bootstyle="light")
  guardian_info_frame.pack(fill="both", expand=True)
  guardian_info_frame.grid_columnconfigure(1, weight=1)
  guardian_info_frame.grid_columnconfigure(3, weight=1)

  # Row 1
  tb.Label(guardian_info_frame, text="Contact Person", bootstyle="light-inverse", font=("Arial", 15, "bold")).grid(row=0, columnspan=4, padx=10, pady=10)

  # Row 2
  tb.Label(guardian_info_frame, text="Full Name: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky='w')
  cp_name_entry = tb.Entry(guardian_info_frame, bootstyle="default", font=("Arial", 12))
  cp_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(guardian_info_frame, text="Contact number: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=1, column=2, padx=5, pady=5, sticky='w')
  cp_contact_entry = tb.Entry(guardian_info_frame, bootstyle="default", font=("Arial", 12))
  cp_contact_entry.grid(row=1, column=3, padx=5, pady=5, sticky='ew')

  # Row 3
  tb.Label(guardian_info_frame, text="Address: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky='w')
  cp_address_entry = tb.Entry(guardian_info_frame, bootstyle="default", font=("Arial", 12))
  cp_address_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

  # Row 4
  submit_guardian_info_button = tb.Button(guardian_info_frame, text="Submit Guardian Info", bootstyle="danger",command=lambda: guardian_state() )
  submit_guardian_info_button.grid(row=3, columnspan=4, sticky="ew", padx=300, pady=10)

  # Row 5
  tb.Separator(guardian_info_frame, orient="horizontal", bootstyle="default").grid(row=4, columnspan=4, sticky="ew", pady=(10, 0), padx=10)

  # Row 6
  tb.Label(guardian_info_frame, text="Economic Status", bootstyle="light-inverse", font=("Arial", 15, "bold")).grid(row=5, columnspan=4, padx=10, pady=10)

  # Row 7
  tb.Label(guardian_info_frame, text="Income Source: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=6, column=0, padx=5, pady=5, sticky='w')
  income_source_entry = tb.Entry(guardian_info_frame, bootstyle="default", font=("Arial", 12))
  income_source_entry.grid(row=6, column=1, padx=5, pady=5, sticky='ew')

  # Row 8
  tb.Label(guardian_info_frame, text="Annual Income: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=7, column=0, padx=5, pady=5, sticky='w')
  annual_income_entry = tb.Entry(guardian_info_frame, bootstyle="default", font=("Arial", 12))
  annual_income_entry.grid(row=7, column=1, padx=5, pady=5, sticky='ew')

  # Row 9
  submit_guardian_info_button = tb.Button(guardian_info_frame, text="Submit Economic Status", bootstyle="danger", command=lambda: economic_state())
  submit_guardian_info_button.grid(row=8, columnspan=4, sticky="ew", padx=300, pady=10)


  # SCHOOL GRADUATED TAB
  school_grad_frame = tb.Frame(content_frame, bootstyle="light")
  school_grad_frame.pack(fill="both", expand=True)
  school_grad_frame.grid_columnconfigure(1, weight=1)
  school_grad_frame.grid_columnconfigure(3, weight=1)

  # Row 1
  tb.Label(school_grad_frame, text="School Name: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky='w')
  lastschool_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  lastschool_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(school_grad_frame, text="School ID", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5, pady=5, sticky='w')
  # school_address_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  # school_address_entry.grid(row=0, column=3, padx=5, pady=5, sticky='ew')
  school_id_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  school_id_entry.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

  # Row 2
  tb.Label(school_grad_frame, text="Year of graduation: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky='w')
  yog_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  yog_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(school_grad_frame, text="School type: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=1, column=2, padx=5, pady=5, sticky='w')
  school_type_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  school_type_entry.grid(row=1, column=3, padx=5, pady=5, sticky='ew')

  # Row 3
  tb.Label(school_grad_frame, text="School Address", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky='w')
  school_address_entry = tb.Entry(school_grad_frame, bootstyle="default", font=("Arial", 12))
  school_address_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky='ew')

  # Row 4
  submit_school_button = tb.Button(school_grad_frame, text="Submit School", bootstyle="danger", command=lambda: school_state_function())
  submit_school_button.grid(row=3, columnspan=4, sticky="ew", padx=300, pady=10)
  
  

  # GRADES TAB

  grades_frame = tb.Frame(content_frame, bootstyle="light")
  grades_frame.pack(fill="both", expand=True)
  grades_frame.grid_columnconfigure(1, weight=1)
  grades_frame.grid_columnconfigure(3, weight=1)

  # Row 1
  tb.Label(grades_frame, text="Report Card", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky='w')
  rc_attach_button = tb.Button(grades_frame, bootstyle="info", text="Attach File", command=upload_pdf)
  rc_attach_button.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

  rc_download_button = tb.Button(grades_frame, bootstyle="info", text="Download File", command=download_pdf)
  rc_download_button.grid(row=0, column=2, padx=5, pady=5, sticky='ew')

  # Row 2
  tb.Label(grades_frame, text="Grade 11 Grades", bootstyle="light-inverse", font=("Arial", 15, "bold")).grid(row=1, columnspan=4, padx=10)

  # Row 3
  tb.Label(grades_frame, text="First Semester GWA: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky='w')
  firstsem_entry = tb.Entry(grades_frame, bootstyle="default", font=("Arial", 12))
  firstsem_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

  tb.Label(grades_frame, text="Second Semester GWA: ", bootstyle="light-inverse", font=("Arial", 12, "bold")).grid(row=2, column=2, padx=5, pady=5, sticky='w')
  secondsem_entry = tb.Entry(grades_frame, bootstyle="default", font=("Arial", 12))
  secondsem_entry.grid(row=2, column=3, padx=5, pady=5, sticky='ew')

  # Row 4
  submit_button1 = tb.Button(grades_frame, text="Submit", bootstyle="danger", command=lambda: grades_state_function(infoID))
  submit_button1.grid(row=3, columnspan=4, sticky="ew", padx=300, pady=100)

  

  

    
  # FINALIZE FORM
  global finalize_frame
  finalize_frame = tb.Frame(content_frame, bootstyle="light")
  finalize_frame.pack(fill="both", expand=True)
  finalize_frame.grid_columnconfigure(1, weight=1)
  finalize_frame.grid_columnconfigure(3, weight=1)

  generate_final_frame()

  
  


  

  # ADD frames to notebook
  app_form_notebook.add(personal_info_frame, text="Personal Information")
  app_form_notebook.add(contact_info_frame, text="Contact Information")
  app_form_notebook.add(guardian_info_frame, text="Guardian Information and Economic Status")
  app_form_notebook.add(school_grad_frame, text="Last School Attended")
  app_form_notebook.add(grades_frame, text="Grades (Grade 11)")
  app_form_notebook.add(finalize_frame, text="Finalize Application")
