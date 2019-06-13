nums1 = [1,2,3,7,10,0,0,0]
m = 4
nums2 = [2,5,6]
n = 3
i1 = 0
i2 = 0
i1og = 0
while i1 < m+n and i2 < n:
    if i1og == m:
        nums1[i1] = nums2[i2]
        i1 += 1
        i2 += 1
    elif nums2[i2] < nums1[i1]:
        nums1[:] = nums1[:i1] + [nums2[i2]] + nums1[i1:-1]
        i1 += 1
        i2 += 1
    else:
        i1 += 1
        i1og += 1
print(nums1,nums2)

