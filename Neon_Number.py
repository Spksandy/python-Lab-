#********...Checking a Number is Neon or Not...******
num=int(input("Enter a number:"))
b=num*num
l=len(str(b))
sum=0
i=0
while(i<l):
    p=b%10
    sum=sum+p
    b=b//10
    i=i+1
if num==sum:
    print("Wow,it's a Neon Number")
else:
    print("Not A Neon Number")
    

