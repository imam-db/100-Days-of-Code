"""
Project day 10 : Calculator
"""

from art import logo

print(logo)

#add
def add(n1, n2):
    return n1+n2

#multiply
def multiply(n1,n2):
    return n1*n2

#substract
def substract(n1,n2):
    return n1-n2

#divide
def divide(n1,n2):
    return n1/n2

def operate(n1, operation, n2):
    if operation == '+':
        return add(n1, n2)
    elif operation == '-':
        return substract(n1, n2)
    elif operation == '*':
        return multiply(n1, n2)
    elif operation == '/':
        return divide(n1, n2)

def calculator():
    n1 = float(input("What's the first number : "))


    operate_again = True
    while operate_again:    
        operation = input("Pick an operation from the line below:\n+\n-\n*\n/\n")
        n2 = float(input("What's the next number : "))
        temp_value = operate(n1, operation, n2) 
        print(temp_value)
        again = input(f"Type 'y' to continue calculating with {temp_value}, or type 'n' to start a new calculations, or type 'x' to exit :" )
        if again == 'n':
            operate_again = False
            calculator()
        elif again == 'y':
            n1 = temp_value
        else:
            operate_again = False
            # operationx = input('Pick an operation from the line below:\n+\n-\n*\n/\n')
            # nx = int(input("What's the antoher number : "))
            # temp_valuex = operate(temp_value, operationx, nx)
            # print(temp_valuex)

calculator()