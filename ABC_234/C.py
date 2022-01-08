import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

k=I();s=bin(k)[2:];l=[]
for i in s:
	if i=='1':l.append('2')
	else:l.append(i)
print(''.join(l))