n = 10
def climbing(n):
    if n==1:
        return 1
    dp = [1,1,2]
    for i in range(3,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]

print(climbing(n))