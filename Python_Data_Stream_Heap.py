#!/usr/bin/env python
import sys
from math import floor, log
class myHeap():
	def __init__(self):
		self.list = []
	def push(self, x):
		i = len(self.list)
		self.list += [x]
		while True:
			if i == 0:
				break
			if self.list[int(floor((i-1)/2.0))] >= x:
				break
			parent = int(floor((i-1)/2.0))
			self.list[parent], self.list[int(i)] = self.list[int(i)], self.list[parent]
			i = floor((i-1)/2.0)
	def pop(self):
		tbp = self.list[0]
		x = self.list.pop(-1)
		self.list[0] = x
		i = 0
		l = len(self.list)
		while True:
			if log(i+1,2) == log(l,2) or l <= 2*i + 2:
				self.list[-1], self.list[i] = self.list[i], self.list[-1]
				break
			elif self.list[2*i + 1] > self.list[2*i + 2]:				
				self.list[2*i + 1], self.list[i] = self.list[i], self.list[2*i +1]
				i = 2*i+1
			else:
				self.list[2*i + 2], self.list[i] = self.list[i], self.list[2*i +2]
				i = 2*i+2
		return tbp
k = None
a = myHeap()
for line in sys.stdin:
	if k == None:
		k = int(line)
	if len(a.list) < k:
		a.push(int(line))
	elif a.list[0] > int(line):
		a.pop()
		a.push(int(line))
a.list.sort()
for i in a.list:
	print i,
