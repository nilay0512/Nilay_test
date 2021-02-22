x=123
for i in x:
    print(i)

# output -  for i in x:
# TypeError: 'int' object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")

#output -
# 0
# error
# 1
# error
# 2


count =0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Output - spellcheck - original Break/ break (compile error)
# 0
# 1
# 2
# 3
# 4
