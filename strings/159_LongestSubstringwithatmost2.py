from collections import defaultdict
s = "ccaabbb"
def longestwith2(s):
    n = len(s)
    if n==0:
        return 0
    max_len = 1
    left,right = 0,0
    d = defaultdict()
    while right<n:
        d[s[right]]=right
        right = right+1
        if len(d.keys())==3:
            del_idx = min(d.values())
            del d[s[del_idx]]
            left = del_idx+1
        max_len = max(max_len,right-left)
    return max_len

print(longestwith2(s))