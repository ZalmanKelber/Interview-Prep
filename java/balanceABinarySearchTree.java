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
    //will store nodes in order
    List<TreeNode> nodes = new ArrayList();
    
    public TreeNode balanceBST(TreeNode root) {
        //traverse tree in order and store the nodes in the right order in a list
        visit(root);
        //each subproblem of addDescendants takes a left and right bound and the index of the parent element (which will be in the middle)
        int leftBound = 0, middle = (nodes.size() - 1) / 2, rightBound = nodes.size() - 1;
        addDescendants(leftBound, middle, rightBound);
        return nodes.get(middle);
    }
    
    private void addDescendants(int leftBound, int middle, int rightBound) {
        //if there is at least one element to the left of the parent element, add it as the left child
        int leftRight = middle - 1, rightLeft = middle + 1;
        if (leftRight >= leftBound) {
            int leftMiddle = leftBound + (leftRight - leftBound) / 2;
            nodes.get(middle).left = nodes.get(leftMiddle);
            addDescendants(leftBound, leftMiddle, leftRight);
        } else {
            nodes.get(middle).left = null;
        }
        //if there is at least one element to the right of the parent element, add it as the right child
        if (rightLeft <= rightBound) {
            int rightMiddle = rightLeft + (rightBound - rightLeft) / 2;
            nodes.get(middle).right = nodes.get(rightMiddle);
            addDescendants(rightLeft, rightMiddle, rightBound);
        } else {
            nodes.get(middle).right = null;
        }
    }
    
    private void visit(TreeNode node) {
        //uses in-order traversal to add nodes to nodes list
        if (node != null) {
            visit(node.left);
            nodes.add(node);
            visit(node.right);
        }
    }
}