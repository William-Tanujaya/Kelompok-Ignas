print("Available operators: +, -, /, *")
print("Input format: [number1] [operation] [number2]")
print("Example: 2 + 2\n")

num = input("Enter operation: ")

num1, operator, num2 = num.split()

num1 = float(num1)
num2 = float(num2)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error")
        exit()
    result = num1 / num2
else:
    print("Invalid operator")
    exit()
    
def formating(n):
    n = round(n, 10)
    if n.is_integer():
        return int(n)
    return n

print(f"{formating(num1)} {operator} {formating(num2)} = {formating(result)}")
