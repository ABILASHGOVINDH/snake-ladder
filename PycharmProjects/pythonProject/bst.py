class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right =None
        self.val = key

def insert(root,key):
     if root is None:
         return TreeNode(key)
     else:
         if root.val <key:
             root.right = insert(root.right,key)
         else:
             root.left = insert(root.left,key)

     return root

def find_parent(root,node,parent=None):
    if root is None:
        return None
    if root.val == node:
        return parent
    if root.val > node:
        return find_parent(root.left, node,root)
    else:
        return find_parent(root.right,node,root)

root = None
keys = [20, 5, 30, 15, 17, 9, 37]

for key in keys:
    root = insert(root, key)

node_to_find = 17
parent = find_parent(root,node_to_find)

if parent:
    print(f" The parent:{node_to_find}  node: {parent.val} ")
else:
    print(f" The parent {node_to_find}")

