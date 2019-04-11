def seq(a,x):
    k = [1 for x in range(x)]
    for i in range(1,l):
        for j in range(0,i):
           if a[j]<a[i]:
               k[i]=k[j]+1 
    return k

a = [3,4,-1,0,6,2,3]
l = len(a)
v = seq(a,l)
print(v)