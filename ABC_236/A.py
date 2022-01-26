import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

s=S();a,b=M()
l=list(s)
l[a-1],l[b-1]=l[b-1],l[a-1]
print(''.join(l))