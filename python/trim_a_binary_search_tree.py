# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        #first update the root
        while root is not None and root.val < low or root.val > high:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
        #then, go down the tree twice, removing the lowest and highest branches, respectively, on the way down
        low_pointer, high_pointer = root, root
        while low_pointer is not None:
            if low_pointer.left is not None and low_pointer.left.val < low:
                low_pointer.left = low_pointer.left.right
            else:
                low_pointer = low_pointer.left
        while high_pointer is not None:
            if high_pointer.right is not None and high_pointer.right.val > high:
                high_pointer.right = high_pointer.right.left
            else:
                high_pointer = high_pointer.right
        return root