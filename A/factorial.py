# Factorial
a = int(input("enter anumber = "))
i = 1
res = 1
if a > 0:
    while i < a+1:
        res *= i
        i += 1
    print(res)
else:
    print("*ERROR*  Not allowed for negative number")
