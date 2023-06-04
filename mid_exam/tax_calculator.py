vehicle = input().split(">>")
total_tax = 0
info = {
    "family": {
        "tax": 50,
        "declines": 5,
        "increase": 12,
        "traveled km": 3000
    },
    "heavyDuty": {
        "tax": 80,
        "declines": 8,
        "increase": 14,
        "traveled km": 9000
    },
    "sports": {
        "tax": 100,
        "declines": 9,
        "increase": 18,
        "traveled km": 2000
    }
}
for car in vehicle:
    current_car_taxes = 0
    if any([True for car_type in list(info.keys()) if car_type in car]):
        type_car, car_years, car_km = [int(x) if x.isdigit() else x for x in car.split()]
        current_car_taxes = info[type_car]["tax"] + (
                int(car_km / info[type_car]['traveled km']) * info[type_car]['increase']) \
                            - (info[type_car]["declines"] * car_years)
        total_tax += current_car_taxes
        print(f"A {type_car} car will pay {current_car_taxes:.2f} euros in taxes.")
    else:
        print(f"Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")