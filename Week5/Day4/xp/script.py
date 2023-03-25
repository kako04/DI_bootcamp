import random

def get_words_from_file(filename):
    with open(filename) as f:
        words = f.read().split()
    return words

def get_random_sentence(length):
    words = get_words_from_file('sowpods.txt')
    sentence = ' '.join(random.sample(words, length)).lower()
    return sentence

def main():
    print('Welcome to the random sentence generator!')
    while True:
        try:
            length = int(input('How many words do you want in your sentence? (2-20) '))
            if length < 2 or length > 20:
                print('Error: The input must be an integer between 2 and 20.')
            else:
                break
        except ValueError:
            print('Error: The input must be an integer between 2 and 20.')
    sentence = get_random_sentence(length)
    print('Your random sentence is:', sentence)

if __name__ == '__main__':
    main()

# exe 2

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Load the JSON string into a dictionary
data = json.loads(sampleJson)

# Access the nested "salary" key
salary = data['company']['employee']['payable']['salary']
print("Salary:", salary)

# Add a "birth_date" key
data['company']['employee']['birth_date'] = "1990-01-01"

# Save the updated dictionary as JSON to a file
with open('updated.json', 'w') as outfile:
    json.dump(data, outfile)
