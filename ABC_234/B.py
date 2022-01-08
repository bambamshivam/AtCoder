import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n=I();l=[];ans=0
for i in range(n):l.append(L())
for i in range(n):
	for j in range(i+1,n):
		ans=max(ans,(l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2)
print(math.sqrt(ans))