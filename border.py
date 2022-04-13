ls=[]
for i in range(3):
	ls1=[]
	for j in range(3):
		ls1.append(int(input()))
	ls.append(ls1)
print(ls)
for i in range(3):
	for j in range(3):
		if(i==0 or j==0 or i==1 or j==2):
			print(ls[i][j],end='')
		else:
			print(' ',end='')
