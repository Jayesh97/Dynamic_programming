nums = [1,2,3,4,5]
def triplets(nums):
    if len(nums)<=2:
        return False
    minn = nums[0]
    maxx = float('inf') #This will be the mid number (ie. 2nd largest)
    for i in nums[1:]:
        if i>maxx:
            return True
        elif maxx>i>minn:
            maxx = i
        elif i<minn:
            minn = i
    return False
