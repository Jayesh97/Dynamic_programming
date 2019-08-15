A = [1,1,0,1,1,1]
def maxconsq(A):
    n=len(A)
    if n==0:
        return 0
    low,high = 0,0
    local_max,max_len=0,0
    for high in range(n):
        if A[high]==0:
            local_max=0
            low=high
            continue
        local_max = local_max+1
        max_len = max(max_len,local_max)
    return max_len
print(maxconsq(A))