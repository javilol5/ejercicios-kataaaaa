#https://www.codewars.com/kata/52bef5e3588c56132c0003bc

class Node:
    def __init__(self, L=None, R=None, n=None):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(root):
    if root is None:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result