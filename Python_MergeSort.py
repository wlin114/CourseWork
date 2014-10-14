#!/usr/local/bin/python2.7
def merge_sort(ls):
  if len(ls) <= 1:
    return ls
  left = ls[:int(len(ls)/2)]
  right = ls[int(len(ls)/2):]
  
  return merge(left, right)

def merge(left, right):
  left = merge_sort(left)
  right = merge_sort(right)
  
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
print merge_sort([3,1,4,1,5,9,2,6,5,3]);