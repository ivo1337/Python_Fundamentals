password = input()

while True:
    command = input()
    if command == "Complete":
        break

    commands = command.split()[0]

    if commands == "Make":
        idx = int(command.split()[2])
        if command.split()[1] == "Upper":
            if idx < len(password):
                password = password[:idx] + password[idx].upper() + password[idx + 1:]
                print(password)
        elif command.split()[1] == "Lower":
            if idx < len(password):
                password = password[:idx] + password[idx].lower() + password[idx + 1:]
                print(password)
    elif commands == "Insert":
        idx = int(command.split()[1])
        char = command.split()[2]
        if idx <= len(password):
            password = password[:idx] + char + password[idx:]
            print(password)
    elif commands == "Replace":
        char = command.split()[1]
        value = int(command.split()[2])
        if char in password:
            new_char = chr(ord(char) + value)
            password = password.replace(char, new_char)
            print(password)
    elif commands == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        elif not all(char.isalnum() or char == "_" for char in password):
            print("Password must consist only of letters, digits and _!")
        elif not any(char.isupper() for char in password):
            print("Password must consist at least one uppercase letter!")
        elif not any(char.islower() for char in password):
            print("Password must consist at least one lowercase letter!")
        elif not any(char.isdigit() for char in password):
            print("Password must consist at least one digit!")

