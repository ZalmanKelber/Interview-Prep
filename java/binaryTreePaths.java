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
    public List<String> binaryTreePaths(TreeNode root) {
        //keep track of all paths
        List<String> paths = new ArrayList();
        if (root == null) {
            return paths;
        }
        Set<TreeNode> foundNodes = new HashSet();
        //the stack, at any given point, will contain the path from the root to the current node
        Stack<TreeNode> stack = new Stack();
        stack.push(root);
        while (stack.size() > 0) {
            TreeNode cur = stack.get(stack.size() - 1);
            foundNodes.add(cur);
            //if the current node is a leaf, add the path
            if (cur.right == null && cur.left == null) {
                paths.add(getStringPath(stack));
            }
            //traverse the tree in pre-order
            if (cur.left != null && !foundNodes.contains(cur.left)) {
                stack.push(cur.left);
            } else if (cur.right != null && !foundNodes.contains(cur.right)) {
                stack.push(cur.right);
            } else {
                stack.pop();
            }
        }
        return paths;
    }
    private String getStringPath(Stack<TreeNode> stack) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < stack.size(); i++) {
            sb.append(stack.get(i).val);
            if (i < stack.size() - 1) {
                sb.append("->");
            }
        }
        System.out.println(sb.toString());
        return sb.toString();
    }
}