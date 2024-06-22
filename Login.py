import tkinter as tk
from tkinter import ttk
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
    reg_window.geometry("300x200")  # Set resolution for the registration window

    tk.Label(reg_window, text="Username").grid(row=0, column=0, padx=10, pady=5, sticky='w')
    reg_entry_username = tk.Entry(reg_window)
    reg_entry_username.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(reg_window, text="Password").grid(row=1, column=0, padx=10, pady=5, sticky='w')
    reg_entry_password = tk.Entry(reg_window, show="*")
    reg_entry_password.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(reg_window, text="Register", command=register_user).grid(row=2, column=0, columnspan=2, pady=10)

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

# Function to create gradient
def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        r1, g1, b1 = canvas.winfo_rgb(color1)
        r2, g2, b2 = canvas.winfo_rgb(color2)

        r = int(r1 + (r2 - r1) * (i / height))
        g = int(g1 + (g2 - g1) * (i / height))
        b = int(b1 + (b2 - b1) * (i / height))

        color = f'#{r//256:02x}{g//256:02x}{b//256:02x}'
        canvas.create_line(0, i, width, i, fill=color)

# GUI setup
root = tk.Tk()
root.title("Login Page")

# Left frame for gradient background
left_frame = tk.Frame(root, width=900, height=root.winfo_screenheight())
left_frame.pack(side='left', fill='y')

left_canvas = tk.Canvas(left_frame, width=900, height=root.winfo_screenheight(), highlightthickness=0)
left_canvas.pack(fill='both', expand=True)

# Create gradient in left canvas
create_gradient(left_canvas, 900, root.winfo_screenheight(), '#000000', '#8B4513')

# Right frame for login form
right_frame = tk.Frame(root, bg='#000000', width=1000, height=root.winfo_screenheight())
right_frame.pack(side='right', fill='both', expand=True)

style = ttk.Style()
style.configure('TEntry', padding=10, relief="flat", font=('Arial', 14))
style.configure('TButton', padding=10, background='#0052cc', foreground='white')
style.map('TButton', background=[('active', '#0041b3')])

# Custom style for the SIGN IN button
style.configure('Black.TButton', padding=10, font=('Arial', 14), background='#0052cc', foreground='black')
style.map('Black.TButton', background=[('active', '#0041b3')])

# Title and Logo
logo = tk.Label(right_frame, text="NOAKAY STATE UNIVERSITY", bg='#000000', fg='white', font=('Arial', 18))
logo.pack(pady=(50, 10))

app_title = tk.Label(right_frame, text="NOAKAY APPLY", bg='#000000', fg='white', font=('Arial', 24))
app_title.pack(pady=(10, 30))

# Container frame for form elements
container = tk.Frame(right_frame, bg='#000000')
container.pack(anchor='center', padx=10, pady=10)


# Form fields
tk.Label(container, text="Username:", bg='#000000', fg='white', font=('Arial', 14)).grid(row=0, column=0, padx=20, pady=10, sticky='w')
entry_username = ttk.Entry(container, style='TEntry',width=30)
entry_username.grid(row=0, column=1, padx=20, pady=10)

tk.Label(container, text="Password:", bg='#000000', fg='white', font=('Arial', 14)).grid(row=1, column=0, padx=20, pady=10, sticky='w')
entry_password = ttk.Entry(container, show="*", style='TEntry', width=30)
entry_password.grid(row=1, column=1, padx=20, pady=10)

tk.Label(container, text="Digital Code", bg='#000000', fg='white', font=('Arial', 14)).grid(row=2, column=0, padx=20, pady=10, sticky='w')
entry_code = ttk.Entry(container, style='TEntry',width=30)
entry_code.grid(row=2, column=1, padx=20, pady=10)

# Login button
login_button = ttk.Button(container, text="Log In", style='Black.TButton', command=login)
login_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# Sign Up button
signup_button = ttk.Button(container, text="Sign Up", style='Black.TButton', command=open_registration)
signup_button.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

root.mainloop()
