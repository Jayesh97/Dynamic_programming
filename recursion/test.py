a = [4,5,6,7,0,1,2]
target = 20
l = 0
r = len(a)-1
def search(nums,l,r,target):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        mid = (l + r) // 2
        print(l,r,mid)
        if nums[mid] == target:
            return mid
        if nums[l] > nums[r]:
            l += 1
            r -= 1
        else:
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
    return -1
print(search(a,l,r,target))