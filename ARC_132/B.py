import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n=I();p=L()
if p==sorted(p):print(0)
else:
	i=p.index(1)
	if p[(i+1)%n]==2:print(min(i,n-i+2))
	else:print(min(n-i,i+2))