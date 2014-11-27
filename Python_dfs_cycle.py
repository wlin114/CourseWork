color = {"A":0,"B":0,"C":0,"D":0,"E":0}
graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}
flag = False

def dfs(head, stack):
	global flag
	color[head] = 1
	if head not in graph:
		color[head] = 2
		return flag
	for x in graph[head]:
		if color[x] == 0:  #Tree edge
			stack+=x
			dfs(x, stack)
			stack = stack[:-1]
		elif color[x] == 1: #Back edge: cycle detected!
			flag = True
			print "cycle detected: ",
			for x in stack:
				print x,"->",
			print stack[0]
			break
	return flag

if dfs("A", "A") != True:
	print "ACYCLIC"