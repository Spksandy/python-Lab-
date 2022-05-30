a=int(input("Enter a mobile number:"))
l=len(str(a))
i,os,es=0,0,0
for i in range (l):
     if(a%10)%2==0:
          es=es+(a%10)
     else:
          os=os+(a%10)
     a=a//10
if(es==os):
     print("Wow,its a magic number")
else:
     print("Given Number is not a magic number")

      
