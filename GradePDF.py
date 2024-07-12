import sqlite3
import fitz  # PyMuPDF
import tempfile
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import io
import sys

def fetch_pdf_blob(account_id):
    # Connect to SQLite database
    conn = sqlite3.connect('Database/CAS.db')
    cursor = conn.cursor()
    try:
        # Retrieve the PDF blob from the table
        cursor.execute('SELECT gradeDoc FROM Grades WHERE accountID = ?', (account_id,))
        pdf_blob = cursor.fetchone()[0]
    except Exception as e:
        messagebox.showerror("Error", str(e))
        pdf_blob = None
    finally:
        conn.close()
    return pdf_blob

def save_pdf_to_tempfile(pdf_blob):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(pdf_blob)
        temp_pdf_path = temp_file.name  # Get the temporary file path
    return temp_pdf_path

def display_pdf_page(pdf_document, page_num):
    page = pdf_document.load_page(page_num)
    pix = page.get_pixmap()

    # Convert Pixmap to an Image object using Pillow
    img_data = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_data))

    # Resize image to fit within the canvas
    img.thumbnail((canvas.winfo_width(), canvas.winfo_height()))
    img_tk = ImageTk.PhotoImage(img)

    # Clear the canvas and display the image
    canvas.delete("all")
    canvas.create_image(0, 0, anchor='nw', image=img_tk)
    canvas.image = img_tk  # Keep a reference to avoid garbage collection

def load_pdf():
    global pdf_document, current_page
    account_id = sys.argv[1]
    if account_id:
        pdf_blob = fetch_pdf_blob(account_id)
        if pdf_blob:
            temp_pdf_path = save_pdf_to_tempfile(pdf_blob)
            pdf_document = fitz.open(temp_pdf_path)
            current_page = 0
            display_pdf_page(pdf_document, current_page)
            update_buttons()

def next_page():
    global current_page
    if pdf_document and current_page < len(pdf_document) - 1:
        current_page += 1
        display_pdf_page(pdf_document, current_page)
        update_buttons()

def previous_page():
    global current_page
    if pdf_document and current_page > 0:
        current_page -= 1
        display_pdf_page(pdf_document, current_page)
        update_buttons()

def update_buttons():
    if current_page == 0:
        prev_button.config(state=tk.DISABLED)
    else:
        prev_button.config(state=tk.NORMAL)
    if current_page == len(pdf_document) - 1:
        next_button.config(state=tk.DISABLED)
    else:
        next_button.config(state=tk.NORMAL)

# Initialize global variables
pdf_document = None
current_page = 0

# Create the main application window
root = tk.Tk()
root.title("PDF Viewer")
root.attributes('-topmost', True)

# Create a frame to hold the canvas
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)



# Create a canvas to display the PDF pages
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Add a scrollbar to the canvas
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a button to load the PDF
load_button = tk.Button(root, text="Load PDF", command=load_pdf)
load_button.pack()

# Create navigation buttons
prev_button = tk.Button(root, text="Previous Page", command=previous_page, state=tk.DISABLED)
prev_button.pack(side=tk.LEFT, padx=5, pady=5)

next_button = tk.Button(root, text="Next Page", command=next_page, state=tk.DISABLED)
next_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Run the tkinter main loop
root.mainloop()
