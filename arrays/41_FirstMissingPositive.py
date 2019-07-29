nums = [1,2,3]
def missing(nums):
    nums.append(0)
    n = len(nums)
    for i in range(n):
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    #print(nums)
    for i in range(n):
        #print(nums[i]%n)
        nums[nums[i]%n] = nums[nums[i]%n]+n #storing frequency keeping intact of the values
        #print(nums)
    for i in range(1,n):
        if nums[i]/n==0:
            return i
    return n


print(missing(nums))
