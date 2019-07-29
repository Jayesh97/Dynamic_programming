from collections import deque
nums = [1,3,-1,-3,5,3,6,7]
k = 3
def sliding(nums,k):
    res = []
    bigger = deque()
    for i,j in enumerate(nums):
        while bigger and nums[bigger[-1]]<=j:
            bigger.pop()
        bigger.append(i)
        if i-bigger[0]>=k:
            bigger.popleft()
        if i+1>=k:
            res.append(nums[bigger[0]])
        #print(bigger)
    return res

print(sliding(nums,k))