n = [1,5,8,4,7,6,5,3,1]
#n = [1,3,2]
def nextperm(n):
    #finding pivot
    for i in range(len(n)-1,-1,-1):
        if i==0:
            reverse(n,l,r)
            return
        if i!=0 and n[i]>n[i-1]:
            pivot = i-1
            #print(n[i-1])
            break
    #finding number just greater than pivot
    for i in range(len(n)-1,pivot,-1):
        if n[i]>n[pivot]:
            swapper=i
            break
    n[pivot],n[swapper]=n[swapper],n[pivot]
    #reverse the remaining
    l=pivot+1
    r = len(n)-1
    reverse(n,l,r)
    print(n)
def reverse(n,l,r):
    while l<r:
        n[l],n[r]=n[r],n[l]
        l=l+1
        r=r-1
    return
print(nextperm(n))