keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(tuple(zip(keys, values)))

# exe2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
totalprice=0
name=input("name: ")
age = int(input("age: "))
family[name] = age
for name, age in family.items():
    if age < 3:
        ticket_price = 0
    elif age >= 3 and age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    totalprice += ticket_price
    print(name + " needs to pay $" + str(ticket_price) + " for the movie ticket.")
print("totalprice is "+ str(totalprice))
# rick needs to pay $15 for the movie ticket.
# beth needs to pay $15 for the movie ticket.
# morty needs to pay $10 for the movie ticket.
# summer needs to pay $10 for the movie ticket.
print("||||||||||||||||||||||||||||")
# exe 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": "men, women, children, home",
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print("Zara's clients are", brand["type_of_clothes"], "shoppers.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print(brand["number_stores"])

print("||||||||||||||||||||||||||||")

# exe 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}

for i, user in enumerate(users):
    disney_users_A[user] = i

print(disney_users_A)

# 
disney_users_B = {}

for i, user in enumerate(users):
    disney_users_B[i] = user

print(disney_users_B)
# 
disney_users_C = dict(zip(sorted(users), range(len(users))))

print(disney_users_C)
# 
disney_users_A = {}

for i, user in enumerate(users):
    if "i" in user:
        disney_users_A[user] = i

print(disney_users_A)

disney_users_A = {}

for i, user in enumerate(users):
    if user.startswith("m") or user.startswith("p"):
        disney_users_A[user] = i

print(disney_users_A)