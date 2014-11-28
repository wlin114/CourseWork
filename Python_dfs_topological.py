graph = {"CS10":["CS20", "CS11"], "CS20":["CS30"], "CS11":["CS21"], "CS21":["CS20","CS12"], "CS12":["CS30"]}
#graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A","E"]}
coming = {"CS20":["CS10", "CS21"], "CS30":["CS20", "CS12"], "CS11":["CS10"],"CS21":["CS11"], "CS12":["CS21"]}
#coming = {"A":["D"], "B":["A"], "C":["B"], "D":["B"], "E":["B","C","D"]}
q = ["CS10"]
#q = ["A"]
visit = [q[0]]

def dfs(head, flag):
    if head in graph:
        for x in graph[head]:
            if head in coming[x]:
                coming[x].remove(head)
                if coming[x] == []:
	                visit.append(x)
	                flag = dfs(x, flag)
            elif flag == True:
                return False
    return flag
if dfs(q[0], True) == True:
    print visit.pop(0),
    for x in visit:
        print "->", x,
    print 
else:
    print "NO TOPOLOGICAL ORDER"
