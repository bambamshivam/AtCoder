def bfs(i,adj,v):
	q=[]
	q.append(i)
	v[i]=1
	while q:
		s=q.pop()
		for k in range(len(adj[s])):
			if v[adj[s][k]]==0:
				q.append(adj[s][k])
				v[adj[s][k]]=1

n=int(input())
l=list(map(int,input().split()))
cc={}
adj={}
for i in range(n//2):
	if l[i]!=l[n-1-i]:
		adj.setdefault(l[i],[])
		adj.setdefault(l[n-1-i],[])
		t=(l[i],l[n-1-i])
		if l[i]>l[n-i-1]:
			t=(l[n-1-i],l[i])
		cc[t]=1
v={}
for ke in cc:
	adj[ke[0]].append(ke[1])
	v[ke[0]]=0
	adj[ke[1]].append(ke[0])
	v[ke[1]]=0
c=0
for ke in v:
	if v[ke]==0:
		bfs(ke,adj,v)
		c+=1

print(len(v)-c)