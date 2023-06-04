number = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for idx in range(len(number)):
    beggar_idx = idx % beggars_count
    num = int(number[idx])
    beggars[beggar_idx] += num

print(beggars)