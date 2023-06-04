command = input()
a = int(input())
b = int(input())


def calculate(command, a, b):
    result = 0
    if command == "multiply":
        result = a * b
    elif command == "divide":
        result = a // b
    elif command == "add":
        result = a + b
    else:
        result = a - b
    return result


res = calculate(command, a, b)
print(res)
