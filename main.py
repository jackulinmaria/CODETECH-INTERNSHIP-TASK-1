'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Define a function for each operation
def add(u, v):
    return u + v

def subtract(u, v):
    return u - v

def multiply(u, v):
    return u * v

def divide(u, v):
    if v == 0:
        return "Error: Division by zero is not allowed"
    return u / v

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input("Enter the operation number (1/2/3/4): "))

# Perform the selected operation
if operation == 1:
    result = add(num1, num2)
elif operation == 2:
    result = subtract(num1, num2)
elif operation == 3:
    result = multiply(num1, num2)
elif operation == 4:
    result = divide(num1, num2)
else:
    result = "Error: Invalid operation chosen"

# Display the result to the user
print("The result is:", result)