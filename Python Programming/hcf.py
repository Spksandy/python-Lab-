# Finding HCF and LCM of two numbers.....
a=int(input("Enter first no.:"))
b=int(input("Enter first no.:"))
hcf=1
for i in range(2,a+1):
    if (a%i==0 and b%i==0):
        hcf=i
print("First Number",a)
print('Second Number',b)
print('hcf=',hcf)
lcm=a*b//hcf
print('lcm=',lcm)