from collections import defaultdict


class TrieNode():
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isword = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    #each character represents a Trie Node
    def insert(self,word):
        curr = self.root
        for i in word:
            curr = curr.nodes[i]
        curr.isword = True

    def search(self,word):
        curr = self.root
        for i in word:
            if i not in curr.nodes:
                return False
            curr = curr.nodes[i]
        return curr.isword


    def startswith(self,prefix):
        curr = self.root
        for i in prefix:
            if i not in curr.nodes:
                return False
            curr = curr.nodes[i]
        return True

ob = Trie()
ob.insert("apple")
print(ob.search("app"))
print(ob.startswith("ap"))