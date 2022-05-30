import time
ls=[]
for i in range(3):
	ls1=[]
	for j in range(3):
		ls1.append(int(input()))
	ls.append(ls1)
print(ls)
for i in range(3):
	for j in range(3):
		if(i==0 or j==0 or i==3-1 or j==3-1):
			print(ls[i][j],'\t',end='')
		else:
			print(' ','\t',end='')
		time.sleep(0.4)
	print()