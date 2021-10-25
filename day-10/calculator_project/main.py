from art import logo
from os import system

clear = lambda: system('clear') 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

operators = {
    "+": add,
    "-": subtract,
    "*": multiplication,
    "/": division
}

def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))

    for operator in operators:
        print(operator)

    while True:
        operator_symbol = input("Pick an operation: ")
        next_number = float(input("What's the next number? "))

        calculation = operators[operator_symbol]

        result = calculation(first_number, next_number)

        print(f"{first_number} {operator_symbol} {next_number} = {result}")

        cont_or_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if cont_or_calc == 'y':
            first_number = result
            continue
        else:
            clear()
            calculator()
            break
        
calculator()