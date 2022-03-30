# Python programm to find second largest element in a list.....
a=[2,6,1,7,15,80,100]
'''counter=0
for i in range (len(a)):
	if a[i]>counter:
		counter=a[i]
print(counter)'''
z=max(a)
temp=0
slar=0
for i in range (len(a)):
	if a[i]>slar:
		slar=a[i]
