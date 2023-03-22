# exe1
print("||||||||||||||||1|||||||||||||||")

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Kitty", 3)
cat2 = Cat("Tom", 5)
cat3 = Cat("Fluffy", 2)

def find_oldest_cat(*cats):
    oldest_cat = None
    for cat in cats:
        if oldest_cat is None or cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# exe 2
print("||||||||||||||||2|||||||||||||||")

class dog:
    def __init__(self, name, height):
        self.name=name
        self.height=height

    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")
        
davids_dog = dog("Rex", 50)
print(f"dogs name is {davids_dog.name}, height is {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = dog("Teacup", 20)
print(f"Sarah's dog: name={sarahs_dog.name}, height={sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
else:
    print(f"{sarahs_dog.name} is bigger")

# exe3
print("|||||||||||||||3||||||||||||||||")

class song:
    def __init__(self, lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

stairway= song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# exe4
print("|||||||||||||||||4||||||||||||||")

class zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the {self.name}")
        else:
            print(f"{new_animal} is already in the {self.name}")

    def get_animals(self):
        print(f"Animals in the {self.name}: {', '.join(sorted(self.animals))}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from the {self.name}")
        else:
            print(f"{animal_sold} is not in the {self.name}")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            if animal[0] not in sorted_animals:
                sorted_animals[animal[0]] = [animal]
            else:
                sorted_animals[animal[0]].append(animal)
        sorted_animals = dict(sorted(sorted_animals.items()))
        return sorted_animals
    
    def get_groups(self):
        print("Groups of animals in the zoo:")
        groups = {}
        for animal in self.animals:
            group = type(animal).__name__
            if group not in groups:
                groups[group] = []
            groups[group].append(animal)
        for group, animals in groups.items():
            animal_str = ", ".join([str(animal) for animal in animals])
            print(f"{group}s: {animal_str}")
