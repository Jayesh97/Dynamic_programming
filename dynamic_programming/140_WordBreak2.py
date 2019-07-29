s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
def wordbreak(s,wordDict):
    def helper(s,wordDict,cache):
        if s in cache:
            return cache[s]
        if not s:
            return []
        ans = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            print(word)
            if len(word)==len(s):
                ans.append(s)
            else:
                resultofRest = helper(s[len(word):],wordDict,cache)
                #print(s,cache,ans,resultofRest)
                for item in resultofRest:
                    item = word+" "+item
                    ans.append(item)
        cache[s]=ans
        #print(cache)
        return ans
    return helper(s,wordDict,{})

print(wordbreak(s,wordDict))