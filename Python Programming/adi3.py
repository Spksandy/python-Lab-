n=int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    for j in range(i):
        print(" ",end='')
    for j in range(i):
        print(" ",end='')
    for j in range(n-i):
        print("*",end='')
    print()