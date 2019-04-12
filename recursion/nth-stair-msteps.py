def ways(n,m):
    if n<=1:
        return n
    total = 0
    i = 1
    while i<=m and i<=n:
        total = total + ways(n-i,m)
        i=i+1
    return total

print(ways(3+1,3))


def countWaysUtil(n,m): 
    total = [0 for x in range(n+1)] # Creates list res witth all elements 0 
    total[0],total[1] = 0,1
      
    for i in range(2,n+1): 
        j = 1
        while j<=m and j<=i: 
            total[i] = total[i] + total[i-j] 
            j = j + 1 
    return total[n] 
print(countWaysUtil(3+1,3))