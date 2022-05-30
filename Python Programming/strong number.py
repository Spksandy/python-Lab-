#Checking of a strong number.....e.g=145=1!+4!+5!
n=int(input("Enter a number:"))
sum=0
temp=n
while(n):
    i=1
    f=1
    r=n%10
    while(i<=r):
        f=f*i
        i=i+1
    sum=sum+f
    n=n//10
if(sum==temp):
    print("Wow,it's a strong number.")
else:
    print("Not a strong number.")
