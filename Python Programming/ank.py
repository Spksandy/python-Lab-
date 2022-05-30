a = int(input('Enter the row : '))
b = 0
for i in range(1,a+1):
    for j in range(1,i+1):
        b+=1
        print(b,end = "  ")
    print(end = "\n\n") 
for i in range(a-1,0,-1):
    for j in range(i,0,-1):
        b+=1
        print(b,end = "  ")
    print(end = "\n\n")