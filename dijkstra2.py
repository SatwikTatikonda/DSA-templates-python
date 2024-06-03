# Better approach----------

from collections import defaultdict
import heapq


graph=[[0,1,2],[0,2,4],[1,3,7],[1,2,1],[2,4,3],[3,5,1],[4,3,2],[4,5,5]]

dic=defaultdict(list)
for src,dst,wt in graph:
    dic[src].append([dst,wt])
print(dic)
n=len(dic)
minH=[[0,0]] #[DST,NODE]
dist=[0]+[float("inf")]*(n)
v=[0]*(n+1)
while minH:
    print(minH)
    mindst,node=heapq.heappop(minH)

    if not v[node]:
        v[node]=1
        for dst,wt in dic[node]:
            if dist[node]+wt<dist[dst]:
                dist[dst]=wt+dist[node]
            heapq.heappush(minH,[dist[dst],dst])

for i in dist:
    print(i)



   

