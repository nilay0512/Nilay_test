import random

counter = 1
while counter <= 5:
    number = random.randint(0, 9)
    print(number)
    print("Type in the ", counter, "number ")
    answer = int(input())
    counter = counter + 1
    if number == answer:
        print("Good Guess")
        break
    else:
        if counter!=6:
            print("Try again")
    if counter==6:
        print("Sorry but that was not very successful")
