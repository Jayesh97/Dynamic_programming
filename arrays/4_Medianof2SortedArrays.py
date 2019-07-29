a = [1,2,3,4,5]
b = [13,14,15,16,17,18,19,20]
def mediann(a,b):
    la = len(a)
    lb = len(b)
    if la>lb:
        mediann(b,a) #keeping smaller in a
    low = 0
    high = la
    half = (la+lb+1)/2
    while low<=high:
        mid1 = (low+high)/2
        mid2 = half-mid1
        if mid1<la and b[mid2-1]>a[mid1]:
            low = mid1+1 #in binary search we update low to mid+1
        elif mid1>0 and a[mid1-1]>b[mid2]:
            high = mid1-1 #binary on lower number(ie m)
        else:
            #values are perfect
            if mid1==0: 
                max_left = b[mid2-1]
            elif mid2==0: 
                max_left = a[mid1-1]
            else:
                max_left = max(a[mid1-1],b[mid2-1])
            if (la+lb)%2==1:
                return max_left
            if mid1==la:
                min_rigth = b[mid2]
            elif mid2==lb:
                min_rigth = a[mid1]
            else:
                min_rigth = min(a[mid1],b[mid2])
            return (max_left+min_rigth)/2.0

print(mediann(a,b))