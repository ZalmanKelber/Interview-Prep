# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #set k (level of cousins) and parent (value of parent of first found element) to None
        self.k = None
        self.parent = None
        #set result to false
        self.is_cousins = False
        #visit each node recursively
        def visit(level: int, parent_value: int, node: TreeNode) -> None:
            if node is None: 
                return
            #if the node is one of the target nodes, determine if it's the first or second one that's found
            if node.val in [x, y]:
                #if it's the root, the result is false
                if parent_value is None:
                    self.is_cousins = False
                    return  
                #if we've found the other node, determine if the two are cousins
                if self.k is not None:
                    self.is_cousins = self.k == level and parent_value != self.parent
                    return
                #otherwise, assign k and parent to the appropriate values
                self.k = level
                self.parent = parent_value
            if node.left is not None:
                visit(level + 1, node.val, node.left)
            if node.right is not None:
                visit(level + 1, node.val, node.right)
        visit(0, None, root)
        return self.is_cousins