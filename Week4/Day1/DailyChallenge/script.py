# 1
u_str = input("string at least 10 charachters long: ")
if len(u_str)< 10:
    print('string not long enough my guy')
elif len(u_str)>10:
    print('too long oe')
else:
    (print("yay"))
# 2
print(u_str[0], u_str[-1])
# 3
for x in range(len(u_str)):
    print(u_str[:x+1])
# 4
import random

l= list(u_str)
random.shuffle(l)
result = ''.join(l)
print(result)