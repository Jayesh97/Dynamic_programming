def search(a,l,r,target):
    if l<=r:
        mid = (l+r)/2
        #print(l,r,mid)
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            return search(a,mid+1,r,target)
        return search(a,l,mid-1,target)
    return -1
def expand(a,mid,target):
    left = mid
    right = mid
    if mid==-1:
        return [-1,-1]
    #expand left
    while left>0 and a[left-1]==target:
        left = left-1
    while right<len(a)-1 and a[right+1]==target:
        right=right+1
    return [left,right]
a=[8,8,8,9,10]
target = 8
l = 0
r = len(a)-1
mid = search(a,l,r,target)
print(mid)
print(expand(a,mid,target))