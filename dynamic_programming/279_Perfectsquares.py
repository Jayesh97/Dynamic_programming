def tot_sq(n):
    if n<=3:
        return n
    k = [0,1,2,3]
    for i in range(4,n+1):
        k.append(i)
        #print(k)
        for j in range(2,i):
            temp = j*j
            if i==temp:
                k[i]=1
                break
            elif temp>i:
                break
            else:
                k[i]=min(k[i],k[i-temp]+1)
        #print(k)
    return k[n]

print(tot_sq(12))

import math
from collections import deque

def numSquares(n):

    sqrt_vals = [i*i for i in range(int(math.sqrt(n)), 0, -1)]
    print(sqrt_vals)
    visited = set()
    
    queue = deque([(n, 0)])
    
    while len(queue):
        val, step = queue.popleft()
        
        for sqrt_val in sqrt_vals:
            if val - sqrt_val == 0:
                return step + 1
            elif val - sqrt_val > 0 and (val - sqrt_val) not in visited:
                queue.append((val - sqrt_val, step + 1))
                visited.add(val - sqrt_val)

print(numSquares(12))