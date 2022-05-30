a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
hcf=1
for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        hcf=i
print("First number",a)
print("Second Number",b)
print("hcf",hcf)
lcm=a*b//hcf
print("Lcm ",lcm)