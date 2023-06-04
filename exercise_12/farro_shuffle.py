cards = input().split()
shuffle = int(input())
middle_of_deck = len(cards) // 2

for number_of_shuffle in range(shuffle):
    cards = [c for pair in zip(cards[:middle_of_deck], cards[middle_of_deck:]) for c in pair]

print(cards)