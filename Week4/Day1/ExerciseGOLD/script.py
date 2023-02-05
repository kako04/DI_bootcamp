print("hello world\n"*4 + "i love python\n"*4)
# exercise 2
u_inp = input("input a month (1 to 12) : ")
if int(u_inp)>= 3 and int(u_inp)<=5 :
    print("spring")
elif int(u_inp)>= 6 and int(u_inp)<=8 :
    print("summer")
elif int(u_inp)>= 9 and int(u_inp)<=11 :
    print("autumn")
else:
    print("winter")