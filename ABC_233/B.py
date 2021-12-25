import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

l,r=M();s=S()
print(s[:l-1]+s[l-1:r][::-1]+s[r:])