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
    private int x;
    private int y;
    private int k = -1;
    private int parent = -1;
    private boolean cousins = false;
    
    public boolean isCousins(TreeNode root, int x, int y) {
        this.x = x;
        this.y = y;
        visit(root, 0, 0);
        return cousins;
    }
    
    private void visit(TreeNode node, int level, int parentValue) {
        //check if this is a target node
        if (node.val == x || node.val == y) {
            //if the parent is zero, this is the root and the result is false
            if (parentValue == 0) {
                cousins = false;
                return;
            }
            //check if we've found the other target node
            if (k > 0) {
                //if so, determine whether the two nodes are cousins
                cousins = level == k && parentValue != parent;
                return;
            } else {
                //otherwise, assign k and parent to the appropriate values of this node, to check against
                //the second node when it's found
                k = level;
                parent = parentValue;
            }
        }
        //visit the other nodes in the tree recursively
        if (node.right != null) {
            visit(node.right, level + 1, node.val);
        }
        if (node.left != null) {
            visit(node.left, level + 1, node.val);
        }
    }
}