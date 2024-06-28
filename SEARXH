import tkinter as tk
from tkinter import ttk

# Function to search applications
def search_applications():
    search_term = entry_search.get()
    # For demonstration, we'll add a static row to the treeview
    # In a real application, you'd query a database or another data source
    treeview.insert('', 'end', values=('1', 'MSC', 'Amit', 'Kumar Singh', '1236987410', 'amitk@gmail.com', 'View Details'))

# Function to create a gradient background
def create_gradient(canvas, color1, color2):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    limit = height  # Gradient to fill the entire height

    (r1, g1, b1) = canvas.winfo_rgb(color1)
    (r2, g2, b2) = canvas.winfo_rgb(color2)

    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color, width=2)

# Create the main window
root = tk.Tk()
root.title("Search Application")
root.geometry("900x700")

# Create a canvas to draw the gradient
canvas = tk.Canvas(root, width=900, height=700)
canvas.pack(fill=tk.BOTH, expand=True)

# Draw the gradient background
canvas.bind("<Configure>", lambda event: create_gradient(canvas, "#b04c4c", "#b04c4c"))

# Create a frame for the form elements
form_frame = tk.Frame(canvas, bg="white", bd=2, relief=tk.GROOVE)
form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.7)

# Search label
search_label = tk.Label(form_frame, text="Search Applications", bg="white", fg="black", font=('Helvetica', 18, 'bold'))
search_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

# Search field
entry_search = ttk.Entry(form_frame, width=50)
entry_search.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Search button
search_button = ttk.Button(form_frame, text="Search", command=search_applications)
search_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Result label
result_label = tk.Label(form_frame, text='Result against "Amit" keyword', bg="white", fg="black", font=('Helvetica', 14))
result_label.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")

# Treeview for displaying results
columns = ('S.NO', 'Course Applied', 'First Name', 'Last Name', 'Mobile Number', 'Email', 'Action')
treeview = ttk.Treeview(form_frame, columns=columns, show='headings')
treeview.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

# Define headings
for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, anchor='center', width=100)

# Add scrollbars
scrollbar_y = ttk.Scrollbar(form_frame, orient="vertical", command=treeview.yview)
scrollbar_y.grid(row=3, column=2, sticky="ns")
treeview.configure(yscroll=scrollbar_y.set)

# Adjust layout to fit the window
form_frame.grid_rowconfigure(3, weight=1)
form_frame.grid_columnconfigure(1, weight=1)

# Run the main loop
root.mainloop()
