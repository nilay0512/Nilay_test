a=int(input("Value1:"))
b=int(input("Value2:"))
c=int(input("Value3:"))
avg = (a+b+c)/3
print("avg=",avg)
if avg>a and avg>b and avg>c:
    print("avg is higher than a,b,c")
elif avg>a and avg>b:
    print("avg is higher than a,b")
elif avg>a and avg>c:
    print("avg is higher than a,c")
elif avg>b and avg>c:
    print("avg is higher than b,c")
elif avg>a:
    print("avg is higher than a")
elif avg>b:
    print("avg is higher than b")
elif avg>c:
    print("avg is higher than c")