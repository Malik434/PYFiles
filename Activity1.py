print("Enter 0 to exit the program")
x=int(input("Enter X: "))
while x != 0:
    if x % 2 == 0:
        print( "%d is even" %x)
    else:
        print("%d is odd" %x)
    x=int(input("Enter X: "))