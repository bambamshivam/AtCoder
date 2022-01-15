import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import defaultdict
n,q=M();a=L();d=defaultdict(list)
for i in range(n):d[a[i]].append(i)
for i in range(q):
	x,k=M()
	if len(d[x])<k:print(-1)
	else:print(d[x][k-1]+1)