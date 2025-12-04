import tkinter as tk

calculation = ""
def add_to_calculation(symbol):
    global calculation 
    calculation += str(symbol)
    text_box.delete(1.0, "end-1c")
    text_box.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation.strip()))
        text_box.delete(1.0, "end-1c")
        text_box.insert(1.0, calculation)

    except:
        clear_field()
        text_box.insert(1.0, "Error")


def clear_field():
    global calculation
    text_box.delete(1.0, "end-1c")
    calculation = ""

def backspace():
    global calculation
    calculation = calculation[:-1]
    text_box.delete(1.0, "end-1c")
    text_box.insert(1.0, calculation)

root = tk.Tk()

root.geometry("370x275")

text_box = tk.Text(root, height = 2, width = 20, font=("Arial", 24))

text_box.grid(row= 1, columnspan=5)

button_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width = 7, font=("Arial", 14))
button_1.grid(row= 2, column= 1) 

button_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width = 7, font=("Arial", 14))
button_2.grid(row= 2, column= 2)

button_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width = 7, font=("Arial", 14))
button_3.grid(row= 2, column= 3)

button_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width = 7, font=("Arial", 14))
button_4.grid(row= 3, column= 1)

button_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width = 7, font=("Arial", 14))
button_5.grid(row= 3, column= 2)

button_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width = 7, font=("Arial", 14))
button_6.grid(row= 3, column= 3)

button_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width = 7, font=("Arial", 14))
button_7.grid(row= 4, column= 1)

button_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width = 7, font=("Arial", 14))
button_8.grid(row= 4, column= 2)

button_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width = 7, font=("Arial", 14))
button_9.grid(row= 4, column= 3)


button_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width = 7, font=("Arial", 14) )
button_0.grid(row = 5, column= 1)
button_addition = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width = 7, font=("Arial", 14) )
button_addition.grid(row = 2, column= 4)

button_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width = 7, font=("Arial", 14) )
button_minus.grid(row = 3, column= 4)

button_multiplication = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width = 7, font=("Arial", 14) )
button_multiplication.grid(row = 4, column= 4)

button_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width = 7, font=("Arial", 14) )
button_division.grid(row = 5, column= 4)

button_result = tk.Button(root, text="=", command=lambda: evaluate_calculation(), width = 7, font=("Arial", 14) )
button_result.grid(row = 6, column= 4)

button_clear = tk.Button(root, text="C", command=lambda: clear_field(), width = 7, font=("Arial", 14) )
button_clear.grid(row = 6, column= 1)

button_backspace = tk.Button(root, text="⌫", command=lambda: backspace(), width = 7, font=("Arial", 14) )
button_backspace.grid(row = 6, column= 2)

button_bracket_1 = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width = 7, font=("Arial", 14) )
button_bracket_1.grid(row = 5, column= 2)

button_bracket_2 = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width = 7, font=("Arial", 14) )
button_bracket_2.grid(row = 5, column= 3)

root.mainloop()