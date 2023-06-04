string = input()
char_count = {}

for char in string:
    if char != " ":
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

for char, count in char_count.items():
    print(f"{char} -> {count}")