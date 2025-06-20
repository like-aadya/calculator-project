# Simple Calculator in Python

print("Welcome to the Calculator!")

# Input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Logic
if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 == 0:
         print("Error: Cannot divide by zero.")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operator!")