class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
        
    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of their new child, {kwargs['name']}!")
        
    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        print(f"No family member with the name {name} was found.")
        return False
    
    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(f"- {member['name']}") 


my_family = Family(members=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
], last_name='Smith')

my_family.born(name='John', age=0, gender='Male')

print(my_family.is_18('Michael'))


print(my_family.is_18('Sarah'))


print(my_family.is_18('John'))

my_family.family_presentation()

