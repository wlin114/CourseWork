a = []
n = len(a)
best = [0] * n 
best[1] = max(0, a[1])
back = {}

def bottom_up():
	for i in range(1, n):
		best[i] = max(best[i-1], best[i-2]+a[i])
		back[i] = best[i] == best[i-1]

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

bottom_up()
print best[-1]
print solution(n-1)
best = {0:0, 1: max(0,a[1])}
print top_down(n-1)
print solution(n-1)