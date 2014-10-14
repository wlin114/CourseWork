#!/usr/local/bin/python2.7
# A* with manhattan
goal = [1,2,3,8,0,4,7,6,5]
moveList = [[1,3],[0,2,4],[1,5],[0,4,6],[1,5,7,3],[2,4,8],[3,7],[4,6,8],[5,7]]
class puzzle:                     #puzzle object class
  def __init__(self, caseList):   #contains node
    self.node = caseList          #and getHtion value
    self.g = 0
    self.h = self.getH()
    self.pre = None
  def getF(self):                 #get getHtion for f value
    return self.g + self.getH()
  def getH(self):                 #get getHtion for h value
    counter = 0
    for x in range(9):
      if goal[x] != self.node[x]:
        counter += abs(self.node.index(x)%3 - goal.index(x)%3) + abs(self.node.index(x)/3 -goal.index(x)/3)
    return counter
  def __str__(self):              #print
    print self.node[0:3]
    print self.node[3:6]
    print self.node[6:9]
    return " "

def move(node, a, b):             #move function, check if direction is ok and then move,
  newN = puzzle(node.node[::])    #node is the puzzle board, a is empty tile, b is the tile to be swap with
  newN.pre = node
  if b in moveList[a]:
    newN.node[a],newN.node[b] = newN.node[b], newN.node[a]
    newN.g = node.g + 1
    newN.h = newN.getH();
    return newN
  return None
  
def neighbor(node):                 #generate all the dirction and call move() function
  l = []
  index = node.node.index(0)
  temp = move(node, index, index-3)
  if temp != None:
    l.append(temp)
  temp = move(node, index, index+1)
  if temp != None:
    l.append(temp)
  temp = move(node, index, index+3)
  if temp != None:
    l.append(temp)
  temp = move(node, index, index-1)
  if temp != None:
    l.append(temp)
  return l

def search(a, l):                   #search function, see if the pattern of a is exist in list l
  for x in range(len(l)):
    if a.node == l[x].node:
      return x
  return -1  

def aStar(case):                  #main
  openL = [case]
  closeL = []
  count = 1
  while True:
    openL.sort(key=lambda x: x.getF(), reverse=False)    
    best = openL[0]
    if best.node == goal:
      print str(best.g) + " steps"
#      print best
#      while best.pre != None:
#        print best.pre
#        best = best.pre
      print "total expanded: ", count
      print case
      break
    closeL.append(openL.pop(0))
    nL = neighbor(best)
    count += len(nL)
    for x in nL:
      cIndex = search(x, closeL)
      oIndex = search(x, openL)
      if cIndex !=-1 and closeL[cIndex].g-1>best.g:
        openL.append(closeL.pop(cIndex))
        closeL[cIndex].g = best.g+1
        closeL[cIndex].pre = best
      elif oIndex !=-1 and openL[oIndex].g-1>best.g:
        openL[oIndex].g = best.g+1
        openL[oIndex].pre = best
      elif cIndex == -1 and oIndex == -1:
        openL.append(x)

easy = puzzle([1,3,4,8,6,2,7,0,5])
medium = puzzle([2,8,1,0,4,3,7,6,5])
hard = puzzle([2,8,1,4,6,3,0,7,5])
worst = puzzle([5,6,7,4,0,8,3,2,1])
#aStar(easy)
#aStar(medium)
#aStar(hard)
aStar(worst)