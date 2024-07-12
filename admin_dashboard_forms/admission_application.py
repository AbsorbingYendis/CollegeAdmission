import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import sqlite3
import subprocess

def show_all():
    load_data()
def show_pending():
    conn = sqlite3.connect("Database/CAS.db")
    cursor = conn.cursor()
    conn.commit()

    # rows = ((1,2,3,4,5,6),(11,22,33,44,55,66),(111,222,333,444,555,666))
    # for row in rows:
    #     tree.insert("", tk.END, values=row)

    # Clear the current contents of the tree
    destroy_tree()

    cursor.execute('''select Application_Form.applicationID,
courseOption.firstChoice,
User_Info.firstName,
User_Info.lastName,
User_Info.mobileNumber,
User_Info.emailAddress,
    CASE 
        WHEN Application_Form.status = 1 THEN 'Pending'
        WHEN Application_Form.status = 2 THEN 'Accepted'
        WHEN Application_Form.status = 3 THEN 'Rejected'
        ELSE 'Unknown'
    END AS status
from Application_Form 
inner join User_Info on User_Info.infoID = Application_Form.infoID
inner join courseOption on courseOption.courseOptionID = Application_Form.courseOptionID
where Application_Form.status = 1
''')
    
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("",tk.END, values=row)

    conn.close()

def show_accepted():
    conn = sqlite3.connect("Database/CAS.db")
    cursor = conn.cursor()
    conn.commit()

    # rows = ((1,2,3,4,5,6),(11,22,33,44,55,66),(111,222,333,444,555,666))
    # for row in rows:
    #     tree.insert("", tk.END, values=row)

    # Clear the current contents of the tree
    destroy_tree()

    cursor.execute('''select Application_Form.applicationID,
courseOption.firstChoice,
User_Info.firstName,
User_Info.lastName,
User_Info.mobileNumber,
User_Info.emailAddress,
    CASE 
        WHEN Application_Form.status = 1 THEN 'Pending'
        WHEN Application_Form.status = 2 THEN 'Accepted'
        WHEN Application_Form.status = 3 THEN 'Rejected'
        ELSE 'Unknown'
    END AS status
from Application_Form 
inner join User_Info on User_Info.infoID = Application_Form.infoID
inner join courseOption on courseOption.courseOptionID = Application_Form.courseOptionID
where Application_Form.status = 2
''')
    
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("",tk.END, values=row)

    conn.close()

def show_rejected():
    conn = sqlite3.connect("Database/CAS.db")
    cursor = conn.cursor()
    conn.commit()

    # rows = ((1,2,3,4,5,6),(11,22,33,44,55,66),(111,222,333,444,555,666))
    # for row in rows:
    #     tree.insert("", tk.END, values=row)

    # Clear the current contents of the tree
    destroy_tree()

    cursor.execute('''select Application_Form.applicationID,
courseOption.firstChoice,
User_Info.firstName,
User_Info.lastName,
User_Info.mobileNumber,
User_Info.emailAddress,
    CASE 
        WHEN Application_Form.status = 1 THEN 'Pending'
        WHEN Application_Form.status = 2 THEN 'Accepted'
        WHEN Application_Form.status = 3 THEN 'Rejected'
        ELSE 'Unknown'
    END AS status
from Application_Form 
inner join User_Info on User_Info.infoID = Application_Form.infoID
inner join courseOption on courseOption.courseOptionID = Application_Form.courseOptionID
where Application_Form.status = 3
''')
    
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("",tk.END, values=row)

    conn.close()


def accept_entry():
    selected_item = tree.selection()
    item_id = tree.item(selected_item[0], "values")[0]

    conn = sqlite3.connect("Database/CAS.db")
    cursor = conn.cursor()

    cursor.execute(f'''update Application_Form
set status = 2
where applicationID = {item_id}''')
    
    conn.commit()
    conn.close()

    destroy_tree()
    load_data()

def destroy_tree():
    for item in tree.get_children():
        tree.delete(item)

    
def reject_entry():
    selected_item = tree.selection()
    item_id = tree.item(selected_item[0], "values")[0]
    
    conn = sqlite3.connect("Database/CAS.db")
    cursor = conn.cursor()

    cursor.execute(f'''update Application_Form
set status = 3
where applicationID = {item_id}''')
    
    conn.commit()
    conn.close()

    destroy_tree()
    load_data()

def view_entry():
    selected_item = tree.selection()
    item_id = tree.item(selected_item[0], "values")[0]

    conn = sqlite3.connect("Database/CAS.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT accountID FROM Application_Form WHERE applicationID = ?''', (item_id,))

    account_id = cursor.fetchone()
    account_id = account_id[0]

    subprocess.Popen(["python", "GradePDF.py",f"{account_id}"])
    


def load_data():
    conn = sqlite3.connect("Database/CAS.db")
    cursor = conn.cursor()
    conn.commit()

    # rows = ((1,2,3,4,5,6),(11,22,33,44,55,66),(111,222,333,444,555,666))
    # for row in rows:
    #     tree.insert("", tk.END, values=row)

    # Clear the current contents of the tree
    destroy_tree()

    cursor.execute('''select Application_Form.applicationID,
courseOption.firstChoice,
User_Info.firstName,
User_Info.lastName,
User_Info.mobileNumber,
User_Info.emailAddress,
    CASE 
        WHEN Application_Form.status = 1 THEN 'Pending'
        WHEN Application_Form.status = 2 THEN 'Accepted'
        WHEN Application_Form.status = 3 THEN 'Rejected'
        ELSE 'Unknown'
    END AS status
from Application_Form 
inner join User_Info on User_Info.infoID = Application_Form.infoID
inner join courseOption on courseOption.courseOptionID = Application_Form.courseOptionID
''')
    
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("",tk.END, values=row)

    conn.close()


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
        text="View Form 138",
        font=font1
    )
    lblViewApplication.grid(row=0, column=0)


    # ===== Radio buttons =====
    radiobuttons_frame = tb.Frame(mainframe)
    radiobuttons_frame.grid(row=1, column=0, padx=20, sticky='nsew')

    radio_var = tk.StringVar(value="All")

    radio_all = tb.Radiobutton(radiobuttons_frame, text="All", variable=radio_var, value="All", bootstyle="primary",command=lambda: show_all())
    radio_all.grid(row=0,column=0, padx=5, pady=5)

    radio_pending = tb.Radiobutton(radiobuttons_frame, text="Pending", variable=radio_var, value="Pending", bootstyle="primary", command=lambda: show_pending())
    radio_pending.grid(row=0,column=1, padx=5, pady=5)

    radio_accepted = tb.Radiobutton(radiobuttons_frame, text="Accepted", variable=radio_var, value="Accepted", bootstyle="primary", command=lambda: show_accepted())
    radio_accepted.grid(row=0,column=2, padx=5, pady=5)

    radio_rejected = tb.Radiobutton(radiobuttons_frame, text="Rejected", variable=radio_var, value="Rejected", bootstyle="primary", command=lambda: show_rejected())
    radio_rejected.grid(row=0,column=3, padx=5, pady=5)


    # ====== LOWERFRAME ======
    lowerframe = tb.Frame(mainframe)
    lowerframe.grid(row=2, column=0, padx=20, sticky='nsew')

    # TREEVIEW
    global tree
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

    load_data()

    context_menu = tk.Menu(lowerframe, tearoff=0)
    context_menu.add_command(label="Accept", command=lambda: accept_entry())
    context_menu.add_command(label="Reject", command=reject_entry)
    context_menu.add_command(label="View Application", command=view_entry)


    # Bind right-click event to show context menu
    tree.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))


    mainframe.grid_columnconfigure(0, weight=1)
    lowerframe.grid_columnconfigure(0, weight=1)
