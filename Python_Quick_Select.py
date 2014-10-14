#!/usr/local/bin/python2.7
import random

def _qselect(target, a):
  if len(a) == 1:
    return a[0]
  else:
    pivot = a[random.randint(0,len(a)-1)]
    left = [x for x in a if x <= pivot ]
    if len(left) == target:
      return pivot
    elif len(left) < target:
      right = [x for x in a if x > pivot]
      return _qselect(target-(len(left)), right)
    else:
      left.remove(pivot)
      return _qselect(target, left)

def qselect(target, a):
  if a == []:
    return "empty list"
  print _qselect(target, a)