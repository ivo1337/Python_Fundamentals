number_ = int(input())
positive_number = []
negative_number = []
counter_positive = 0
counter_negative = 0

for _ in range(number_):
    chisla = int(input())
    if chisla >= 0:
        positive_number.append(chisla)
        counter_positive += 1
    else:
        negative_number.append(chisla)
        counter_negative += chisla
print(positive_number)
print(negative_number)
print(f"Count of positives: {counter_positive}")
print(f"Sum of negatives: {counter_negative}")