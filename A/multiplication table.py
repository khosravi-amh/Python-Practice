#multiplication table a*b
a=int(input("enter number one between 1-10 = "))
b=int(input("enter number two = "))
for a in range (1,a+1):
    for b in range (1,b+1):
        print(a*b,'  ',end='  ')
    print()