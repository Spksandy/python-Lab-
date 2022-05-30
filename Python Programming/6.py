#  Diamond Pattern......
n=int(input("Enter the No. of rows:>"))
for i in range(n): 
    for j in range(n-i-1):
        print(" ",end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for j in range(n-i-1):
        print("*",end='')
    for j in range(n-i-2):
        print("*",end='')
    print()
    
