import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
import itertools
n,m=M();s1=set();s2=set()
for i in range(m):
	a,b=M()
	if a>b:a,b=b,a
	s1.add((a,b))
a=[i for i in range(1,n+1)];p=list(itertools.permutations(a));l=[];f=0
for i in range(m):l.append(L())
for d in p:
	s2=set()
	for i in range(m):
		a,b=l[i];p=d[a-1];q=d[b-1]
		if p>q:p,q=q,p
		s2.add((p,q))
	if s1==s2:f=1;break
if f==1:print("Yes")
else:print("No")