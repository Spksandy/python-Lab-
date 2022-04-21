'''n=int(input("Enter the no. of items:"))
d={1:{2:3},4:{5:6}}
for i in d.keys():
	for j in d[i].keys():
		print(d[i][j])

s=0
d={1:[2,3,4,5,6,7,8],4:[10,11,121,13,14]}
for i in d.values():
	print(sum(i))
'''
n=int(input("Enter the no. of subjects:"))
m=int(input("Enter the no. of students:"))
d={}
j=0
while(j>m):
	for i in range(n):
		k=int(input("Enter the key"))
		d[k]={}
		k1=input("Input subject:")
		v=int(input("Enter marks:"))
		d.update({k1:v})
	j=j+1
print(d)
for i in d.keys():
	for j in  d[i].keys():
		s=d[i][j]
		sum=sum+x
print("Total marks=",sum)
#print("Average marks=",sum//n)
	
