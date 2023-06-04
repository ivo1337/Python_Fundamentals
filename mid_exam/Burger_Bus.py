number_of_cities = int(input())
profit = 0

for city in range(1, number_of_cities + 1):
    bus_city = input()
    money_earning = float(input())
    expenses = float(input())
    if city % 3 == 0 and city % 5 != 0:
        expenses *= 1.5
    elif city % 5 == 0:
        money_earning = 0.9 * money_earning
    current_profit = money_earning - expenses
    profit += current_profit
    print(f"In {bus_city} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {profit:.2f} leva.")