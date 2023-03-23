class Farm:
    def __init__(self, name) -> None:
        self.mac_name = name
        self.animals: dict= {}

    def add_animal(self, animal: str, amount: int = 1):
        if animal not in self.animals:
            self.animals[animal] = amount
        else:
            self.animals[animal] +=amount
    def get_info(self):
        out_str: str=f"{self.mac_name}'s farm \n\n"
        for animal, amount in self.animals.items():
            out_str += f'{animal} : {amount} \n'
        strange_str = '\n      E-I-E-I-0'
        out_str += strange_str
        print(out_str)

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.animals)
print(macdonald.get_info())

