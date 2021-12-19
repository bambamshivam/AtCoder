import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353;sys.setrecursionlimit(10000000)
n,m=M();adj=[[] for i in range(n)];deg=[0]*n
for i in range(m):
	a,b=M()
	adj[a-1].append(b-1)
	adj[b-1].append(a-1)
	deg[a-1]+=1;deg[b-1]+=1
v=[0]*n
def dfs(i,d):
	v[i]=1
	for j in adj[i]:
		if v[j]==0:
			d[j]=1
			dfs(j,d)
ans=1
for i in range(n):
	if v[i]==0:
		d={};d[i]=1;s=0
		dfs(i,d)
		for key in d:
			s+=deg[key]
		if s//2==len(d):
			ans=(ans*2)%mod2
		else:
			ans=0
			break
print(ans)