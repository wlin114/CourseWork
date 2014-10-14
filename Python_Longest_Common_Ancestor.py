#!/usr/bin/env python
def _solutionA(tree, x):
	if tree == []:
		return False, []
	left, node, right = tree
	found, path = _solutionA(left, x)
	if found == True:
		path.append(node)
		return True, path
	if x == node:
		return True, [x]
	found, path = _solutionA(right, x)
	if found == True:
		path.append(node)
		return True, path
	return found, path 

def solutionA(tree, x, y):
	a = _solutionA(tree, x)[1]
	b = _solutionA(tree, y)[1]
	LCA = None
	al = len(a)
	bl = len(b)
	for x in range(max(al, bl) - abs(al-bl)):
		if a[-1] != b[-1]:
			return LCA, len(a) + len(b)
		else:
			LCA = a[-1]
			a, b = a[:-1], b[:-1]
	return LCA, len(a) + len(b)

def _solutionB(tree, x, y):
	if tree == []:
		return 	False, False, 0, 0

	left, node, right = tree
	l1, l2, pl, nl = _solutionB(left, x, y)
	r1, r2, pr, nr = _solutionB(right, x, y)
	if (l1 and r2) or (l2 and r1):
		return True, True, node, nl + nr
	elif l1 and l2:
		return l1, l2, pl, nl
	elif r1 and r2:
		return r1, r2, pr, nr

	if x == node and (r2 or l2):
		return True, True, node, max(nr, nl)
	elif y == node and (r1 or l1):
		return True, True, node, max(nr, nl)
	elif x == node and not r2 and not l2:
		return True, False, None, 1
	elif y == node and not l1 and not r1:
		return False, True, None, 1

	if (l1 and not l2) or (l2 and not l1):
		return l1, l2, None, nl+1
	elif (r1 and not r2) or (r2 and not r1):
		return r1, r2, None, nr+1

	return False, False, 0, 0

def solutionB(tree, x, y):
	a, b, lca, length = _solutionB(tree, x, y)
	if a and b:
		return lca, length
	return "No Found"
tree = [[[], 1, [[[], 3, []], 4, []]], 5, [[[],5.5,[]], 6, [[],7,[]]]]
print solutionA(tree, 7, 5.5)
print solutionB(tree, 7, 5.5)