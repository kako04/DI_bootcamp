# exe 2

import random

def accept_num(self):
    if self < 1 or self>100:
        print("only number that is between 1 and 100")
        return
    roll =random.randint(1,100)
    if self == roll:
        print("same num!")
    else:
        print("try again")

accept_num(50)

# exe 3

import random
import string

def generate_random_string(length=5):
    # Generate a string containing uppercase and lowercase letters
    letters = string.ascii_letters
    
    # Generate a random string of the specified length
    random_string = ''.join(random.choices(letters, k=length))
    
    return random_string

print(generate_random_string())

# exe 4

import datetime

def display_current_date():
    current_date = datetime.date.today()
    print("Today's date is:", current_date)
display_current_date()

# exe 5
import datetime

def time_left_until_january_1st():
    current_datetime = datetime.datetime.now()
    
    january_1st = datetime.datetime(current_datetime.year, 1, 1)
    
    time_difference = january_1st - current_datetime
    
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"The 1st of January is in {days} days and {hours:02d}:{minutes:02d}:{seconds:02d} hours.")
time_left_until_january_1st()


# exe 6

import datetime

def minutes_lived(birthdate):
    birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    
    current_datetime = datetime.datetime.now()
    
    time_difference = current_datetime - birth_datetime
    minutes_lived = round(time_difference.total_seconds() / 60)
    
    print(f"You have lived for {minutes_lived} minutes so far!")
minutes_lived("2004-05-15")

# exe 7
import datetime

def display_today_and_next_holiday():
    today_date = datetime.date.today()
    
    next_holiday_name = "Labor Day"
    next_holiday_date = datetime.date(today_date.year, 9, 5)
    if next_holiday_date < today_date:
        next_holiday_date = datetime.date(today_date.year + 1, 9, 5)
    
    time_difference = datetime.datetime.combine(next_holiday_date, datetime.time.min) - datetime.datetime.now()
    
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Today's date is: {today_date}")
    print(f"The next holiday is {next_holiday_name} and it is in {days} days and {hours:02d}:{minutes:02d}:{seconds:02d} hours.")
display_today_and_next_holiday()

# exe 8

def age_on_planet(age_seconds):
    earth_year_in_seconds = 31557600
    age_earth_years = age_seconds / earth_year_in_seconds
    
    mercury_age = age_earth_years / 0.2408467
    venus_age = age_earth_years / 0.61519726
    mars_age = age_earth_years / 1.8808158
    jupiter_age = age_earth_years / 11.862615
    saturn_age = age_earth_years / 29.447498
    uranus_age = age_earth_years / 84.016846
    neptune_age = age_earth_years / 164.79132
    
    return {
        'Earth': round(age_earth_years, 2),
        'Mercury': round(mercury_age, 2),
        'Venus': round(venus_age, 2),
        'Mars': round(mars_age, 2),
        'Jupiter': round(jupiter_age, 2),
        'Saturn': round(saturn_age, 2),
        'Uranus': round(uranus_age, 2),
        'Neptune': round(neptune_age, 2)
    }
print(age_on_planet(1000000000))

# exe 9

from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Create an empty list to store users
users = []

# Define a function to add new users to the list
def add_user():
    # Generate fake data using faker
    name = fake.name()
    address = fake.address()
    language_code = fake.language_code()
    
    # Create a dictionary for the new user and add it to the list
    user = {
        'name': name,
        'address': address,
        'language_code': language_code
    }
    users.append(user)

add_user()

for i in range(10):
    add_user()
