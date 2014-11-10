best = {}
def top_down(n,k):
	if (n, k) in best:
		return best[n,k]
	if k == 1:
		return n
	if n == 1:
		return 1
	if n == 0:
		return 0
	best[n,k] = float("inf")
	for i in range(1, n+1):
		s = max(top_down(n-i, k), top_down(i-1, k-1)) + 1
		if s < best[n,k]:
			best[n,k] = s
	return best[n, k]
def bottom_up(n,k):
	return
def drop(n,k):
	print top_down(n,k)
	#print bottom_up(n,k)

drop(100,4)