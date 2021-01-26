# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        #keep track of all paths
        paths = []
        if root is None:
            return paths
        #the stack, at any given point, will contain the path from the root to the current node
        stack = [root]
        found_nodes = set()
        while stack:
            cur = stack[-1]
            found_nodes.add(cur)
            #if the current node is a leaf, add the path
            if cur.left is None and cur.right is None:
                paths.append(self.getPathString(stack))
            #traverse the tree in pre-order
            if cur.left is not None and cur.left not in found_nodes:
                stack.append(cur.left)
            elif cur.right is not None and cur.right not in found_nodes:
                stack.append(cur.right)
            else: stack.pop()
        return paths 
    
    def getPathString(self, stack: List[TreeNode]) -> str:
        result = []
        for i, node in enumerate(stack):
            result.append(str(node.val))
            if i < len(stack) - 1:
                result.append("->")
        return "".join(result)