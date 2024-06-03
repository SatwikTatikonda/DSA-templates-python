# find sum of given range in query after every range update made
 
# RANGE UPDATE AND RANGE QUERY ---------

lst=[10,2,7,-3,5,8,1,15]
n=len(lst)
segment=[0]*(4*n)
isLazy=[0]*(4*n)
unPropUpd=[0]*(4*n)


def apply(idx,l,r,val):

    if l!=r:
        isLazy[idx]=False
        unPropUpd[idx]=val 
    segment[idx]=(r-l+1)*val 

def pushDown(idx,l,r):

    if not isLazy[idx]:return 
    isLazy[idx]=False
    m=(l+r)//2
    apply(2*idx+1,l,m,unPropUpd[idx])
    apply(2*idx+2,m+1,r,unPropUpd[idx])
    unPropUpd[idx]=0

def build(idx,l,r):

    if l==r:
        segment[idx]=lst[l]
        return

    m=(l+r)//2

    build(2*(idx)+1,l,m)
    build(2*idx+2,m+1,r)

    segment[idx]=segment[2*idx+1]+segment[2*idx+2]

# query - to find sum from range l-r 
# current node range x-y 
def query(idx,x,y,l,r):

    if x>=l and y<=r:
        return segment[idx]

    if x>r or y<l:
        return 0

    pushDown(idx,l,r)
    m=(x+y)//2
    res=query(2*idx+1,x,m,l,r)+query(2*idx+2,m+1,y,l,r)

    return res

# upadte the value at index 'i' with 'val' value
# current node range x-y 
#quert range l-r
def update(idx,x,y,l,r,val):

    if x>r or y<l:
        return 0

    if l<=x and r>=y:

        apply(idx,x,y,val)
        return 

    pushDown(idx,x,y)
    m=(x+y)//2
    update(2*idx+1,x,m,l,r,val)
    update(2*idx+2,m+1,y,l,r,val)
    segment[idx]=segment[2*idx+1]+segment[2*idx+2]


build(0,0,len(lst)-1)
# update(0,0,len(lst)-1,2,-7)
print(segment)
update(0,0,len(lst)-1,2,5,10)
print(query(0,0,len(lst)-1,1,4))
print(segment)



