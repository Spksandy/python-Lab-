ls=[]
for i in range(5):
	ls1=[]
	for j in range(5):
		ls1.append(int(input()))
	ls.append(ls1)
print(ls)
for i in range(5):
	for j in range(5):
		if((i==0 or j==0 or i==1 or j==1 or i==2 or j==2 or i==3 or j==3 or i==4 or j==4 or i==5 or j==5) and i==j and i+j==2):
		print(ls[i][j] ,end='')
		else:
			print(' ',end='')
