a = [4,5,6,7,0,1,2]
target = 20
l = 0
r = len(a)-1
def search(a,l,r,target):
    print(l,r)
    if l == r and a[l]!=target:
        return -1
    mid = (l+r)/2
    if a[mid]==target:
        return mid
    if a[l]==target:
        return l
    '''
    #8>4 8>7 go right
    if target>a[l] and target>a[mid]:
        return search(a,mid+1,r,target)
    #6 7 0 1 2 3 4 5, 5 is target
    if target>a[mid] and target<a[l]:
        return search(a,mid+1,r,target)
    #0<4 0<7 go right
    if target<a[l] and target<a[mid]:
        return search(a,mid+1,r,target)
    '''
    if target>a[mid] or (target<a[l] and target<a[mid]):
        return search(a,mid+1,r,target)
    #6>4 6<7 go left
    if target>a[l] and target<a[mid]:
        return search(a,l,mid,target)
    else:
        return -1
print(search(a,l,r,target))
