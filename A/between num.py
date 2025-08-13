# Display between numbers
a = int(input("enter num1 = "))
b = int(input("enter num2 = "))
start = min(a, b)
end = max(a, b)
print("1- Ascending")
print("2- Descending")
c = int(input("select from menue = "))
match c:
    case 1:
        while start < end-1:
            print(start+1, end=' ')
            start += 1
    case 2:
        while start+1 < end:
            print(end-1, end=' ')
            end -= 1
