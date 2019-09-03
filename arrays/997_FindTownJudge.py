n = 2
trust = [[1,2]]
n = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
def findjudge(n,trust):
    val = [0]*(n+1)
    for p1,p2 in trust:
        val[p1]=val[p1]-1
        val[p2]=val[p2]+1
    print(val)
    for i in range(n+1):
        if val[i]==n-1:
            return i
    return -1
print(findjudge(n,trust))
    
