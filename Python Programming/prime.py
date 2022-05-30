n = int(input("Enter a number to check whether it is prime or not:\n"))
c=0
for i in range(1,n+1):
    if n % i == 0:
        c+=1
if c == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")