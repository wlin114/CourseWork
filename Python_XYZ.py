#!/usr/bin/env python
import time
def xyz(list):
  list.sort()
  lens = len(list)
  count = 0
  for i in range(lens-1):
    for j in range(lens-1):
      if i != j:
        offset = max(i,j)
        for k in range(lens-offset):
          if list[i] + list[j] == list[k+offset]:
 #           print (list[i], list[j], list[k+offset])
            count += 1
  print "Total: ",count

def xyz_HT(list):
  dict = {}
  for x in list:
    dict[x] = True
  lens = len(dict)
  count = 0
  for i in range(lens-1):
    for j in range(lens-1):
      if i!=j:
        if dict.get(list[i] + list[j]):
  #        print (list[i], list[j], list[i]+list[j])
          count +=1
  print "Total: ", count
  
a=[]
for i in range(100):
  a.append(i)
xyz_HT(a)
#xyz(a)