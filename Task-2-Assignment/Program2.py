

# Python program under following conditions
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Division")
print("Enter 4 for Multiplication")
print("Enter 5 for Average")
op = int(input("choose your option: "))
x = int(input("Input number 1: "))
y = int(input("Input number 2: "))
if op == 1:
    if (x+y)<0:
        print("addition:  NEGATIVE")
    else:
        print("addition: ", (x+y))
elif op == 2:
    if (x-y)<0:
        print("subtraction:  NEGATIVE")
    else:
        print("subtraction: ", (x-y))
elif op == 3:
    if (x / y) < 0:
        print("Divide:  NEGATIVE")
    else:
        print("Divide: ", (x / y))
elif op == 4:
    if (x * y) < 0:
        print("Multiplication:  NEGATIVE")
    else:
        print("Multiplication: ", (x * y))
elif op == 5:
    if (x + y)/2 < 0:
        print("Average:  NEGATIVE")
    else:
        print("Average: ", (x + y)/2)