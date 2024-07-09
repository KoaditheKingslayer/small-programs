#Cody Wagar - Code Project - Console Calculator

#Define Functions (Addition, Subtraction, Multiplication, Division)

#Addition
def add(x, y):
    return x + y

#Subtraction
def sub(x, y):
    return x - y

#Multiplication
def mul(x, y):
    return x * y

#Division
def div(x, y):
    if y == 0:
        return "Error: Division by Zero Not Allowed."
    else:
        return x / y

def calculator():
    print("Select Operation. + (1), - (2), * (3), / (4).")

    while True:
        choice = input("Enter Choice 1/2/3/4: ")
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue

            if choice == '1': #Addition 
                if float(num1 + num2).is_integer() == True: #Integer Display
                    print(f"{int(num1)} + {int(num2)} = {int(add(num1, num2))}")
                else:
                    print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2': #Subtraction
                if float(num1 - num2).is_integer() == True: #Integer Display
                    print(f"{int(num1)} - {int(num2)} = {int(sub(num1, num2))}")
                else:
                    print(f"{num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3': #Multiplication
                print(f"{num1} * {num2} = {int(mul(num1, num2))}")
            elif choice == '4': #Division
                print(f"{num1} / {num2} = {div(num1, num2)}")

        next_calculation = input("Perform another calculation? Y/N? ")
        if next_calculation.lower() != 'y':
            break
    else:
        print("Invalid Input.")

calculator()
