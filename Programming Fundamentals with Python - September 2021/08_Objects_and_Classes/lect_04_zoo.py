class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, curr_species, name):
        if curr_species == "mammal":
            self.mammals.append(name)
            Zoo.__animals += 1
        elif curr_species == "bird":
            self.birds.append(name)
            Zoo.__animals += 1
        elif curr_species == "fish":
            self.fishes.append(name)
            Zoo.__animals += 1

    def get_info(self, curr_species):
        if curr_species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\n Total animals: {Zoo.__animals}"
        elif curr_species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\n Total animals: {Zoo.__animals}"
        elif curr_species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\n Total animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for animal in range(count):
    species, anim_name = input().split()
    zoo.add_animal(species, anim_name)

species = input()

print(zoo.get_info(species))

