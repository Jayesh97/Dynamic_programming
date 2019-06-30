nums = [0, -1, 2, -3, 1] 
def t_sum(nums):
    nums = sorted(nums)
    n = len(nums)
    li = []
    for i in range(n-2):
        l = i+1 
        r = n-1
        while l<r and nums[i]<=0:
            total = nums[i]+nums[l]+nums[r]
            if total == 0:
                if [nums[i],nums[l],nums[r]] not in li:
                    li.append([nums[i],nums[l],nums[r]])
                l = l+1
                r = r-1
            if total<0:
                l = l+1
            if total>0:
                r = r-1
    return li

print(t_sum(nums))

def top_sum(nums):
    nums = sorted(nums)
    n = len(nums)
    l = set()
    for i in range(n-2):
        cur = nums[i]
        if cur<=0:
            if i==0 or cur>nums[i-1]:
                d = {}
                for val in nums[i+1:]:
                    if val not in d:
                        d[-cur-val]=1
                    else:
                        l.add((val,cur,-cur-val))

    return map(list,l)

print(top_sum(nums))