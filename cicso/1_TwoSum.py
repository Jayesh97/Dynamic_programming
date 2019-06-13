nums = [2, 7, 11, 15]
target = 13
d = {}
def two_sum(nums,target):
    for i,j in enumerate(nums):
        if target-j in d:
            return [i,d[target-j][1]]
        d[j]=[target-j,i] #location where u can find j
    return [-1,-1]
print(two_sum(nums,target))