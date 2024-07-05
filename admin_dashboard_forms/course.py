import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sqlite3
from tkinter import messagebox

# Function to fetch data from SQLite database
def load_data(search_query=""):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            CourseId INTEGER PRIMARY KEY AUTOINCREMENT,
            CourseName TEXT NOT NULL
        )
    """)
    conn.commit()

    # Clear the current contents of the tree
    for item in tree.get_children():
        tree.delete(item)

    # Modify query based on search_query
    if search_query:
        cursor.execute("SELECT * FROM students WHERE CourseName LIKE ?", (search_query + '%',))
    else:
        cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    # Populate the Treeview
    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()

# Function to handle editing an entry
def edit_entry(content_frame):
    selected_item = tree.selection()
    if selected_item:
        item_id = selected_item[0]
        values = tree.item(item_id, "values")

        edit_window = tk.Toplevel(content_frame)
        edit_window.title("Edit Entry")

        tk.Label(edit_window, text="Course Name:").grid(row=0, column=0, padx=10, pady=5)
        entry_course = tk.Entry(edit_window)
        entry_course.grid(row=0, column=1, padx=10, pady=5)
        entry_course.insert(0, values[1])

        def save_changes():
            new_values = (entry_course.get(), values[0])
            update_entry(new_values)
            edit_window.destroy()

        tk.Button(edit_window, text="Save", command=save_changes).grid(row=1, column=0, columnspan=2, pady=10)

        center_window(edit_window)  # Center the edit window
    else:
        messagebox.showwarning("No Selection", "Please select an entry to edit.")

# Function to update an entry in SQLite database
def update_entry(new_values):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    query = "UPDATE students SET CourseName=? WHERE CourseId=?"
    cursor.execute(query, new_values)
    conn.commit()
    conn.close()
    load_data(search_var.get())  # Refresh Treeview after update

# Function to handle deleting an entry
def delete_entry():
    selected_item = tree.selection()
    if selected_item:
        item_id = tree.item(selected_item[0], "values")[0]  # Get the CourseId
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this entry?"):
            conn = sqlite3.connect("students.db")
            cursor = conn.cursor()
            query = "DELETE FROM students WHERE CourseId=?"
            cursor.execute(query, (item_id,))
            conn.commit()
            conn.close()
            load_data(search_var.get())  # Refresh Treeview after delete
    else:
        messagebox.showwarning("No Selection", "Please select an entry to delete.")

def add_entry(manage_course):
    add_window = tk.Toplevel(manage_course)
    add_window.title("Add Entry")

    # Window layout
    tk.Label(add_window, text="Course Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_course = tk.Entry(add_window)
    entry_course.grid(row=0, column=1, padx=10, pady=5)

    def create_entry():
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        entry = entry_course.get()
        if not entry.strip():
            messagebox.showwarning("Input Error", "Course Name cannot be empty.")
            return
        query = "INSERT INTO students(CourseName) values (?)"
        cursor.execute(query, (entry,))
        conn.commit()
        conn.close()
        load_data(search_var.get())  # Refresh Treeview after update
        add_window.destroy()

    tk.Button(add_window, text="Save", command=create_entry).grid(row=1, column=0, columnspan=2, pady=10)

    center_window(add_window)  # Center the add window

# Function to handle search
def search_data():
    search_query = search_var.get()
    load_data(search_query)

# Utility function to center a window on the screen
def center_window(window):
    window.update_idletasks()  # Ensure the window size is calculated
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

def course(content_frame):
  
  # remove all widgets in content_frame
  for widget in content_frame.winfo_children():
        widget.destroy()

  label = tb.Label(content_frame, text="This is course frame")
  label.pack()

  # Create notebook
  nb = tb.Notebook(content_frame, bootstyle="primary")
  nb.pack(fill=BOTH, expand=1)

  # Create frames for notebook
  add_course = tb.Frame(content_frame, bootstyle="light")
  add_course.pack(fill="both", expand=True)
  manage_course = tb.Frame(content_frame, bootstyle="light")
  manage_course.pack(fill="both", expand=True)

  # Manage Course tab
#   manage_course.title("Grid View with Edit and Delete")
#   manage_course.state('zoomed')

  upper_frame = tk.Frame(manage_course, bg="#e0f7fa")
  upper_frame.pack(pady=30, fill=tk.X)

  label_title = tk.Label(upper_frame, text="Manage Course", font=("Arial", 20, "bold"))
  label_title.pack(side="left", padx=(20, 200))

  btn_add = tk.Button(upper_frame, text="Add new course", font=("Arial", 12), bg="#4caf50", width=20, height=2, command=lambda: add_entry(manage_course))
  btn_add.pack(side="right", padx=(10, 20))

  # Search feature
  search_frame = tk.Frame(manage_course, bg="#e0f7fa")
  search_frame.pack(padx=20, pady=(1, 30))

  global search_var
  search_var = tk.StringVar()
  entry_search = tk.Entry(search_frame, textvariable=search_var, font=("Arial", 14))
  entry_search.pack(side="left", padx=10)

  btn_search = tk.Button(search_frame, text="Search", font=("Arial", 14), command=search_data)
  btn_search.pack(side="left", padx=10)

  # Create a Treeview widget
  global tree
  tree = tb.Treeview(manage_course, columns=("Course ID", "Course Name"), show='headings')
  tree.pack(fill=tk.BOTH, expand=True)

  # Define headings
  tree.heading("Course ID", text="Course ID")
  tree.heading("Course Name", text="Course Name")

  # Adjust column widths
  tree.column("Course ID", width=100, anchor="center")
  tree.column("Course Name", width=300, anchor="center")

  # Load initial data from SQLite database
  load_data()

  # Right-click context menu
  context_menu = tk.Menu(manage_course, tearoff=0)
  context_menu.add_command(label="Edit", command=lambda: edit_entry(content_frame))
  context_menu.add_command(label="Delete", command=delete_entry)

  # Bind right-click event to show context menu
  tree.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))


  # Add frames to notebook
  nb.add(add_course, text="Add course")
  nb.add(manage_course, text="Manage course")
  