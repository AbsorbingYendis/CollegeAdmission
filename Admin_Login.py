import tkinter as tk
from tkinter import messagebox
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
app.title("NSU Admin Login")
app.state('zoomed')
app.configure(bg="#b04c4c")

# Create a frame
frame = tk.LabelFrame(app, bg="#e0f7fa", width=550, height=550)
frame.pack(expand=True)
frame.pack_propagate(False)

# Labels and entries inside the frame
label_title = tk.Label(frame, text="NSU Admin Login", font=("Arial", 20, "bold"), bg="#e0f7fa")
label_title.pack(pady=(20, 20))

# Frame for email entry & label
email_frame = tk.Frame(frame, bg="#e0f7fa")
email_frame.pack(pady=(45,20))

label_email = tk.Label(email_frame, text="Email or Username:", font=("Arial", 12), bg="#e0f7fa")
label_email.pack(side="left",pady=(5, 5))

entry_email = tk.Entry(email_frame, font=("Arial", 12), width=40)
entry_email.pack(side="right",padx=(5,5))

# Frame for pass entry & label
pass_frame = tk.Frame(frame, bg="#e0f7fa")
pass_frame.pack(pady=1)

label_password = tk.Label(pass_frame, text="Password:", font=("Arial", 12), bg="#e0f7fa")
label_password.pack(side="left",pady=(5, 5),padx=(60,1))

entry_password = tk.Entry(pass_frame, show='*', font=("Arial", 12), width=40)
entry_password.pack(side="right",padx=(5,1))

# Verification code section
label_verification_code = tk.Label(frame, text="Verification Code:", font=("Arial", 12), bg="#e0f7fa")
label_verification_code.pack(pady=(10, 5))

entry_verification_code = tk.Entry(frame, font=("Arial", 12), width=10)
entry_verification_code.pack()

# Buttons and link inside the frame
btn_generate_code = tk.Button(frame, text="Generate Code", font=("Arial", 12), bg="#4caf50", fg="white", width=15, height=1, command=generate_code)
btn_generate_code.pack(pady=(20, 5))

# Frame for login and register buttons
button_frame = tk.Frame(frame, bg="#e0f7fa")
button_frame.pack(pady=(45,20))

btn_login = tk.Button(button_frame, text="Login", font=("Arial", 12), bg="#1976d2", fg="white", width=20, height=2, command=login_action)
btn_login.pack( padx=(50, 50))


label_forgot_password = tk.Label(frame, text="Forgot password?", font=("Arial", 10), fg="#1e88e5", bg="#e0f7fa", cursor="hand2")
label_forgot_password.pack(pady=(15, 10))

label_back_home = tk.Label(frame, text="Back Home", font=("Arial", 10), fg="#1e88e5", bg="#e0f7fa", cursor="hand2")
label_back_home.pack(pady=(10, 20))

# Functionality for forgot password link
def show_forgot_password_info(event):
    messagebox.showinfo("Forgot Password", "Password recovery not implemented.")

label_forgot_password.bind("<Button-1>", show_forgot_password_info)

# Functionality for back home link
def show_back_home_info(event):
    messagebox.showinfo("Back Home", "Going back to Home not implemented.")

label_back_home.bind("<Button-1>", show_back_home_info)

app.mainloop()