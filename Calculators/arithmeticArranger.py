# Project From: Build an Arithmetic Formatter -> FreeCodeCamp - Scientific Computing with Python
# Code is my own answer to the project's requirements.

first_row = ''
second_row = ''
third_row = ''
fourth_row = ''
counter = 0

def arranger_output(number_1, op, number_2, answers, number_problems):
    spacing = 0
    row_1 = ''
    row_2 = ''
    dashes = ''
    answer = 0
    
    global counter
    counter += 1
    
    if len(number_1) >= len(number_2):
        spacing = len(number_1) + 2
        row_1 += ' ' * (spacing - len(number_1)) + number_1
    else:
        spacing = len(number_2) + 2
        row_1 += ' ' * (spacing - len(number_1)) + number_1
        
    # Math Part if show_answers was True
    
    if answers:
        if op == "+":
            answer = int(number_1) + int(number_2)
        elif op == "-":
            answer = int(number_1) - int(number_2)
    
    row_4 = ' ' * (spacing - len(str(answer))) + str(answer)
    
    row_2 += op + (' ' * (spacing - 1 - len(number_2))) + number_2 
    dashes += '-' * spacing
    
    global first_row
    global second_row
    global third_row
    global fourth_row
    
    if counter < number_problems:
        first_row += row_1 + '    '
        second_row += row_2 + '    '
        third_row += dashes + '    '
        fourth_row += row_4 + '    '
    else:
        first_row += row_1 
        second_row += row_2
        third_row += dashes
        fourth_row += row_4       

def arithmetic_arranger(problems, show_answers=False):
    global first_row, second_row, third_row, fourth_row, counter
    
    # Reset global rows and counter at the beginning of each call
    first_row = ''
    second_row = ''
    third_row = ''
    fourth_row = ''
    counter = 0

    # If more than 5 Problems entered, Error.
    if len(problems) > 5:
        return('Error: Too many problems.')

    # Check operators
    if not all(('+' in problem or '-' in problem) for problem in problems):
        return("Error: Operator must be '+' or '-'.")

    # Verify and collect numbers and operators
    numbers = [] # operands as strings
    operators = []
    for problem in problems:
        parts = problem.split()
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return('Error: Numbers cannot be more than four digits.')
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return('Error: Numbers must only contain digits.')
        
        numbers.append(parts[0])
        numbers.append(parts[2])
        operators.append(parts[1])

    iterations = len(operators)
    
    for i in range(iterations):
        arranger_output(numbers[i * 2], operators[i], numbers[i * 2 + 1], show_answers, iterations)

    final_string = first_row + '\n' + second_row +'\n' + third_row
    if show_answers:
        final_string += '\n' + fourth_row
    return final_string

input = ["3801 - 2", "123 + 49"]
print(arithmetic_arranger(input))
