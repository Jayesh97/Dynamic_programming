a = [2,0,2,1,1,0]
l = 0 #keeps track of zeros, but points to the 1st 1
mid = 0 #keeps track of 1's
r = len(a)-1 #keeps track of 2's
while mid<=r:
    if a[mid] == 0:
        a[l],a[mid] = a[mid],a[l]
        l = l+1
        mid = mid+1
    elif a[mid]==1:
        mid = mid+1
    else:
        a[mid],a[r]=a[r],a[mid]
        r = r-1
print(a)
