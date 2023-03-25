def functions():
    num = input("Enter a number: ")
    num_int = int(num)
    abs_num = abs(num_int)
    print(f"The absolute value of {num_int} is {abs_num}.")

functions()

# exe2

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        elif self.currency == other.currency:
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
        elif self.currency == other.currency:
            self.amount += other.amount
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        return self

    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1)) 
print(repr(c1))

print(c1 + 5)
print(c1 + c2) 

print(c1)
c1 += 5
print(c1)

c1 += c2
print(c1)

print(c1 + c3)





