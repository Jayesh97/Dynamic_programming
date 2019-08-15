A = [1,0,1,1,0]
def oneflip(A):
    n = len(A)
    if n==0:
        return 0
    max_len=1
    k = 1
    low,high=0,0
    for high in range(n):
        if A[high]==0:
            k=k-1
        while k<0:
            if A[low]==0:
                k=k+1
            low=low+1
        max_len = max(max_len,high+1-low)
    return max_len
print(oneflip(A))

nums = [1,0,1,1,0]
#followup - datastream
def streamones(nums):
    pre,curr,max_len = -1,0,0
    for n in nums:
        if n==0:
            pre,curr=curr,0
        else:
            curr=curr+1
        max_len=max(max_len,pre+1+curr)
    return max_len

print(streamones(nums))
