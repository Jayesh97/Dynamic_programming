nums1 = [1,2,2,1]
nums2 = [2,2]
def intersection(nums1,nums2):
    d = {}
    for i in nums1:
        d[i]=d.get(i,0)+1
    res = []
    for i in nums2:
        if i in d and d[i]>0:
            res.append(i)
            d[i]=d[i]-1
    return res

print(intersection(nums1,nums2))