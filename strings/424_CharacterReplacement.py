s = "ABABCAABCB"
k = 2
def characterReplacement(s,k):
    n = len(s)
    if n==0:
        return 0
    d = {}
    low,high = 0,0
    while high<n:
        d[s[high]] = d.get(s[high],0)+1
        max_char_count = max(d.values())
        if ((high+1)-low-max_char_count)>k:
            d[s[low]]=d[s[low]]-1
            low = low+1
        high = high+1
    return high-low

print(characterReplacement(s,k))