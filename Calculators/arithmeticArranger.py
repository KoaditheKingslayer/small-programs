# TODO
# Operand/number only 4 digits: 'Error: Numbers cannot be more than four digits.'
# 
# If the user supplied the correct format of problems
# the conversion returned will follow these rules.
# Single Space between Operator and Longest Operand.
# Operator on same line as second Operand.
# Both Operands in same ordera as provided. Left is top, right is bottom.
# Numbers should be right-aligned.
# There should be four spaces between each problem.
# There should be dashes at the bottom of each problem, along the entire length of each problem individually.


def arithmetic_arranger(problems, show_answers=False):
    # If more than 5 Problems entered, Error.
    if len(problems) > 5:
        raise RuntimeError('Error: Too Many Problems.')

    # check operators
    if not all(('+' in problem or '-' in problem) for problem in problems):
        raise RuntimeError("Error: Operator must be '+' or '-'.")

    # verify and collect numbers
    numbers = [] # operands as strings
    for i in problems:
        collection = i.split()
        numbers.extend([collection[0], collection[2]])
    if not all(map(lambda x: x.isdigit(), numbers)):
        raise RuntimeError('Error: Numbers must contain only digits.')


input = ["5 + 3", "2 + 2", "100 + 200", "1129 - 876", "1024 + 768"]
arithmetic_arranger(input)