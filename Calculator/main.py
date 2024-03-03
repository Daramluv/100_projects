#calculator
from art import logo
import os

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def mutiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation = {
    "+":add,
    "-":subtract,
    "*":mutiply,
    "/":divide
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for i in operation:
        print(i)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number?: "))
        calc_function = operation[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        try_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if try_again == "y":
            num1 = answer
        else:
            should_continue = False
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()

calculator()