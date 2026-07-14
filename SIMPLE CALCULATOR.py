import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def square(a):
    return a * a

def square_root(a):
    if a < 0:
        return "Error! Square root of a negative number is not possible."
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error! Factorial of a negative number is not possible."
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

while True:
    print("\n===== Calculator =====")

    menu = [
        "1. Addition",
        "2. Subtraction",
        "3. Multiplication",
        "4. Division",
        "5. Modulus",
        "6. Power",
        "7. Square",
        "8. Square Root",
        "9. Factorial",
        "10. Exit"
    ]

    for item in menu:
        print(item)

    break

    