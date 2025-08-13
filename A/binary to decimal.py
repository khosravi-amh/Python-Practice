# Convert binary numbers to desimal
a = input("enter a number in binary = ")
desimal = 0
for i in a:
    desimal = desimal*2+int(i)
print(a, "=", desimal)

# Convert desimal numbers to binary
x = int(input("enter a number in desimal = "))
binary = ""
if x == 0:
    binary = "0"
else:
    while x > 0:
        res = x % 2
        binary = str(res)+binary
        x = x//2
print(x, "=", binary)
