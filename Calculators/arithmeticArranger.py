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
    # If more than 5 Problems entered, Error.
    if len(problems) > 5:
        raise RuntimeError('Error: Too Many Problems.')

    # check operators
    if not all(('+' in problem or '-' in problem) for problem in problems):
        raise RuntimeError("Error: Operator must be '+' or '-'.")

    # verify and collect numbers
    numbers = [] # operands as strings
    operators = []
    for i in problems:
        collection = i.split()
        if len(collection[0]) > 4 or len(collection[2]) > 4:
            raise RuntimeError('Error: Numbers can only be 4 digits long.')
        else:
            numbers.append(collection[0])
            numbers.append(collection[2])
            operators.append(collection[1])
    if not all(map(lambda x: x.isdigit(), numbers)):
        raise RuntimeError('Error: Numbers must contain only digits.')
    
    iterations = len(numbers) / 2
    
    for iter in range(int(iterations)):
        arranger_output(numbers[iter], operators[iter], numbers[iter + 1 * 2], show_answers, len(numbers) / 2)
        if iter >= iterations - 1:
            break
    
    final_string = first_row + '\n' + second_row +'\n' + third_row
    if show_answers:
        final_string += '\n' + fourth_row
    return  final_string


input = ["3801 - 2", "123 + 49"]
print(arithmetic_arranger(input))