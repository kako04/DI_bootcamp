import re

from anagram_checker import AnagramChecker

WORD_LIST_FILE = r'C:\Users\kakom\OneDrive\Desktop\bootcamp\DI-Bootcamp\Week5\Day5\mini_project2\sowpods.txt'


def display_anagrams(word):
    anagram_checker = AnagramChecker(WORD_LIST_FILE)
    if not anagram_checker.is_valid_word(word):
        print(f"'{word}' is not a valid English word.")
        return
    anagrams = anagram_checker.get_anagrams(word)
    if not anagrams:
        print(f"No anagrams found for '{word}'.")
        return
    print(f"Anagrams '{word}': {' '.join(anagrams)}")
def main():
    while True:
        choice = input("Enter a word or 'exit' to quit: ").strip().lower()

        if choice == 'exit':
            break

        if len(choice.split()) != 1:
            print("Error: Please enter a single word.")
            continue

        if not re.match("^[a-zA-Z]+$", choice):
            print("Error: Only alphabetic characters are allowed.")
            continue

        word = choice.strip()

        display_anagrams(word)


if __name__ == '__main__':
    main()
