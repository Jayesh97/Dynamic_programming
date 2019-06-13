a = "aab"
d = {}
st = 0 #start of each substring
lenn = 0 #sub len
start = 0 #start of max string
maxx = 0 #len of max string

for i,j in enumerate(a):
    if j not in d:
        d[j] = i
    else:
        #check if the already existing character is part of non-repeating-string or not
        if d[j]>=st:
            #It is part of string, so string breaks
            lenn = i-st
            if lenn>maxx:
                maxx=lenn
                start=st
            #start a new substring
            st = d[j]+1
        d[j]=i
if maxx<i+1-st:
    maxx = i+1-st
    start = st
print(a[start:start+maxx])
