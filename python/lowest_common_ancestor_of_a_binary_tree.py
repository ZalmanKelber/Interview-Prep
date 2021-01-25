# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #keep track of whether we've found the first target
        found_first = False
        #keep a hash set of the nodes we've found so far
        found_nodes = set()
        #once we find the first target, keep a copy of the stack at the time, which will be the path from 
        #the root to it
        first_stack_copy = []
        #the stack will traverse the tree, maintaining the path from the root to the current node
        stack = [root]
        while stack:
            cur = stack[-1]
            #check if the top of the stack hasn't been found and is one of the targets
            if cur not in found_nodes and cur in { p, q }:
                if not found_first:
                    #if it's the first target, record the path from the root to it
                    found_first = True
                    first_stack_copy = stack[:]
                else:
                    #if it's the second target, compare the paths to the two targets to find the lowest common ancestor
                    for i, node in enumerate(first_stack_copy):
                        if i == len(first_stack_copy) - 1 or i == len(stack) - 1 or first_stack_copy[i + 1] != stack[i + 1]:
                            return node
            found_nodes.add(cur)
            #visit other nodes pre-order traversal
            if cur.left is not None and cur.left not in found_nodes:
                stack.append(cur.left)
            elif cur.right is not None and cur.right not in found_nodes:
                stack.append(cur.right)
            else:
                stack.pop()