nums = [10,9,2,5,3,7,101,18]
def lisub(nums):
    if len(nums)==0:
        return 0
    k = [0 for i in range(len(nums))]
    k[0]=1
    maxx = 1
    for i in range(1,len(nums)):
        maxval = 0
        for j in range(i):
            if nums[i]>nums[j]:
                maxval = max(maxval,k[j])
        k[i]=maxval+1
        maxx = max(maxval,k[i])
    return maxx
print(lisub(nums))
