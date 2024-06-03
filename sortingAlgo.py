# lst=[1,3,12,7,10]
# for i in range(len(lst)-1):
#     for j in range(len(lst)-i-1):
#         if lst[j]>lst[j+1]:
#             lst[j],lst[j+1]=lst[j+1],lst[j]
# print(lst)
# in bubble sort after every ith iteration  ith largest number is set

# lst=[17,3,12,7,10]
# for i in range(len(lst)-1):
#     mini=i
#     for j in range(i+1,len(lst)):
#         if lst[j]<lst[mini]:
#             mini=j
#     if mini!=i:
#         lst[mini],lst[i]=lst[i],lst[mini]
# print(lst)

# INSERTION SORT-------------------------------------

# we assume that first element is already sorted 
# and so we start from ele 2 

# we compare cur ele with all the elemenets to tits left and palce it at correct postion

# to every current element , all the elemenets to its left are sorted 
# lst=[17,3,12,7,10]
# for i in range(1,len(lst)):
#     key=lst[i]
#     j=i-1
#     while j>=0 and lst[j]>key:
#         lst[j+1]=lst[j]
#         j-=1
#     lst[j+1]=key
# print(lst)


# MERGE SORT-----------------------------------------

# lst=[3,2,6,4,1]
# def mergeSort(lst,l,m,h):
#     i=l
#     j=m+1
#     res=[]
#     while(i<=m and j<=h):
#         if lst[i]<=lst[j]:
#             res.append(lst[i])
#             i+=1
#         else:
#             res.append(lst[j])
#             j+=1

#     while i<=m:
#        res.append(lst[i])
#        i+=1

#     while j<=h:
#        res.append(lst[j])
#        j+=1
#     for p in range(len(res)):
#         lst[l]=res[p]
#         l+=1


# def merge(lst,l,h):
#     if l<h:
#         m=(l+h)//2
#         merge(lst,l,m)
#         merge(lst,m+1,h)
#         print(lst,l,m,h)
#         mergeSort(lst,l,m,h)
# merge(lst,0,4)
# print(lst)

# lst=[17,3,12,7,10]




# merge sort for count iversions-------------

# lst=[2,4,1,3,5]
# inversions=[]
# def mergeSort(lst,l,m,h):
    
#     print(lst,l,m,h)
#     i=l
#     j=m+1
#     res=[]
#     while(i<=m and j<=h):
#         if lst[i]<=lst[j]:
#             res.append(lst[i])
#             i+=1
#         else:
#             inversions.append(m-i+1)
#             res.append(lst[j])
#             j+=1

#     while i<=m:
#        res.append(lst[i])
#        i+=1

#     while j<=h:
#        res.append(lst[j])
#        j+=1
#     for p in range(len(res)):
#         lst[l]=res[p]
#         l+=1


# def merge(lst,l,h):
#     if l<h:
#         m=(l+h)//2
#         merge(lst,l,m)
#         merge(lst,m+1,h)
#         mergeSort(lst,l,m,h)
# merge(lst,0,4)
# print(sum(inversions))


lst=[20,8,30,5,18,35,15,41,10,12,22,11,32,7,21,37,17,43,2,46]



# Quick sort----------------


def partition(lst,l,h):

   pivot=lst[h] #choosing last ele as pivot 
   pindex=l #index indicating the position of swapped elements thse are less than pivot 

   for i in range(l,h):
      if lst[i]<pivot: 
         lst[i],lst[pindex]=lst[pindex],lst[i] #ele less than pivot are places in pindex position
         pindex+=1 #incrementing pindex for the next element
      
   lst[pindex],lst[h]=lst[h],lst[pindex] #bringing the pivot to its postion that is to centre
 
   return pindex #return the index of pivot 
   #  pivot=lst[end]
   #  l=start
   #  h=end-1
#  while l<=h:
   #     if lst[l]<=pivot:
   #        l+=1
   #     if lst[h]>pivot:
   #        h-=1
   #     if lst[l]>pivot and lst[h]<=pivot:
   #        lst[l],lst[h]=lst[h],lst[l]
   #        l+=1
   #        h-=1
   #  lst[l],lst[end]=lst[end],lst[l]
   #  return l
  

def quickSort(lst,l,h):
    if l<h:
      p=partition(lst,l,h)
      quickSort(lst,l,p-1)
      quickSort(lst,p+1,h)
quickSort(lst,0,len(lst)-1)
print(lst)



# Tim sort----------

# lst=[20,8,30,5,18,35,15,41,10,12,22,11,32,7,21,37,17,43,2,46]

# def insertionSort(nums,start,end):
#     for i in range(start+1,end+1):
#         key=nums[i]
#         j=i-1
#         while j>=start and key<nums[j]:
#             nums[j+1]=nums[j]
#             j-=1
#         nums[j+1]=key

# def mergeSort(nums,left,mid,right):
#     i=left
#     j=mid+1
#     res=[]
#     while i<=mid and j<=right:

#         if nums[i]<=nums[j]:
#             res.append(nums[i])
#             i+=1

#         else:
#             res.append(nums[j])
#             j+=1 
    
#     while i<=mid:
#         res.append(nums[i])
#         i+=1
#     while j<=right:
#         res.append(nums[j])
#         j+=1
    
#     for ele in res:
#         nums[left]=ele
#         left+=1

    
# def timSort(nums,runSize):
#     for start in range(0,len(nums),runSize):
#         end=min(start+runSize-1,len(nums)-1)
#         insertionSort(nums,start,end)
   
#     rs=runSize
#     while rs<len(nums):
#         for left in range(0,len(nums),2*rs):
#             mid=min(left+rs-1,len(nums)-1)
#             right=min(left+(2*rs)-1,len(nums)-1)
#             print(left,mid,right)
#             if mid<right:
#                 mergeSort(nums,left,mid,right)
              
#         rs=2*rs

# timSort(lst,4)
# print(lst)


    
