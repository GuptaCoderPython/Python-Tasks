# using arithmetic operations making a calculator 

def arithmetic_operations(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return "Error: Division by zero" if num2 == 0 else num1 / num2
    else:
        return "Error: Invalid operator"

num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the second value: "))
operator = input("Enter the operator (+, -, *, /): ")

result = arithmetic_operations(num1, num2, operator)
print("Result:", result)