countries = input().split(", ")
capitals = input().split(", ")

capital_by_country = {countries[idx]: capitals[idx] for idx in range(len(countries))}

for countries, capitals in capital_by_country.items():
    print(f"{countries} -> {capitals}")

