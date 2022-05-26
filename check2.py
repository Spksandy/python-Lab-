f=open("spk.txt",'r+')
nf=open("test.txt",'a+')
r=f.readlines()  # Change every lines into list
for i in range (len(r)):
	if i%2==0:
		s=r[i]
		nf.write(s)
f.close()
nf.close()		

