n=int(input())
l=list(map(int,input().split()))
di={}
for i in l:
	if i in di:
		di[i]+=1
	else:
		di[i]=1
c=(n*(n-1))//2
for ke in di:
	if di[ke]>1:
		c-=((di[ke]*(di[ke]-1))//2)
print(c)
