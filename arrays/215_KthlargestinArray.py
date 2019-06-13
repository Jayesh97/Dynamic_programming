#quick select
def kthsmallest(a,l,r,k):
    if k>0 and k<=r-l+1: #1st smallest and indexex of arrays differ by 1
        pivot = partition(a,l,r)
        print(a,l,pivot,r)
        if pivot-l == k-1:
            return a[pivot] 
        if pivot-l > k-1:
            return kthsmallest(a,l,pivot-1,k)
        return kthsmallest(a,pivot+1,r,k-((pivot-l)+1)) #k-pivot = fails for single element
    return -1
#Finding the correct position of pivot
def partition(a,l,r):
    x = a[r] #taking last element as pivot
    i = l
    #finding proper position of pivot
    for j in range(l,r):
        if a[j]<=x:
            a[j],a[i]=a[i],a[j]
            i = i+1
    a[i],a[r]=a[r],a[i]
    return i

a = [3,2,1,5,6,4]
n = len(a) 
k = 2
print(kthsmallest(a,0,n-1,n-k+1))