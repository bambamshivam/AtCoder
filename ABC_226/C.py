import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
sys.setrecursionlimit(10000000)
n=I();l=[]
for i in range(n):
	l.append(L())
def solve(i,d):
	for j in range(2,len(l[i])):
		if l[i][j]-1 not in d:
			d[l[i][j]-1]=1
			solve(l[i][j]-1,d)
d={};d[n-1]=1;solve(n-1,d);c=0
for ke in d:
	c+=l[ke][0]
print(c)