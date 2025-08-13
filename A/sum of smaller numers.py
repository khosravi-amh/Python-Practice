# Sum of all smaller numbers
x = int(input("enter number for Sum of all smaller numbers = "))
sum = 0
i = 1
while i < x+1:
    sum += i
    i += 1
print("sum = ", sum)
