def matrix(a,m,n):
    k = [[0 for y in range(n+1)] for x in range(m+1)]
    for x in range(m+1):
        for y in range(n+1):
            if x==0 or y==0:
                k[x][y]=0
            elif x==1:
                k[x][y] = k[x][y-1]+a[x-1][y-1]
            elif y==1:
                k[x][y] = k[x-1][y]+a[x-1][y-1]
            else:
                k[x][y] = k[x][y-1]+k[x-1][y]+a[x-1][y-1]-k[x-1][y-1]
    return k

def query(k,q1,q2):
    [r1,c1] = [x+1 for x in q1]
    [r2,c2] = [x+1 for x in q2]
    sum = k[r2][c2]-k[r2][c1-1]-k[r1-1][c2]+k[r1-1][c1-1]
    return sum


a = [[2,0,-3,4],[6,3,2,-1],[5,4,7,3],[2,-6,8,1]]
m = len(a)
n = len(a[0])
k = matrix(a,m,n)
q1 = [1,1]
q2 = [3,2]
q = query(k,q1,q2)
print(k)
print(q)