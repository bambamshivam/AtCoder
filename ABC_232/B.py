import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

s=S()
t=S()
if len(s)!=len(t):print("No")
else:
	l=[]
	for i in range(len(s)):
		a=ord(s[i])
		b=ord(t[i])
		if b<a:b+=26
		l.append(b-a)
	if max(l)==min(l):print("Yes")
	else:print("No")