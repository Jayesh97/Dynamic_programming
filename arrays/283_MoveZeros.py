nums = [0,1,2,0,4,5,0]
def movezeros(nums):
    i = 0 #marks the position of 0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i = i+1
movezeros(nums)
print(nums)