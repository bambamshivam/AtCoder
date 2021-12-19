import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())

a,b,c,d=M()
if  d*c - b<=0:
	print(-1)
else:
	print(int(math.ceil(a/(d*c - b))))
