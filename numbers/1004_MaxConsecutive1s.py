A = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
A = [0,0,0,0]
k = 0
def maxconsq(A,k):
    n = len(A)
    if n==0:
        return 0
    low,high = 0,0
    max_len=0
    for high in range(n):
        if A[high]==0:
            k=k-1
        while k<0:
            if A[low]==0:      
                k=k+1
            low=low+1
        print(high,low)
        max_len = max(max_len,high+1-low)
    return max_len

print(maxconsq(A,k))