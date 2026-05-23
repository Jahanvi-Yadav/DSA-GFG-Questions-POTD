''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def solve(self,root):
        if not root:
            return 0
        left = self.solve(root.left)
        right = self.solve(root.right)
        temp = root.data
        root.data = left + right
        return root.data + temp
        
    def toSumTree(self, root):
        self.solve(root)
