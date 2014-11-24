from math import pow

top_Down_cache = {0:0, 1:2, 2:3}
bottom_Up_cache = {0:0, 1:2, 2:3}

def Top_down(n):
	if n in top_Down_cache:
		return top_Down_cache[n]
	top_Down_cache[n] = Top_down(n-1) + Top_down(n-2) 
	return top_Down_cache[n]
def Bottom_up(n):
	if n < 3:
		return bottom_Up_cache[n]
	for i in range(3, n+1):
		bottom_Up_cache[i] = bottom_Up_cache[i-1] + bottom_Up_cache[i-2]
	return bottom_Up_cache[n]
def num_no(n):
	if n not in top_Down_cache:
		Top_down(n)
	if n not in bottom_Up_cache:
		Bottom_up(n)
	return top_Down_cache[n], bottom_Up_cache[n]
def num_yes(n):
	if n == 0:
		return 0
	if n not in top_Down_cache:
		Top_down(n)
	if n not in bottom_Up_cache:
		Bottom_up(n)
	return int(pow(2, n)) - top_Down_cache[n], int(pow(2, n)) - bottom_Up_cache[n]

print num_yes(7)
print num_no(7)