color = {"A":0,"B":0,"C":0,"D":0,"E":0}
graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}
q = [("","A")]
visit = ""
back = []
cross = []

def bfs():
	while q!=[]:
		global visit
		head = q.pop(0)
		if head[1] not in graph and color[head[1]]!=2:
			visit = visit + head[1] + " "
			color[head[1]] = 2
		elif color[head[1]] == 0:
			visit = visit + head[1] + " "
			color[head[1]] = 1
			for i in graph[head[1]]:
				q.append((head[1], i))
		elif color[head[1]] == 1:
			back.append(head)
		elif color[head[1]] == 2:
			cross.append(head[1])


bfs()
print visit,  back