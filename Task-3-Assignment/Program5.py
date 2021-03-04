#list1 = [2,3,4,5,6,8,10,12,13,15,17]
#list1 = [x for x in list1 if x%2!=0]
#print(list1)


list2=[1,3,5,2,4,6,10,12,13,15]
listx = list2;
#print(list2)
for i in listx:
	if(i%2 == 0):
		{
	    list2.remove(i)
		}
print(list2)
