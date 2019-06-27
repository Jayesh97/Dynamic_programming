nums = [1,2,3,4]

def product(nums):
    n = len(nums)
    result = [0]*n
    result[0]=1
    for i in range(1,n):
        result[i]=result[i-1]*nums[i-1]
    print(result)
    R = 1
    for i in range(n-2,-1,-1):
        R = R*nums[i+1]
        result[i]=result[i]*R
    return result

print(product(nums))