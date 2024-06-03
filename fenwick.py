# POINT UPDATE AND RANGE QUERY ---------

def update(idx,val):
    while idx<=n:
        bit[idx]+=val
        idx=idx+(idx&(-idx))

def query(idx):
    res=0

    # removing last set bit---
    while idx>0:
        res+=(bit[idx])
        idx=idx-(idx&(-idx))
     
    return res 

def fenwick():
    q=int(input("enter no of queries"))

    while q:
        type=int(input('enter 1 for query and 2 for update'))
        if type==1:
            L,R=[int(i) for i in input("enter left and right").split()]
            res=query(R)-query(L-1)
            print(res)
            

        else:
            idx,val=[int(i) for i in input("enter idx and val").split()]
            lst[idx]=val

            #increment index 'idx' by value lst[idx]
            update(idx,lst[idx])
       

n=int(input())
#o index for dummy value
lst=[0,2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
bit=[0]*(n+1)
for i in range(1,n+1):
    update(i,lst[i])
print(bit)

fenwick()



