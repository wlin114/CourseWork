#!/usr/bin/env python
from __future__ import division
import heapq
def medians(list):
	result = [list[0], (list[0]+list[1])/2]
	if list[0] > list[1]:
		maxh = [-list[1]]
		minh = [list[0]]
	else:
		maxh = [-list[0]]
		minh = [list[1]]
		
	for i in list[2:]:
		if i >= abs(maxh[0]):
			heapq.heappush(minh, i)
		else:
			heapq.heappush(maxh, -i)
		if len(maxh) - len(minh) >= 2:
			heapq.heappush(minh, abs(heapq.heappop(maxh)))
		if len(minh) - len(maxh) >= 2:
			heapq.heappush(maxh, -(heapq.heappop(minh)))
		result += [(minh[0] + abs(maxh[0]))/2]
	print result
a = [5,3,4,1,6]
medians(a)