#!/usr/local/bin/python2.7
def sort(a):
  if a == []:
    return []
  else:
    pivot = a[0]
    left = [x for x in a if x < pivot ]
    right = [x for x in a[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]

def sorted(t):
  result = []
  inFix(t, result)
  print result

def inFix(t,result):
  if t == []:
    return
  left, root, right = t
  inFix(left, result)
  result.append(root)
  inFix(right, result)

def _search(tree, target):
  if tree == []:
    return tree
  left, root, right = tree
  if root == target:
    return tree
  elif root > target:
    return _search(left, target)
  return _search(right, target)

def search(tree, target):
  print _search(tree, target) != []

def insert(tree, target):
  where = _search(tree, target)
  if where == []:
    where.append([])
    where.append(target)
    where.append([])

def leaf(tree):
  for x in range(len(tree)):
      tree.pop()

def twoChild(tree):
  left = tree[0]
  while len(left[2]) > 1:
    left = left[2]
  tree[1] = left[1]
  leaf(left)

def delete(tree, target):
  where = _search(tree, target)
  if where == []:
    return
  left, root, right = where
  if left == [] and right == []:
    leaf(where)
  elif left == [] and right != []:
    for x in range(len(where)):
      where.pop()
    for x in right:
      where.append(x)
  elif left != [] and right == []:
    for x in range(len(where)):
      where.pop()
    for x in left:
      where.append(x)
  else: twoChild(where)
    

tree = sort([4,2,6,3,5,7,1,9])
"""
sorted(tree)
search(tree, 6)
search(tree, 6.5)
insert(tree, 3)
print tree
insert(tree, 6.5)
print tree
delete(tree, 4)
print tree
print [[[[], 1, []], 2, []], 3, [[[], 5, []], 6, [[[], 6.5, []], 7, [[], 9, []]]]]
"""