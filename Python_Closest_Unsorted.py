#!/usr/bin/env python
class node():
	def __init__(self, a, b):
		self.x = a
		self.y = b

def qselect(a, target):
  if len(a) == 1:
    return a[0]
  else:
    pivot = a[0]
    left = [x for x in a if x.y <= pivot.y ]
    if len(left) == target:
      return pivot
    elif len(left) < target:
      right = [x for x in a if x.y > pivot.y]
      return qselect(right, target-(len(left)))
    else:
      left.remove(pivot)
      return qselect(left, target)

def find(list, x, k):
	list1 = []
	for i in list:
		list1.append(node(i, abs(i-x)))
	partition = qselect(list1, k).y
	result = []
	for i in list1:
		if i.y <= partition and len(result) < k:
			result.append(i.x)
	print result		
	

find([4,1,3,2,7,4], 5.2, 2)
find([4,1,3,2,7,4], 6.5, 3)

