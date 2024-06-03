# find min of given range in query after every update made
 
# POINT UPDATE AND RANGE QUERY ---------

lst=[10,2,7,-3,5,8,1,15]
n=len(lst)
segment=[0]*(4*n)

def build(idx,l,r):

    if l==r:
        segment[idx]=lst[l]
        return

    m=(l+r)//2

    build(2*(idx)+1,l,m)
    build(2*idx+2,m+1,r)

    segment[idx]=min(segment[2*idx+1],segment[2*idx+2])

# query - to find min from range l-r 
# current node range x-y 
def query(idx,x,y,l,r):

    if x>=l and y<=r:
        return segment[idx]

    if x>r or y<l:
        return float('inf')

    m=(x+y)//2
    res=min(query(2*idx+1,x,m,l,r),query(2*idx+2,m+1,y,l,r))

    return res

# upadte the value at index 'i' with 'val' value
# current node range x-y 
def update(idx,x,y,i,val):

    if x==y:
        segment[idx]=val
        lst[i]=val
        return

    m=(x+y)//2

    if i<=m:

        update(2*idx+1,x,m,i,val)
    
    else:

        update(2*idx+2,m+1,y,i,val)
    
    segment[idx]=min(segment[2*idx+1],segment[2*idx+2])


build(0,0,len(lst)-1)
update(0,0,len(lst)-1,2,-7)
print(query(0,0,len(lst)-1,1,4))



