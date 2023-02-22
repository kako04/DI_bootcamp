file_location = 'C:\Users\kakom\OneDrive\Desktop\bootcamp\DI-Bootcamp\Week5\Day4\files\nameslist.txt'

all_text = ""
text_lines = []

with open(file_location, 'r') as file:
    print(file.tell())
    all_text: str = file.read()
    print(file.tell()) # tell() tells where the pointer is 
    file.seek(0) # puts the pointer at a given location (0[zero] means the start)
    print(file.tell())
    text_lines: list = file.readlines()

print(text_lines)
