n=10
def countps(n):
    if n<2:
        return 0
    val=[True]*n
    val[0],val[1]=False,False
    for i in range(2,n):
        if val[i]==True:
            for j in range(i*i,n,i):
                val[j]=False
    return sum(val)

print(countps(n))