a = [2,3,1,1,4]
b = [3,2,2,0,4]
last = len(a)-1
for i in range(last,-1,-1):
    if i + b[i] >= last:
        last = i
print(last)