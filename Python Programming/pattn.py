'''
                *
              * * *
            * * * * *
              * * *
                *
'''
n=int(input("Enter the no. of rows:"))
'''for i in range(n-3):
	for j in range(n-i-3):
		print("  ",end='')
	for j in range(2*i+1):
		print('* ',end='')
	print()'''
for i in range(n-3):
    for j in range(i+1):
        print('  ',end='')
    for j in range(n-2*i-2):
        print("* ",end='')
    print()

