import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import random
import string

# Global variables for verification code and registered email
verification_code = None
registered_email = None

# Function for login button
def login_action():
    global verification_code
    entered_email = entry_email.get()
    entered_password = entry_password.get()
    entered_code = entry_verification_code.get()

    if entered_email == "qwe" and entered_password == "123" and entered_code == verification_code:
        messagebox.showinfo("Login Successful", f"Welcome, {entered_email}!")
    else:
        messagebox.showerror("Login Failed", "Invalid email, password, or verification code.")


# Function for generating verification code with symbols
# Function for generating verification code with symbols
def generate_code():
    global verification_code
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    code_length = 4  # total length of code
    code_digits = random.choices(string.digits, k=code_length)  # Random digits for the code
    code_symbols = random.choices(symbols, k=code_length)  # Random symbols for display only
    combined_code = ''.join(code_symbols[i] + code_digits[i] for i in range(code_length))  # Combine symbols and digits
    verification_code = ''.join(code_digits)  # Store only digits for verification
    messagebox.showinfo("Verification Code", f"Generated code: {combined_code}")

def register_action():
    global registered_email
    registered_email = entry_email.get()
    messagebox.showinfo("Register", f"Registration in progress")

# Main application window
app = tk.Tk()
app.title("CAMS User Login")
app.geometry("1280x720")
app.configure(bg="#b04c4c")

# Create a frame
frame = tk.Frame(app, bg="#e0f7fa", width=650, height=550)
frame.pack(expand=True)
frame.pack_propagate(False)

# Labels and entries inside the frame
label_email = tk.Label(frame, text="Registered Email or Contact Number:", font=("Arial", 12), bg="#e0f7fa")
label_email.pack(pady=(60, 10))

entry_email = tk.Entry(frame, font=("Arial", 12), width=30)
entry_email.pack()

label_password = tk.Label(frame, text="Password:", font=("Arial", 12), bg="#e0f7fa")
label_password.pack(pady=(20, 5))

entry_password = tk.Entry(frame, show='*', font=("Arial", 12), width=30)
entry_password.pack()

# Verification code section
label_verification_code = tk.Label(frame, text="Verification Code:", font=("Arial", 12), bg="#e0f7fa")
label_verification_code.pack(pady=(20, 5))

entry_verification_code = tk.Entry(frame, font=("Arial", 12), width=10)
entry_verification_code.pack()

# Buttons inside the frame

btn_generate_code = tk.Button(frame, text="Generate Code", font=("Arial", 12), bg="#4caf50", fg="white", width=15, command=generate_code)
btn_generate_code.pack(pady=(20, 5))

btn_login = tk.Button(frame, text="Login", font=("Arial", 12), bg="#1976d2", fg="white", width=10, command=login_action)
btn_login.pack(pady=(40, 5))

btn_register = tk.Button(frame, text="Register", font=("Arial", 12), bg="#d32f2f", fg="white", width=10, command=register_action)
btn_register.pack(pady=(20, 5))

# Links inside the frame
label_forgot_password = tk.Label(frame, text="Forgot password?", font=("Arial", 10), fg="#1e88e5", bg="#e0f7fa", cursor="hand2")
label_forgot_password.pack(pady=(40, 5))
label_forgot_password.bind("<Button-1>", lambda e: messagebox.showinfo("Forgot Password", "Password recovery not implemented."))

label_back_home = tk.Label(frame, text="Back Home", font=("Arial", 10), fg="#1e88e5", bg="#e0f7fa", cursor="hand2")
label_back_home.pack(pady=(5, 5))
label_back_home.bind("<Button-1>", lambda e: messagebox.showinfo("Back Home", "Going back to Home not implemented."))

app.mainloop()