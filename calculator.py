# A simple calculator script using conditional statements

print("Simple Calculator")

# Prompt for the first number
num1_input = input("Enter the first number: ")
try:
    num1 = float(num1_input)
except ValueError:
    print("Invalid input for the first number. Please enter a number.")
    exit()

# Prompt for the second number
num2_input = input("Enter the second number: ")
try:
    num2 = float(num2_input)
except ValueError:
    print("Invalid input for the second number. Please enter a number.")
    exit()

# Prompt for the operator
operator = input("Enter an operator (+, -, *, /): ")

# Perform the calculation using conditional statements
if operator == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator entered. Please use +, -, *, or /.")