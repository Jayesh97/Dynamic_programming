nums = [1, 5, 1, 1, 6, 4]
n = len(nums)
clone = sorted(nums)
start = n/2-1 if n%2==0 else n/2
end = n-1
for i in range(n):
    if i%2==0:
        nums[i] = clone[start]
        start = start-1
    else:
        nums[i] = clone[end]
        end = end-1
print(nums)

nums = [1, 5, 1, 1, 6, 4]
