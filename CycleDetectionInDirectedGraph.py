# we are traversing through graph when ever we encounter a true ,we stop there start returning the true to its parent function

# we return true if we encounter a node thaat is already in recursivestack


from collections import defaultdict
# graph=[[0,2],[1,0],[2,3]]
# graph=[[0,1],[0,3],[1,2],[2,4],[3,0]]
graph=[[0,1],[2,1],[2,3],[3,4],[4,2]]

dic=defaultdict(list)
for src,dst in graph:
    dic[src].append(dst)
v=[0]*5
recstk=[0]*5
def chk(node):
    recstk[node]=1
    v[node]=1
    for nei in dic[node]:

        if recstk[nei]:
            return 1
        elif not v[nei]:
         if chk(nei):
            return 1
    recstk[node]=0
    return 0
for i in range(5):
#    there may be some graphs which are unconnected components in that case we have cycle in any other component 
#    we return true if no component contains cycle 
#    and false if any one component has cycle
   if not v[i]:
      if not chk(i):
         print("exits")
         break
print("no cylce exists")


