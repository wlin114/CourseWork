#!/usr/bin/env python
from math import ceil
def merge(ls, k):
  for i in range(len(ls)):
      ls[i] = _kmergesort(ls[i], k)
      if len(ls[i]) == 2 and ls[i][0] > ls[i][1]:
        ls[i][0], ls[i][1] = ls[i][1], ls[i][0]
  result = []
  while True:
    min_val = float('inf')
    index = []
    for x in ls:
      if x != [] and min_val > x[0]:
        min_val = x[0]
        index = x
    if index == []:
      break
    ls[ls.index(index)].remove(min_val)
    result.append(min_val)
  return result
  
def _kmergesort(ls, k):
  if len(ls) < k:
    return ls
  l = int(ceil(len(ls)/float(k)))
  split = [ls[i:i+l] for i in range(0, len(ls), l)]
  return merge(split, k)

def kmergesort(ls, k):
  if k<2 or k>len(ls):
    print "invalid k value"
  else:
    print _kmergesort(ls, k)

kmergesort([4,1,5,2,6,3,7,0],3)
