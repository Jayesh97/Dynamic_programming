a = [10,20,9,40]
num = 180
d = {}
for i,j in enumerate(a):
    if j in d:
        print(d[j][1],i)
        break
    d[num/j]=(j,i)