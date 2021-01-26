# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        #the max_depths dictionary will map the value of a node to the greatest
        #depth of its descendants
        max_depths = dict()
        def visit(node: TreeNode, level: int) -> int:
            #determine if the node is a leaf:
            if node.left is None and node.right is None:
                max_depths[node.val] = level
                return level
            depths = []
            if node.left is not None:
                depths.append(visit(node.left, level + 1))
            if node.right is not None:
                depths.append(visit(node.right, level + 1))
            max_depth = max(depths)
            max_depths[node.val] = max_depth
            return max_depth
        visit(root, 0)
        #now traverse the tree until we find a node in which two children have the deepest max depth
        deepest = max_depths[root.val]
        node_pointer = root
        #if a node has exactly one descendant or one of its descendants doesn't contain the deepest level, it's not the lowest
        #common ancestor
        while node_pointer.left is None or node_pointer.right is None or max_depths[node_pointer.left.val] != deepest or max_depths[node_pointer.right.val] != deepest:
            #if the node is a leaf, then this is the lowest common ancestor
            if node_pointer.left is None and node_pointer.right is None:
                return node_pointer
            #otherwise, go down the tree
            elif node_pointer.left is None or (node_pointer.left is not None and max_depths[node_pointer.left.val]) != deepest:
                node_pointer = node_pointer.right
            else:
                node_pointer = node_pointer.left
        return node_pointer