import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

h,w=M();l=[];m=0
for i in range(h):l.append(S())
dp=[[-1 for i in range(w)] for j in range(h)];dp[0][0]=1
for i in range(1,h):
	if l[i][0]=='#':break
	dp[i][0]=dp[i-1][0]+1
for i in range(1,w):
	if l[0][i]=='#':break
	dp[0][i]=dp[0][i-1]+1
for i in range(1,h):
	for j in range(1,w):
		if l[i][j]=='#':continue
		a=b=-1
		if dp[i-1][j]!=-1:a=dp[i-1][j]
		if dp[i][j-1]!=-1:b=dp[i][j-1]
		if a!=-1 or b!=-1:
			dp[i][j]=max(a,b)+1
for i in range(h):
	for j in range(w):
		m=max(dp[i][j],m)
print(m)