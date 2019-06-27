s = "leetcode"
wordDict = ["leet", "code"]
def recurse(s,seen,wordset,lengths):
    if s=="":
        return True
    if s in seen:
        return seen[s]
    for length in lengths:
        if s[:length] in wordset and recurse(s[length:],seen,wordset,lengths):
            #print(s[:length])
            seen[s]=True
            return True
    seen[s]=False
    return False
seen = {}
wordset = set(wordDict)
lengths = sorted(set(len(x) for x in wordDict))
print(lengths)
print(recurse(s,seen,wordset,lengths))