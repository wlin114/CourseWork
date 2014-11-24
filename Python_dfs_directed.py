color = {"A":0,"B":0,"C":0,"D":0,"E":0}
time = {"A":0,"B":0,"C":0,"D":0,"E":0}
graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}
timer = 0

def dfs(head, level):
	color[head] = 1
	global timer
	time[head] = timer;
	timer+=1
	if head not in graph:
		color[head] = 2
		return 
	for x in graph[head]:
		if color[x] == 0:  #grey to white
			print '     '*level, head,"->",x
			dfs(x, level+1)
		elif color[x] == 1: #grey to grey
			print '     '*level, "*", head,"->",x,"(back)"
		elif time[x] < time[head]: #grey to black
			print '     '*level, "*", head,"->",x,"(cross)"
		else:
			print '     '*level, "*", head,"->",x,"(forward)"
	color[head] = 2
	return

dfs("A", 0)