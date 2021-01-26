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
import java.math.BigInteger;

class Solution {
    List<Integer> sums = new ArrayList();
    
    public int maxProduct(TreeNode root) {
        int totalSum = getSums(root);
        BigInteger maxProduct = BigInteger.valueOf(1);
        for (int s : sums) {
            BigInteger prod = BigInteger.valueOf(s * (totalSum - s));
            if (prod.compareTo(maxProduct) == 1) {
                maxProduct = prod;
            }
        }
        return (maxProduct.mod(BigInteger.valueOf(1000000007))).intValue();
    }
    
    private int getSums(TreeNode root) {
        //recursive base case
        if (root == null) {
            return 0;
        }
        int currentSum = getSums(root.left) + getSums(root.right) + root.val;
        sums.add(currentSum);
        return currentSum;
    }
}