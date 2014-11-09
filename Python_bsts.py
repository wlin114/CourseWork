cache = {0:1}
def Top_down(n):			#top_down
	if n in cache:
		return cache[n]
	cache[n] = sum(Top_down(i-1) * Top_down(n-i) for i in range(1, n+1))
	return cache[n]

def Bottom_up(n):
	for i in range(1, n+1):
		cache[i] = sum(cache[j-1]*cache[i-j] for j in range(1, i+1))
	return cache[n]

def bsts(n):
	if n < 0:
		print "Error"
	else:
		print Top_down(n)
		print Bottom_up(n)

import sys
sys.setrecursionlimit(10000)

bsts(5)