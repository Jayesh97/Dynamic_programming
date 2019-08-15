from collections import defaultdict
s = "eceba"
k = 2
def lenoflongest(s,k):
    n = len(s)
    if k==0 or n==0:
        return 0
    left,right = 0,0
    d = defaultdict()
    max_len = 1
    while right<n:
        d[s[right]]=right
        #print(d)
        right = right+1
        if len(d.keys())==k+1:
            del_idx = min(d.values())
            del d[s[del_idx]]
            left = del_idx+1
        max_len = max(max_len,right-left)
    return max_len
        
print(lenoflongest(s,k))