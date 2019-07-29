S = "abbcabca"
T = "aa"
def max_sub(s,t):
    if not t or not s:
        return ""
    #count chars in t
    dt = {}
    for char in t:
        dt[char]=dt.get(char,0)+1
    #l,r,required,formed,windowcount,ans
    required = len(dt)
    l,r = 0,0
    formed = 0 
    window_count = {}
    ans = float("inf"),None,None
    #outer loop - expand r and check for formed
    while r<len(s):
        char = s[r]
        window_count[char]=window_count.get(char,0)+1
        if char in dt and window_count[char]==dt[char]:
            formed = formed + 1
        #contracting after finding and then expanding again
        while l<=r and formed==required:
            char = s[l]
            #saving the smallest window
            if r-l+1<ans[0]:
                ans = (r-l+1,l,r)
            window_count[char]=window_count[char]-1
            if char in dt and window_count[char]<dt[char]:
                formed = formed-1
            l = l+1
        r=r+1
    return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]

print(max_sub(S,T))
