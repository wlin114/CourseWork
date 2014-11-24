color = {"A":0,"B":0,"C":0,"D":0,"E":0}
graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}
q = ["A"]
visit = ""
back = []
cross = []

def bfs():
	while q!=[]:
		global visit
		head = q.pop(0)
		if head not in graph and color[head]!=2:
			visit = visit + " " + head
			color[head] = 2
		elif color[head] == 0:
			visit = visit + " " + head
			color[head] = 1
			q.extend(graph[head])
		elif color[head] == 1:
			back.append(head)
		elif color[head] == 2:
			cross.append(head)


bfs()
print visit,  back, 