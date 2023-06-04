import re

n = int(input())

for i in range(n):
    password = input()
    match = re.match(r'(.*)(>)([0-9]{3})[|]([a-z]{3})[|]([A-Z]{3})[|]([^\<\>]{3})(<)(.*)', password)
    if match:
        group_1 = match[1]
        group_2 = match[2]
        group_3 = match[3]
        group_4 = match[4]
        group_5 = match[5]
        group_6 = match[6]
        group_7 = match[7]
        group_8 = match[8]
        if len(group_1) == len(group_8):
            group = group_3 + group_4 + group_5 + group_6
            print(f"Password: {group}")
        else:
            print("Try another password!")
    else:
        print("Try another password!")