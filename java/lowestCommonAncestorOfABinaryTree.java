/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        //keep track of whether we've found the first target
        boolean foundFirst = false;
        //keep a hash set of the nodes we've found so far
        Set<Integer> foundNodes = new HashSet<>();
        //once we find the first target, keep a copy of the stack at the time, which will be the path from 
        //the root to it
        int[] firstPath = new int[0];
        //the stack will traverse the tree, maintaining the path from the root to the current node
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (stack.size() > 0) {
            TreeNode cur = stack.peek();
            //check if the top of the stack hasn't been found and is one of the targets
            if (!foundNodes.contains(cur.val) && (cur == p || cur == q)) {
                if (!foundFirst) {
                    //if it's the first target, record the path from the root to it
                    foundFirst = true;
                    firstPath = new int[stack.size()];
                    for (int i = 0; i < stack.size(); i++) {
                        firstPath[i] = stack.get(i).val;
                    }
                } else {
                    //if it's the second target, compare the paths to the two targets to find the lowest common ancestor
                    for (int i = 0; i < firstPath.length; i++) {
                        if (i == firstPath.length - 1 || i == stack.size() - 1 || firstPath[i + 1] != stack.get(i + 1).val) {
                            return stack.get(i);
                        }
                    }
                }
            }
            //visit other nodes pre-order traversal
            foundNodes.add(cur.val);
            if (cur.left != null && !foundNodes.contains(cur.left.val)) {
                stack.push(cur.left);
            } else if (cur.right != null && !foundNodes.contains(cur.right.val)) {
                stack.push(cur.right);
            } else {
                stack.pop();
            }
        }
        return root;
    }
}