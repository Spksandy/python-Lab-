a=int(input("Enter lower limit of range:"))
b=int(input("Enter upper limit of range:"))
order=len(str(a))
for a in range(a,b):
    temp=a
    count=0
    while(temp>0):
        digit=temp%10
        count=(count*10)+digit
        temp=temp//10
    if count==a:
        print(a)
    
