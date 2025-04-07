print("This is my first commit")
print("Hello World")
# Set up project
import tkinter as tk # for GUi
from tkinter import messagebox # 
import matplotlib.pyplot as plt # for graph and quiz reslut

 
# Code: Create Welcome Page and input name， font
Welcome_page = tk.Tk()
Welcome_page.title("Python Quiz Game")
Welcome_page.geometry("400x300")
 
Welcome_label = tk.Label(Welcome_page, text = "Welcome to Python Quiz Game", font = ("Arial", 16))
Welcome_label.pack(pady = 10)
 
Name_label = tk.Label (Welcome_page, text = "Please enter your name:", font = ("Arial", 14))
Name_label.pack()

Name_entry = tk.Entry(Welcome_page, font=("Arial", 12))
Name_entry.pack(pady=10)

user_name = ""
score = 0
question_index = 0

# Code: Create data stucture for quiz and answer
question = [
    {
        "question": "Which of these is a Boolean value in Python?", 
        "options": ["A. float", "B. string", "C. bool", "D. int"], 
        "answer": "C"
    },
    {
        "question": "What symbol is used to define a function in Python?", 
        "options": ["A. =", "B. def", "C. class", "D. loop"], 
        "answer": "B"
    },
    {
        "question": "Which keyword is used for loops in Python?", 
        "options": ["A. if", "B. class", "C. try", "D. for"], 
        "answer": "D"
    },
    {
        "question": "Which of these is a correct Python variable name?", 
        "options": ["A. 2name", "B. name_1", "C. name-1", "D. name.1"], 
        "answer": "B"
    },
    {
        "question": "Which data type is used to store text in Python?", 
        "options": ["A. int", "B. float", "C. str", "D. bool"], 
        "answer": "C"
    }
]
# Code: Display the quiz question and options
def start_quiz():
    global user_name
    user_name = Name_entry.get()
    if user_name == "":
        messagebox.showwarning("Error","Please enter your name.")
    elif any(char.isdigit() for char in user_name):
        messagebox.showwarning("Invalid Name", "Name cannot contain numbers.")
    else:
        Welcome_page.destroy()
        show_question()
start_button = tk.Button(Welcome_page, text="Start Quiz", font=("Arial", 12), command=start_quiz)
start_button.pack(pady=20)

# Display question and options
def show_question():
    global quiz_window, question_label, var, option_buttons, question_index

    quiz_window = tk.Tk()
    quiz_window.title("Quiz")
    quiz_window.geometry("500x350")

    question_data = question[question_index]

    question_label = tk.Label(quiz_window, text=question_data["question"], font=("Arial", 14), wraplength=400)
    question_label.pack(pady=10)

    var = tk.StringVar()
    var.set("")

    option_buttons = []
    for opt in question_data["options"]:
        btn = tk.Radiobutton(quiz_window, text=opt, variable=var, value=opt[0], font=("Arial", 12))
        btn.pack(anchor="w", padx=20)
        option_buttons.append(btn)

# next button
    next_button = tk.Button(quiz_window, text="Next", font=("Arial", 12), command=lambda: check_answer(var, quiz_window))
    next_button.pack(pady=20)


# check answer
def check_answer(var, window):
    global score, question_index

    selected = var.get()
    if selected == "":
        messagebox.showwarning("No Selection", "Please select an answer.")
        return

    correct = question[question_index]["answer"]
    if selected == correct:
        score += 1

    question_index += 1
    window.destroy()

    if question_index < len(question):
        show_question()
    else:
        show_result()

# show test result
def show_result():
    result_window = tk.Tk()
    result_window.title("Quiz Result")
    result_window.geometry("400x300")

    result_text = f"Thank you, {user_name}!\nYour Score: {score} / {len(question)}"
    result_label = tk.Label(result_window, text=result_text, font=("Arial", 14))
    result_label.pack(pady=20)

# show graph
    def show_chart():
        labels = ['Correct', 'Incorrect']
        values = [score, len(question) - score]
        colors = ['green', 'red']

        plt.bar(labels, values, color=colors)
        plt.title("Quiz Result")
        plt.xlabel("Answers")
        plt.ylabel("Count")
        plt.show()

    show_graph_button = tk.Button(result_window, text="Show Result Chart", font=("Arial", 12), command=show_chart)
    show_graph_button.pack(pady=20)
Welcome_page.mainloop()






