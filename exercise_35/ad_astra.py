import re
text = input()

pattern = re.compile(r"([#|])(?P<item_name>[A-Za-z ]+)\1(?P<exp_date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]{1,5})\1")
result = re.finditer(pattern, text)

calories = 0
final_result = []

for show in result:
    calories += int(show["calories"])
    final_result.append({"name": show["item_name"],
                        "exp date": show["exp_date"],
                        "calories": show["calories"]})

calories_for_days = int(calories / 2000)
print(f"You have food to last you for: {calories_for_days} days!")

for show in final_result:
    print(f"Item: {show['name']}, Best before: {show['exp date']}, Nutrition: {show['calories']}")

