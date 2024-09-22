from collections import deque

class TreeNode:
    def __init__(self,key):
        self.right = None
        self.left =None
        self.val = key

def traversal(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

print(traversal(root))