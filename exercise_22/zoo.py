class Zoo:
    __animals = 0

    def __init__(self, name_zoo, name, type):
        self.name_zoo = name_zoo
        self.name = name
        self.type = type

    def get_info(self, species):
        if species == self.type:
            return True
        return False


animals_info = []
name_animal = {"mammal": "Mammals", "fish": "Fishes", "bird": "Birds"}


zoo_name = input()
Zoo.animals = int(input())
for _ in range(Zoo.animals):
    type, name = input().split()
    animals_info.append(Zoo(zoo_name, name, type))

show_animals = input()
print(f"{name_animal[show_animals]} in {zoo_name}: {', '.join([x.name for x in animals_info if x.get_info(show_animals)])}")
print(f"Total animals: {Zoo.animals}")
