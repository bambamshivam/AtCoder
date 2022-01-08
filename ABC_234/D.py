import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
import heapq
n,k=M();p=L();h1=[];h2=[]
for i in range(n):
	heapq.heappush(h1,p[i])
	if i>=k-1:
		s=heapq.heappop(h1)
		heapq.heappush(h2,-s)
		ans=heapq.heappop(h2)
		print(-ans)
		heapq.heappush(h2,ans)