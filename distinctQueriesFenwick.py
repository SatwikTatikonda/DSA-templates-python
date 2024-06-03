n=int(input())

def update(idx,val):
    while idx<=n:
        print("in update",idx,n)
        bit[idx]+=val 
        idx=idx+(idx&(-idx))

def value(idx):
    res=0
    while idx>0:
        print("in value")
        res+=bit[idx]
        idx=idx-(idx&(-idx))
    
    return res


bit=[0]*(n+1)
# arr=[0]*(n+1)
# for i in range(1,n+1):
#     arr[i]=int(input("enter input array"))
arr=[0,1,1,2,1,3]

# q=int(input("enter q"))
q=3
# queries=[]
queries=[[1,5,1],[2,4,2],[3,5,3]]
ans=[0]*(q+1)

# for i in range(q):
#     start,end=[int(i) for i in input("enter start and end").split()]
#     queries.append([start,end,i])

queries.sort(key=lambda x:x[1])

print("q ",queries)

total=0
k=0
vis=[-1]*(10**6)

for s,e,idx in queries:
    
    print(s,e,idx)
    if vis[arr[idx]]!=-1:
        update(vis[arr[idx]],-1)
    else:
        total+=1 
    update(idx,1)
    vis[arr[idx]]=idx

    while k<q and queries[k][1]==idx:
       print('in while')
       ans[queries[k][2]]=total-value(queries[k][0]-1)
       k+=1


print('out')

for i in range(1,q):
    print(ans[i])






