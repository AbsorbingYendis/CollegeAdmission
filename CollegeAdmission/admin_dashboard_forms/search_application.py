import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def search_application(content_frame):
  
  # remove all widgets in content_frame
  for widget in content_frame.winfo_children():
        widget.destroy()



  frame = tb.Frame(content_frame, bootstyle="default")
  frame.pack(side=TOP)
  # Search label
  search_label = tk.Label(frame, text="Search Applications", bg="white", fg="black", font=('Helvetica', 18, 'bold'))
  search_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

  # Search field
  entry_search = tb.Entry(frame, width=50)
  entry_search.grid(row=1, column=0, padx=10, pady=10, sticky="w")

  # Search button
  search_button = tb.Button(frame, text="Search", command=search_application)
  search_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

  # Result label
  result_label = tk.Label(frame, text='Result against "Amit" keyword', bg="white", fg="black", font=('Helvetica', 14))
  result_label.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")

  # Treeview for displaying results
  columns = ('S.NO', 'Course Applied', 'First Name', 'Last Name', 'Mobile Number', 'Email', 'Action')
  treeview = tb.Treeview(frame, columns=columns, show='headings')
  treeview.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

  # Define headings
  for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, anchor='center', width=100)

  # Add scrollbars
  scrollbar_y = tb.Scrollbar(frame, orient="vertical", command=treeview.yview)
  scrollbar_y.grid(row=3, column=2, sticky="ns")
  treeview.configure(yscroll=scrollbar_y.set)

  # Adjust layout to fit the window
  content_frame.grid_rowconfigure(3, weight=1)
  content_frame.grid_columnconfigure(1, weight=1)