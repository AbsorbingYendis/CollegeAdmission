import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import subprocess


# Function to handle registration
def register():
    user_name = entry_user_name.get()
    email = entry_email.get()
    password = entry_password.get()
    repeat_password = entry_repeat_password.get()
    # Add logic for registration (e.g., save to database, validate input)
    if (user_name=="" or email=="" or password == "" or repeat_password == ""):
        messagebox.showinfo("Registration Failed","Please enter all fields!")
    else:

            # Insert values into the database
            conn = sqlite3.connect('Database/CAS.db')
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO User_Account (username, emailAddress, password)
                VALUES (?, ?, ?)
                """, (user_name, email, password))
           
            conn.commit()
            conn.close()

            messagebox.showinfo("Registration Successful", f"Registered with\nUsername: {user_name}\nEmail: {email}")

            # Go back to Applicant_Login form
            root.destroy()
            subprocess.Popen(["python", "Applicant_Login.py"])


# Function to handle forgot password
def forgot_password():
    email = entry_email.get()
    # Add logic for forgot password (e.g., send reset email)
    messagebox.showinfo("Forgot Password", f"Password reset link sent to {email}")

# Function to go back home
def back_home():
    # Logic for back home (e.g., navigate to home screen)
    root.destroy()
    subprocess.Popen(["python", "Applicant_Login.py"])

# Create the main window
root = tk.Tk()
root.title("User Signup")
root.geometry("550x550")
root.configure(bg='#b04c4c')
root.attributes('-topmost', True)


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

# Username
ttk.Label(center_frame, text="Username", background='#f0f0f0').grid(row=2, column=0, padx=10, pady=10, sticky='E')
entry_user_name = ttk.Entry(center_frame)
entry_user_name.grid(row=2, column=1, padx=10, pady=10, sticky='W')

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

# Register button
ttk.Button(center_frame, text="Register", command=register).grid(row=7, column=0, columnspan=2, pady=20, padx=10, sticky='E')

# Forgot Password and Back Home links
forgot_password_label = ttk.Label(center_frame, text="Forgot Password?", foreground="blue", background='#f0f0f0', cursor="hand2")
forgot_password_label.grid(row=8, column=0, columnspan=4, pady=5)
forgot_password_label.bind("<Button-1>", lambda e: forgot_password())

back_home_label = ttk.Label(center_frame, text="Back Home", foreground="blue", background='#f0f0f0', cursor="hand2")
back_home_label.grid(row=9, column=0, columnspan=4, pady=5)
back_home_label.bind("<Button-1>", lambda e: back_home())

# Run the main loop
root.mainloop()