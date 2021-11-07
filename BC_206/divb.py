import math
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
	for j in range(i+1,r+1):
		k=math.gcd(i,j)
		if k!=1 and k!=i and k!=j:
			c+=1
print(2*c)