# it is used for DAG(directed acyclic graphs)
# it is a linear order of vertices such that every vertice such that every directed edge u-->v, the vertex u comes before v in the order

# there are multiple topolocial sortings

# nodes with no neighbours are added first to the stack and  then when it comes to the nodes with neighbours(all its neighbours are added then later the node itself  is added)

# eg in topology.png

# TE:o(V+E)

from collections import defaultdict
v=set()
graph=[[5,0],[5,2],[2,3],[4,0],[4,1],[3,1]]
s=[]
dic=defaultdict(list)
for src,dst in graph:
    dic[src].append(dst)
def topology(node):

    if node in v:
        return 
    v.add(node)
    for nei in dic[node]:
         
         topology(nei)

         
    s.append(node)

for i in range(6):
 if i not in v:
    topology(i)

while s:
    print(s.pop())
