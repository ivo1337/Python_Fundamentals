text = input()

while True:
    line = input()
    if line == "Decode":
        break
    strip_data = line.split("|")
    command = strip_data[0]
    if command == "Move":
        number = int(strip_data[1])
        text = text[number:] + text[:number]
    elif command == "Insert":
        idx = int(strip_data[1])
        symbol = strip_data[2]
        text = text[:idx] + symbol + text[idx:]
    elif command == "ChangeAll":
        first = strip_data[1]
        second = strip_data[2]
        text = text.replace(first, second)

print(f"The decrypted message is: {text}")