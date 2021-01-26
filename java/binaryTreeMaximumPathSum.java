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

    //keep track of the max we've found so far outside of the recursive function
    int maxPath;
    
    public int maxPathSum(TreeNode root) {
        maxPath = root.val;
        getMaxPath(root);
        return maxPath;
    }
    
    private int getMaxPath(TreeNode root) {
        //recursive base case
        if (root.left == null && root.right == null) {
            maxPath = Math.max(maxPath, root.val);
        }
        //we need to compare four possibilities: the v-shaped path through this root, 
        //the root by itself, the left path and the right path
        int leftPath = root.left == null ? 0 : getMaxPath(root.left);
        int rightPath = root.right == null ? 0 : getMaxPath(root.right);
        //the v path is not returned since it's not accessible to the parent roots
        int returnMax = Math.max(root.val, Math.max(root.val + leftPath, root.val + rightPath));
        maxPath = Math.max(maxPath, Math.max(returnMax, leftPath + rightPath + root.val));
        return returnMax;
    }
}