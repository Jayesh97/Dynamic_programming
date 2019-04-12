a = [1,6,4,10,2,5,0]
l = []

#Running 2 loops
l.append(None) 
# Start from second element 
for i in range(1, len(a)): 
    for j in range(i-1 ,-2 ,-1): 
        if (a[j] < a[i]): 
            l.append(a[j]) 
            break 
    if (j == -1): 
        l.append(None) 
print(l)


#Using stack
a = [1,6,4,10,2,5,1]
s = []
l = []
for i in a:
    while len(s)>0 and s[-1]>=i:
        s.pop()
    if len(s)==0:
        l.append(None)
    else:
        l.append(s[-1])
    s.append(i)
print(l)