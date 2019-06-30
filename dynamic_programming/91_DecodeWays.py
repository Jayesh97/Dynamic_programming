from collections import defaultdict
s = "226"
def decode(s):
    d = defaultdict(int)
    d[len(s)]=1
    for i in reversed(range(len(s))):
        #print(i)
        if s[i]=="0":
            d[i]=0
        elif i==len(s)-1:
            d[i]=1
        else:
            d[i]=d[i]+d[i+1]
            if int(s[i:i+2])<=26:
                d[i]=d[i]+d[i+2]
    return d[0]


print(decode(s))

def numDecodings(s):
    cache = defaultdict(int)
    cache[len(s)] = 1
    
    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s)-1:
            cache[i] = 1
        else:
            cache[i] += cache[i+1]
            if int(s[i:i+2]) <= 26:
                cache[i] += cache[i+2]
    return cache[0]
print(numDecodings(s))