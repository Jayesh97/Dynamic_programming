coins = [1,2,5]
amount = 11
k = [-1 for i in range(amount+1)]
k[0] = 0
for i in range(1,amount+1):
    for j in coins:
        if i>=j and k[i-j]!=-1:
            if k[i]==-1 or k[i]>k[i-j]+1:
                k[i] = k[i-j]+1
print(k)