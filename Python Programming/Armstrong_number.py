# Armstrong number in range.....
a=int(input("Enter lower limit:"))
b=int(input("Enter lower limit:"))
order=len(str(a))
for i  in range(a,b+1):
    count=0
    temp=i
    while(temp>0):
        digit=temp%10
        count=count+digit**order
        temp=temp//10
    if count==i:
        print(i)
    
