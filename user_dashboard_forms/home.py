import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sqlite3
from tkinter import messagebox


def load_status(accountID):
      conn = sqlite3.connect("Database/CAS.db")
      cursor = conn.cursor()
      # cursor.execute('''SELECT status FROM Application_Form WHERE accountID = ?''', (accountID,))

      cursor.execute(f'''SELECT status FROM Application_Form WHERE accountID = {accountID}''')

      status = cursor.fetchone()
      # messagebox.showinfo("Status", f"{status[0]}...{accountID}")
      if status[0] == 1:
            label_progress_status.config(text="Pending")
      elif status[0] == 2:
           label_progress_status.config(text="Accepted",bootstyle="success-inverse")
      else:
           label_progress_status.config(text="Rejected", bootstyle="danger-inverse")


def home(content_frame, accountID):
  
  # remove all widgets in content_frame
  for widget in content_frame.winfo_children():
        widget.destroy()

  frame_widgets = tb.Frame(content_frame, bootstyle="light")
  frame_widgets.pack(fill=BOTH, expand=1,padx=20,pady=20)

  # Application form progress 
  frame_progress_status = tb.Frame(frame_widgets, bootstyle="light")
  frame_progress_status.pack(pady=(30,0))

  tb.Label(frame_progress_status, bootstyle="light-inverse", text = "Application Form Progress Status: ", font=("Arial",15, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="ew")
  
  global label_progress_status
  label_progress_status = tb.Label(frame_progress_status, bootstyle="danger", text = "Not yet done", font=("Arial",12,"bold"))
  label_progress_status.grid(row=0, column=1, padx=10, pady=10, sticky="ew")


  load_status(accountID)

