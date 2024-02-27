sum = 0
i = 0
print("Enter 0 to exit the program")
x=int(input("Enter Number: "))
while x != 0:
    sum += x
    x=int(input("Enter Next Number: "))
print("%d is the sum of all the numbers entered" %sum)
