import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from bisect import bisect_left
n,m,q=M();l=[];p=list(range(n+1));cnt=0;ans=["No"]*q
for i in range(m):
	a,b,c=M();l.append([a,b,c,-1])
for i in range(q):
	u,v,w=M();l.append([u,v,w,i])
l.sort(key=lambda x:x[2])
def find(x):
	if x==p[x]:return x
	p[x]=find(p[x]);return p[x]
for i in range(q+m):
	if cnt==n-1:break
	u,v,w,e=l[i]
	if e>=0:
		if find(u)!=find(v):
			ans[e]="Yes"
			continue
	u=find(u);v=find(v)
	if u!=v:p[u]=v;cnt+=1
print(*ans)