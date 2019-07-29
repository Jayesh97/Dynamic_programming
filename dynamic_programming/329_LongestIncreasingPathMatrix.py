matrix = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
def longestpath(matrix):
    if len(matrix)==0:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)]  for j in range(m)]
    maxx = 1
    for i in range(m):
        for j in range(n):
            length = dfs(matrix,i,j,m,n,dp)
            maxx = max(maxx,length)
    return maxx
def dfs(matrix,i,j,m,n,dp):
    if dp[i][j] != 0:
        return dp[i][j] #caching the values
    maxx = 1
    for x,y in neighbors:
        r = i+x
        c = j+y
        if (r>=0 and r<m) and (c>=0 and c<n) and matrix[r][c]>matrix[i][j]:
            length = 1+dfs(matrix,r,c,m,n,dp)
            maxx = max(maxx,length)
        dp[i][j]=maxx
    return maxx

print(longestpath(matrix))



