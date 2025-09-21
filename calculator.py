while True:  
    # Ask the user to enter an operation (e.g., "5 + 3")
    text_user = input("Please enter your operation: ")

    # Split the input into three parts: number1, operation, number2
    number1, operation, number2 = text_user.split()

    # Convert the numbers from string to float (so we can calculate)
    number1 = float(number1)
    number2 = float(number2)

    # Check the operation type and perform the calculation
    if operation == "+":
        print("Result: ", number1 + number2)   # Addition
    elif operation == "-":
        print("Result: ", number1 - number2)   # Subtraction
    elif operation == "/":
        print("Result: ", number1 / number2)   # Division
    elif operation == "*":
        print("Result: ", number1 * number2)   # Multiplication
    elif operation == "**":
        print("Result: ", number1 ** number2)  # Exponentiation (power)
