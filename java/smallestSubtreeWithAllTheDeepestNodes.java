/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    //hashmap maps values of nodes onto the max depth of its descendants
    private Map<Integer, Integer> valuesToMaxDepths = new HashMap();
    
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        //recursive visit function maps all node values onto max depth of their descendants 
        visit(0, root);
        //maxDepth is the max depth of the root and thus max depth of the tree
        int maxDepth = valuesToMaxDepths.get(root.val);
        TreeNode pointer = root;
        //start with the root; if a node has exactly one descendant or one descandant has a 
        //max depth lower than the tree's max depth, it's not the lowest common ancestor
        while (pointer.left == null || pointer.right == null || 
              valuesToMaxDepths.get(pointer.left.val) != maxDepth ||
              valuesToMaxDepths.get(pointer.right.val) != maxDepth) {
            //if a node is a leaf, it's the lowest common ancestor
            if (pointer.left == null && pointer.right == null) {
                return pointer;
            }
            //otherwise continue down the path
            if (pointer.left == null || valuesToMaxDepths.get(pointer.left.val) != maxDepth) {
                pointer = pointer.right;
            } else {
                pointer = pointer.left;
            }
        }
        return pointer;
    }
    
    private int visit(int level, TreeNode node) {
        //recursive function uses post order traversal to map node values onto max depths of descandant nodes
        int rightMaxDepth = node.right == null ? level : visit(level + 1, node.right);
        int leftMaxDepth = node.left == null ? level : visit(level + 1, node.left);
        int maxDepth = Math.max(rightMaxDepth, leftMaxDepth);
        valuesToMaxDepths.put(node.val, maxDepth);
        return maxDepth;
    }
}