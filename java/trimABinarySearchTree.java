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
    public TreeNode trimBST(TreeNode root, int low, int high) {
        //start by updating the root
        while (root.val < low || root.val > high) {
            if (root.val < low) {
                root = root.right;
            } else {
                root = root.left;
            }
        }
        //remove all branches that are too low
        TreeNode pointer = root;
        while (pointer != null) {
            if (pointer.left != null && pointer.left.val < low) {
                pointer.left = pointer.left.right;
            } else {
                pointer = pointer.left;
            }
        }
        //remove all branches that are too high
        pointer = root;
        while (pointer != null) {
            if (pointer.right != null && pointer.right.val > high) {
                pointer.right = pointer.right.left;
            } else {
                pointer = pointer.right;
            }
        }
        return root;
    }
}