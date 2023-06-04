phonebook = {}
n = 0
while True:
    line = input()
    parts = line.split("-")
    if len(parts) == 1:
        n = int(line)
        break
    name = parts[0]
    numbers = parts[1]
    phonebook[name] = numbers

for _ in range(n):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')