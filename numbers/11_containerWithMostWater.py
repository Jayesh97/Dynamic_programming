a = [1,8,6,2,5,4,8,3,7]
#O(n**2) complexity
maxx = 0
for i in range(len(a)):
    for j in range(i,len(a)):
        #print(i,j)
        vol = min(a[i],a[j])*(j-i)
        if vol>maxx:
            maxx = vol
print(maxx)
#Using 2-pointer method
l = 0
r = len(a)-1
maxx = 0
while(r>l):
    maxx = max(maxx,min(a[l],a[r])*(r-l))
    if a[l]<a[r]:
        l = l+1
    else:
        r = r-1
print(maxx)
