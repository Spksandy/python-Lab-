#  To create a list using append and insert function using user choice....
x=int(input("Enter the no. of elements you want to insert:"))
lst=[]
for i in range(x):
	#lst.append(int(input()))
	lst.insert(i,int(input()))
print(lst)
