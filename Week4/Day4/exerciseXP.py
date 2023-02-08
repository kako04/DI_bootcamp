import random

# exe 1 

def display_message() -> str:
    sentence = "i am learning in this course!"
    return sentence
display_message()

# exe 2
def favorite_book(title):
    print("One of my favorite books is {}".format(title))
favorite_book("Tom_sawyer")

# exe 3
def describe_city(city, country = "israel") -> str:
    sentence = (city," is in ", country)
    return sentence
describe_city("Batman", "Turkey")

# exe 4

def number(user_number, random_number):
    if user_number == random_number:
        print( "success")
    else :
        print("try again")

rand_num = random.randint(1, 100)

number(int(input("your number: ")), rand_num)

# exe 5

def make_shirt(size = "L" , printed_text = "i love python"):
    print ( "The size of the shirt is {} and the text is {}".format(size, printed_text))

make_shirt("L",)
make_shirt('M',)
make_shirt("","hollup.")

# exe 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for i in magician_names:
        print(i) 
show_magicians()

def make_great():
    string = "the great "
    for i in magician_names:
        great_magicians = (string + i) 
        print(great_magicians)


make_great()
# exe 7

# def get_random_temp() ->int:
#     temp =  random.randint(-10,40)
#     return temp 

# def main():
#     rand_temp = get_random_temp()
#     print(f"The temperature right now is {rand_temp} degrees Celsius.")
#     if rand_temp <= 0 :
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif rand_temp > 0 and rand_temp <= 16:
#         print("Quite chilly! Don’t forget your coat")
#     elif rand_temp > 16 and rand_temp <= 23:
#         print("nice weather out! wear something light and comfortable")
#     elif rand_temp > 23 and rand_temp <= 32:
#         print("warm weather! wear something short sleeved")
#     else:
#         print("very warm! wear swimming gear")
    
# main()

def get_random_temp(season):
    if season == "winter":
        temp =  random.randint(-10,5)
    elif season == "spring":
        temp =  random.randint(5,21)
    elif season == "summer":
        temp =  random.randint(21,40)
    elif season == "fall":
        temp =  random.randint(4,19)
    return temp

def main():
    season = input("‘summer’, ‘fall’, ‘winter’, or ‘spring’?")

    rand_temp = get_random_temp(season)
    print(f"The temperature right now is {rand_temp} degrees Celsius.")
    if rand_temp <= 0 :
        print("Brrr, that’s freezing! lets go skiing!")
    elif rand_temp > 0 and rand_temp <= 16:
        print("Quite chilly! Don’t forget your coat")
    elif rand_temp > 16 and rand_temp <= 23:
        print("nice weather out! wear something light and comfortable")
    elif rand_temp > 23 and rand_temp <= 32:
        print("warm weather! wear something short sleeved")
    else:
        print("very warm! wear swimming gear")
    
main()