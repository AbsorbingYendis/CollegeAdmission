import tkinter as tk
from tkinter import messagebox, ttk

# Function to submit payment
def submit_payment():
    payment_amount = entry_payment_amount.get()
    transaction_number = entry_transaction_number.get()
    mode_of_payment = mode_var.get()
    messagebox.showinfo("Payment Submitted", f"Payment Amount: {payment_amount}\nTransaction Number: {transaction_number}\nMode of Payment: {mode_of_payment}")

# Function to choose mode of payment
def choose_mode_of_payment():
    mode_of_payment_menu.post(mode_button.winfo_rootx(), mode_button.winfo_rooty() + mode_button.winfo_height())

# Function to change password
def change_password():
    messagebox.showinfo("Change Password", "Password change functionality goes here!")

# Function to logout
def logout():
    root.quit()

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
root.title("Submit Fees")
root.geometry("900x700")

# Create a canvas to draw the gradient
canvas = tk.Canvas(root, width=900, height=700)
canvas.pack(fill=tk.BOTH, expand=True)

# Draw the gradient background
canvas.bind("<Configure>", lambda event: create_gradient(canvas, "#090979", "#4c4cb0"))

# Create a frame for the form elements
form_frame = tk.Frame(canvas, bg="#4c4cb0")
form_frame.place(relx=0.5, rely=0.5, anchor='center')  # Centering the form frame

# Add the "Admission Fees" label in the upper left corner
header_label = tk.Label(form_frame, text="Admission Fees", bg="#4c4cb0", fg="white", font=('Helvetica', 18, 'bold'))
header_label.pack(pady=(20, 10))  # Add some padding

# Style configuration
style = ttk.Style()
style.configure('TLabel', background='#4c4cb0', foreground='white', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TEntry', font=('Helvetica', 12), padding=5)

# Use a grid to layout the form elements
form_inner_frame = tk.Frame(form_frame, bg="#4c4cb0")
form_inner_frame.pack(padx=20, pady=20)

ttk.Label(form_inner_frame, text="Payment Amount").grid(row=0, column=0, pady=10, sticky='e')
entry_payment_amount = ttk.Entry(form_inner_frame, width=30)
entry_payment_amount.grid(row=0, column=1, pady=20)

ttk.Label(form_inner_frame, text="Mode of Payment").grid(row=1, column=0, pady=10, sticky='e')
mode_var = tk.StringVar()
mode_button = ttk.Button(form_inner_frame, text="Choose Mode of Payment", command=choose_mode_of_payment, width=20)
mode_button.grid(row=1, column=1, pady=10,padx=(10,1))

# Mode of Payment Menu
mode_of_payment_menu = tk.Menu(root, tearoff=0)
mode_of_payment_menu.add_radiobutton(label="Credit Card", variable=mode_var, value="Credit Card")
mode_of_payment_menu.add_radiobutton(label="Debit Card", variable=mode_var, value="Debit Card")
mode_of_payment_menu.add_radiobutton(label="E-Wallet", variable=mode_var, value="E-Wallet")
mode_of_payment_menu.add_radiobutton(label="UPI", variable=mode_var, value="UPI")

ttk.Label(form_inner_frame, text="Transaction Number").grid(row=2, column=0, pady=10, sticky='e')
entry_transaction_number = ttk.Entry(form_inner_frame, width=30)
entry_transaction_number.grid(row=2, column=1, pady=20,padx=5)

# Submit button
submit_button = ttk.Button(form_inner_frame, text="Submit", command=submit_payment)
submit_button.grid(row=3, column=1, pady=20)

# Styling for the submit button
submit_button.configure(style='Submit.TButton')
style.configure('Submit.TButton', background='#007bff', foreground='white', font=('Helvetica', 14, 'bold'))

# Create a profile container in the upper right corner
profile_button = ttk.Button(root, text="Profile", style='TButton', command=lambda: profile_menu.post(profile_button.winfo_rootx(), profile_button.winfo_rooty() + profile_button.winfo_height()))
profile_button.place(relx=1, rely=0, anchor='ne', y=20)

profile_menu = tk.Menu(form_frame, tearoff=0)
profile_menu.add_command(label="Edit Profile")
profile_menu.add_command(label="Change Password", command=change_password)
profile_menu.add_separator()
profile_menu.add_command(label="Logout", command=logout)

# Run the main loop
root.mainloop()
