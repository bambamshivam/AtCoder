import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import Counter
n,k=M();a=L();p=[0]
for i in range(n):p.append(p[-1]+a[i])
c=Counter(p);d={};ans=0
for i in range(n+1):
	d[p[i]]=d.get(p[i],0)+1
	ans+=(c[p[i]+k]-d.get(p[i]+k,0))
print(ans)