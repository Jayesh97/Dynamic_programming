words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
def superword(words):
    s = set(words)
    cache = {}
    def dfs(word):
        if word in cache:
            return cache[word]
        cache[word]=False
        for i in range(1,len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in s and suffix in s:
                cache[word]=True
                break
            if prefix in s and dfs(suffix):
                cache[word]=True
                break
            if suffix in s and dfs(prefix):
                cache[word]=True
                break
        return cache[word]
    ans = []
    for word in words:
        if dfs(word):
            ans.append(word)
    return ans
print(superword(words))