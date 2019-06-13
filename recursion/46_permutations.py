#backtracking
def permute(string,l,r,d):
    if l==r:
        print(string)
        d.append(string)
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l] #swapping
            permute(a,l+1,r,d)
            a[l],a[i]=a[i],a[l] #swapping for backtracking
string = "ABC"
d = []
a = list(string)
permute(a,0,len(a)-1,d)
print(d)

