# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        self.sums = []
        self.max_product = 1
        #traverse the tree and get the sum of every subtree and add them to self.sums
        #because we're using post-order traversal, the total sum will be returned last
        total_sum = self.getSums(root)
        #for each subtree, calculate the product of the two trees formed by excizing the subtree from the tree
        for current_sum in self.sums:
            current_product = current_sum * (total_sum - current_sum)
            self.max_product = max(self.max_product, current_product)
        return self.max_product % 1000000007
        
    def getSums(self, root) -> int:
        #recursive base case
        if root is None:
            return 0
        #use post-order traversal
        left = self.getSums(root.left)
        right = self.getSums(root.right)
        current_sum = left + right + root.val
        self.sums.append(current_sum)
        return current_sum