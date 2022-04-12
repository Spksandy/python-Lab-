import time

"""n=5
for i in range(n):
	for j in range(i):
		print(' ',end='')
	for j in range(i+1):
		print('*')
	for j in range()"""

n=int(input("Enter a no. greater than 8:>"))
for i in range(n): 
  
        # Inner for loop for printing *'s and  &nbsp's(columns) 
        for j in range((n // 2) + 1): 
  
            # prints two column lines 
            if ((j == 0 or j == n //2) and i != 0 or
  
                # print first line of alphabet 
                i == 0 and j != 0 and j != n // 2 or
  
                # prints middle line 
                i == n // 2): 
                print("*", end = "") 
            else: 
                print(" ", end = "") 
            time.sleep(0.5)
          
        print() 
        
        
        
