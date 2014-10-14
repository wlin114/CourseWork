#!/usr/bin/env python
from random import randrange
import heapq

def nbest_1(a, b):
	c = [(x,y) for x in a for y in b]
	c.sort(key=lambda x: (x[0] + x[1] , x[1]))
	print c[:len(a)]

def _nbest_2(c, l):
	if l <= 0:
		return []
	if c == []:
		return c
	p = c[randrange(len(c))]
	c.remove(p)
	c.insert(0,p)
	left = [x for x in c[1:] if x[0]+x[1] < p[0]+p[1] or (x[0]+x[1] == p[0]+p[1] and x[1]<p[1])]
	right = [x for x in c[1:] if x[0]+x[1] > p[0]+p[1] or (x[0]+x[1] == p[0]+p[1] and x[1]>=p[1])]
	if l == len(left):
		return _nbest_2(left, l)
	elif l == len(left) + 1 :
		return _nbest_2(left, l) + [p]
	elif l > len(left) + 1:
		return _nbest_2(left, l) + [p] + _nbest_2(right, l-len(left)-1)
	return _nbest_2(left, l)
def nbest_2(a, b):
	c = [(x,y) for x in a for y in b]
	d = _nbest_2(c, len(a))
	print d

def nbest_3(a,b):
	a.sort()
	b.sort()
	l = len(a)
	result = []
	dict = {}
	list = [( (a[0]+b[0])*10 + b[0], 0, 0)]
	while True:
		if len(result) == l:
			 break
		best = heapq.heappop(list)
		x = best[1]
		y = best[2]
		result.append((a[x],b[y]))
		if x < l-1:
			right = ((a[x+1] + b[y]) * 10 + b[y], x+1, y)
			if right not in dict:
				heapq.heappush(list, ( ( a[x+1] + b[y] ) * 10 + b[y], x+1, y))
				dict[right] = ((a[x+1], b[y]))
		if y < l-1:
			down = ((a[x] + b[y+1]) * 10 + b[y+1], x, y+1)
			if down not in dict:
				heapq.heappush(list, ( ( a[x] + b[y+1] ) * 10 + b[y+1], x, y+1))
				dict[down] = ((a[x], b[y+1]))
	print result


a, b = [4,1,5,3],[2,6,3,4]
c, d = [3,3,3,3],[3,3,3,3]
e,f = [],[]
for i in range(5000):
	e.append(randrange(10000))
	f.append(randrange(10000))
"""
nbest_1(a,b)
nbest_1(c,d)
nbest_2(a,b)
nbest_2(c,d)
nbest_3(a,b)
nbest_3(c,d)
"""
#nbest_1(e,f)
#nbest_2(e,f)
#nbest_3(e,f)