a = [10,20,9,40]
sum = 29
d = {}
for i,j in enumerate(a):
    if j in d:
        print(d[j][1],i)
        print(a[d[j][1]],a[i])
        break
    d[sum-j]=(j,i)