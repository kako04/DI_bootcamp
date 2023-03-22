word = input("gimme a word: ")
letter_indexes = {}

for i, letter in enumerate(word):
    if letter in letter_indexes:
        letter_indexes[letter].append(i)
    else:
        letter_indexes[letter] = [i]

print(letter_indexes)

# exe 2

def items_you_can_afford(items_purchase, wallet):
    wallet = int(wallet.strip('$').replace(',', ''))
    affordable_items = [item for item, price in items_purchase.items() if int(price.strip('$').replace(',', '')) <= wallet]
    if affordable_items:
        return sorted(affordable_items)
    else:
        return "Nothing"

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

print(items_you_can_afford(items_purchase, wallet))
