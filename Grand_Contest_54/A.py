import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(input())
def L():
	return list(map(int,input().split()))

def mo(s):
	if len(s)==0:
		return (True,0)
	if s==s[0]*len(s):
		return (False,-1)
	m=1000000000000000
	f=0
	for i in range(1,len(s)):
		if s[i]!=s[0]:
			x=mo(s[i+1:])
			if x[0]==True:
				m=min(m,x[1]+1)
				f=1


	if f==1:
		return (True,m)
	else:
		return (False,-1)
			

n=I()
s=S()
print(mo(s)[1])
