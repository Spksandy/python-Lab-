n=int(input("Enter a number:"))
order=len(str(n))
count=0
temp=n
while(temp>0):
    digit=temp%10
    count=count+digit**order
    temp=temp//10
if count==n:
    print("It's a Armstrong Number:")
else:
    print("Given number is not a armstrong numbers:")
