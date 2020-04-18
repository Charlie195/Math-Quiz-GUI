from tkinter import *

import random


root = Tk()

root.title("Math Quiz App")
root.geometry("600x400")

heading = Label(root, text="Hey! Welcome to the Math Quiz App", font=("calibri", 20))
heading.pack(side=TOP)

num_questions = Label(root, text="How many questions would you like to do: ")
num_questions.place(x=20, y=80)

Num_questions = StringVar()

num_questions_ans = Entry(root, textvariable=Num_questions, width=5)
num_questions_ans.place(x=255, y=80)

run = 1

def start():
    global num_of_questions
    error_label = Label(root, text="Please enter an integer")                               # Try to use global and create label when needed
    try:
        num_of_questions = int(Num_questions.get())
    except ValueError:
        error_label.place(x=350, y=80)
        pass
    else:
        num_of_questions = int(Num_questions.get())
        heading.destroy()
        num_questions.destroy()
        num_questions_ans.destroy()
        space = Label(root, text="                                                                                                                                   ")
        space.place(x=350, y=80)
        error_label.destroy()
        heading2 = Label(root, text="Let's begin!", font=("calibri", 20))
        heading2.pack(side=TOP)
        start_button.destroy()
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        random.choice(operations)(num1, num2)


def add(N1, N2):
    global user_sum
    global sum
    global addition_question
    global sum_entry
    global submit_sum_button
    addition_question = Label(root, text=str(N1) + " + " + str(N2) + " = ")
    addition_question.place(x=20, y=80)
    user_sum = StringVar()
    sum_entry = Entry(root, textvariable=user_sum, width=5)
    sum_entry.place(x=75, y=80)
    sum = str(N1 + N2)
    submit_sum_button = Button(root, text="Submit", command=submit_sum_answer)
    submit_sum_button.place(x=115, y=75)

def submit_sum_answer():
    global run
    next_question_button = Button(root, text="Next Question", command=next_question)
    if run < num_of_questions:
        response2 = Label(root, text="Sorry, your answer is wrong. Please try again")
        if user_sum.get() == sum:
            addition_question.destroy()
            sum_entry.destroy()
            submit_sum_button.destroy()
            response = Label(root, text="You are correct!                                                     ")
            response.place(x=20, y=120)
            next_question_button.place(x=20, y=150)
            run += 1
        else:
            response2.place(x=20, y=120)
            sum_entry.delete(0, END)
    else:
        response2 = Label(root, text="Sorry, your answer is wrong. Please try again")
        if user_sum.get() == sum:
            next_question_button.destroy()
            addition_question.destroy()
            sum_entry.destroy()
            submit_sum_button.destroy()
            end_label = Label(root, text="You are done!", font=("calibri", 20))
            end_label.pack(side=TOP)
        else:
            response2.place(x=20, y=120)
            sum_entry.delete(0, END)

def subtract(N1, N2):
    global user_difference
    global difference
    global subtraction_question
    global difference_entry
    global submit_difference_button
    subtraction_question = Label(root, text=str(N1) + " - " + str(N2) + " = ")
    subtraction_question.place(x=20, y=80)
    user_difference = StringVar()
    difference_entry = Entry(root, textvariable=user_difference, width=5)
    difference_entry.place(x=75, y=80)
    difference = str(N1 - N2)
    submit_difference_button = Button(root, text="Submit", command=submit_difference_answer)
    submit_difference_button.place(x=115, y=75)

def submit_difference_answer():
    global run
    next_question_button = Button(root, text="Next Question", command=next_question)
    if run < num_of_questions:
        response2 = Label(root, text="Sorry, your answer is wrong. Please try again")
        if user_difference.get() == difference:
            subtraction_question.destroy()
            difference_entry.destroy()
            submit_difference_button.destroy()
            response = Label(root, text="You are correct!                                                     ")
            response.place(x=20, y=120)
            next_question_button = Button(root, text="Next Question", command=next_question)
            next_question_button.place(x=20, y=150)
            run += 1
        else:
            response2.place(x=20, y=120)
            difference_entry.delete(0, END)
    else:
        response2 = Label(root, text="Sorry, your answer is wrong. Please try again")
        if user_difference.get() == difference:
            next_question_button.destroy()
            subtraction_question.destroy()
            difference_entry.destroy()
            submit_difference_button.destroy()
            end_label = Label(root, text="You are done!", font=("calibri", 20))
            end_label.pack(side=TOP)
        else:
            response2.place(x=20, y=120)
            difference_entry.delete(0, END)

def multiply(N1, N2):
    global user_product
    global product
    global multiplication_question
    global product_entry
    global submit_product_button
    multiplication_question = Label(root, text=str(N1) + " x " + str(N2) + " = ")
    multiplication_question.place(x=20, y=80)
    user_product = StringVar()
    product_entry = Entry(root, textvariable=user_product, width=5)
    product_entry.place(x=75, y=80)
    product = str(N1 * N2)
    submit_product_button = Button(root, text="Submit", command=submit_product_answer)
    submit_product_button.place(x=115, y=75)

def submit_product_answer():
    global run
    next_question_button = Button(root, text="Next Question", command=next_question)
    if run < num_of_questions:
        response2 = Label(root, text="Sorry, your answer is wrong. Please try again")
        if user_product.get() == product:
            multiplication_question.destroy()
            product_entry.destroy()
            submit_product_button.destroy()
            response = Label(root, text="You are correct!                                                     ")
            response.place(x=20, y=120)
            next_question_button = Button(root, text="Next Question", command=next_question)
            next_question_button.place(x=20, y=150)
            run += 1
        else:
            response2.place(x=20, y=120)
            product_entry.delete(0, END)
    else:
        next_question_button.destroy()
        multiplication_question.destroy()
        product_entry.destroy()
        submit_product_button.destroy()
        end_label = Label(root, text="You are done!", font=("calibri", 20))
        end_label.pack(side=TOP)

def divide(N1, N2):
    global user_quotient
    global quotient
    global division_question
    global quotient_entry
    global submit_quotient_button
    division_question = Label(root, text=str(N1) + " ÷ " + str(N2) + " = ")
    division_question.place(x=20, y=80)
    user_quotient = StringVar()
    quotient_entry = Entry(root, textvariable=user_quotient, width=20)
    quotient_entry.place(x=75, y=80)
    quotient = str(int(N1 / N2)) + " and " + str(N1 % N2) + " remaining"
    submit_quotient_button = Button(root, text="Submit", command=submit_quotient_answer)
    submit_quotient_button.place(x=205, y=75)

def submit_quotient_answer():
    global run
    next_question_button = Button(root, text="Next Question", command=next_question)
    if run < num_of_questions:
        response2 = Label(root, text="Sorry, your answer is wrong. Please try again")
        if user_quotient.get() == quotient:
            division_question.destroy()
            quotient_entry.destroy()
            submit_quotient_button.destroy()
            response = Label(root, text="You are correct!                                                     ")
            response.place(x=20, y=120)
            next_question_button = Button(root, text="Next Question", command=next_question)
            next_question_button.place(x=20, y=150)
            run += 1
        else:
            response2.place(x=20, y=120)
            quotient_entry.delete(0, END)
    else:
        next_question_button.destroy()
        division_question.destroy()
        quotient_entry.destroy()
        submit_quotient_button.destroy()
        end_label = Label(root, text="You are done!", font=("calibri", 20))
        end_label.pack(side=TOP)

def next_question():
    for widget in root.winfo_children():
        widget.destroy()
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)
    random.choice(operations)(num1, num2)

start_button = Button(root, text="Submit", command=start)
start_button.place(x=295, y=75)

operations = [add, subtract, multiply, divide]

root.mainloop()