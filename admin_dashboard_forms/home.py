import tkinter as tk
from ttkbootstrap.widgets import Frame, Label
import ttkbootstrap as tb

def home(content_frame):
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
    lblNumCourse = tb.Label(left_upper, text="0000", bootstyle="info-inverse", font=font1) # change nalang yung data then lagay sa 'text'
    lblNumCourse.grid(row=0, column=0, sticky='w')
    lblListedCourse = tb.Label(left_upper, text="Listed Courses", bootstyle="info-inverse")
    lblListedCourse.grid(row=1, column=0, padx=90, pady=20, sticky='w')

    # Middle frame
    middle_upper = tb.Frame(upperframe, padding=10, bootstyle="warning")
    middle_upper.grid(pady=10, padx=10, column=1, row=0, sticky='nsew')
    lblNumRegisteredUsers = tb.Label(middle_upper, text="0000", bootstyle="warning-inverse", font=font1) # change nalang yung data then lagay sa 'text'
    lblNumRegisteredUsers.grid(row=0, column=0, sticky='w')
    lblRegisteredUsers = tb.Label(middle_upper, text="Registered Courses", bootstyle="warning-inverse")
    lblRegisteredUsers.grid(row=1, column=0, padx=90, pady=20, sticky='w')

    # Right frame
    right_upper = tb.Frame(upperframe, padding=10, bootstyle="success")
    right_upper.grid(pady=10, padx=10, column=2, row=0, sticky='nsew')
    lblNumTotalApplication = tb.Label(right_upper, text="0000", bootstyle="success-inverse",  font=font1) # change nalang yung data then lagay sa 'text'
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
    lblNumPending = tb.Label(left_lower, text="0000", bootstyle="info-inverse", font=font1) # change nalang yung data then lagay sa 'text'
    lblNumPending.grid(row=0, column=0, sticky='w')
    lblPendingApplication = tb.Label(left_lower, text="Pending Application", bootstyle="info-inverse")
    lblPendingApplication.grid(row=1, column=0, padx=70, pady=20, sticky='w')

    # Middle frame
    middle_lower = tb.Frame(lowerframe, padding=10, bootstyle="warning")
    middle_lower.grid(pady=10, padx=10, column=1, row=0, sticky='nsew')
    lblNumSelected = tb.Label(middle_lower, text="0000", bootstyle="warning-inverse",  font=font1) # change nalang yung data then lagay sa 'text'
    lblNumSelected.grid(row=0, column=0, sticky='w')
    lblSelectedApplication = tb.Label(middle_lower, text="Selected Application", bootstyle="warning-inverse")
    lblSelectedApplication.grid(row=1, column=0, padx=70, pady=20, sticky='w')

    # Right frame
    right_lower = tb.Frame(lowerframe, padding=10, bootstyle="danger")
    right_lower.grid(pady=10, padx=10, column=2, row=0, sticky='nsew')
    lblNumRejected = tb.Label(right_lower, text="0000", bootstyle="danger-inverse",  font=font1) # change nalang yung data then lagay sa 'text'
    lblNumRejected.grid(row=0, column=0, sticky='w')
    lblRejectedApplication = tb.Label(right_lower, text="Rejected Application", bootstyle="danger-inverse")
    lblRejectedApplication.grid(row=1, column=0, padx=70, pady=20, sticky='w')