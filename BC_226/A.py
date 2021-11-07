import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
x=input()
l=list(x.split('.'))

if int(l[1])/1000>=0.5:
	print(int(l[0])+1)
else:
	print(int(l[0]))