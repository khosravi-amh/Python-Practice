#Display the students status according to the following grades :
#A=20-18  B=18-16  c=16-14
a=float(input("Enter the students grade to view status= "))
if a>=18 and a<=20:
    print("*GOOD*  Status A")
elif a>=16 and a<18:
    print("*AVERAGE*  Status B")
elif a>=14 and a<16:
    print("*BAD*  Status C")
else:
    print("ERROR enter betwen 14-20")

