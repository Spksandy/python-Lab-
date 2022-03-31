'''
			************
			*****  *****
			***      ***
			*	   *
'''
n=int(input("Enter the no. of rows:"))
for i in range(n+2):
	print('*',end='')
print()
for i in range(n):
	for j in range((n//2)-i):
		print('*',end='')
	for j in range(2*(i+1)):
		print(" ",end='')
	for j in range((n//2)-i):
		print('*',end='')	
	print()
	
	
