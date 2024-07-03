import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to handle user registration
def register_user():
    username = reg_entry_username.get()
    password = reg_entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    # Check if username already exists
    c.execute('SELECT * FROM users WHERE username=?', (username,))
    if c.fetchone():
        messagebox.showerror("Error", "Username already exists")
    else:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
        reg_window.destroy()

    conn.close()

# Function to open the registration window
def open_registration():
    global reg_window, reg_entry_username, reg_entry_password

    reg_window = tk.Toplevel(root)
    reg_window.title("Sign Up")

    tk.Label(reg_window, text="Username").pack()
    reg_entry_username = tk.Entry(reg_window)
    reg_entry_username.pack()

    tk.Label(reg_window, text="Password").pack()
    reg_entry_password = tk.Entry(reg_window, show="*")
    reg_entry_password.pack()

    tk.Button(reg_window, text="Register", command=register_user).pack()

# Function to handle login button click
def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    result = c.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Incorrect username or password")

    conn.close()

# GUI setup
root = tk.Tk()
root.title("Login Page")

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack()
tk.Button(root, text="Sign Up", command=open_registration).pack()

root.mainloop()