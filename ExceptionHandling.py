try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    operator = input("Choose the operator (+, -, /, *): ")

    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2   
    else:
        raise ValueError("Invalid operator selected")             
 
except ValueError as e:
    print(f"Input error: {e}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else: 
    print(f"Result: {result}")