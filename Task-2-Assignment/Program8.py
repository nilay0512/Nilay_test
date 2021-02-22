letter =0
num =0
s = input("Enter Value: ")
for i in s:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        num+=1
print("Letters ", letter)
print("Digits ", num)