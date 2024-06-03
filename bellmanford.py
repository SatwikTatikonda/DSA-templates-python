

# this algo is used to handle negative weights which is not possible with dijkstras

# this doesnt work for -ve weight cycles

# T.C:o(VE)

# TC of bellman>TC of Dijkstra

# it uses DP where dijkstras uses greeedy


import heapq

graph=[[0,1,2],[0,2,4],[1,2,-4],[2,3,2],[3,4,4],[4,1,-1]]
minH=[[0,0]]
v=5
dist=[0]
for i in range(v-1):
    dist.append(float("inf"))

visit=[0]*v

while minH:
    mindst,node=heapq.heappop(minH)
    if not visit[node]:
     visit[node]=1
     for src,dst,wt in graph:
        if src==node:
           if dist[src]+wt<dist[dst]:
              dist[dst]=dist[src]+wt
              heapq.heappush(minH,[dist[dst],dst])

for i in dist:
   print(i)
              
           



