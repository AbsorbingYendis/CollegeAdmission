import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to handle registration
def register():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    contact_number = entry_contact_number.get()
    email = entry_email.get()
    password = entry_password.get()
    repeat_password = entry_repeat_password.get()
    # Add logic for registration (e.g., save to database, validate input)
    messagebox.showinfo("Register", f"Registered with\nName: {first_name} {last_name}\nContact: {contact_number}\nEmail: {email}")

# Function to handle login
def login():
    email = entry_email.get()
    password = entry_password.get()
    # Add logic for login (e.g., verify credentials)
    messagebox.showinfo("Login", f"Logged in with\nEmail: {email}")

# Function to handle forgot password
def forgot_password():
    email = entry_email.get()
    # Add logic for forgot password (e.g., send reset email)
    messagebox.showinfo("Forgot Password", f"Password reset link sent to {email}")

# Function to go back home
def back_home():
    # Logic for back home (e.g., navigate to home screen)
    messagebox.showinfo("Back Home", "Navigating to home screen")

# Create the main window
root = tk.Tk()
root.title("User Signup")
root.geometry("400x600")
root.configure(bg='#b04c4c')

# Style configuration
style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))

# Create a centered container frame for the form
center_frame = ttk.Frame(root, padding="20", style='TFrame')
center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Form title
ttk.Label(center_frame, text="CAMS User Signup", font=('Helvetica', 16, 'bold'), background='#f0f0f0').grid(row=0, column=0, columnspan=4, pady=10)
ttk.Label(center_frame, text="Please Sign Up", font=('Helvetica', 10), background='#f0f0f0').grid(row=1, column=0, columnspan=4, pady=5)

# First Name
ttk.Label(center_frame, text="First Name", background='#f0f0f0').grid(row=2, column=0, padx=10, pady=10, sticky='E')
entry_first_name = ttk.Entry(center_frame)
entry_first_name.grid(row=2, column=1, padx=10, pady=10, sticky='W')

# Last Name
ttk.Label(center_frame, text="Last Name", background='#f0f0f0').grid(row=2, column=2, padx=10, pady=10, sticky='E')
entry_last_name = ttk.Entry(center_frame)
entry_last_name.grid(row=2, column=3, padx=10, pady=10, sticky='W')

# Contact Number
ttk.Label(center_frame, text="Contact Number", background='#f0f0f0').grid(row=3, column=0, padx=10, pady=10, sticky='E')
entry_contact_number = ttk.Entry(center_frame)
entry_contact_number.grid(row=3, column=1, padx=10, pady=10, columnspan=3, sticky='WE')

# Email
ttk.Label(center_frame, text="Email Address", background='#f0f0f0').grid(row=4, column=0, padx=10, pady=10, sticky='E')
entry_email = ttk.Entry(center_frame)
entry_email.grid(row=4, column=1, padx=10, pady=10, columnspan=3, sticky='WE')

# Password
ttk.Label(center_frame, text="Password", background='#f0f0f0').grid(row=5, column=0, padx=10, pady=10, sticky='E')
entry_password = ttk.Entry(center_frame, show='*')
entry_password.grid(row=5, column=1, padx=10, pady=10, columnspan=3, sticky='WE')

# Repeat Password
ttk.Label(center_frame, text="Repeat Password", background='#f0f0f0').grid(row=6, column=0, padx=10, pady=10, sticky='E')
entry_repeat_password = ttk.Entry(center_frame, show='*')
entry_repeat_password.grid(row=6, column=1, padx=10, pady=10, columnspan=3, sticky='WE')

# Register and Login buttons
ttk.Button(center_frame, text="Register", command=register).grid(row=7, column=0, columnspan=2, pady=20, padx=10, sticky='E')
ttk.Button(center_frame, text="Login", command=login).grid(row=7, column=2, columnspan=2, pady=20, padx=10, sticky='W')

# Forgot Password and Back Home links
forgot_password_label = ttk.Label(center_frame, text="Forgot Password?", foreground="blue", background='#f0f0f0', cursor="hand2")
forgot_password_label.grid(row=8, column=0, columnspan=4, pady=5)
forgot_password_label.bind("<Button-1>", lambda e: forgot_password())

back_home_label = ttk.Label(center_frame, text="Back Home", foreground="blue", background='#f0f0f0', cursor="hand2")
back_home_label.grid(row=9, column=0, columnspan=4, pady=5)
back_home_label.bind("<Button-1>", lambda e: back_home())

# Run the main loop
root.mainloop()
