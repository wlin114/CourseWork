def find(t, tar):
	if t == []:
		return float('inf')
	if len(t) == 1:
		return abs(t[0] - tar)
	node, left, right = t
	if node < tar:
		return min(tar-node, find(right,tar))
	elif node > tar:
		return min(abs(tar-node), find(left, tar))
	return 0

t= [5, [3,[2,[1],[]],[4]], [7,[6],[8]]]
print find(t, 6.7) 