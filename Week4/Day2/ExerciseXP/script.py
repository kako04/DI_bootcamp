my_fav_numbers = set()
my_fav_numbers.add(5)
my_fav_numbers.add(9)
my_fav_numbers.pop()

friend_fav_numbers = set()
friend_fav_numbers.add(2)
friend_fav_numbers.add(25)
friend_fav_numbers.add(6)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# 2
my_tuple = (5,6,7)
# my_tuple.add(9) returns error
# its not possible

# 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana")
basket.pop(-1)
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket)
res = basket.count('Apples')
print('there are ', res ," Apples in basket")
basket.clear()
print(basket)

# 4

# float is 1.0 integer is 1

# 5

for x in range(20):
    i=x+1
    print(i)
for x in range(20):
    i=x+1
    if (i)%2==0:
        print(i)

# 6
while 1==1:
    name= input("say my name. ")
    if name=="heisenberg":
        print("you're goddamn right")
        break
# 7
fav_fruit = input("favorite fruit(s) (separate fruits with single space): ")
fav_fruits=fav_fruit.split(" ")
print (fav_fruits)
any_fruit=input("any fruit?: ")
if any_fruit == fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")