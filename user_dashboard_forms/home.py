import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sqlite3
from tkinter import messagebox

def home(content_frame):

  # remove all widgets in content_frame
  for widget in content_frame.winfo_children():
        widget.destroy()

  label = tb.Label(content_frame, text="This is home form", bootstyle="success")
  label.pack()