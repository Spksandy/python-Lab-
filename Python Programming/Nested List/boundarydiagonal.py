"""
    >>Printing boundary elements of array of a list....
        1(0,0)   2(0,1)   3(0,2)       1    2   3 
        4(1.0)   5(1,1)   6(1,2)  ==   4        6
        7(2,0)   8(2,1)   9(2,2)       7    8   9
"""
import time
n=int(input("Enter the no. of rows:"))
list1=[]
for i in range(n):
    list2=[]
    for j in range(n):
        list2.append(int(input()))
    list1.append(list2)
print(list1)
print("Boundary elements of array of list:")
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1: 
            print(list1[i][j],'\t',end='')
        else:
            print(" ",'\t',end='')
        time.sleep(0.5)
    print()