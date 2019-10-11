#unique paths
def paths(m,n):
    k = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        k[i][0]=1
    for i in range(n):
        k[0][i]=1
    for i in range(1,m):
        for j in range(n):
            k[i][j] = k[i-1][j]+k[i][j-1]
    return k[m-1][n-1]
print(paths(3,2))
    
