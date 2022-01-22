import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n=I();a=L();ans=n-1;l=[]
for i in range(1,n):
	if a[i]<a[i-1]:ans=i-1;break
for i in range(n):
	if a[i]!=a[ans]:l.append(a[i])
print(*l)