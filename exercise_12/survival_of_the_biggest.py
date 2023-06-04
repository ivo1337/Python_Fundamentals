numbers = [int(x) for x in input().split()]
remover = int(input())

for _ in range(remover):
    number_to_remove = min(numbers)
    numbers.remove(number_to_remove)

print(', '.join([str(x) for x in numbers]))
