import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n,m=M()
s=list(input().split());t=list(input().split())
d=set(t)
for i in s:
	print("Yes" if i in d else "No")