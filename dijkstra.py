# APNA COLLEGE IMPLEMENTATION------

# TC:O(E+ElogV)
# this aglo is used for calculating  the minimum distance from  source node(0) to all destination nodes in a weighted graph

from collections import defaultdict
import heapq


graph=[[0,1,2],[0,2,4],[1,3,7],[1,2,1],[2,4,3],[3,5,1],[4,3,2],[4,5,5]]
v=5
minH=[[0,0]] #[dst,node]
dist=[0]
for i in range(5):
    dist.append(float("inf"))
visit=[0]*6

while minH:
    # retrieving the neighbour with minimum distance 
    mindst,node=heapq.heappop(minH)

    # checking if the neighbour is visited or not previous
    if (not visit[node]):
        
        visit[node]=1
        for src,dst,wt in graph:
          if src==node:

            # we are comparing distance between zero to destination  node and distance between zero to the intermediate node + distance between intermediate node to the destination node


            # dist[src]-->dist from 0 to src
            #   wt-->dist from src to dst
            # dist[dst]-->dist from 0 to  dst
            if dist[src]+wt<dist[dst]:            
                dist[dst]=dist[src]+wt
                # print(dst,dist[dst])
                heapq.heappush(minH,[dist[dst],dst])
        
     
for i in dist:
    print(i)           

            
        




    


