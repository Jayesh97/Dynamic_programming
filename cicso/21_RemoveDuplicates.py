nums = [0,0,1,1,1,2,2,3,3,4]
def remove_duplicates(nums):
    i = 0
    for j in nums:
        if nums[i]==j:
            continue
        i = i+1
        nums[i]=j
    return nums
print(remove_duplicates(nums))