import random

number = random.randint(0, 9)
while number > 0:
    guess = input("Enter the lucky number or type no to stop: ")

    if guess.lower()=='no':
        break

    answer = int(guess)
    if number == answer:
        print("Cong you are right!")
        break
    else:
        continue
