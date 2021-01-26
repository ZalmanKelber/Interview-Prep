# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        #modes list will be cleared everytime a higher mode is found
        self.modes = []
        #keep track of previous node in order to compare
        self.prevNode = None
        #highest number of repetitions found so far
        self.maxCount = 0
        #current number of repetitions
        self.curCount = 0
        #traverse the tree in-order to count each element in order
        self.visit(root)
        return self.modes
    
    def visit(self, node: TreeNode) -> None:
        if node is None:
            return
        #order: left subtree -> root -> right subtree
        self.visit(node.left)
        #if the current node has the same value as the previous one, update the current count
        if self.prevNode is not None and node.val == self.prevNode.val:
            self.curCount += 1
        else: 
            self.curCount = 1
        #if the current count equals the max count, add the current node's value to the results
        if self.curCount == self.maxCount:
            self.modes.append(node.val)
        #if the current count exceeds the max count, clear the results and add the current node's value
        elif self.curCount > self.maxCount:
            self.maxCount = self.curCount
            self.modes = [node.val]
        self.prevNode = node
        self.visit(node.right)