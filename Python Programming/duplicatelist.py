list1=[2,4,2,3,1,6,8,9,5,7]
print(list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
list2=set(list2)
print(list2)