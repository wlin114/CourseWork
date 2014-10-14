def find(list, x, k):
	result = []
	left = [a for a in list if a < x]
	right = [b for b in list if b > x]
	for i in range(k):
		if left != [] and right != []:
			if abs(left[-1] - x) <= right[0] - x:
				result.append(left.pop(-1))
			else:
				result.append(right.pop(0))
		elif left == []:
			result.append(right.pop(0))
		elif right == []:
			result.append(left[-1])
	print result

find([1,2,3,4,4,7], 5.2, 2)
find([1,2,3,4,4,7], 6.5, 3)