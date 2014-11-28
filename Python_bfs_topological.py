graph = {"CS10":["CS20", "CS11"], "CS20":["CS30"], "CS11":["CS21"], "CS21":["CS20","CS12"], "CS12":["CS30"]}
graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A","E"]}
coming = {"CS20":["CS10", "CS21"], "CS30":["CS20", "CS12"], "CS11":["CS10"], "CS21":["CS11"], "CS12":["CS21"]}
coming = {"A":["D"], "B":["A"], "C":["B"], "D":["B"], "E":["B","C","D"]}
q = ["CS10"]
q = ["A"]
def bfs(ans):
	while q!=[]:
		head = q.pop(0)
		if head in graph:
			for i in graph[head]:
			    if head not in coming[i]:
			        return "NO TOPOLOGICAL ORDER"
			    coming[i].remove(head)
			    if coming[i] == []:
			        ans += " -> "+i
			        q.append(i)
	return ans
    
print bfs(q[0])
