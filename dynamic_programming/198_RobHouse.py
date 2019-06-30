nums = [2,7,9,3,1]
def rob(nums):
    incl = 0
    excl = 0
    for i in nums:
        temp = incl #including prev ==== dp[i-1]
        incl = excl + i #excl_this was from prev iteration === dp[i]
        #print(temp,excl)
        excl = max(temp,excl) #=== dp[i-1] or dp[i-2]
    return max(incl,excl)

print(rob(nums))