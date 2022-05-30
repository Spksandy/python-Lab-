#Program to merge two lists inputted from user....10
n=int(input("Enter the no. of elements u want to input:"))
a=[]
b=[]
c=[]
print('staring element of a1')
for i in range(n):
    s=int(input())
    a.append(s)
print('stating element of a2')
for i in range(n):
    y=int(input())
    b.append(y)
print(a)
print(b)
print("List after merging:")
for i in range(n):
    c.append((a[i],b[i]))
print(c)