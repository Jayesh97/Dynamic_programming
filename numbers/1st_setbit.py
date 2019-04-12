import math

#using complement
n = 32
p = math.log(n&-n,2)+1
print(int(p))

#Iterating the binary
n = 32
b = bin(n)
for i in range(len(b)):
    if b[-i]=="1":
        print(i)
        break