s = "abcabcbb"
def substr(s):
    st = 0
    l = 0
    start = 0
    maxx = 0
    d = {}
    if len(s)==0:
        return 0
    if len(s)==1:
        return 1
    for i,j in enumerate(s):
        if j not in d:
            d[j]=i
        else:
            if st<=d[j]:
                l = i-st
                if l>maxx:
                    maxx=l
                    start = st
                st = d[j]+1
            d[j]=i
    #special case for complete string
    if maxx<i+1-st:
        maxx=i+1-st
        start = st
    return maxx

print(substr(s))