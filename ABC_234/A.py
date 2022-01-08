import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

t=I()
def f(x):return x*x+2*x+3
print(f(f(f(t)+t)+f(f(t))))