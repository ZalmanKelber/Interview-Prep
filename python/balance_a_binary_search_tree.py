# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        #add the nodes to a list using in-order traversal
        def visit(node: TreeNode) -> None:
            if node is None:
                return
            visit(node.left)
            nodes.append(node)
            visit(node.right)
        visit(root)
        root_index = len(nodes) // 2
        new_root = nodes[root_index]
        #each subproblem takes the root index and the left and right bounds of the nodes array
        #it assigns the left child to the node halfway between the left bound and the node index and the
        #right child to the node halfway between the node index and the right bound
        def add_descendants(node_index: int, l: int, r: int) -> None:
            left_l, left_r = l, node_index - 1
            right_l, right_r = node_index + 1, r
            if left_l <= left_r:
                left_child_index = left_l + (left_r - left_l) // 2
                nodes[node_index].left = nodes[left_child_index]
                add_descendants(left_child_index, left_l, left_r)
            else:
                nodes[node_index].left = None
            if right_l <= right_r:
                right_child_index = right_l + (right_r - right_l) // 2
                nodes[node_index].right = nodes[right_child_index]
                add_descendants(right_child_index, right_l, right_r)
            else:
                nodes[node_index].right = None
        add_descendants(root_index, 0, len(nodes) - 1)
        return new_root