import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n=I();l=[]
for i in range(n):
	a,b=M()
	l.append([a,b])
s=set()
for i in range(n):
	for j in range(n):
		if j!=i:
			dx=l[i][0]-l[j][0]
			dy=l[i][1]-l[j][1]
			g=math.gcd(abs(dx),abs(dy))
			s.add((dx//g,dy//g))
print(len(s))