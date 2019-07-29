from collections import defaultdict
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isword = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for i in word:
            node = node.children[i]
        node.isword = True

    def search(self,word):
        node = self.root
        for i in word:
            node = node.children.get(i)
            if node==None:
                return False
        return node.isword
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

words = ["oath","pea","eat","rain"]

def findwords(board,words):
    ans = []
    ob = Trie()
    node = ob.root
    for word in words:
        ob.insert(word)
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board,node,i,j,"",ans)
    return ans

def dfs(board,node,i,j,path,ans):
    if node.isword:
        ans.append(path)
        node.isword = False
    if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
        return
    temp = board[i][j]
    node = node.children.get(temp)
    if node==None:
        return
    board[i][j]="#"
    neighbors = [(1,0),(0,1),(0,-1),(-1,0)]
    for di,dj in neighbors:
        dfs(board,node,i+di,j+dj,path+temp,ans)
    board[i][j]=temp

print(findwords(board,words))