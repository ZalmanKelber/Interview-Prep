# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        #keep track of the max we've found so far outside of the recursive function
        self.maxPath = root.val
        self.getMaxPath(root)
        return self.maxPath
        
    def getMaxPath(self, root: TreeNode) -> int:
        #recursive base case
        if root.left is None and root.right is None:
            self.maxPath = max(self.maxPath, root.val)
            return root.val
        #we need to compare four possibilities: the v-shaped path through this root, 
        # the root by itself, the left path and the right path
        leftMaxPath = self.getMaxPath(root.left) if root.left is not None else 0
        rightMaxPath = self.getMaxPath(root.right) if root.right is not None else 0
        vPath = root.val + leftMaxPath + rightMaxPath
        leftPath = leftMaxPath + root.val
        rightPath = rightMaxPath + root.val
        self.maxPath = max(self.maxPath, root.val, leftPath, rightPath, vPath)
        #the v path is not returned since it's not accessible to the parent roots
        return max(root.val, leftPath, rightPath)