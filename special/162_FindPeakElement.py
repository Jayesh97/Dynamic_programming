def search(a,l,r):
    if l==r:
        return a[l]
    mid =(l+r)/2
    if a[mid]>a[mid+1]:
        return search(a,l,mid)
    return search(a,mid+1,r) #if only 2 elements are present it would go infinite if (mid+1) is not given


a = [1,10,1,3,5,6,4]
l = 0
r = len(a)-1
print(search(a,l,r))