def reverse(nums,start,end):
    while start<end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start = start+1
        end = end-1

def rotate(nums,k):
    k = k%len(nums)
    reverse(nums,0,len(nums)-1)
    reverse(nums,0,k-1)
    reverse(nums,k,len(nums)-1)
    return nums

nums = [1,2,3,4,5,6,7]
k = 2
print(rotate(nums,k))
