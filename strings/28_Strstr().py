#**********************Watch video*******************
#bruteforce O(mn)-worst case
haystack = "hello"
needle = "ll"
def str_str_b(haystack,needle):
    if not haystack or not needle:
        return -1
    #outer-loop to revert back to the previous occurance
    for i in range(len(haystack)+len(needle)-1):
        for j in range(len(needle)):
            if haystack[i+j]==needle[j]:             
                if j==len(needle)-1:
                    return i
            else:
                break
    return -1
print(str_str_b(haystack,needle))


#KMP O(m+n)
#suffix prefix array O(n) space O(n)
haystack = "hello"
needle = "ll"
def kmp(haystack,needle):
    def preprocess(needle):
        i = 1
        j = 0
        res = [0]*len(needle)
        while i<len(needle):
            if needle[i]==needle[j]:
                res[i]=j+1
                i = i+1
                j = j+1
            #value at the previous
            elif j>0:
                j = res[j-1]
            else:
                res[i]=0
                i = i+1
        return res
    if not haystack or not needle or len(needle)>len(haystack):
        return -1
    prefix = preprocess(needle)
    i = 0
    j = 0
    while i<len(haystack) and j<len(needle):
        if haystack[i]==needle[j]:
            i = i+1
            j = j+1
        elif j>0:
            j = prefix[j-1]
        else:
            i=i+1
    if j==len(needle):
        return i-j
    return -1
print(kmp(haystack,needle))