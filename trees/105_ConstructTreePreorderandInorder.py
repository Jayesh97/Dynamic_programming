class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
def build(l,r):
    if l<=r:
        node = Node(preorder[build.pre_indx])
        build.pre_indx = build.pre_indx+1
        node.left = build(l,inorder_indx[node.value]-1)
        node.right = build(inorder_indx[node.value]+1,r)
        return node
def inorder_t(root,l):
    if root == None:
        return []
    if root.left!=None:
        inorder_t(root.left,l)
    l.append(root.value)
    if root.right!=None:
        inorder_t(root.right,l)
    return l

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
build.pre_indx = 0
inorder_indx = {n:i for i,n in enumerate(inorder)}
print(inorder_indx)
root = build(0,len(inorder)-1)
l = []
print(root.value)
print(inorder_t(root,l))
