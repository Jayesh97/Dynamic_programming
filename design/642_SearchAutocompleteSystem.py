class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False
        self.data = None
        self.rank = 0
    
class Autocomplete(object):
    def __init__(self,sentences,frequencies):
        self.root = TrieNode()
        self.keyword = ""
        for i,sentance in enumerate(sentences):
            self.addRecord(sentance,frequencies[i])
        
    def addRecord(self,sentance,frequency):
        p=self.root
        for c in sentance:
            if c not in p.children:
                p.children[c]=TrieNode()
            p=p.children[c]
        p.end = True
        p.data = sentance
        p.rank = p.rank-frequency

    def dfs(self,root):
        res = []
        if root:
            if root.end:
                res.append((root.rank,root.data))
            for child in root.children:
                res.extend(self.dfs(root.children[child]))
        return res
    
    def search(self,sentance):
        p=self.root
        for c in sentance:
            if c not in p.children:
                return []
            p=p.children[c]
        #we are passing the trienode of end character of search sentance
        #and passing it by the dfs
        return self.dfs(p) 

    def input(self,c):
        search_results=[]
        if c!="#":
            self.keyword=self.keyword+c
            results = self.search(self.keyword)
        else:
            self.addRecord(self.keyword,1)
            self.keyword=""
        return [item[1] for item in sorted(results)[:3]]

obj = Autocomplete(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
f = obj.input("i")
print(f)
f = obj.input(" ")
print(f)

