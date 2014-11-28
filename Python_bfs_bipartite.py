graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}
#graph = {"A": ["B", "C"], "B": ["D"],"C":["E"], "D": ["C"], "E":["A"],  "F":["C"]}
graph = {"A": ["D", "E"], "B": ["D"], "C": ["E"]}
color = {"A":0, "B":0, "C":0, "D":-1, "E":-1, "F":-1}
q = ["A", "B", "C"] #initial q with all starting point (no incoming edge)

def bfs():
	while q!=[]:
		head = q.pop(0)
		if head in graph:
			for i in graph[head]:
				if color[i] < 0:
					color[i] = 1 - color[head] 
					q.append(i)
				elif color[i] == color[head]:
				    print "NOT BIPARTITE"
				    return False
	return True

if bfs() == True:
    left = [x for x in color if color[x] == 0]
    right = [x for x in color if color[x] == 1]
    print "LEFT: ",left,"; RIGHT: ",right,"."
