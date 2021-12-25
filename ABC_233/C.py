import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import Counter
n,x=M();l=[];ans=[0]
for i in range(n):l.append(Counter(L()[1:]))
def solve(i,a,c):
	if i==n-1:ans[0]+=(c*l[-1][a]);return
	for j in l[i]:
		if a%j==0:solve(i+1,a//j,c*l[i][j])
solve(0,x,1);print(ans[0])