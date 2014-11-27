graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}
#graph = {"A": ["B", "C"], "B": ["D"],"C":["E"], "D": ["C"], "E":["A"],  "F":["C"]}
graph = {"A": ["B", "C"], "B":["D"], "C":["E"], "D":["E","F"], "E":[], "F":["C"]}
distance = {"A":0, "B":-1, "C":-1, "D":-1, "E":-1, "F":-1}
q = ["A"]
visit = []
back = []
cross = []

def bfs():
	while q!=[]:
		head = q.pop(0)
		if head in graph:
			for i in graph[head]:
				if distance[i] < 0:
					distance[i] = distance[head] + 1
					q.append(i)
				elif distance[head] > distance[i] + 1:
					back.append((head,"->",i))

bfs() 
print "back: ", back