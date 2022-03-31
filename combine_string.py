'''
	input:>> list1=[13,55,45,76,65]
		 list2=[99,66,77,22,35]
	Output:>>list3=[[13,99],[55,66],[45,77],[76,22],[65,35]]
'''
a=[1,2,5,7,6,9]
b=[10,56,8,4,3,9]
print(a)
print(b)
c=[]
for i in range(6):
	c.append([a[i],b[i]])
print(c)

