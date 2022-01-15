import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n=I();a=L();ans=a[0]
for i in range(1,n):
	if a[i]>ans:ans=a[i]
	else:break
print(ans)