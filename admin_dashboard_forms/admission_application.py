import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def admission_application(content_frame):
    # remove all widgets in content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    font1 = ('Arial', 15, 'bold')

    # ====== MAINFRAME ======
    mainframe = tb.Frame(content_frame)
    mainframe.pack(fill='both', expand=True)

    # ====== UPPERFRAME ======
    upperframe = tb.Frame(mainframe)
    upperframe.grid(row=0, column=0, pady=20, padx=20, sticky='w')

    lblViewApplication = tb.Label(
        upperframe,
        text="View Application",
        font=font1
    )
    lblViewApplication.grid(row=0, column=0)

    # ====== LOWERFRAME ======
    lowerframe = tb.Frame(mainframe)
    lowerframe.grid(row=1, column=0, padx=20, sticky='nsew')

    # TREEVIEW
    tree = tb.Treeview(
        lowerframe,
        columns=('S.NO', 'Course Applied', 'First Name', 'Last Name', 'Mobile Number', 'Email', 'Status', 'Action'),
        show='headings',
        height=15
    )

    tree.heading('S.NO', text='S.NO')
    tree.heading('Course Applied', text='Course Applied')
    tree.heading('First Name', text='First Name')
    tree.heading('Last Name', text='Last Name')
    tree.heading('Mobile Number', text='Mobile Number')
    tree.heading('Email', text='Email')
    tree.heading('Status', text='Status')
    tree.heading('Action', text='Action')

    tree.column('S.NO', width=50, anchor='center')
    tree.column('Course Applied', width=100, anchor='center')
    tree.column('First Name', width=100, anchor='center')
    tree.column('Last Name', width=100, anchor='center')
    tree.column('Mobile Number', width=100, anchor='center')
    tree.column('Email', width=100, anchor='center')
    tree.column('Status', width=100, anchor='center')
    tree.column('Action', width=100, anchor='center')

    tree.pack(fill='both', expand=True)

    mainframe.grid_columnconfigure(0, weight=1)
    lowerframe.grid_columnconfigure(0, weight=1)
