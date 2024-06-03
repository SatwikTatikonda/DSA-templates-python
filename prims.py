# TC:o(ElogE)
# this algo is used to find th MST
import heapq

graph=[[0,1,10],[0,2,15],[0,3,30],[1,0,10],[1,3,40],[2,0,15],[2,3,50],[3,1,40],[3,2,50]]
v=[0]*5
minH=[[0,0]] #cost,node
finalCost=0
while minH:
    cost,node=heapq.heappop(minH)
    if not v[node]:
        v[node]=1
        finalCost+=cost
        for src,dst,wt in graph:
          if src==node:
           if not v[dst]:
              # adding unvisited nei of node to the minH
              heapq.heappush(minH,[wt,dst])

print(finalCost)
           
