def bottom_up():
	for i in range(1, n):
		best[i] = max(best[i-1], best[i-2]+a[i])
		back[i] = best[i] == best[i-1]
	return best[-1]

def top_down(i):
	if i in best:
		return best[i]
	best[i] = max(top_down(i-1), top_down(i-2)+a[i])
	back[i] = best[i] == best[i-1]
	return best[i]

def solution(i):
	if i <= 0:
		return []
	if i==1:
		return [a[i]] if a[1] > 0 else []
	if back[i]:
		return solution(i-1)
	return solution(i-2) + [a[i]]

def max_wiz(list):
	if list == []:
		print (0, [])
	else:
		global a, n, best, back
		a = [0] + list
		n = len(a)
		best = [0] * n
		best[1] = max(0, a[1])
		back = {}

		result = bottom_up()
		path = solution(n-1)
		print "Bottom up:"
		print (result, path)

		best = {0:0, 1: max(0,a[1])}

		result = top_down(n-1)
		path = solution(n-1)
		print "Top down:"
		print (result, path)

max_wiz([])