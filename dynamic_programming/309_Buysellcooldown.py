prices = [1,2,3,0,2]
def buysellcool(prices):
    if not prices:
        return 0
    b0 = -prices[0] #buy[i]
    b1 = -prices[0] #buy[i-1]
    s0,s1,s2 = 0,0,0
    for i in range(len(prices)):
        b0=max(b1,s2-prices[i]) #base case max(0,-1) - buy or not buy
        s0=max(s1,b1+prices[i]) #max(do nothing,sell)
        s2=s1
        s1=s0
        b1=b0
    return s0 #actuall s1 ie sell[i-1]
print(buysellcool(prices))