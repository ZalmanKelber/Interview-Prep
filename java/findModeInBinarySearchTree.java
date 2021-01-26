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
    //keeps track of the number of repetitions in the mode so far
    int maxCount = 0;
    //keeps track of the number of repetitions in the values we're currently examining
    int curCount = 0;
    //keeps track of the previous value we looked at in order to compare
    int prevVal;
    //stores the modes and clears them when maxCount increases
    List<Integer> modes = new ArrayList();
    
    public int[] findMode(TreeNode root) {
        //traverse the tree in order to collect the modes
        visit(root);
        //convert modes into an array
        int[] result = new int[modes.size()];
        for (int i = 0; i < modes.size(); i++) {
            result[i] = modes.get(i);
        }
        return result;
    }
    
    private void visit(TreeNode node) {
        //recursive base case
        if (node == null) {
            return;
        }
        //visit left subtree -> root -> right subtree for in-order traversal
        visit(node.left);
        //increment current count if appropriate
        if (node.val == prevVal) {
            curCount++;
        } else {
            curCount = 1;
        }
        //reassign previous value
        prevVal = node.val;
        //if the current value is a mode, add it to the mdoes list
        if (curCount == maxCount) {
            modes.add(node.val);
        //if the current value is greater than the previous modes, clear the modes list then add it
        } else if (curCount > maxCount) {
            maxCount = curCount;
            modes.clear();
            modes.add(node.val);
        }
        visit(node.right);
    }
}