def knapSack(W, wt, val, n): 
    k = [[0 for x in range(W+1)] for x in range(n+1)] 
    for x in range(n+1): 
        for y in range(t+1): 
            if x==0 or y==0:
                k[x][y] = 0
            elif y >= wt[x-1]:
                we = y-wt[x-1]
                k[x][y] = max(val[x-1]+k[x-1][we], k[x-1][y])
            else:
                k[x][y] = k[x-1][y]    
    return k

#Instead of calling li - returning it will give us a retun value
def li(Array,x,y,item):
    if Array[x][y] == Array[x-1][y]:
        return li(Array,x-1,y,item)
    elif Array[x][y] != Array[x-1][y]:
        item.append(wt[x-1])
        x = x-1
        y = y - wt[x]
        if x == 0 or y==0:
            return item
        return li(Array,x,y,item)
        

val = [1,4,5,7] 
wt = [1,3,4,5] 
t = 7
n = len(wt) 
k = knapSack(t, wt, val, n)
print(li(k,n,t,[]),k[n][t])
  