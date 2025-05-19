first_number = int(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
second_number = int(input("Enter second number: "))


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

answer = 0
while True:
    if operation == "+":
        answer += add(first_number, second_number)
    elif operation == "-":
        answer += subtract(first_number, second_number) 
    elif operation == "*":
        answer += multiply(first_number, second_number)
    elif operation == "/":
        answer += divide(first_number, second_number)
    else:
        print("Invalid operation!")
        break
    print(f"= {answer}")
    continue_calculation = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_calculation == "yes":
        first_number = answer
        operation = input("Enter operation (+, -, *, /): ")
        second_number = int(input("Enter second number: "))
    else:
        print("Exiting calculator.")
        break
    