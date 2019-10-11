nums = [7,2,5,10,8]
m = 2
def splitarray(nums,m):
    n = len(nums)
    dp = [[float('inf') for j in range(m+1)] for i in range(n+1)]
    print(dp)
    cumsum = [0]*(n+1) #cummulative sum
    for i in range(n):
        #print(cumsum)
        cumsum[i+1] = cumsum[i] + nums[i]
    print(cumsum) 
    dp[0][0]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            for k in range(i):
                #print(i,j,k)
                dp[i][j]=min(dp[i][j],max(dp[k][j-1],cumsum[i]-cumsum[k]))

    return dp[n][m]
print(splitarray(nums,m))