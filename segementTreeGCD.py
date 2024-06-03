# find gcd of range given in query after every update

# POINT UPDATE AND RANGE QUERY-----------
lst=[10, 4, 6, 12, 20, 8, 16, 32]
n=len(lst)
segment=[0]*(4*n) 

def gcd(n,m):

    if m==0:
        return n 

    if n==0:
        return m 

    return gcd(m,n%m)

def build(idx,l,r):
    
    if l==r:
        segment[idx]=lst[l]
        return 
    
    m=(l+r)//2

    build(2*idx+1,l,m)
    build(2*idx+2,m+1,r)

    segment[idx]=gcd(segment[2*idx+1],segment[2*idx+2])


def query(idx,x,y,l,r):

    if x>=l and y<=r:
        return segment[idx]
    
    if x>r or y<l:
        return 0  #identity element
    
    m=(x+y)//2

    return gcd(query(2*idx+1,x,m,l,r),query(2*idx+2,m+1,y,l,r))


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

    segment[idx]=gcd(segment[2*idx+1],segment[2*idx+2])

build(0,0,len(lst)-1)
update(0,0,len(lst)-1,2,24)
print(query(0,0,len(lst)-1,1,4))
