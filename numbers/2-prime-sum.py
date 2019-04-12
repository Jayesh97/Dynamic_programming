l = []
num = 1024
for i in range(2,1024):
    for x in range(2,i):
        if i%x == 0:
            break
    else:
        l.append(i)

d = {}
for i,j in enumerate(l):
    if j in d:
        print(l[d[j][1]],l[i])
        break
    d[num-j]=(j,i)