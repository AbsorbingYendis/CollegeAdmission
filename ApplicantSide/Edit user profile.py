import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to update user profile
def update_profile():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    contact_number = entry_contact_number.get()
    email = entry_email.get()
    # Here you would typically save these details to a database or file
    messagebox.showinfo("Profile Updated", "User profile updated successfully!")

# Function to change password
def change_password():
    # This function can be expanded to include password changing functionality
    messagebox.showinfo("Change Password", "Password change functionality goes here!")

# Function to logout
def logout():
    root.quit()

# Function to show profile menu
def show_profile_menu(event=None):
    profile_menu.post(profile_button.winfo_rootx(), profile_button.winfo_rooty() + profile_button.winfo_height())

# Create the main window
root = tk.Tk()
root.title("Dashboard")
root.geometry("600x500")

# Set the background color of the main window
root.configure(background='#b04c4c')

# Style configuration
style = ttk.Style()
style.configure('TLabel', background='#ffffff', foreground='black', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12), padding=5)
style.configure('TEntry', font=('Helvetica', 12), padding=5)
style.configure('White.TFrame', background='#ffffff')

# Create a frame for the dashboard
dashboard_frame = ttk.Frame(root, padding="10", style='TFrame')
dashboard_frame.pack(fill=tk.BOTH, expand=True)

# Create a profile button in the upper right corner
profile_button = ttk.Button(dashboard_frame, text="Profile", command=show_profile_menu)
profile_button.place(relx=1, rely=0, anchor='ne')

# Create a menu for profile options
profile_menu = tk.Menu(root, tearoff=0)
profile_menu.add_command(label="Edit Profile")
profile_menu.add_command(label="Change Password", command=change_password)
profile_menu.add_separator()
profile_menu.add_command(label="Logout", command=logout)

# Create a frame for the profile details container with the specified color
profile_frame_container = ttk.Frame(dashboard_frame, padding="20", style='White.TFrame')
profile_frame_container.place(relx=0.5, rely=0.5, anchor='center')

# Center the container and set the background color
center_frame = ttk.Frame(profile_frame_container, padding="20", style='White.TFrame')
center_frame.pack(expand=True)
center_frame.config(style="White.TFrame")

# Add profile details inside the centered container
ttk.Label(center_frame, text="First Name", style='TLabel').grid(row=0, column=0, padx=10, pady=10, sticky='E')
entry_first_name = ttk.Entry(center_frame)
entry_first_name.grid(row=0, column=1, padx=10, pady=10, sticky='W')

ttk.Label(center_frame, text="Last Name", style='TLabel').grid(row=0, column=2, padx=10, pady=10, sticky='E')
entry_last_name = ttk.Entry(center_frame)
entry_last_name.grid(row=0, column=3, padx=10, pady=10, sticky='W')

ttk.Label(center_frame, text="Contact Number", style='TLabel').grid(row=1, column=0, padx=10, pady=10, sticky='E')
entry_contact_number = ttk.Entry(center_frame)
entry_contact_number.grid(row=1, column=1, padx=10, pady=10, sticky='W')

ttk.Label(center_frame, text="Email", style='TLabel').grid(row=1, column=2, padx=10, pady=10, sticky='E')
entry_email = ttk.Entry(center_frame)
entry_email.grid(row=1, column=3, padx=10, pady=10, sticky='W')

ttk.Button(center_frame, text="Update", command=update_profile).grid(row=2, column=0, columnspan=4, pady=10)

# Run the main loop
root.mainloop()
