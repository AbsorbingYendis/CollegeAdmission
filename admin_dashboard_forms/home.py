import tkinter as tk
from ttkbootstrap.widgets import Frame, Label
import ttkbootstrap as tb
import sqlite3

listed_courses = 0
registered_courses = 0
total_application = 0
pending_application = 0
selected_application = 0
rejected_application = 0

def refresh(content_frame):
    load_tables()
    home(content_frame)
def load_tables():
    global listed_courses, registered_courses, total_application, pending_application, selected_application, rejected_application

    conn =  sqlite3.connect("Database/CAS.db")
    cursor = conn.cursor()
    conn.commit()
    
    cursor.execute('''select * from Course
''')
    listed_courses = len(cursor.fetchall())

    cursor.execute('''select * from User_Account
''')
    registered_courses = len(cursor.fetchall())

    cursor.execute('''select * from Application_Form
''')
    total_application = len(cursor.fetchall())

    cursor.execute('''select * from Application_Form where status = 1
''')
    pending_application = len(cursor.fetchall())

    cursor.execute('''select * from Application_Form where status = 2
''')
    selected_application = len(cursor.fetchall())

    cursor.execute('''select * from Application_Form where status = 3
''')
    rejected_application = len(cursor.fetchall())

def home(content_frame):
    load_tables()
    # Clear content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    font1= ('Arial', 15, 'bold')

    # Create main frame
    mainframe = tb.Frame(content_frame)
    mainframe.pack(fill='both', expand=True)
    
    # Configure grid to expand with window resize
    mainframe.grid_columnconfigure(0, weight=1)

    # ====== UPPER FRAME ======
    upperframe = tb.Frame(mainframe, padding=10)
    upperframe.grid(row=0, column=0, sticky='nsew')
    upperframe.grid_columnconfigure((0, 1, 2), weight=1)
    
    # Left frame
    left_upper = tb.Frame(upperframe, padding=10, bootstyle="info")
    left_upper.grid(pady=10, padx=10, column=0, row=0, sticky='nsew')
    lblNumCourse = tb.Label(left_upper, text=f"{listed_courses}", bootstyle="info-inverse", font=font1) # change nalang yung data then lagay sa 'text'
    lblNumCourse.grid(row=0, column=0, sticky='w')
    lblListedCourse = tb.Label(left_upper, text="Listed Courses", bootstyle="info-inverse")
    lblListedCourse.grid(row=1, column=0, padx=90, pady=20, sticky='w')

    # Middle frame
    middle_upper = tb.Frame(upperframe, padding=10, bootstyle="warning")
    middle_upper.grid(pady=10, padx=10, column=1, row=0, sticky='nsew')
    lblNumRegisteredUsers = tb.Label(middle_upper, text=f"{registered_courses}", bootstyle="warning-inverse", font=font1) # change nalang yung data then lagay sa 'text'
    lblNumRegisteredUsers.grid(row=0, column=0, sticky='w')
    lblRegisteredUsers = tb.Label(middle_upper, text="Registered Users", bootstyle="warning-inverse")
    lblRegisteredUsers.grid(row=1, column=0, padx=90, pady=20, sticky='w')

    # Right frame
    right_upper = tb.Frame(upperframe, padding=10, bootstyle="success")
    right_upper.grid(pady=10, padx=10, column=2, row=0, sticky='nsew')
    lblNumTotalApplication = tb.Label(right_upper, text=f"{total_application}", bootstyle="success-inverse",  font=font1) # change nalang yung data then lagay sa 'text'
    lblNumTotalApplication.grid(row=0, column=0, sticky='w')
    lblTotalApplication = tb.Label(right_upper, text="Total Application", bootstyle="success-inverse")
    lblTotalApplication.grid(row=1, column=0, padx=90, pady=20, sticky='w')
    
    # ======= LOWER FRAME ======
    lowerframe = tb.Frame(mainframe, padding=10)
    lowerframe.grid(row=1, column=0, sticky='nsew')
    lowerframe.grid_columnconfigure((0, 1, 2), weight=1)
    
    # Left frame
    left_lower = tb.Frame(lowerframe, padding=10, bootstyle="info")
    left_lower.grid(pady=10, padx=10, column=0, row=0, sticky='nsew')
    lblNumPending = tb.Label(left_lower, text=f"{pending_application}", bootstyle="info-inverse", font=font1) # change nalang yung data then lagay sa 'text'
    lblNumPending.grid(row=0, column=0, sticky='w')
    lblPendingApplication = tb.Label(left_lower, text="Pending Application", bootstyle="info-inverse")
    lblPendingApplication.grid(row=1, column=0, padx=70, pady=20, sticky='w')

    # Middle frame
    middle_lower = tb.Frame(lowerframe, padding=10, bootstyle="warning")
    middle_lower.grid(pady=10, padx=10, column=1, row=0, sticky='nsew')
    lblNumSelected = tb.Label(middle_lower, text=f"{selected_application}", bootstyle="warning-inverse",  font=font1) # change nalang yung data then lagay sa 'text'
    lblNumSelected.grid(row=0, column=0, sticky='w')
    lblSelectedApplication = tb.Label(middle_lower, text="Selected Application", bootstyle="warning-inverse")
    lblSelectedApplication.grid(row=1, column=0, padx=70, pady=20, sticky='w')

    # Right frame
    right_lower = tb.Frame(lowerframe, padding=10, bootstyle="danger")
    right_lower.grid(pady=10, padx=10, column=2, row=0, sticky='nsew')
    lblNumRejected = tb.Label(right_lower, text=f"{rejected_application}", bootstyle="danger-inverse",  font=font1) # change nalang yung data then lagay sa 'text'
    lblNumRejected.grid(row=0, column=0, sticky='w')
    lblRejectedApplication = tb.Label(right_lower, text="Rejected Application", bootstyle="danger-inverse")
    lblRejectedApplication.grid(row=1, column=0, padx=70, pady=20, sticky='w')

    button = tb.Button(lowerframe, text="Refresh", bootstyle="warning", command=lambda: refresh(content_frame))
    button.grid(row=2,column=0,pady=15)