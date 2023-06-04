from collections import defaultdict

input_str = input()
food_map = {}
area_map = defaultdict(list)

while input_str != "EndDay":
    command_input = input_str.split()
    command = command_input[0]
    command2 = command_input[1].split("-")

    if command == "Add:":
        name = command2[0]
        needed_food = int(command2[1])
        area = command2[2]

        if name in food_map:
            current_food = food_map[name]
            total_food = current_food + needed_food
            food_map[name] = total_food
        else:
            food_map[name] = needed_food
            area_map[area].append(name)

    elif command == "Feed:":
        name_fed = command2[0]
        amount_of_food = int(command2[1])
        if name_fed in food_map:
            current_food = food_map[name_fed]
            food_left = current_food - amount_of_food
            if food_left <= 0:
                print(f"{name_fed} was successfully fed")
                del food_map[name_fed]
                area_map = {area: [name for name in names if name != name_fed] for area, names in area_map.items()}
            else:
                food_map[name_fed] = food_left

    input_str = input()

empty_areas = [area for area, names in area_map.items() if len(names) == 0]
for area in empty_areas:
    del area_map[area]

print("Animals:")
if food_map:
    for name, food in food_map.items():
        print(f" {name} -> {food}g")
else:
    print("None")

print("Areas with hungry animals:")
if area_map:
    for area, names in area_map.items():
        num_hungry = len(names)
        print(f" {area}: {num_hungry}")
else:
    print("None")