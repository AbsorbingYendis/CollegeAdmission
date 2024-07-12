import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess

# Function to handle the accept button
def accept_terms():
    messagebox.showinfo("Accepted", "Thank you for accepting the Terms of Service!")
    app.destroy()
    subprocess.Popen(["python", "register.py"])


# Function to handle the decline button
def decline_terms():
    messagebox.showwarning("Declined", "You can't register an account because you declined the Terms of Service.")
    app.destroy()
    subprocess.Popen(["python", "Applicant_Login.py"])

# Main application window
app = tk.Tk()
app.title("Terms of Service")
app.state('zoomed')
app.configure(bg="#b04c4c")
app.attributes('-topmost', True)


# Label for the title
label_title = tk.Label(app, text="Terms of Service Agreement", font=("Arial", 18, "bold"), bg="#b04c4c", pady=30)
label_title.pack()

# Frame for scrollable text
text_frame = tk.Frame(app, bg="#f2f2f2", pady=10, padx=10, width=350, height=350)
text_frame.pack()

# Scrollable text widget for the Terms of Service content
terms_text = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, font=("Arial", 12), bg="#ffffff", relief=tk.GROOVE, height=20)
terms_text.pack(fill=tk.BOTH, expand=True)

# Sample Terms of Service content
terms_of_service = """
Admission Terms of Service

1. Introduction
   By applying for admission to Noakay State University, you agree to comply with and be bound by the following terms and conditions. This document outlines the rights and responsibilities of applicants.

2. Admission Policies
   - Applicants must meet all academic and non-academic requirements specified by the NSU.
   - Admission is contingent upon the verification of all application information.
   - The NSU reserves the right to withdraw or amend any offer of admission at any time if the applicant is found to have provided false or misleading information.

3. Application Process
   - Applications must be submitted by the deadlines specified on the university’s official website.
   - All required documents must be uploaded in the correct format and size as specified by the NSU.

4. Privacy and Data Protection
   - The NSU is committed to protecting the personal information of applicants. All personal data will be  processed in accordance,but not limited to,RA 10173, also known as the "Data Privacy Act of 2012".
   - Applicants’ data may be shared with relevant third parties for the purpose of processing their application.

5. Student Responsibilities
   - Applicants who accept an offer of admission must adhere to all NSU policies and regulations.
   - Students are expected to uphold the integrity and values of the NSU community.

6. Equal Opportunity
   - NSU is committed to providing equal opportunities for all applicants regardless of race, gender, religion, or disability.
   - The NSU does not discriminate against applicants on the basis of protected characteristics.

7. Appeals and Complaints
   - Applicants have the right to appeal any admission decision or lodge a complaint if they believe there has been a procedural error.
   - Appeals must be submitted in writing within the timeframe specified by the NSU.

8. Changes to the Terms
   - The NSU reserves the right to modify these terms at any time. Any changes will be communicated to applicants through the official NSU channels.
   - Continued use of the admission services constitutes acceptance of the modified terms.

9. Governing Law
   - These terms are governed by the laws of the jurisdiction in which NSU is located.
   - Any disputes arising under these terms shall be subject to the exclusive jurisdiction of the courts in that jurisdiction.

By submitting your application, you acknowledge that you have read and understand these terms and agree to be bound by them.

Contact Information
For any questions or concerns regarding these terms, please contact the admissions office at
 
admissions@noakaystateuniversity.edu.ph
"""

# Insert the Terms of Service content into the text widget
terms_text.insert(tk.END, terms_of_service)
terms_text.config(state=tk.DISABLED)  # Make the text read-only

# Frame for the buttons within text_frame
button_frame = tk.Frame(text_frame, bg="#f2f2f2", pady=10)
button_frame.pack(fill=tk.X, side=tk.BOTTOM)

# Accept button
btn_accept = tk.Button(button_frame, text="Yes, I accept all of the terms of services", font=("Arial", 14), bg="#4caf50", fg="white", width=31, command=accept_terms)
btn_accept.pack(side=tk.LEFT, padx=(20, 10), pady=10)

# Decline button
btn_decline = tk.Button(button_frame, text="Decline", font=("Arial", 14), bg="#d32f2f", fg="white", width=12, command=decline_terms)
btn_decline.pack(side=tk.RIGHT, padx=(10, 20), pady=10)

app.mainloop()
