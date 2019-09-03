from collections import defaultdict

#my solution
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
    
class FileSystem():
    def __init__(self):
        self.root = TrieNode()
        self.fileinfo = defaultdict(str)
    def ls(self, path):
        cur = self.root
        for token in path.split("/"):
            if token and cur:
                cur = cur[token]
        return sorted(cur.children.keys()) if cur else []
    def mkdir(self, path):
        cur = self.root
        for token in path.split("/"):
            if token:
                cur = cur.children[token]
    #a/b/c/d - "hello". Create a file d and make its fileinfo hello
    def addcontenttofile(self,path,content):
        self.mkdir(path)
        self.fileinfo[path]=self.fileinfo[path]+content
    def readcontentfromfile(self,path):
        return self.fileinfo[path]



















#standard answer
class TrieNode(object):
    def __init__(self):
        self.children = {}
    def setdefault(self,token):
        return self.children.setdefault(token,TrieNode())
    def get(self,token):
        return self.children.get(token,None)
    
class FileSystem(object):
    def __init__(self):
        self.root = TrieNode()
        self.fileinfo = defaultdict(str)
    def ls(self, path):
        cur = self.root
        for token in path.split("/"):
            if token and cur:
                cur = cur.get(token)
        return sorted(cur.children.keys()) if cur else []
    def mkdir(self, path):
        cur = self.root
        for token in path.split("/"):
            if token:
                cur = cur.setdefault(token)
    #a/b/c/d - "hello". Create a file d and make its fileinfo hello
    def addcontenttofile(self,path,content):
        self.mkdir(path)
        self.fileinfo[path]=self.fileinfo[path]+content
    def readcontentfromfile(self,path):
        return self.fileinfo[path]

obj = FileSystem()
obj.mkdir("a/b/c")
print(obj.ls("/"))
obj.mkdir("fdf")
print(obj.ls("/"))
