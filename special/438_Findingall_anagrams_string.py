from collections import defaultdict
def findAnagrams(s: str, p: str):
    req, sliding = {},{}
    indices = []
    n , total_len = len(p),len(s)
    for i in p:
        req[i] = req.get(i,0)+1
    #print(req)
    for i in s[:n-1]:
        sliding[i] = sliding.get(i,0)+1
    #print(sliding)
    for i in range(n-1,total_len):
        sliding[s[i]]= sliding.get(s[i],0)+1
        #print(s[i],sliding)
        if sliding == req:
            indices.append(i-(n-1))
        sliding[s[i-(n-1)]] -= 1
        if sliding[s[i-(n-1)]] == 0:
            del(sliding[s[i-(n-1)]])
    return indices

print(findAnagrams(s="cbaebabacd",p="abc"))
    
