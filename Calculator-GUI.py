import tkinter as tk
from tkinter import ttk

rootWindow = tk.Tk()  # Creates a Window
rootWindow.title('GUI-Based Calculator')  # Updates the Window Title
rootWindow.geometry('300x400')  # Sets the Shape and Location of the Window
rootWindow.resizable(False, False)  # Width / Height Cannot Be Resized.
rootWindow.attributes('-alpha', 1)  # Set Transparency (1 Opaque, 0.## percentage Transparent)

# Create a Container Frame for Input
inFrame = ttk.Frame(rootWindow, height=20, width=400)
inFrame.grid(row=0, column=0, columnspan=4)
inFrame['padding'] = (5, 5, 5, 5)
inFrame['borderwidth'] = 5
inFrame['relief'] = 'groove'

# Create the Input/Text Box
numBox = ttk.Entry(inFrame, width=20, font=('Helvetica', 18), justify='right')
numBox.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
numBox.focus()

# Global variable to store the operation
operation = ''

# Global variable to store the first number
numOne = None

# Global variable to store the second number
numTwo = None

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def display(x):
    numBox.delete(0, tk.END)
    numBox.insert(0, x)

def button_clicked(button_id):
    global operation, numOne, numTwo
    
    # Add the value of numeric buttons to the input box
    if button_id.isdigit() or button_id == '.':
        current_text = numBox.get()
        if button_id == '.' and current_text.__contains__('.'):
            print("Only one point/period")
        else:
            numBox.delete(0, tk.END)
            numBox.insert(0, current_text + button_id)
    
    # Set the Operation to be performed
    elif button_id in ['+', '-', '*', '/']:
        current_text = numBox.get()
        if numOne is None:
            numOne = float(current_text)
            numBox.delete(0, tk.END)
        else:
            numTwo = float(current_text)
            if operation == '+':
                numOne = add(numOne, numTwo)
                display(numOne)
            elif operation == '-':
                numOne = sub(numOne, numTwo)
                display(numOne)
            elif operation == '*':
                numOne = mul(numOne, numTwo)
                display(numOne)
            elif operation == '/':
                numOne = div(numOne, numTwo)
                display(numOne)
            display(numOne)
            numTwo = None
        operation = button_id

        
    elif button_id == '=':
        current_text = numBox.get()
        numTwo = float(current_text)
        if operation == '+':
            answer = add(numOne, numTwo)
        elif operation == '-':
            answer = sub(numOne, numTwo)
        elif operation == '*':
            answer = mul(numOne, numTwo)
        elif operation == '/':
            answer = div(numOne, numTwo)
        display(answer)
        operation = ''
        numOne = None
        numTwo = None
        
    elif button_id == 'C':
        numBox.delete(0, tk.END)
        operation = ''
        numOne = None
        numTwo = None
        
    print(f'Button Clicked: {button_id}')  # Console Log

# Button configuration
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

# Create and place buttons
for button in buttons:
    text = button[0]
    row = button[1]
    col = button[2]
    if len(button) == 4:
        colspan = button[3]
        btn = ttk.Button(rootWindow, text=text, command=lambda t=text: button_clicked(t))
        btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky='nsew')
    else:
        btn = ttk.Button(rootWindow, text=text, command=lambda t=text: button_clicked(t))
        btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

# Adjust the row and column weights so they expand with the window
for i in range(6):
    rootWindow.grid_rowconfigure(i, weight=1)
for j in range(4):
    rootWindow.grid_columnconfigure(j, weight=1)

rootWindow.mainloop()  # Start the main event loop
