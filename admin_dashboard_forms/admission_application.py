import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def admission_application(content_frame):
  
  # remove all widgets in content_frame
  for widget in content_frame.winfo_children():
        widget.destroy()

  label = tb.Label(content_frame, text="This is admission_application frame")
  label.pack()