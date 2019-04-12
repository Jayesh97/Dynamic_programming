#without menmonization
def ways(n):
    if n<=1:
        return n
    return ways(n-1)+ways(n-2)
print(ways(2+1))


#with menmonization
d = {0:0,1:1}
def ways_d(n):
    if n-2 in d and n-1 in d:
        d[n] = d[n-2]+d[n-1]
        return d[n]
    elif n-2 in d:
        d[n-1]=ways_d(n-1)
        d[n] = d[n-1]+d[n-2]
        return d[n]
    else:
        d[n] = ways_d(n-1)+ways_d(n-2)
        return d[n]
print(ways_d(4+1))
print(d)
