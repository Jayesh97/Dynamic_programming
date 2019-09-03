nums = [1,1,1]
k = 2
def subarraysum(nums,k):
    total = 0
    summ = 0
    d = {0:1}
    for i in range(len(nums)):
        summ = summ + nums[i]
        total=total+d.get(summ-k,0)
        d[summ]=d.get(summ,0)+1
    return total

print(subarraysum(nums,k))