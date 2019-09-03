nums=[3,2,3]
def majorityelement(nums):
    d = {}
    for i in nums:
        d[i]=d.get(i,0)+1
    for i in d.keys():
        if d[i]>len(nums)/2:
            return i
print(majorityelement(nums))