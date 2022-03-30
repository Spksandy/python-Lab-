c='y'
b=[]
while c=='y' or c=='Y':
	c=input('do u want to continue y/n')
	if c=='y' or c=='Y':
		i=input('enter the elements')
		b.append(i)
print(b)
print(count(b))
