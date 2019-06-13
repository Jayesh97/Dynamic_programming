a = [6,-3,-10,0,2]
a = [-1,-3,-10,0,60]
#a = [-2,-3,0,-2,-40]
#a = [2,3,-2,4]
#a = [-2,0,-1]
#a = [0,2]

minn = a[0]
maxx = a[0]
mprod = a[0]
for i in range(1,len(a)):
    if a[i]<0:
        temp = maxx
        maxx = minn
        minn = temp
    maxx = max(a[i],maxx*a[i])
    minn = min(a[i],minn*a[i])
    mprod = max(mprod,maxx)
print(mprod)

    