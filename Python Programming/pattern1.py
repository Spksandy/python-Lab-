# Two ways of printing the same pattern
"""
    *
    **
    ***
    **
    *
"""

'''n = int(input("Enter a number\n"))
for i in range(n):
    for j in range(i):
        print("*", end=' ')
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()'''


n=int(input("Enter the no. of rows:"))
for i in range(n):
    for j in range(i):
        print("* ",end="")
    print()
for i in range(n):
    print("* ",end='')
print()
for i in range(i+1):
    for j in range(n-1-i):
        print("* ",end='')
    print()

