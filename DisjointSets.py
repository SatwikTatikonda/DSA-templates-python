# source:take you forward
# tc:o(4alpha)

class Disjointset:

    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.size=[1]*(n+1)
        self.parent=[i for i in  range(n+1)]
        
    # path compression
    def findUltimateParent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self,u,v):
        pu=self.findUltimateParent(u)
        pv=self.findUltimateParent(v)
        
        if pu==pv:
            return 
        if self.size[pu]<self.size[pv]:
                self.parent[pu]=pv
                self.size[pu]+=self.size[pv]
        
        else:
                self.parent[pv]=pu  
                self.size[pv]+=self.size[pu]   
       


    def unionByRank(self,u,v):
        pu=self.findUltimateParent(u)
        pv=self.findUltimateParent(v)  
        if pu==pv:
             return 
        if self.rank[pu]<self.rank[pv]:
             self.parent[pu]=pv
        elif self.rank[pu]>self.rank[pv]:
             self.parent[pv]=pu
        else:
             self.parent[pv]=pu
             self.rank[pv]+=1

        
ds=Disjointset(7)
ds.unionBySize(1,2)
ds.unionBySize(2,3)
ds.unionBySize(4,5)
ds.unionBySize(6,7)
ds.unionBySize(5,6)

if (ds.findUltimateParent(3)==ds.findUltimateParent(7)):
     print("Same")
else:
     print("Not Same")

ds.unionBySize(3,7)

if (ds.findUltimateParent(3)==ds.findUltimateParent(7)):
     print("Same")
else:
     print("Not Same")

         