color = {"A":0,"B":0,"C":0,"D":0,"E":0}
graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}
flag = True

def dfs(head, c):
	global flag
	color[head] = c  
	if head not in graph:
		return
	for x in graph[head]:
		if color[x] == 0:  #Tree edge
			dfs(x, 3-c)
		elif color[head] == c: #Visited!
			flag = False
			return
	return

dfs("A", 1)
if flag == True:
	print "LEFT: ", [x for x in color if color[x] == 1], "; ",
	print "RIGHT: ", [y for y in color if color[y] == 2]
else:
	print "NOT BIPARTITE"