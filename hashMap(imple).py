# usually in java bucket is array of linkedlists of nodes
# but in java it is list of list of nodes

class Hashmap:
     
    class HmNode:
        def  __init__(self,k,v):
            self.key=k
            self.val=v

    def __init__(self,n) -> None:
        self.n=n
        self.size=0
        self.bucket=[[] for _ in range(self.n)] #[[(k1,v1),(k2,v2)],[(k3,v3),(k4,v5),(k6,v6)]..........] 

    def put(self,k,v):

        btNo=self.hashFunc(k)
        fdt=self.foundAt(btNo,k)
        if fdt==-1:
            h=self.HmNode(k,v)
            self.bucket[btNo].append((h))
        else:
            node=self.bucket[btNo][fdt]
            node.val=v

        self.size+=1
    
        thresoldLambda=(self.size/len(self.bucket))
        if thresoldLambda>2:
            self.rehash()
    
    def rehash(self):
        oldbucket=self.bucket.copy()
        self.bucket=[[0] for _ in range(2*len(oldbucket))]
        self.size=0
        for i in range(len(oldbucket)):

            for j in range(len(self.bucket)):

                node=oldbucket[i][j]
                self.put(node.key,node.val)
    
    def get(self,k):
        btNo=self.hashFunc(k)
        fdt=self.foundAt(btNo,k)
        if fdt==-1:
            return -1
        else:
            node=self.bucket[btNo][fdt]
            return node.val
    
    def remove(self,k):
        btNo=self.hashFunc(k)
        fdt=self.foundAt(btNo,k)

        if fdt==-1:
            return -1

        else:
            self.size-=1
            node=self.bucket[btNo].pop(fdt)
            return node.val
    
    def containsKey(self,k):
        btNo=self.hashFunc(k)
        fdt=self.foundAt(btNo,k)

        if fdt==-1:
            return 0
        else:
            return 1
    

    def display(self):
        print(self.bucket)
        for i in range(len(self.bucket)):

            for node in self.bucket[i]:

                print(node.key," --> ",node.val)
    
    def hashFunc(self,k):
        idx=(abs(hash(k)))%len(self.bucket)
        return idx

    def foundAt(self,btNo,k):

        if k in self.bucket[btNo]:  
            return self.bucket[btNo].index(k)
        else:
            return -1




hm=Hashmap()
hm.put(5,1)
hm.put(15,2)
hm.put(52,3)
hm.put(23,5)
hm.display()

    


            
        




    