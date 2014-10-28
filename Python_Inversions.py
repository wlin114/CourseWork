#!/usr/local/bin/python2.7
num = 0
def merge_sort(ls):
  if len(ls) <= 1:
    return ls
  left = ls[:int(len(ls)/2)]
  right = ls[int(len(ls)/2):]
  
  return merge(left, right)

def merge(left, right):
  global num
  left = merge_sort(left)
  right = merge_sort(right)
  
  for x in right:
    j = len(left)+1
    for y in left:
      j-=1
      if x<y:
        num+=j
	break
  result = []
  while left !=[] or right !=[]:
      
    if left == []:
      result += right
      break
    elif right == []:
      result += left
      break
    elif left[0] < right[0]:
      result.append(left[0])
      left = left[1:]
    else:
      result.append(right[0])
      right = right[1:]
  return result

def inversions(list):
  merge_sort(list)
  print num

inversions([5,3,1,4,2,0])
