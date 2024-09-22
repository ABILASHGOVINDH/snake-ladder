class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(root,key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)

def local_comman_ancensaor(root,n1,n2):
    if root is None:
        return None
    if root.val>n1 and root.val >n2:
        return local_comman_ancensaor(root.left,n1,n2)
    if root.val < n1 and root.val <n2:
        return local_comman_ancensaor(root.left,n1,n2)

root = None
keys = [20, 5, 30, 15, 17, 9, 37]

for key in keys:
    root = insert(root, key)

n1,n2= 17,15
lca = local_comman_ancensaor(root,n1,n2)
print(f"lac of {n1} and {n2} and {lca.val if lca else None}")










