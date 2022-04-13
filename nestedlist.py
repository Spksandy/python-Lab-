ls=[]
for i in range(3):
	ls1=[]
	for j in range(3):
		ls1.append(int(input()))
	ls.append(ls1)
print(ls)
for i in range(3):
	for j in range(3):
		print(ls[i][j] ,end='')
	print()
