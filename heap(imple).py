#  insert:we insert new element at back of array and then start comapring with its parent 
#  we swap the new value with the parent if parent >new val 
# this takes place till new element is placed at suitabe position

# ------------------------------------

# extractmin: we remove the root  and the heapify to reconstruct the heap again

# ------------------------------------

#  heapify:this stores and index(idx) in the 'small' varaible and comparess the value in the index with value in the left and right child

# if any of these values are smaller than value at idex stored in 'small' variable then index  of the new smaller value will be stored in the 'small' varaible
#  so that at last 'small' consists index of small value

#  swap the value at idx with value at 'small' if they are not same 

#  repeat this recursively till the smallest element is brought back to root

# ------------------------------------

#  dlte key: we make the key value to lowest poassible and perfoem heapify
#  after heapify the lowest value will be at root
#  so that exrtractMin will remove the value at root


class Heap:
    def __init__(self,cap):
        self.capacity=cap
        self.heapArr=[]
        self.size=0
    
    def ls(self,harr,k):
        for i in harr:
            if i==k:
                print("val found")
                return 
        print("val not found")
        return 

    def console(self):
        for i in range(len(self.heapArr)):
            print(self.heapArr[i],end=" ")
        print("")

    def parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return (2*i)+1

    def right(self,i):
        return (2*i)+2

    def height(self):
        return 

    def insert(self,value):

        if len(self.heapArr)==self.capacity:
            print("overflow")
            return
        else:
            self.heapArr.append(value)
            i=len(self.heapArr)-1
            while i :
                if self.heapArr[self.parent(i)]>self.heapArr[i]:
                    self.heapArr[self.parent(i)],self.heapArr[i]=self.heapArr[i],self.heapArr[self.parent(i)]
                    i=(i-1)//2
                else:
                    break                    
            print(self.heapArr)

    def heapify(self,idx):
        
   
        while (2*idx)+1<len(self.heapArr): 
            l=self.left(idx)
            r=self.right(idx)
            smallest=min(self.heapArr[idx],self.heapArr[l],(self.heapArr[r] if r<len(self.heapArr) else float('inf')))

            if smallest==self.heapArr[idx]:
                break

            elif smallest==self.heapArr[l]:
                self.heapArr[idx],self.heapArr[l]= self.heapArr[l],self.heapArr[idx]
                idx=l

            elif smallest==self.heapArr[r]:
                self.heapArr[idx],self.heapArr[r]= self.heapArr[r],self.heapArr[idx]
                idx=r

          
    def dlteMin(self):
        
        if len(self.heapArr)<=0:
            print("heap empty")
            return 

        self.heapArr[-1],self.heapArr[0]=self.heapArr[0],self.heapArr[-1]
        val=self.heapArr.pop()
        self.heapify(0)
        print(val," deleted")
      
    

 
    
    def extractMin(self):
       return self.heapArr[0]



    
hp=Heap(4)
hp.insert(5)
hp.insert(7)
hp.insert(4)
hp.insert(3)
hp.console()
hp.dlteMin()
print(hp.extractMin())
hp.dlteMin()
print(hp.extractMin())
print("-------------")
hp.console()

