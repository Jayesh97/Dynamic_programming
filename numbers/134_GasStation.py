gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
def circuit(gas,cost):
    i = 0
    n = len(gas)
    while i<n:
        carry = 0
        for j in range(n):
            k = (i+j)%n
            carry = carry + gas[k] - cost[k]
            if carry<0:
                i = i+j+1
                break
        else:
            return i
    return -1
print(circuit(gas,cost))