s = "leetcode"
s = "aabbcc"
def firstunique(s):
    d = {}
    for i,j in enumerate(s):
        d[j]=d.get(j,[0,i])
        d[j][0]+=1
    print(d)
    minn = float('inf')
    for key,value in d.items():
        if value[0] == 1:
            minn = min(value[1],minn)
    return -1 if minn==float('inf') else minn
print(firstunique(s))

