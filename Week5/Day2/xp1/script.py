class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_cat = Bengal("Bengal", 2)
chartreux_cat = Chartreux("Chartreux", 4)
siamese_cat = Siamese("Siamese", 1)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)

sara_pets.walk()

# exe2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self):
        return f"{self.name} is barking."
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        self_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if self_score > other_score:
            return f"{self.name} won the fight."
        elif other_score > self_score:
            return f"{other_dog.name} won the fight."
        else:
            return "It's a tie."

dog1 = Dog("Rufus", 5, 25)
dog2 = Dog("Buddy", 3, 18)
dog3 = Dog("Lola", 7, 32)

print(dog1.bark()) 
print(dog2.run_speed())
print(dog3.fight(dog2))

# exe3

import random

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

class PetDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        dog_names = [dog.name for dog in args]
        dog_names.append(self.name)
        print(f"{' '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            trick = random.choice(["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"])
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} is not trained yet!")
