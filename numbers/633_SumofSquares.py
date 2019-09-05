import math
x = 7
def sumofsquares(x):
    #generate suares
    d = set()
    for i in range(int(math.sqrt(x)+1)):
        d.add(i**2)
    #two sum
    #5 = 4+1, {4:1,1:4}
    for i in d:
        if x-i in d:
            return True
    return False
        


print(sumofsquares(x))
    