# This program is a simple calculator in Python

# Define the calculator function
def calculator():
    # Get user input for the operation to be performed
    operation = input("Enter an operation (+, -, *, /): ")

    # Get user input for the two operands
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operation!")
        return

    # Print the result
    print("Result: ", result)

# Call the calculator function
calculator()
