import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

x=S();res=[]
def f(s,d,i,l):
	if len(s)==len(x):l.append(s);return
	if i>9:return
	f(s+str(i),d,i+d,l)
for i in range(10):
	for d in range(10):
		l=[];f("",d,i,l)
		res+=l
a=[]
for i in res:a.append(str(i)[::-1])
ans=a+res
for i in range(len(ans)):ans[i]=int(ans[i])
ans.sort()
for i in ans:
	if i>=int(x):break
print(i)