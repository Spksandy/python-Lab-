n=int(input("Enter the no. of rows:"))
list1=[]
for i in range(n):
    list2=[]
    for j in range(n):
        list2.append(int(input()))
    list1.append(list2)
print(list1)
for i in range(n):
    for j in range(n):
        print(list1[i][j],'\t',end='')
    print()
    
    