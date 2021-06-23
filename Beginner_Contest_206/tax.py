import math
n=int(input())
k=math.floor(n*1.08)
if k<206.0:
	print("Yay!")
elif k==206:
	print("so-so")
else:
	print(":(")