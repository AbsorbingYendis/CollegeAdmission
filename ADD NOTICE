import tkinter as tk
from tkinter import messagebox, ttk

# Function to add notice
def add_notice():
    title = entry_title.get()
    description = text_description.get("1.0", tk.END)
    messagebox.showinfo("Notice Added", f"Title: {title}\nDescription: {description}")

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
root.title("Add Notice")
root.geometry("900x700")

# Create a canvas to draw the gradient
canvas = tk.Canvas(root, width=900, height=700)
canvas.pack(fill=tk.BOTH, expand=True)

# Draw the gradient background
canvas.bind("<Configure>", lambda event: create_gradient(canvas, "#b04c4c", "#b04c4c"))

# Create a frame for the form elements
form_frame = tk.Frame(canvas, bg="#b04c4c")
form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Form title
header_label = tk.Label(form_frame, text="Notice", bg="#b04c4c", fg="white", font=('Helvetica', 18, 'bold'))
header_label.grid(row=0, column=0, columnspan=2, pady=10)

# Style configuration
style = ttk.Style()
style.configure('TLabel', background='#b04c4c', foreground='white', font=('Helvetica', 14))
style.configure('TButton', font=('Helvetica', 14), padding=10)
style.configure('TEntry', font=('Helvetica', 14), padding=5)
style.configure('TText', font=('Helvetica', 14), padding=5)

# Title
ttk.Label(form_frame, text="Title").grid(row=1, column=0, padx=10, pady=10, sticky='E')
entry_title = ttk.Entry(form_frame, width=50)
entry_title.grid(row=1, column=1, padx=10, pady=10, sticky='W')

# Description
ttk.Label(form_frame, text="Description").grid(row=2, column=0, padx=10, pady=10, sticky='NE')
text_description = tk.Text(form_frame, width=48, height=10, font=('Helvetica', 14))
text_description.grid(row=2, column=1, padx=10, pady=10, sticky='W')

# Add button
add_button = ttk.Button(form_frame, text="ADD", command=add_notice)
add_button.grid(row=3, column=1, pady=20, sticky='W')

# Styling for the add button
add_button.configure(style='Add.TButton')
style.configure('Add.TButton', background='#007bff', foreground='white', font=('Helvetica', 14, 'bold'))

# Run the main loop
root.mainloop()
