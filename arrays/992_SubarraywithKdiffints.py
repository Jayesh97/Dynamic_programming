A = [1,2,1,2,3]
k = 2
def subarray(A,k):
    return atmostk(A,k)-atmostk(A,k-1)

def atmostk(A,k):
    d = {}
    res = 0
    low,high = 0,0
    for high in range(len(A)):
        #if a new letter comes
        if d.get(A[high],0)==0:
            k=k-1
        d[A[high]]=d.get(A[high],0)+1
        while k<0:
            d[A[low]]=d[A[low]]-1
            #if a char count becomes 0, which means we can
            #accomodate new one, so k=k+1
            if d[A[low]]==0:
                k=k+1
            low=low+1
        res = res + (high+1)-low
    return res

print(subarray(A,k))