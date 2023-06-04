number = int(input())

for _ in range(number):
    num = int(input())
    if num == 88:
        print("Hello")
    elif num == 86:
        print("How are you?")
    elif num < 88:
        print("GREAT!")
    else:
        print("Bye.")