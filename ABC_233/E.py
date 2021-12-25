import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

x=S();s=c=0;res=""
for i in x:s+=int(i)
for i in range(len(x)-1,-1,-1):
	c+=s;res+=str(c%10);c//=10
	if i>=0:s-=int(x[i])
	if i<=0 and c==0:break
if c!=0:res+=str(c)
print(res[::-1])