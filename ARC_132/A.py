import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n=I();r=L();c=L();res=""
for i in range(I()):
	a,b=M()
	if c[b-1]<=n-r[a-1]:res+='.'
	else:res+='#'
print(res)