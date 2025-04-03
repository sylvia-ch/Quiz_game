print("This is my first commit")
print("Hello World")
# Set up project
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Code: Create Welcome Page and input name， font
Welcome_page = tk.Tk()
Welcome_page.title("Python Quiz Game")
Welcome_page.geometry("400x300")

Welcome_label = tk.Label(Welcome_page, text = "Welcome to Python Quiz Game", font = ("Arial", 16))
Welcome_label.pack(pady = 10)

Name_label = tk.Label (Welcome_page, text = "Please enter your name:", font = ("Arial", 14))
Name_label.pack()
# Code: Create data stucture for quiz and answer

Welcome_page.mainloop()