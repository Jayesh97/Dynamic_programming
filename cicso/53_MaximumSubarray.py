nums = [-2,1,-3,4,-1,2,1,-5,4]
def max_sum(nums):
    local_max = nums[0]
    maxx = nums[0]
    for i in nums:
        local_max = max(local_max+i,i)
        if local_max>maxx:
            maxx = local_max
    return maxx
print(max_sum(nums))